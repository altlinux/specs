%define _unpackaged_files_terminate_build 1
%define pypi_name pdoc3
%def_with check

Name: python3-module-%pypi_name
Version: 0.11.6
Release: alt2

Summary: Auto-generate API documentation for Python 3+ projects
License: AGPL-3.0-or-later
Group: Development/Python3
Url: https://pypi.org/project/pdoc3
Vcs: https://github.com/pdoc3/pdoc
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject

%add_pyproject_deps_build_filter setuptools-git
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%endif

%description
Enter pdoc, the perfect documentation generator 
for small-to-medium-sized, tidy Python projects.
It generates documentation simply from your projects 
already-existing public modules and objects docstrings,
like sphinx-apidoc or sphinx.ext.autodoc, 
but without the hassle of these tools.
Minimal and lightweight.
Guaranteed 99%% correct magic out of the box!

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

# Create MANIFEST.in for recoursive-include .mako files from templates.
cat <<EOF > MANIFEST.in
recursive-include pdoc/templates *.mako
EOF

%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest

%files
%_bindir/pdoc
%_bindir/pdoc3
%python3_sitelibdir_noarch/pdoc/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Wed May 14 2025 Ivan Khanas <xeno@altlinux.org> 0.11.6-alt2
- Maintainer`s work.

* Tue Apr 22 2025 Ivan Khanas <xeno@altlinux.org> 0.11.6-alt1
- First build for ALT.
