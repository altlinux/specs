%def_without openblas

%define lname libfflas0

Name: fflas-ffpack
Version: 2.4.3
Release: alt3

Summary: Finite Field Linear Algebra Subroutines
License: LGPL-2.1+
Group: Sciences/Mathematics

Url: https://linbox-team.github.io/fflas-ffpack/
#Git-Clone: https://github.com/linbox-team/fflas-ffpack
Source: https://github.com/linbox-team/fflas-ffpack/releases/download/%version/fflas-ffpack-%version.tar.gz
Patch: reproducible.patch

# Couldn't find package libatlas-devel on aarch64, armh and ppc64le.
ExclusiveArch: i586 x86_64 %e2k

BuildPreReq: fdupes
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: libgmp-devel >= 3.1.1
BuildRequires: libtool >= 2.2
%if_with openblas
BuildRequires: libopenblas-devel
%else
BuildRequires: libatlas-devel
%endif
BuildRequires: libgivaro-devel

%description
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

%package devel
Summary: Development files for FFLAS-FFPACK
Group: Development/Other

%description devel
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

This subpackage contains the include files for
developing against the fflas-ffpack library.

%package doc
Summary: API documentation for FFLAS-FFPACK
Group: Documentation
BuildArch: noarch

%description doc
The FFLAS-FFPACK library provides functionalities for dense linear
algebra over word size prime finite field.

This subpackage contains the Doxygen-generated HTML documentation for
the FFLAS-FFPACK API.

%prep
%setup
%patch -p1

#Do not compile in DATE and TIME
sed '/HTML_TIMESTAMP/s/YES/NO/' -i doc/Doxyfile

%build
# tarball strangely created; wants to rerun aclocal-1.15.
%autoreconf

trap "cat config.log; exit 1" ERR
%configure \
	--with-blas-cflags=" " \
%if_with openblas
	--with-blas-libs="-lopenblas" \
%else
	--with-blas-libs="-lcblas -lblas" \
%endif
	--enable-doc --with-docdir="%_docdir/%name" --disable-simd
trap "" ERR
%make_build

%install
%makeinstall_std
rm -f "%buildroot%_docdir/%name/fflas-ffpack-html/INSTALL"
fdupes %buildroot%prefix

%ifarch %e2k
# unsupported as of lcc 1.25.20 (linbox-1.6.3 ftbfs)
sed -i 's,-fabi-version=6,,' \
	%buildroot%_bindir/fflas-ffpack-config \
	%buildroot%_pkgconfigdir/fflas-ffpack.pc
%endif

%files devel
%doc ChangeLog
%doc COPYING.LESSER
%_bindir/fflas-ffpack-config
%_includedir/fflas-ffpack/
%_pkgconfigdir/ff*.pc

%files doc
%_docdir/%name/

%changelog
* Wed Jan 19 2022 Michael Shigorin <mike@altlinux.org> 2.4.3-alt3
- E2K: avoid lcc-unsupported option hardwired into fflas-ffpack-config

* Sat Jan 15 2022 Michael Shigorin <mike@altlinux.org> 2.4.3-alt2
- E2K: build against openblas (specified on girar side)
- minor spec cleanup

* Thu Nov 11 2021 Leontiy Volodin <lvol@altlinux.org> 2.4.3-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
- Built as require for sagemath.
