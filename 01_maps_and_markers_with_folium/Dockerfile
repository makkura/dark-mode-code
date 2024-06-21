# Use a jupyter lab image and add in requirements
FROM quay.io/jupyter/base-notebook:python-3.11

USER jovyan
WORKDIR /home/jovyan

COPY --chown=jovyan overrides.json /opt/conda/share/jupyter/lab/settings/overrides.json

#COPY --chown=jovyan requirements.txt .
#RUN pip install -r requirements.txt
