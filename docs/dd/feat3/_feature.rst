##############
Thired Feature
##############

.. toctree::
   :maxdepth: 1
   :glob:

   requirements/index

.. feat:: Third Feature
   :id: F_FEAT_3

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
      {{ cn }} -> {{ components[components|length - 1] }}
      activate {{ components[components|length - 1] }}
      {% for i in range(components|length - 1, 0, -1) %}
      {{ components[i] }} -> {{ components[i-1] }}
      activate {{ components[i-1] }}
      {{ components[i] }} <- {{ components[i-1] }}
      {{ components[i] }} <- {{ components[i-1] }}
      deactivate {{ components[i-1] }}
      {% endfor %}
      {{ cn }} <- {{ components[components|length - 1] }}
      deactivate {{ components[components|length - 1] }}
      deactivate {{ cn }}
