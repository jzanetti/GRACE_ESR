
override MAMBA = $(CONDA_BASE)/bin/mamba
override PKG=grace_esr

clear_env:
	rm -rf $(CONDA_BASE)/envs/$(PKG)

clear_all:
	rm -rf $(CONDA_BASE)/envs/$(PKG)
	rm -rf $(CONDA_BASE)/pkgs/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/.cache/paths/$(PKG)*
	rm -rf $(CONDA_BASE)/conda-bld/linux-64/.cache/recipe/$(PKG)*
	# $(CONDA) index $(CONDA_BASE)/conda-bld

create_env: clear_all clear_env
	$(MAMBA) env create -n $(PKG) -f env.yml
