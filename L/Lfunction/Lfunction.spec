%define soname 1

Name: Lfunction
Version: 2.0.5
Release: alt1

Summary: C++ L-function command line interface

License: GPL-2.0+
Group: Sciences/Mathematics
Url: https://gitlab.com/sagemath/lcalc

Source: %url/-/archive/%version/lcalc-%version.tar.bz2

# Fix use of the wrong delete operator
# https://gitlab.com/sagemath/lcalc/-/merge_requests/5
Patch: L-function-mismatched-delete.patch

Provides: L-function = %version-%release

BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: pari-devel
BuildRequires: libmpfr-devel
BuildRequires: gengetopt

%description
C++ L-function command line interface.

%package -n lib%name%soname
Summary: C++ L-function class library
Group: System/Libraries

%description -n lib%name%soname
C++ L-function class library.

%package -n lib%name-devel
Summary: Development libraries/headers for %name
Group: Development/Other

%description -n lib%name-devel
Headers and libraries for development with %name.

%prep
%setup -n lcalc-%version
%patch -p1

%build
%autoreconf
%configure --with-pari

# Get rid of undesirable hardcoded rpaths.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build

%install
%makeinstall_std

rm %buildroot%_libdir/libLfunction.la
# We select the files we want in doc
rm -fr %buildroot%_docdir/lcalc

%files
%doc doc/{ChangeLog,CONTRIBUTORS,README.md,COPYING}
%_bindir/lcalc
%_man1dir/lcalc.1*

%files -n lib%name%soname
%_libdir/libLfunction.so.%{soname}*

%files -n lib%name-devel
%doc doc/examples
%_includedir/lcalc/
%_libdir/libLfunction.so
%_pkgconfigdir/lcalc.pc

%changelog
* Thu Mar 02 2023 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version.
- Updated url and source links.

* Wed Oct 27 2021 Leontiy Volodin <lvol@altlinux.org> 1.23-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
