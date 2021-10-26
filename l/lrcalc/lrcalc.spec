%define soname 2

Name: lrcalc
Version: 2.1
Release: alt1
License: GPL-3.0+
Summary: Littlewood-Richardson Calculator
Group: Sciences/Mathematics
Url: https://math.rutgers.edu/~asbuch/lrcalc

Source: %url/%name-%version.tar.gz
Source1: lrcalc.module.in
# Requires: environment(modules)
# sagemath patch
Patch: includes.patch

BuildRequires: gcc-c++

%description
The "Littlewood-Richardson Calculator" is a package of C and Maple programs
for computing Littlewood-Richardson coefficients. The C programs form the
engine of the package, providing fast calculation of single LR coefficients,
products of Schur functions, and skew Schur functions. The Maple code mainly
gives an interface which makes it possible to use the C programs from Maple.
This interface uses the same notation as the SF package of John Stembridge,
to make it easier to use both packages at the same time.

%package -n lib%name%soname
Summary: Littlewood-Richardson Calculator library
Group: System/Libraries

%description -n lib%name%soname
This subpackage contains the shared library for
launching applications that use %name.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
#%%patch0 -p1

%build
%configure \
    --enable-shared \
    --disable-static

# Kill rpaths
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make

%install
%makeinstall_std
rm %buildroot%_datadir/%name/README
rm %buildroot%_datadir/%name/%name.maple

%check
LD_LIBRARY_PATH=%buildroot%_libdir: make check

%files
%doc AUTHORS ChangeLog COPYING LICENSE README
%_bindir/%name
%_bindir/schubmult

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so

%changelog
* Tue Oct 26 2021 Leontiy Volodin <lvol@altlinux.org> 2.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
