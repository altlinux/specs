%define oname moto

# slow:
%def_disable check

Name: python3-module-%oname
Version: 0.4.10
Release: alt2

Summary: A library that allows your python tests to easily mock out the boto library
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/moto/
# https://github.com/spulec/moto.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires jinja2 boto dicttoxml flask httpretty requests xmltodict
%py3_requires six werkzeug xml bisect

BuildRequires: python3-module-chardet python3-module-coverage
BuildRequires: python3-module-dicttoxml python3-module-ecdsa
BuildRequires: python3-module-html5lib python3-module-mimeparse
BuildRequires: python3-module-nose python3-module-pbr
BuildRequires: python3-module-pycrypto python3-module-pytest
BuildRequires: python3-module-unittest2 python3-module-urllib3
BuildRequires: python3-module-yaml python3-module-yieldfrom.urllib3


%description
Moto is a library that allows your python tests to easily mock out the
boto library.

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
sed -i 's|nosetests|nosetests3|' Makefile
%make test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt1.git20150808.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.10-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.10-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.git20150808
- Version 0.4.10

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.git20150722
- Version 0.4.7

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150222
- Version 0.4.1

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git201500203
- Version 0.4.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150117
- Initial build for Sisyphus

