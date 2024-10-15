import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import { HttpClient } from '@angular/common/http';
import { PlayerSummary } from './player-summary.interface';

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
    private http: HttpClient
  ) {

  }

  ngOnInit(): void {
    this.fetchPlayerSummary();
  }

  ngOnDestroy() {
  }

  playerSummary: PlayerSummary | null = null;
  playerID: string = ''; // You might want to get this from a route parameter or user input
  error: string | null = null;

  fetchPlayerSummary(): void {
    if (!this.playerID) {
      this.error = 'Please enter a player ID';
      return;
    }
    this.error = null;
    this.http.get<PlayerSummary>(`/api/v1/playerSummary/${this.playerID}`).subscribe(
      data => {
        this.playerSummary = data;
      },
      error => {
        console.error('Error fetching player summary:', error);
        this.error = 'Error fetching player data. Please try again.';
      }
    );
  }
}
