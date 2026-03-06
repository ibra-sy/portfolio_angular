import { Component, inject } from '@angular/core';
import { ProjectService } from '../../../shared/service/ProjectService';

@Component({
  selector: 'app-projet',
  standalone: true,
  imports: [],
  templateUrl: './projet.html'
})
export class Projet {
  private projectService = inject(ProjectService);
}
