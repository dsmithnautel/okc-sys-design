export interface PlayerSummary {
  player_id: string;
  name: string;
  team: string;
  height: number;
  weight: number;
  position: string;
  games: Game[];
}

interface Game {
  game_id: string;
  date: string;
  home_team: string;
  away_team: string;
  shots: Shot[];
}

interface Shot {
  x: number;
  y: number;
  made: boolean;
}
