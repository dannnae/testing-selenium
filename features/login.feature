Feature: Ingreso a Sence

  Scenario: Acceso correcto a la página de Sence
    Given que puedo acceder a la página Sence
    When puedo acceder al login
    And ingreso a Clave Única
    And ingreso los datos correspondientes
    And realizo el envío de los datos
    Then aparece un mensaje de ingreso correcto
