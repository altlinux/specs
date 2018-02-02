%define oname WebDAV
Name: python-module-%oname
Version: 0.4.2
Release: alt2.1
Summary: This library provides a WebDAV client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/Python_WebDAV_Library/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools
BuildArch: noarch

%description
This library provides a WebDAV client including ACP and searching
support.

%package -n python-module-webdav
Summary: webdav submodule
Group: Development/Python
Requires: %name = %EVR
Conflicts: python-module-Zope2

%description -n python-module-webdav
This library provides a WebDAV client including ACP and searching
support.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/webdav

%files -n python-module-webdav
%python_sitelibdir/webdav

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Moved webdav into separate package

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

