import { inject } from '@angular/core/primitives/di';
import { IProject } from './../models/IProject';
import { BaseService } from '../base/BaseService';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: "root"
})
export class ProjectService {

    private baseService = inject(BaseService);
    
    getAllProjectByUserId(id:number): IProject[]{
        return [] as IProject[]
    }
}