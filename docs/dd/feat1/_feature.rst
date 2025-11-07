#############
First Feature
#############


.. feat:: First Example Feature
   :id: F_FEAT_1

   :np:`(Sequence)` Diagram

   .. needarch::
      :key: Sequence
      :debug:

      {%- set cn = need().id -%}
      {{sequence(needs, cn)}} {{ref(cn)}}

      'add your needed sphinx-needs elements to the list "components"
      {%- set components = need().details -%}
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
      deactivate {{ components[0] }}
      deactivate {{ cn }}

