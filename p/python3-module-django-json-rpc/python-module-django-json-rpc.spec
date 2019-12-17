%define oname django-json-rpc

Name: python3-module-%oname
Version: 0.7.1
Release: alt1

Summary: Simple Reference JSON-RPC Implementation for Django
License: MIT
Group: Development/Python3
Url: http://github.com/samuraisam/django-json-rpc
BuildArch: noarch

# https://github.com/samuraisam/django-json-rpc.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Simple Reference JSON-RPC Implementation for Django

%prep
%setup
find . -name \*.py -print0|xargs -0 sed -i -e 's/from jsonrpc/from django_jsonrpc/'
sed -i -e 's/from jsonrpc/from django_jsonrpc/' README.mdown
sed -i -e "s/packages=\['jsonrpc'\]/packages=['django_jsonrpc']/" setup.py
sed -i -e "s/package_data={'jsonrpc'/package_data={'django_jsonrpc'/" setup.py
mv jsonrpc django_jsonrpc

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%doc README.*
%python3_sitelibdir/django_jsonrpc*
%python3_sitelibdir/django_json_rpc*


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt1
- Version updated to 0.7.1
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.6.2-alt2.git0d98fb.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.2-alt2.git0d98fb.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt2.git0d98fb
- New snapshot
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.git699856.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git699856
- Version 0.6.2

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt3.git3052f3
- fix gears inheritance check

* Tue Feb 23 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt2.git3052f3
- modify files section

* Mon Feb 22 2010 Denis Klimov <zver@altlinux.org> 0.5.1-alt1.git3052f3
- new version
- jsonrpc module renamed to django_jsonrpc

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt3.gita815e3.1
- Rebuilt with python 2.6

* Thu Nov 19 2009 Denis Klimov <zver@altlinux.org> 0.2-alt3.gita815e3
- new version
- use build and install python macros

* Tue Nov 10 2009 Denis Klimov <zver@altlinux.org> 0.2-alt2.git30fad1
- new version

* Sun Nov 08 2009 Denis Klimov <zver@altlinux.org> 0.2-alt1.gite9c07b
- Initial build for ALT Linux

