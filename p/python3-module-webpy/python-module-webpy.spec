Name: python3-module-webpy
Version: 0.37
Release: alt1.git20130611.1.1
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

Url: http://webpy.org/
# https://github.com/webpy/webpy.git
Source0: web.py-%version.tar.gz

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
BuildArch: noarch

%py3_provides web

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-logging python3 python3-base
BuildRequires: python-modules-compiler python-modules-encodings python-tools-2to3 rpm-build-python3 time

%description
web.py is a web framework for python that is as simple as it is
powerful. web.py is in the public domain; you can use it for whatever
purpose with absolutely no restrictions.

%prep
%setup -n web.py-%version

find web -type f -name '*.py' -exec 2to3 -w -n '{}' +
sed -i 's|qhttp|http|g' web/webapi.py web/httpserver.py

%build
%python3_build

%install
%python3_install

%files
%doc *.txt *.md
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.37-alt1.git20130611.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.37-alt1.git20130611.1
- NMU: Use buildreq for BR.

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.37-alt1.git20130611
- Initial build for Sisyphus

