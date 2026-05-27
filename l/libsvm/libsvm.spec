%define _unpackaged_files_terminate_build 1
%define sover 4

%def_with python3
%def_with java
%def_with octave

Name: libsvm
Version: 3.37
Release: alt1
Summary: A Library for Support Vector Machines
Group: Sciences/Mathematics
License: BSD-3-Clause
URL: http://www.csie.ntu.edu.tw/~cjlin/libsvm/
VCS: https://github.com/cjlin1/libsvm
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
%endif
%if_with java
BuildRequires(pre): rpm-macros-java
BuildRequires: java-devel-default
%endif
%if_with octave
BuildRequires(pre): rpm-build-octave
BuildRequires: octave-devel
%endif

%description
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package -n %name%sover
Summary: A Library for Support Vector Machines
Group: Sciences/Mathematics

%description -n %name%sover
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package devel
Summary: Development files of LIBSVM
Group: Development/C++
Requires: %name%sover = %EVR

%description devel
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains development files of LIBSVM.

%package tools
Summary: Tools for LIBSVM
Group: Sciences/Mathematics
Requires: gnuplot

%description tools
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains tools for LIBSVM.

%if_with python3
%package -n python3-module-%name
Summary: Python interface for LIBSVM
Group: Development/Python3
BuildArch: noarch

Provides: python3-module-svm = %EVR
Obsoletes: python3-module-svm < %EVR
Requires: %name%sover = %EVR

%description -n python3-module-%name
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains Python interface for LIBSVM.
%endif

%if_with java
%package java
Summary: Java implementation of LIBSVM
Group: Development/Java
BuildArch: noarch
Requires: java

%description java
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains native Java implementation of LIBSVM.
%endif

%if_with octave
%global octpkg %name

%package -n octave-%octpkg
Summary: Octave interface for LIBSVM
Group: Sciences/Mathematics
Requires: octave

%description -n octave-%octpkg
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

This package contains Octave interface for LIBSVM.
%endif

%prep
%setup
%autopatch -p1
%python3_fix_shebang tools

%build
%make_build all

%if_with python3
pushd python
%pyproject_build
popd
%endif

%if_with java
%make_build -C java all
%endif

%if_with octave
pushd matlab
export LDFLAGS=-Wl,-rpath,$(octave-config -p OCTLIBDIR)
%octave_cmd make
popd
%endif

%install

install -pD -m644 -t %buildroot%_libdir libsvm.so.%sover
ln -s libsvm.so.%sover %buildroot%_libdir/libsvm.so

install -pD -m644 -t %buildroot%_includedir *.h

install -pD -m755 -t %buildroot%_bindir \
	svm-predict svm-scale svm-train
for py in $(cd tools && ls *.py); do
	install -pD -m755 tools/$py %buildroot%_bindir/svm-${py%%.py}
done

%if_with python3
pushd python
%pyproject_install
popd
%endif

%if_with java
install -pD -m644 -t %buildroot%_javadir java/libsvm.jar
%endif

%if_with octave
install -pD -m644 -t %buildroot%octpkglibdir matlab/*.mex
install -pD -m644 -t %buildroot%octpkglibdir/packinfo matlab/INDEX
install -pD -m644 COPYRIGHT %buildroot%octpkglibdir/packinfo/COPYING
sed \
	-e "s/@VERSION@/%version/" \
	-e "s/@DATE@/$(date -I)/" \
	matlab/DESCRIPTION.in > %buildroot%octpkglibdir/packinfo/DESCRIPTION
%endif

%if_with octave
# Prefixes are set temporarily to make Octave see the package

%post -n octave-%octpkg
%octave_cmd pkg prefix %octarchprefix; pkg rebuild

%postun -n octave-%octpkg
%octave_cmd pkg prefix %octarchprefix; pkg rebuild
%endif

%files -n %name%sover
%doc COPYRIGHT README *.html
%_libdir/*.so.%sover

%files devel
%_libdir/*.so
%_includedir/*

%files tools
%doc tools/README
%_bindir/svm-*

%if_with python3
%files -n python3-module-%name
%doc python/README
%python3_sitelibdir_noarch/%name
%python3_sitelibdir_noarch/%{name}_official-*.dist-info
%endif

%if_with java
%files java
%_javadir/*.jar
%endif

%if_with octave
%files -n octave-%octpkg
%doc matlab/README
%octpkglibdir
%endif

%changelog
* Sat May 23 2026 Valery Zabrovsky <brow@altlinux.org> 3.37-alt1
- New version 3.37.
- Apply Shared Libs Policy to new sover.
- Enable Java implementation and Octave bindings.
- Build Python module with pyproject and rename it to libsvm.
- Use dynamic linking wherever possible.
- Enable OpenMP and re-enable debuginfo for libsvm.

* Sat May 16 2026 Anton Midyukov <antohami@altlinux.org> 3.24-alt3
- NMU: Build without python2 module; cleanup Packager.

* Mon Apr 13 2020 Pavel Vasenkov <pav@altlinux.org> 3.24-alt2
- Set correct tag.

* Mon Apr 05 2020 Pavel Vasenkov <pav@altlinux.org> 3.24-alt1
- Version 3.24

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.18-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18-alt2
- Added module for Python 3

* Thu Jun 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.18-alt1
- Version 3.18

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.17-alt1
- Version 3.17

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.16-alt1
- Version 3.16

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt2
- Fixed build

* Wed Sep 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12-alt1
- Version 3.12

* Wed Dec 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.11-alt1
- Version 3.11

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1-alt1.1
- Rebuild with Python-2.7

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1-alt1
- Version 3.1

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Wed Jul 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.91-alt1
- Initial build for Sisyphus

