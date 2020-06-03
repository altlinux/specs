%define oname random2

Name: python-module-%oname
Version: 1.0.2
Release: alt3

Summary: Python 3 compatible Python 2 `random` Module
License: PSFL
Group: Development/Python
Url: https://pypi.python.org/pypi/random2/
# https://github.com/strichter/random2.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python

%description
Python 3 compatible Python 2 `random` Module.

%prep
%setup
sed -i 's|#!/usr/bin/env python|#!__python|' \
    $(find ./ -name '*.py')

%build
%python_build_debug

%install
%python_install

%check
%__python setup.py test

%files
%doc *.txt
%python_sitelibdir/*

%changelog
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

