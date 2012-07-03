%define oname zope.z2release
Name: python-module-%oname
Version: 0.8
Release: alt2.1
Summary: Zope release helper
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.z2release/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
zope.z2releases is used to generated a PyPI compatible index with
references to all pinned package versions based on a versions.cfg.

It can handle both a Zope 2 release as well as a Zope Toolkit release.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

