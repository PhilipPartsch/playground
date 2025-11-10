########
Platform
########

.. toctree::
   :caption: Components
   :maxdepth: 1
   :glob:

   feat*/*

.. platform:: First platform
   :id: P_PLATFORM_1

   :np:`(Sequence)` Diagram

   .. needarch::
      :key: Sequence

      {%- set cn = need().id -%}
      {{sequence(needs, cn)}} {{ref(cn)}}

      activate {{ cn }}

      'add your needed sphinx-needs elements to the list "features"
      {%- set features = need().consists_of -%}
      {% for f in features %}
      {{ cn }} -> {{ f }}
      {{uml(f, 'Sequence')}}
      {{ f }} -> {{ cn }}
      {% endfor %}

      deactivate {{ cn }}

   :np:`(Detailed)` Diagram

   .. needarch::
      :key: Detailed

      {{flow(need().id)}} {
      'add your needed sphinx-needs elements to the list "features"
      {%- set features = need().consists_of -%}
      {% for f in features %}
      {{uml(f, 'Deployment')}}
      {% endfor %}
      }
