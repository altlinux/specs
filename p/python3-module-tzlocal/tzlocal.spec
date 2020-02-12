%define _unpackaged_files_terminate_build 1
%define oname tzlocal

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: tzinfo object for the local timezone
License: CC0 1.0 Universal
Group: Development/Python3
Url: https://pypi.python.org/pypi/tzlocal/
BuildArch: noarch

# https://github.com/regebro/tzlocal.git
Source0: https://pypi.python.org/packages/d3/64/e4b18738496213f82b88b31c431a0e4ece143801fb6771dddd1c2bf0101b/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytz

%py3_provides %oname


%description
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This module attempts to fix a glaring hole in pytz, that there is no way
to get the local timezone information, unless you know the zoneinfo
name, and under several Linux distros that's hard or impossible to
figure out.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This Python module returns a tzinfo object with the local timezone
information under Unix and Win-32. It requires pytz, and returns pytz
tzinfo objects.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|@PYVER@|%_python3_version|' tzlocal/unix.py

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt2.dev0.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt2.dev0.git20141018
- tzlocal.unix: added path to localtime in pytz

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141018
- Initial build for Sisyphus

