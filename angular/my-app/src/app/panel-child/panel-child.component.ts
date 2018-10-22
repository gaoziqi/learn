import { Component, OnInit } from '@angular/core';
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
    console.log(1);
    this.items.push(e.dragData);
  }

  onDragDrop(e: any) {
    this.items.splice(this.items.indexOf(e), 1);
    console.log(this.items);
  }

  ngOnInit() {}
}
