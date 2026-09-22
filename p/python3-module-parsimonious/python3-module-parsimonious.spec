%define _unpackaged_files_terminate_build 1
%define pypi_name parsimonious
%define mod_name parsimonious

%def_with check

Name: python3-module-%pypi_name
Version: 0.11.0
Release: alt1

Summary: (Soon to be) the fastest pure-Python PEG parser I could muster
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/parsimonious/
Vcs: https://github.com/erikrose/parsimonious

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata_extra testing
%endif

%description
Parsimonious aims to be the fastest arbitrary-lookahead parser written in pure
Python-and the most usable. It's based on parsing expression grammars (PEGs),
which means you feed it a simplified sort of EBNF notation. Parsimonious was
designed to undergird a MediaWiki parser that wouldn't take 5 seconds or a GB of
RAM to do one page, but it's applicable to all sorts of languages.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Sep 22 2026 Anton Zhukharev <ancieg@altlinux.org> 0.11.0-alt1
- Packaged for ALT Sisyphus.
