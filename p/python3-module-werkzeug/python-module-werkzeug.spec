%define oname werkzeug

%def_with python3
%def_disable check

Name: python3-module-%oname
Version: 0.16.1
Release: alt2

Summary: Werkzeug is one of the most advanced WSGI utility modules

License: BSD-3-Clause
Group: Development/Python3
URL: http://werkzeug.pocoo.org/

BuildArch: noarch

# https://github.com/pallets/werkzeug.git
Source: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%description
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%check
python3 ./setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 0.16.1-alt2
- build only python3 package

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.
- Fix License tag according SPDX.
- Build from upstream tag.

* Fri Aug 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.15.5-alt1
- Version updated to 0.15.5

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.1-alt1
- Updated to upstream version 0.14.1.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.8.3-alt1
- 0.8.3 (ALT #28297);
- minor packaging improvements.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
