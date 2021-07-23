%define oname rednose

%def_disable check

Name: python3-module-%oname
Version: 0.4.3
Release: alt3
Summary: Coloured output for nosetests
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/rednose/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-setuptools python3-module-termstyle

%py3_provides %oname

%description
rednose is a nosetests plugin for adding colour (and readability) to
nosetest console results.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc PKG-INFO
%python3_sitelibdir/*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.3-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt2.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.4.3-alt2
- cleanup buildreq

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

