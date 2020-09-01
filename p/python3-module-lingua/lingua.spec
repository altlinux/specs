%define oname lingua

Name: python3-module-%oname
Version: 4.13
Release: alt3
Summary: Translation toolset
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/lingua/

# https://github.com/wichert/lingua.git
Source: %name-%version.tar
BuildArch: noarch
Patch1: %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-polib python3-module-chameleon.core
BuildPreReq: python3-module-mock
BuildRequires: python3-module-pytest

Conflicts: python-module-lingua < %EVR
Obsoletes: python-module-lingua < %EVR

%py3_provides %oname

%description
Lingua is a package with tools to extract translateable texts from your
code, and to check existing translations. It replaces the use of the
xgettext command from gettext, or pybabel from Babel.

%prep
%setup
%patch1 -p1
grep -qsF '[pytest]' setup.cfg || exit 1
sed -i 's/\[pytest\]/[tool:pytest]/g' setup.cfg

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst docs/examples
%_bindir/*
%python3_sitelibdir/*

%changelog
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

