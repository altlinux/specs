%define oname creole

Name: python3-module-%oname
Version: 1.2.0
Release: alt2

Summary: Markup converter in pure Python for: creole2html, html2creole, html2ReSt, html2textile
License: GPLv3+
Group: Development/Python3
BuildArch: noarch
Url: http://code.google.com/p/python-creole

# sourcecode: http://github.com/jedie/python-creole
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Python lib for:
 - creole markup -> html
 - html -> creole markup
python-creole is pure python. No external libs needed.
The creole2html part based on the creole markup parser and emitter from
the MoinMoin project by Radomir Dopieralski and Thomas Waldmann.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%python3_sitelibdir/python_%oname-*.egg-info
%doc AUTHORS README.%oname LICENSE


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1
- Version 1.2.0
- Added module for Python 3

* Fri May 24 2013 Alexey Shabalin <shaba@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Mon Jul 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.2
- exclude tests from package

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3-alt1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 13 2010 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- first build for Sisyphus
