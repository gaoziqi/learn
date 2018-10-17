import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator, MatSort } from '@angular/material';
import { MtDataSource } from './mt-datasource';

@Component({
  selector: 'app-mt',
  templateUrl: './mt.component.html',
  styleUrls: ['./mt.component.css']
})
export class MtComponent implements OnInit {
  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;
  dataSource: MtDataSource;

  /** Columns displayed in the table. Columns IDs can be added, removed, or reordered. */
  displayedColumns = ['id', 'name'];

  ngOnInit() {
    this.dataSource = new MtDataSource(this.paginator, this.sort);
  }
}
