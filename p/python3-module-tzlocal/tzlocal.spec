%define _unpackaged_files_terminate_build 1
%define oname tzlocal

Name: python3-module-%oname
Version: 4.2
Release: alt1

Summary: A Python module that tries to figure out what your local timezone is

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/tzlocal/

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytz-deprecation-shim

%description
This Python module returns a tzinfo object (with a pytz_deprecation_shim,
for pytz compatibility) with the local timezone information, under
Unix and Windows.

It requires Python 3.6 or later, and will use the backports.tzinfo
package, for Python 3.6 to 3.8.

This module attempts to fix a glaring hole in the pytz and zoneinfo
modules, that there is no way to get the local timezone information,
unless you know the zoneinfo name, and under several Linux distros
that's hard or impossible to figure out.

With tzlocal you only need to call get_localzone() and you will get a
tzinfo object with the local time zone info. On some Unices you will
still not get to know what the timezone name is, but you don't need
that when you have the tzinfo file. However, if the timezone name is
readily available it will be used.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 -m pytest tests


%files
%doc CHANGES.txt LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
* Thu Apr 21 2022 Egor Ignatov <egori@altlinux.org> 4.2-alt1
- new version 4.2

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)
- adopt spec for rpmgs util
- temp. ignore test results

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

