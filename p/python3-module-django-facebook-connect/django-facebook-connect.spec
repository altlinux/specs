%define oname django-facebook-connect

%def_with bootstrap

Name: python3-module-%oname
Version: 1.0.2
Release: alt3

Summary: Add facebook connect authentication to your Django website
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-facebook-connect/
BuildArch: noarch

# https://github.com/noamsu/django-facebook-connect.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults
%endif


%description
This package adds facebook connect authentication to a Django web site.
Many of the existing packages are either out of date, using soon to be
deprecated facebook apis (along with out of date documentation), or
simply do not work quite right.

This package is small, does not have external dependencies, and should
"just work".

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- build for python2 disabled

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.git20121127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20121127
- Initial build for Sisyphus

