%define _unpackaged_files_terminate_build 1
%define oname django-countries

Name: python3-module-%oname
Version: 4.0
Release: alt2

Group: Development/Python3
License: BSD License
Summary: Provides a country field for Django models.
URL: https://pypi.python.org/pypi/django-countries
# https://github.com/SmileyChris/django-countries.git

Source0: https://pypi.python.org/packages/91/88/c99df63539deafc9306158e65965e1774eebf3a9f39c8bb2314369fb79a8/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides django_countries


%description
Provides a country field for Django models.

%prep
%setup -q -n %{oname}-%{version}

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%files
%doc *.rst
%python3_sitelibdir/django_countries*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.0-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0.1-alt1.git20141027.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20141027
- Version 3.0.1

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1.git20140829
- Version 2.1.2
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2-alt1
- build for ALT
