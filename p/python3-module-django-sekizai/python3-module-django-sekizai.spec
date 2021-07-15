# vim: set ft=spec: -*- rpm-spec -*-

%define oname django-sekizai

Name: python3-module-%oname
Version: 2.0.0
Release: alt1
Summary: Django Template Blocks with extra functionality
License: BSD-3-Clause
Group: Development/Python3

Url: http://django-sekizai.readthedocs.org/
BuildArch: noarch

# https://pypi.org/project/django-sekizai/#files
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-django

%description
Sekizai means "blocks" in Japanese, and that's what this app provides. A fresh
look at blocks. With django-sekizai you can define placeholders where your
blocks get rendered and at different places in your templates append to those
blocks. This is especially useful for css and javascript. Your sub-templates can
now define css and Javascript files to be included, and the css will be nicely
put at the top and the Javascript to the bottom, just like you should. Also
sekizai will ignore any duplicate content in a single block.

%package tests
Summary: tests for Django sekizai
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
mv %buildroot%python3_sitelibdir/tests %buildroot%python3_sitelibdir/sekizai/

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/sekizai/tests

%files tests
%python3_sitelibdir/sekizai/tests

%changelog
* Tue Jul 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.0.0-alt1
- 2.0.0
- Build python3 only.

* Thu Dec 12 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt2
- Fix license.

* Fri Jan 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.10.0-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt4.git20140813.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7-alt4.git20140813.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt4.git20140813.1
- NMU: Use buildreq for BR.

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.7-alt4.git20140813
- Rebuild with "def_disable check"
- Clean buildreq

* Mon Sep 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt3.git20140813
- New snapshot
- Added module for Python 3

* Fri Oct 04 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt3.1
- Fix build requires.

* Tue Apr 02 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt3
- Fix build requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt2
- Fix requires

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux Sisyphus
