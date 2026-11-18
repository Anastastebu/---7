# Звіт роботи Reasoner (HermiT 1.4.3)

## 1. Перевірка узгодженості (Consistency Check)
- **Статус**: Consistent (Узгоджено)
- **Виведені твердження (Inferred Axioms)**:
  1. `:srv_prod_01`  виведено тип `:ITResource` (через `rdfs:subClassOf`).
  2. `:esxi_01` виведено відношення `:isHostedOn` до `:srv_prod_01` (через `owl:inverseOf`)
  3. `:vm_db_01`  виведено тип `:SoftwareResource`

## 2. Демонстрація суперечності (Inconsistency Test)
- **Дія**: Індивіду `:srv_prod_01` призначено подвійний тип `:ComputeServer` та `:OperatingSystem`
- **Результат HermiT**: `InconsistentOntologyException: Individual :srv_prod_01 belongs to disjoint classes :HardwareResource and :SoftwareResource`
- **Усунення**: Вилучено тип `:OperatingSystem` у індивіда `:srv_prod_01`. Онтологія знову consistent