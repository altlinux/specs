Name: python3-module-webpy
Version: 0.62
Release: alt1
Summary: A simple web framework for Python
Group: Development/Python3

# The entire source code is Public Domain save for the following exceptions:
#   web/wsgiserver (CherryPy/BSD)
#     See LICENSE.wsgiserver.txt
#     See http://fedoraproject.org/wiki/Licensing:BSD#New_BSD_.28no_advertising.2C_3_clause.29
#   web/debugerror.py (Modified BSD)
#     This is from django
#     See http://code.djangoproject.com/browser/django/trunk/LICENSE
#   web/httpserver.py (Modified BSD)
#     This is from WSGIUtils/lib/wsgiutils/wsgiServer.py
#     See http://www.xfree86.org/3.3.6/COPYRIGHT2.html#5
License: Public Domain and BSD
# VCS: https://github.com/webpy/webpy
Url: http://webpy.org/
# https://github.com/webpy/webpy.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildArch: noarch

%py3_provides web

BuildRequires: rpm-build-python3 

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions.

%prep
%setup 

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.md
%python3_sitelibdir/*

%changelog
* Tue Dec 07 2021 Anton Farygin <rider@altlinux.ru> 0.62-alt1
- 0.40 -> 0.62

* Tue Oct 01 2019 Anton Farygin <rider@altlinux.ru> 0.40-alt1
- updated to 0.40

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.37-alt1.git20130611.1.2
- (NMU) rebuild with python3.6

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.37-alt1.git20130611.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.37-alt1.git20130611.1
- NMU: Use buildreq for BR.

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37-alt1.git20130611
- Initial build for Sisyphus

