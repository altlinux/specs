%define oname jsobj

%def_disable check

Name: python3-module-%oname
Version: 1.0.4
Release: alt3

Summary: Jsobj provides JavaScript-Style Objects in Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsobj/
# https://github.com/gkovacs/jsobj.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
jsobj provides JavaScript-Style Objects in Python. It is based on
jsobject, but returns None if you try accessing non-existent keys
instead of throwing an exception.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.4-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.4-alt1.git20150120.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.4-alt1.git20150120.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.4-alt1.git20150120.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Initial build for Sisyphus

