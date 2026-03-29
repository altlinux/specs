%define _unpackaged_files_terminate_build 1

%define pypi_name python-gettext
%define mod_name pythongettext
%define oname gettext

%def_with check

Name: python3-module-%oname
Version: 5.0
Release: alt1.1
Summary: Python Gettext po to mo file compiler
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/python-gettext/
Vcs: https://github.com/hannosch/python-gettext
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch
# mapping from PyPI name
# https://www.altlinux.org/Management_of_Python_dependencies_sources#Mapping_project_names_to_distro_names
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope-testrunner
%endif

%description
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- zope-testrunner --test-path=src -vc

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/%mod_name/tests/

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 5.0-alt1.1
- Demodernized packaging.

* Tue Aug 08 2023 Stanislav Levin <slev@altlinux.org> 5.0-alt1
- 4.0 -> 5.0.

* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- 3.0 -> 4.0.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt2
- Drop python2 support.

* Sat Jul 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt1.2
- NMU: Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt1.dev.git20130210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev.git20130210
- Initial build for Sisyphus

