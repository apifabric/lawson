import { MenuRootItem } from 'ontimize-web-ngx';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DepartmentCardComponent } from './Department-card/Department-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { EmployeeProjectCardComponent } from './EmployeeProject-card/EmployeeProject-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { PositionCardComponent } from './Position-card/Position-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ProjectCardComponent } from './Project-card/Project-card.component';

import { ShipmentCardComponent } from './Shipment-card/Shipment-card.component';

import { VendorCardComponent } from './Vendor-card/Vendor-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Department', name: 'DEPARTMENT', icon: 'view_list', route: '/main/Department' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'EmployeeProject', name: 'EMPLOYEEPROJECT', icon: 'view_list', route: '/main/EmployeeProject' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Position', name: 'POSITION', icon: 'view_list', route: '/main/Position' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Project', name: 'PROJECT', icon: 'view_list', route: '/main/Project' }
    
        ,{ id: 'Shipment', name: 'SHIPMENT', icon: 'view_list', route: '/main/Shipment' }
    
        ,{ id: 'Vendor', name: 'VENDOR', icon: 'view_list', route: '/main/Vendor' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    CustomerCardComponent

    ,DepartmentCardComponent

    ,EmployeeCardComponent

    ,EmployeeProjectCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,PositionCardComponent

    ,ProductCardComponent

    ,ProjectCardComponent

    ,ShipmentCardComponent

    ,VendorCardComponent

];