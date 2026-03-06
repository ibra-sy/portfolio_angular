import { inject } from '@angular/core/primitives/di';
import { IContact } from './../models/IContact';
import { BaseService } from '../base/BaseService';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: "root"
})
export class ContactService {

    private baseService = inject(BaseService);
    
    saveContact(contact: IContact){
    }
}