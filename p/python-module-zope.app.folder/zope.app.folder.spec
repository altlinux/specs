%define oname zope.app.folder

%def_with python3

Name: python-module-%oname
Version: 3.5.2
Release: alt3.1
Summary: Folder Content Type for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.folder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.container zope.site zope.app.content

%description
This packages provides the standard Folder content type for Zope 3. It
also implements the root folder of a Zope application. Folders can also
be converted to sites, which allow one to register components locally.

%package -n python3-module-%oname
Summary: Folder Content Type for Zope 3
Group: Development/Python3
%py3_requires zope.container zope.site zope.app.content

%description -n python3-module-%oname
This packages provides the standard Folder content type for Zope 3. It
also implements the root folder of a Zope application. Folders can also
be converted to sites, which allow one to register components locally.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.5.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.2-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Initial build for Sisyphus

