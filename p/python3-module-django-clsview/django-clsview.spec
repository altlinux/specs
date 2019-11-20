%define oname django-clsview

Name: python3-module-%oname
Version: 0.0.3
Release: alt2

Summary: Yet another class-based view system for Django
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-clsview/
# https://github.com/zacharyvoase/django-clsview.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
django-clsview is a library with yet another solution to the problem of
class-based views in Django.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' setup.py
sed -i 's|#!python|#!/python3|' distribute_setup.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md UNLICENSE
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.3-alt1.git20100818.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.3-alt1.git20100818.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20100818
- Initial build for Sisyphus

