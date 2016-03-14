%define oname zope.z2release

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt2.1
Summary: Zope release helper
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.z2release/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope

%description
zope.z2releases is used to generated a PyPI compatible index with
references to all pinned package versions based on a versions.cfg.

It can handle both a Zope 2 release as well as a Zope Toolkit release.

%package -n python3-module-%oname
Summary: Zope release helper
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
zope.z2releases is used to generated a PyPI compatible index with
references to all pinned package versions based on a versions.cfg.

It can handle both a Zope 2 release as well as a Zope Toolkit release.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

