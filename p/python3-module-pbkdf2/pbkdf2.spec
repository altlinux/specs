%define oname pbkdf2

Name: python3-module-%oname
Version: 1.3
Release: alt3

Summary: PKCS#5 v2.0 PBKDF2 Module
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/pbkdf2
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3 


%description
This module implements the password-based key derivation function,
PBKDF2, specified in RSA PKCS#5 v2.0.

%prep
%setup

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 1.3-alt2
- Restoring python3 provides

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-3.3

* Sun May 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

