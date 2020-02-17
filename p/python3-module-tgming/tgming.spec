%define oname tgming

%def_without bootstrap

Name:       python3-module-%oname
Version:    0.0.8
Release:    alt3

Summary:    TurboGears2 Support for Ming MongoDB ORM
License:    MIT
Group:      Development/Python3
Url:        http://pypi.python.org/pypi/tgming/

BuildArch:  noarch

Source:     %name-%version.tar
Patch0:     fix-incompatibility-with-new-zope.interface.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%if_with bootstrap
%add_python3_req_skip ming
%endif


%description
tgming is used by TurboGears2 to support ming backend. To create a ming
project just use quickstart command with --ming option it will
automatically setup tgming and all the required dependencies.

%prep
%setup
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO *.rst
%python3_sitelibdir/*


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.8-alt3
- Build for python2 disabled.

* Fri May 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.8-alt2.3
- rebuild with all requires

* Sun May 20 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.8-alt2.2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.8-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Version 0.0.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus
