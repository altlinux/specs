%define oname zope.event

%def_with python3

Name: python-module-%oname
Version: 4.0.3
Release: alt1.1
Summary: Very basic event publishing system
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.event/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/zopefoundation/zope.event.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python3-devel python3-module-distribute
%endif

%py_requires zope

%description
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%if_with python3
%package -n python3-module-%oname
Summary: Very basic event publishing system (Python 3)
Group: Development/Python3
%py3_requires zope

%description -n python3-module-%oname
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

%package -n python3-module-%oname-tests
Summary: Tests for zope.event (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

This package contains tests for zope.event.
%endif

%package tests
Summary: Tests for zope.event
Group: Development/Python
Requires: %name = %version-%release

%description tests
The zope.event package provides a simple event system. It provides:

* An event publishing system
* A very simple event-dispatching system on which more sophisticated
  event dispatching systems can be built. For example, a type-based
  event dispatching system that builds on zope.event can be found in
  zope.component.

This package contains tests for zope.event.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests*

%files tests
%python_sitelibdir/*/*/tests*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests*
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 4.0.3-alt1.1
- NMU: Use buildreq for BR.

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Sun Mar 03 2013 Aleksey Avdeev <solo@altlinux.ru> 4.0.2-alt1
- Version 4.0.2

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.2-alt1
- Version 3.5.2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.1-alt1
- Version 3.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0.1-alt4.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt4
- Added necessary requirement

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt3
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt2
- Set as archdep package

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0.1-alt1
- Initial build for Sisyphus

