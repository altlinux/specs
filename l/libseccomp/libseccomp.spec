%define oname seccomp

%def_with python3

Name: lib%oname
Version: 2.3.3
Release: alt1%ubt
Summary: High level interface to the Linux Kernel's seccomp filter
License: LGPLv2.1+
Group: System/Libraries
Url: https://github.com/seccomp/libseccomp

#https://github.com/seccomp/libseccomp.git
Source: %name-%version.tar
Patch100: 0001-Tune-config.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-devel python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-Cython
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
%patch100 -p1

%if_with python3
cp -fR . ../python3
pushd ../python3
sed -i 's|cython -V|cython3 -V|' configure.ac
popd
%endif

%build
subst 's/AC_INIT(\[libseccomp\], \[0.0.0\])/AC_INIT([libseccomp],[%version])/' configure.ac
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

mkdir -p %buildroot/%_lib
# Relocate shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/lib*.so; do
        t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
        [ -n "$t" ]
        ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/


%files
%doc CHANGELOG CREDITS README.md SUBMITTING_PATCHES
%_bindir/*
/%_lib/lib*.so.*
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
* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 2.3.3-alt1%ubt
- 2.3.3

* Fri Dec 15 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.2-alt1%ubt
- 2.3.2

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Wed Apr 20 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.3-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Dec 17 2015 Alexey Shabalin <shaba@altlinux.ru> 2.2.3-alt1
- 2.2.3
- relocate shared libraries from %_libdir/ to /%_lib/.

* Thu Aug 27 2015 Afanasov Dmitry <ender@altlinux.org> 2.1.1-alt2.git20141021
- fix version in pkg-config file

* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20141021
- Initial build for Sisyphus

