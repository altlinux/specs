%define _unpackaged_files_terminate_build 1
%define module_name django-country-dialcode

%def_with bootstrap

Name: python3-module-%module_name
Version: 0.5.1
Release: alt3

Summary: Application providing Dialcode and Countries code
License: MIT
Group: Development/Python3
Url: https://github.com/Star2Billing/django-country-dialcode
BuildArch: noarch

# https://github.com/Star2Billing/django-country-dialcode.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3

%if_with bootstrap
%add_python3_req_skip django.conf.urls.defaults django.core.urlresolvers
%endif


%description
Application providing Dialcode and Countries code

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
export LC_ALL=en_US.UTF-8
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs html

%files
%doc HACKING README.rst MIT-LICENSE.txt docs/build/html
%python3_sitelibdir/country_dialcode*
%python3_sitelibdir/django_country_dialcode*


%changelog
* Mon Dec 16 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt3
- build for python2 disabled

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20140716.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.1-alt1.git20140716.1
- NMU: Use buildreq for BR.

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20140716
- Version 0.5.1
- Added module for Python 3

* Sat May 05 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux
