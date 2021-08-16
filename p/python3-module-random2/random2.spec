%define oname random2

Name: python3-module-%oname
Version: 1.0.2
Release: alt4

Summary: Python 3 compatible Python 2 `random` Module

License: PSFL
Group: Development/Python3
Url: https://pypi.python.org/pypi/random2/

# https://github.com/strichter/random2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Python 3 compatible Python 2 `random` Module.

%prep
%setup

%build
%python3_build

%install
%python3_install

# Remove a test that is invalid as of python 3.9
sed -i '/self\.gen\.getrandbits, 0/d' src/tests.py

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt4
- build python3 module separately

* Wed Jun 03 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt3
- Build for Python2.

* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20130315.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20130315.1
- (NMU) rebuild with rpm-build-python-0.1.9
  (for common python/site-packages/ and auto python.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20130315
- Initial build for Sisyphus

