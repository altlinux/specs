%define oname zopemetadatamaker
Name: python-module-%oname
Version: 0.1.0
Release: alt1.1
Summary: Bulk creation of .metadata files for Zope skins resources
License: GPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zopemetadatamaker/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%description
Bulk creation of .metadata files for Zope skins resources.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.0-alt1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

