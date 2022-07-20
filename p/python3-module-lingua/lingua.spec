%define oname lingua

Name: python3-module-%oname
Version: 4.15.0
Release: alt2

Summary: Translation toolset

License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/lingua/

# https://github.com/wichert/lingua.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit
BuildRequires: python3-module-polib
BuildRequires: python3-module-chameleon.core
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest
BuildRequires: python3-module-click

Conflicts: python-module-lingua < %EVR
Obsoletes: python-module-lingua < %EVR

%py3_provides %oname

%description
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

%prep
%setup

sed -i 's/4.14/4.15/' src/lingua/__init__.py

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc *.rst docs/examples
%_bindir/polint
%_bindir/pot-create
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Thu Jul 21 2022 Grigory Ustinov <grenka@altlinux.org> 4.15.0-alt2
- Built and installed by pyproject_* macros.
- Fixed license.

* Wed May 25 2022 Grigory Ustinov <grenka@altlinux.org> 4.15.0-alt1
- Automatically updated to 4.15.0.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 4.14-alt1
- Automatically updated to 4.14.

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 4.13-alt3
- Transfer on python3.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 4.13-alt2
- Fixed Pytest4.x compatibility error.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.13-alt1
- Updated to upstream release 4.13

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7-alt1.git20141111.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7-alt1.git20141111
- Version 3.7

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1.git20141103
- Version 3.4
- Enabled testing

* Thu Oct 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.git20141003
- Initial build for Sisyphus

