%define _unpackaged_files_terminate_build 1
%define pypi_name lunr
%define module_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: A Python implementation of Lunr.js
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lunr/
Vcs: https://github.com/yeraydiazdiaz/lunr.py
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: nltk_data.tar
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra tests
%endif

%description
A Python implementation of Lunr.js by Oliver Nightingale.
A bit like Solr, but much smaller and not as bright.
This Python version of Lunr.js aims to bring the simple and powerful
full text search capabilities into Python guaranteeing results as close
as the original implementation as possible.

%prep
%setup -a2
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
# acceptance: skip javascript acceptance tests
%pyproject_run -- bash -s <<-'ENDTESTS'
ln -s ../nltk_data .run_venv
python3 -m pytest -k "not acceptance"
ENDTESTS

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.8.0-alt1
- Initial build for ALT Sisyphus.

