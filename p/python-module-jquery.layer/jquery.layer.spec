%define oname jquery.layer
Name: python-module-%oname
Version: 1.0.0
Release: alt1.1
Summary: Base layers for JQuery functionality
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/jquery.layer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires zope.publisher zope.viewlet jquery

%description
This package provides the layer into which all of the resources and
views related to JQuery are registered. The developer can then choose
from those layers to build a new skin.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt1.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

