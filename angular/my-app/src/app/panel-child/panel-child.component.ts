import { Component, OnInit } from '@angular/core';
import * as _ from 'lodash';
import { DropEvent } from '../../../third/ng-drag-drop/shared/drop-event.model';

@Component({
  selector: 'app-panel-child',
  templateUrl: './panel-child.component.html'
})
export class PanelChildComponent implements OnInit {
  constructor() {}
  items = [{ name: 'Apple', type: 'fruit' }, { name: 'Carrot', type: 'vegetable' }, { name: 'Orange', type: 'fruit' }];
  start = null;
  onItemDrop(e: DropEvent) {
    // Get the dropped data here
    console.log(this.items);
    this.items.push(e.dragData);
  }

  ngOnInit() {}
}
