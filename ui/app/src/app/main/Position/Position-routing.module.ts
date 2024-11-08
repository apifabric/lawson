import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PositionHomeComponent } from './home/Position-home.component';
import { PositionNewComponent } from './new/Position-new.component';
import { PositionDetailComponent } from './detail/Position-detail.component';

const routes: Routes = [
  {path: '', component: PositionHomeComponent},
  { path: 'new', component: PositionNewComponent },
  { path: ':id', component: PositionDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Position-detail-permissions'
      }
    }
  }
];

export const POSITION_MODULE_DECLARATIONS = [
    PositionHomeComponent,
    PositionNewComponent,
    PositionDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PositionRoutingModule { }