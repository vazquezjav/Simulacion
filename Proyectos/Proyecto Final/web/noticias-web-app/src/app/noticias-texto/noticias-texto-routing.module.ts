import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { NoticiasTextoPage } from './noticias-texto.page';

const routes: Routes = [
  {
    path: '',
    component: NoticiasTextoPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class NoticiasTextoPageRoutingModule {}
