%define _unpackaged_files_terminate_build 1
%define pypi_name pydoctor
%define module_name %pypi_name
%define bin_name %pypi_name
%def_with check

Name: python3-module-%pypi_name
Version: 25.4.0
Release: alt1

Summary: This is pydoctor, an API documentation generator that works by static analysis
License: MIT and Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pydoctor/
Vcs: https://github.com/twisted/pydoctor
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter cython-test-exception-raiser$
%add_pyproject_deps_check_filter bs4$
BuildRequires: python3-module-beautifulsoup4
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-filelock
%pyproject_builddeps_metadata_extra test
%endif

%description
This is pydoctor, a standalone API documentation generator that works by
static analysis.
It was written primarily to replace epydoc for the purposes of the Twisted
project as epydoc has difficulties with zope.interface. If you are looking
for a successor to epydoc after moving to Python 3, pydoctor might be the
right tool for your project as well.
pydoctor puts a fair bit of effort into resolving imports and computing
inheritance hierarchies and, as it aims at documenting Twisted, knows about
zope.interface's declaration API and can present information about which
classes implement which interface, and vice versa.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONDEVMODE=1
%pyproject_run_pytest

%files
%doc README.rst LICENSE.txt
%_bindir/%bin_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jun 30 2025 Alexandr Shashkin <dutyrok@altlinux.org> 25.4.0-alt1
- Initial build for ALT Sisyphus.

