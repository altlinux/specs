Name: mingw64-binutils
Version: 2.28
Release: alt2%ubt

Summary: MinGW Windows binutils

License: GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/binutils/

Source: binutils-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-mingw64

BuildRequires: flex
BuildRequires: bison
BuildRequires: texinfo
BuildRequires: gcc5-c++

# NB: This must be left in.
Requires: mingw64-filesystem
BuildRequires: perl-podlators

%description
MinGW Windows binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%prep
%setup -n binutils-%version

%build
# without -O0 gnu as doesnt works
%configure \
	CFLAGS="%optflags -O0" \
	--target=%_mingw64_target \
	--verbose --disable-nls \
	--with-included-gettext \
	--disable-win32-registry \
	--disable-werror \
	--with-bugurl=http://bugzilla.altlinux.org/

%make_build

%install
%makeinstall_std

# These files conflict with ordinary binutils.
rm -rf %buildroot%_infodir
rm -f %buildroot%_libdir/libiberty*

ln -sf ../../..%_bindir/%_mingw64_target-windres \
%buildroot%_mingw64_bindir/windres
ln -sf ../../..%_bindir/%_mingw64_target-dllwrap \
%buildroot%_mingw64_bindir/dllwrap

%files
%_man1dir/*
%_bindir/%_mingw64_target-*

%_mingw64_bindir
%_mingw64_libdir/ldscripts

%exclude %_datadir/gdb
%exclude %_includedir/gdb/jit-reader.h
%exclude %_man5dir/x86_64-pc-mingw32-gdbinit.5.xz

%changelog
* Wed Jun 07 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.28-alt2%ubt
- fix ubt-macro usage in changelog

* Mon Jun 05 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.28-alt1%ubt
- 2.28 release

* Mon Jun 05 2017 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.27-alt2%ubt
- rebuild

* Sat Dec 24 2016 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.27-alt1
- 2.27 release

* Sat Apr 16 2011 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- initial build for ALT Linux Sisyphus
