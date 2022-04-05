%define oname cycler

Name: python3-module-%oname
Version: 0.11.0
Release: alt1

Summary: Composable style cycles

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Cycler

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-six
BuildPreReq: python3-module-nose
BuildPreReq: python3-module-pytest

%description
The public API of cycler consists of a class Cycler and a factory
function cycler(). The function provides a simple interface for creating
'base' Cycler objects while the class takes care of the composition and
iteration logic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test -v

%files
%doc *.rst doc/source/*.rst
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)

* Tue Nov 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt2
- build python3 module separately

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 10 2017 Anton Midyukov <antohami@altlinux.org> 0.10.0-alt1
- New version 0.10.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.post1.git20150822.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.post1.git20150822
- Initial build for Sisyphus
