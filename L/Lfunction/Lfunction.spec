%define soname 1

Name: Lfunction
Version: 1.23
Release: alt1

Summary: C++ L-function command line interface

License: GPL-2.0+
Group: Sciences/Mathematics
Url: http://oto.math.uwaterloo.ca/~mrubinst/L_function_public/L.html

Source: http://oto.math.uwaterloo.ca/~mrubinst/L_function_public/CODE/L-1.23.tar.gz
# From sage tarball, lcalc spkg, debian directory
Source1: lcalc.1

### Sagemath patches
# Fix minor code issues that clang warns about; gcc does not warn, but apply
# the fixes anyway for parity with sagemath
Patch: clang.patch
# Fix malformed default parameter declarations for compatibility with gcc 4.9+
Patch1: lcalc-1.23_default_parameters_1.patch
# Fix malformed default parameter declarations for compatibility with gcc 5+
Patch2: lcalc-1.23_default_parameters_2.patch
# Fix the lcalc_to_double definition
Patch3: Lcommon.h.patch
# Fix various Makefile issues
Patch4: Makefile.patch
# Fixes for compatibility with pari 2.7+ and 2.9+
Patch5: pari-2.7.patch
# Fix the pari include path
Patch6: pari_include.patch
# Tell pari to use less memory
Patch7: pari-mem.patch
# Add a missing include of time.h
Patch8: time.h.patch
# Fix some declarations related to the std namespace
Patch9: using_namespace_std.patch
# Add a missing return statement
Patch10: Lvalue.h.patch
### End of Sagemath patches

### Fedora patches
# Update obsolete uses of strstream to modern stringstream
Patch100: stringstream.patch
# Call the unlink system call instead of forking a shell
Patch101: unlink.patch
# Rearrange #includes to avoid bad macro expansions with gcc 11
Patch102: gcc11.patch

BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: pari-devel
BuildRequires: libmpfr-devel

%description
C++ L-function command line interface.

%package -n lib%name%soname
Summary: C++ L-function class library
Group: System/Legacy libraries

%description -n lib%name%soname
C++ L-function class library.

%package -n lib%name-devel
Summary: Development libraries/headers for %name
Group: Development/Other

%description -n lib%name-devel
Headers and libraries for development with %name.

%prep
%setup -n L-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1

# Clean up unnecessary and prebuilt files
rm -f .*DS_Store
rm -f include/*.{swap.crap,bak}
rm -f include/.*{DS_Store,.swp}
rm -f src/.*{DS_Store,.swp}
rm -f src/{Makefile.old,libLfunction.a}

# Give the library an soname, use Fedora link flags, and do not override Fedora
# build flags
sed -e 's|/lib/|/%_lib/|g' \
 -e "s|\(DYN_OPTION=shared\)|\1 -Wl,-soname=libLfunction.so.%version $RPM_LD_FLAGS|" \
 -e 's/^\([[:blank:]]*MACHINE_SPECIFIC_FLAGS = \).*/\1-ffast-math -fPIC/' \
 -i src/Makefile

# Fix end of line encodings
subst 's/\r//' src/example_programs/example.cc

%build
pushd src
# Create link before library is created
ln -sf libLfunction.so.%version libLfunction.so
%make_build all EXTRA="$RPM_OPT_FLAGS"
popd
rm -f src/example_programs/example

%install
mkdir -p %buildroot{%_includedir,%_libdir,%_bindir,%_man1dir}
pushd src
    make INSTALL_DIR="%buildroot%prefix" install
    mkdir -p %buildroot%_datadir/%name
    pushd example_data_files
    for sample in *; do
        install -p -m644 $sample %buildroot%_datadir/%name/$sample
    done
    popd
    install -m644 example_programs/example.cc \
    %buildroot%_datadir/%name/example.cc
popd
install -p -m644 %SOURCE1 %buildroot%_man1dir
install -m755 src/libLfunction.so.%version %buildroot%_libdir
ln -sf libLfunction.so.%version %buildroot%_libdir/libLfunction.so
# Correct permissions
chmod 644 %buildroot%_includedir/Lfunction/*.h

%files
%doc CONTRIBUTORS
%doc COPYING
%doc README
%_bindir/lcalc
%_man1dir/*

%files -n lib%name%soname
%_libdir/libLfunction.so.%version

%files -n lib%name-devel
%doc %_datadir/%name
%_includedir/Lfunction/
%_libdir/libLfunction.so

%changelog
* Wed Oct 27 2021 Leontiy Volodin <lvol@altlinux.org> 1.23-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
