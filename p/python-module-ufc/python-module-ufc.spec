%define origname ufc

Name:           python-module-%origname
Version:        2.0.5
Release:        alt1.bzr20120511
Summary:        Unified Form-assembly Code
Group:          Development/Python
License:        Public domain
URL:            http://www.fenics.org/ufc/
# bzr branch lp:ufc
Source:        %origname-%version.tar.gz
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel swig boost-devel gcc-c++ cmake
%setup_python_module ufc

%description
UFC (Unified Form-assembly Code) is a unified framework for finite
element assembly. More precisely, it defines a fixed interface for
communicating low level routines (functions) for evaluating and
assembling finite element variational forms. The UFC interface
consists of a single header file ufc.h that specifies a C++ interface
that must be implemented by code that complies with the UFC
specification. Examples of form compilers that support the UFC
interface are FFC and SyFi.

%package -n %origname-devel
Summary: Development files for UFC
Group: Development/Other
Requires: %name = %version-%release

%description -n %origname-devel
UFC (Unified Form-assembly Code) is a unified framework for finite
element assembly. More precisely, it defines a fixed interface for
communicating low level routines (functions) for evaluating and
assembling finite element variational forms. The UFC interface
consists of a single header file ufc.h that specifies a C++ interface
that must be implemented by code that complies with the UFC
specification. Examples of form compilers that support the UFC
interface are FFC and SyFi.

This package contains development files for UFC.

%package -n %origname-manual
Summary: User manual for UFC
Group: Development/Documentation
BuildArch: noarch

%description -n %origname-manual
UFC (Unified Form-assembly Code) is a unified framework for finite
element assembly. More precisely, it defines a fixed interface for
communicating low level routines (functions) for evaluating and
assembling finite element variational forms. The UFC interface
consists of a single header file ufc.h that specifies a C++ interface
that must be implemented by code that complies with the UFC
specification. Examples of form compilers that support the UFC
interface are FFC and SyFi.

This package contains user manual for developers.

%package -n python-module-ufc_utils
Summary: Code generation format strings for UFC
Group: Development/Python
BuildArch: noarch

%description -n python-module-ufc_utils
UFC (Unified Form-assembly Code) is a unified framework for finite
element assembly. More precisely, it defines a fixed interface for
communicating low level routines (functions) for evaluating and
assembling finite element variational forms. The UFC interface
consists of a single header file ufc.h that specifies a C++ interface
that must be implemented by code that complies with the UFC
specification. Examples of form compilers that support the UFC
interface are FFC and SyFi.

This package contains code generation format strings for UFC.

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags %optflags_shared" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_STRIP:FILEPATH=/bin/echo \
	.
%make_build

#pushd src/utils/python/ufc_benchmark
#export CC=g++
#python_build_debug
#popd

%install
%makeinstall_std

#pushd src/utils/python/ufc_benchmark
#python_install
#popd

%ifarch x86_64
install -d %buildroot%_pkgconfigdir
mv %buildroot%_libexecdir/pkgconfig/* %buildroot%_pkgconfigdir/
rmdir %buildroot%_libexecdir/pkgconfig
%endif

sed -i 's|%buildroot||' %buildroot%_pkgconfigdir/ufc-1.pc
sed -i 's|^\(Version\).*|\1: %version|' %buildroot%_pkgconfigdir/ufc-1.pc

install -d %buildroot%_docdir/%origname
install -p -m644 doc/manual/ufc-user-manual.pdf %buildroot%_docdir/%origname

%files
%doc AUTHORS ChangeLog README TODO
%python_sitelibdir/*

%files -n %origname-devel
%_includedir/*
%_pkgconfigdir/*
%_datadir/%origname

%files -n %origname-manual
%_docdir/%origname

%files -n python-module-ufc_utils
%python_sitelibdir_noarch/ufc_utils

%changelog
* Sun May 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.bzr20120511
- New snapshot

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.5-alt1.bzr20111207.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1.bzr20111207
- Version 2.0.5

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.bzr20111128
- Version 2.0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.bzr201100627.1.1
- Rebuild with Python-2.7

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.bzr201100627.1
- Rebuilt with SWIG 2.0.4

* Wed Aug 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.bzr201100627
- Version 2.0.1

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.bzr20110314
- Version 2.0.0

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20101028.3
- Rebuilt with SWIG 2.0.2

* Wed Mar 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20101028.2
- Rebuilt for debuginfo

* Thu Dec 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20101028.1
- Fixed pkg-config file

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20101028
- New snapshot

* Thu Nov 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20100701.1
- Rebuilt with SWIG 2.0.1

* Tue Aug 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.bzr20100701
- Version 1.4.1

* Thu Jul 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.bzr20100527.1
- Rebuilt with SWIG 2.0.0

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.bzr20100527
- Version 1.4.0

* Wed Mar 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.bzr20091119.1
- Rebuilt with new SWIG

* Wed Dec 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.bzr20091119
- Version 1.2.0

* Tue Nov 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt5.hg20090831.1
- Rebuilt with python 2.6

* Mon Aug 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt5.hg20090831
- Snapshot 20090831

* Wed Aug 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt5.hg20090819
- New snapshot

* Sun Jul 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt4
- Rebuild with SWIG 1.3.39

* Wed May 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt3
- Rebuild with gcc 4.4

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt2
- Add requirement on instant

* Fri Apr 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Initial build for Sisyphus
