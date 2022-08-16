INSERT INTO Tipos_cliente
        (
            TCLI_tipo,
            TCLI_limites_tranf,
            TCLI_comision_tranf,
            TCLI_Tarjeta_limit
        )
    VALUES
        ('CLASSIC',150000,0,1),
        ('GOLD',500000,0.5,1),
        ('BLACK',0,0,5)
;

CREATE TABLE Relation_Cliente_Tipo(
    id_Relation_Cliente_Tipo INTEGER PRIMARY KEY,
    fk_Tipos_cliente INTEGER NOT NULL,
    fk_cliente Integer NOT NULL,
    FOREIGN KEY (fk_Tipos_cliente) REFERENCES Tipos_Cliente
    FOREIGN KEY (fk_cliente) REFERENCES cliente(customer_id)
);