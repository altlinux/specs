%define oname seccomp

%def_with python3

Name: lib%oname
Version: 2.1.1
Release: alt1.git20141021
Summary: High level interface to the Linux Kernel's seccomp filter
License: LGPLv2
Group: System/Libraries
Url: http://sourceforge.net/projects/libseccomp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://git.code.sf.net/p/libseccomp/libseccomp
Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython
%endif

%description
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

%package devel
Summary: Development files of %name
Group: Development/C
Requires: %name = %EVR

%description devel
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

This package contains development files of %name.

%package -n python-module-%oname
Summary: Python bindings of %name
Group: Development/Python

%description -n python-module-%oname
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

This package contains python bindings of %name.

%package -n python3-module-%oname
Summary: Python bindings of %name
Group: Development/Python3

%description -n python3-module-%oname
The libseccomp library provides and easy to use, platform independent,
interface to the Linux Kernel's syscall filtering mechanism: seccomp.
The libseccomp API is designed to abstract away the underlying BPF based
syscall filter language and present a more conventional function-call
based filtering interface that should be familiar to, and easily adopted
by application developers.

This package contains python bindings of %name.

%prep
%setup

%if_with python3
cp -fR . ../python3
pushd ../python3
sed -i 's|cython -V|cython3 -V|' configure.ac
popd
%endif

%build
./autogen.sh
%configure \
	--enable-python
%make_build V=1

%if_with python3
pushd ../python3
./autogen.sh
%configure \
	--enable-python
%make_build V=1 PYTHON=python3
popd
%endif

%install
%makeinstall_std

%if_with python3
pushd ../python3
%make_install DESTDIR=$PWD/buildroot PYTHON=python3 install
install -d %buildroot%python3_sitelibdir
mv buildroot%python3_sitelibdir/* %buildroot%python3_sitelibdir/
popd
%endif

%files
%doc CHANGELOG CREDITS README SUBMITTING_PATCHES
%_bindir/*
%_libdir/*.so.*
%_man1dir/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/*

%files -n python-module-%oname
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20141021
- Initial build for Sisyphus

