function asociacion = calcularAsociacion(compatibilidad,reglas)
    asociacion = [];
    for i = 1:length(reglas)
        asociacion = [asociacion;compatibilidad(i)*reglas(i,5) reglas(i,6)];
    end
end