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
      :debug:

      'add your needed sphinx-needs elements to the list "features"
      {%- set features = need().details -%}
      {% for f in features %}
      {{uml(f, 'Sequence')}}
      {% endfor %}

   :np:`(Detailed)` Diagram

   .. needarch::
      :key: Detailed
      :debug:

      'add your needed sphinx-needs elements to the list "features"
      {%- set features = need().details -%}
      {% for f in features %}
      {{uml(f, 'Deployment')}}
      {% endfor %}
