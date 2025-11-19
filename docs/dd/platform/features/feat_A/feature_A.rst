###############
Feature A
###############

.. toctree::
   :maxdepth: 1
   :glob:

   requirements/index

.. feat:: Feature A
   :id: F_FEAT_A
   :consists_of: M_MODULE_A

   :np:`(Sequence)` Diagram

   .. needarch::
      :key: Sequence

      {%- set cn = need().id -%}
      {{sequence(needs, cn)}} {{ref(cn)}}

      'add your needed sphinx-needs elements to the list "components"
      {%- set components = need().consists_of -%}
      {% for c in components %}
      {{sequence(needs, c)}} {{ref(c)}}
      {% endfor %}

      'here you can add your plantuml sequence diagramm code.
      'documentation can be found here: https://plantuml.com/en/sequence-diagram

      activate {{ cn }}
      {{ cn }} -> {{ components[0] }}
      activate {{ components[0] }}
      {% for i in range(components|length - 1) %}
      {{ components[i] }} -> {{ components[i+1] }}
      activate {{ components[i+1] }}
      {{ components[i] }} <- {{ components[i+1] }}
      {{ components[i] }} <- {{ components[i+1] }}
      deactivate {{ components[i+1] }}
      {% endfor %}
      {{ cn }} <- {{ components[0] }}
      deactivate {{ components[0] }}
      deactivate {{ cn }}
