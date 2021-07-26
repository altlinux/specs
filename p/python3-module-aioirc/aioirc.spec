%define oname aioirc

%def_disable check

Name: python3-module-%oname
Version: 0.1
Release: alt2.git20140929
Summary: AsyncIO IRC Library for >= Python 3.3
License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/aioirc/

# https://github.com/devunt/aioirc.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires asyncio

BuildRequires: python3-module-pytest

%description
AsyncIO IRC Library for >= Python 3.3.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
export PYTHONPATH=$PWD
python3 examples/test.py

%files
%doc *.rst docs/*.rst docs/aioirc/* examples
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt2.git20140929
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt1.git20140929.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140929.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140929.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140929
- Initial build for Sisyphus

