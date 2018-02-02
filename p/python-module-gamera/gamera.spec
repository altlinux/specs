%define oname gamera

%def_without python3

Name: python-module-%oname
Version: 3.4.2
Release: alt3.1
Summary: Framework for building document analysis applications
License: GPLv2
Group: Development/Python
Url: http://gamera.informatik.hsnr.de/

Source: %name-%version.tar
Patch1: %oname-%version-upstream-build1.patch
Patch2: %oname-%version-upstream-build2.patch

BuildPreReq: gcc-c++ libtiff-devel libpng-devel libgomp-devel
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-wx python-module-docutils python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires wx docutils

%description
Gamera is not a packaged document recognition system, but a toolkit for
building document image recognition systems. It makes the development of
new recognition system quite easy, though this still requires some time
commitment. Gamera is a cross platform library for the Python
programming language. Apart from providing a set of commonly needed
functionality for document image analysis, Gamera additionally allows
for custom extensions as C++ or Python Plugins and as Toolkits.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Gamera is not a packaged document recognition system, but a toolkit for
building document image recognition systems. It makes the development of
new recognition system quite easy, though this still requires some time
commitment. Gamera is a cross platform library for the Python
programming language. Apart from providing a set of commonly needed
functionality for document image analysis, Gamera additionally allows
for custom extensions as C++ or Python Plugins and as Toolkits.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Framework for building document analysis applications
Group: Development/Python3
%py3_requires docutils
%add_python3_req_skip wx

%description -n python3-module-%oname
Gamera is not a packaged document recognition system, but a toolkit for
building document image recognition systems. It makes the development of
new recognition system quite easy, though this still requires some time
commitment. Gamera is a cross platform library for the Python
programming language. Apart from providing a set of commonly needed
functionality for document image analysis, Gamera additionally allows
for custom extensions as C++ or Python Plugins and as Toolkits.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Gamera is not a packaged document recognition system, but a toolkit for
building document image recognition systems. It makes the development of
new recognition system quite easy, though this still requires some time
commitment. Gamera is a cross platform library for the Python
programming language. Apart from providing a set of commonly needed
functionality for document image analysis, Gamera additionally allows
for custom extensions as C++ or Python Plugins and as Toolkits.

This package contains tests for %oname.
%endif

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Gamera is not a packaged document recognition system, but a toolkit for
building document image recognition systems. It makes the development of
new recognition system quite easy, though this still requires some time
commitment. Gamera is a cross platform library for the Python
programming language. Apart from providing a set of commonly needed
functionality for document image analysis, Gamera additionally allows
for custom extensions as C++ or Python Plugins and as Toolkits.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1
%patch2 -p1

%if_with python3
rm -rf ../python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug --openmp=yes

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build_debug --openmp=yes
popd
%endif

%install
%python_install --openmp=yes
%if "%python_sitelibdir_noarch/%oname" != "%python_sitelibdir/%oname"
mv %buildroot%python_sitelibdir_noarch/%oname/src \
	%buildroot%python_sitelibdir/%oname/
%endif

%if_with python3
pushd ../python3
%python3_install --openmp=yes
popd
%if "%python3_sitelibdir_noarch/%oname" != "%python3_sitelibdir/%oname"
mv %buildroot%python3_sitelibdir_noarch/%oname/src \
	%buildroot%python3_sitelibdir/%oname/
%endif
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd doc
./gendoc.py
popd

%check
export PYTHONPATH=%buildroot%python_sitelibdir
pushd tests
py.test -vv
popd
%if_with python3
pushd ../python3/tests
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv
popd
%endif

%files
%doc ACKNOWLEDGEMENTS CHANGES examples KNOWN_BUGS README TODO
%_bindir/*
%_includedir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files docs
%doc doc/html/*

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc ACKNOWLEDGEMENTS CHANGES examples KNOWN_BUGS README TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.2-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.2-alt3
- Fixed build.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.2-alt2.1
- (AUTO) subst_x86_64.

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.4.2-alt2
- NMU: added python-module-Pygments to BRs.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.2-alt1
- Initial build for Sisyphus

