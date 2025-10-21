%define _unpackaged_files_terminate_build 1
%define pypi_name python-ctags3

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.0
Release: alt1

Summary: Exuberant Ctags indexing python bindings
License: LGPL-3
Group: Development/Python3
Url: https://pypi.org/project/python-ctags3/
Vcs: https://github.com/universal-ctags/python-ctags3

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%endif

ExclusiveArch: x86_64

%description
Exuberant Ctags supports indexing of many modern programming languages.
Python is a powerful scriptable dynamic language. Using Python to access
Ctags index file is a natural fit in extending an settings of the application
capability to examine source code.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
cp -f build/lib.linux-%{_arch}-cpython-%(echo %{__python3_version} | tr -d .)/ctags/* src/ctags/.
%pyproject_run_pytest

%files
%doc README.* license.txt CHANGELOG.md 
%python3_sitelibdir/ctags
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Sep 17 2025 Denis Rastyogin <gerben@altlinux.org> 1.6.0-alt1
- Initial build for ALT Sisyphus.
