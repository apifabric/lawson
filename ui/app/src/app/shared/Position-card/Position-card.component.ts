import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Position-card.component.html',
  styleUrls: ['./Position-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Position-card]': 'true'
  }
})

export class PositionCardComponent {


}