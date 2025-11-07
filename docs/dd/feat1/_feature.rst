#############
First Feature
#############


.. feat:: First Example Feature
   :id: F_FEAT_1

   .. needarch::
      :key: sequence
      :debug:

      {%- set components = need().details -%}
      {% for c in components %}
      {{sequence(needs, c)}} {{ref(c)}}
      {% endfor %}

      {% for c in components %}
      activate {{c}}
      {% endfor %}

      {% for c in components %}
      deactivate {{c}}
      {% endfor %}
