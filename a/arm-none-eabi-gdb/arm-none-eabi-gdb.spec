%define target arm-none-eabi

Name: arm-none-eabi-gdb
Version: 7.9
Release: alt1
Summary: GDB for (remote) debugging %target binaries
Group: Development/Debuggers
License: GPLv3+
Url:  http://www.gnu.org/software/gdb/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: texinfo
BuildRequires: libncurses-devel
BuildRequires: python-devel
BuildRequires: libexpat-devel
BuildRequires: rpm-build-python
%add_python_req_skip _gdb

%description
This is a version of GDB, the GNU Project debugger, for (remote)
debugging %target binaries. GDB allows you to see and modify what is
going on inside another program while it is executing.

%package devel
Summary: GDB for (remote) debugging %target binaries
Group: Development/Debuggers
Requires: %name = %version-%release

%description devel
This is a version of GDB, the GNU Project debugger, for (remote)
debugging %target binaries.  GDB allows you to see and modify what is
going on inside another program while it is executing.  This package
contains development headers for working with gdb.

%prep
%setup

%build
mkdir -p build
cd build
# Set datarootdir to have target and version in so that we can exist
# side-by-side with other gdb installations of different versions
CFLAGS="$RPM_OPT_FLAGS" ../configure \
    --prefix=%prefix \
	--libdir=%_libdir \
    --mandir=%_mandir \
    --infodir=%_infodir \
    --includedir=%_includedir/%target \
	--datarootdir=%_datadir/gdb-%target-%version \
    --disable-rpath \
	--target=%target \
    --disable-nls \
    --disable-werror \
    --with-python \
    --without-doc \
    --with-xml \
    --with-expat
%make_build

%install
cd build
%makeinstall_std

# we don't want these as this is a cross-compiler
rm -rf %buildroot%_infodir
rm -f %buildroot%_libdir/libiberty.a

# Get rid of the shared lib
rm -f %buildroot%_libdir/lib%target-sim.a

# Non-linux targets don't have syscalls
rm -rf %buildroot%_datadir/gdb/syscalls

%files
%doc COPYING*
%_bindir/%target-*
%_man1dir/%target-*.1.*
%dir %_datadir/gdb-%target-%version
%_datadir/gdb-%target-%version/*

%files devel
%dir %_includedir/%target
%dir %_includedir/%target/gdb
%_includedir/%target/gdb/jit-reader.h

%changelog
* Sat Jul 01 2017 Anton Midyukov <antohami@altlinux.org> 7.9-alt1
- Initial build for ALT Sisyphus.
