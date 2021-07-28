%define oname tornado_xstatic

Name: python3-module-%oname
Version: 0.1
Release: alt1.git20140929.3
Summary: Utilities for using XStatic in Tornado applications
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tornado_xstatic/

# https://github.com/takluyver/tornado_xstatic.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires tornado

BuildRequires: python3-module-pycares python3-module-pytest python3-module-zope

%description
XStatic is a means of packaging static files, especially JS libraries,
for Python applications. Tornado is a Python web framework.

This integration provides two pieces:

* XStaticFileHandler to serve static files from XStatic packages.
* url_maker to build URLs for XStatic files, including the ?v=... tag
  that Tornado uses for cache invalidation.

%prep
%setup

%build
%python3_build

%install
%python3_install

#check
#py.test3

%files
%doc *.rst *.html example.py
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 0.1-alt1.git20140929.3
- Drop python2 support.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1-alt1.git20140929.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20140929.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140929.1
- NMU: Use buildreq for BR.

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140929
- Initial build for Sisyphus

