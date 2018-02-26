Name: mingw64-binutils
Version: 2.21
Release: alt1

Summary: MinGW Windows binutils

License: GPLv2+ and LGPLv2+ and GPLv3+ and LGPLv3+
Group: Development/Other
Url: http://www.gnu.org/software/binutils/

Source: http://ftp.gnu.org/gnu/binutils/binutils-%version.tar

BuildRequires: flex
BuildRequires: bison
BuildRequires: texinfo
BuildRequires: rpm-build-mingw64

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
%buildroot%prefix/%_mingw64_target/bin/windres
ln -sf ../../..%_bindir/%_mingw64_target-dllwrap \
%buildroot%prefix/%_mingw64_target/bin/dllwrap

%files
%_man1dir/*
%_bindir/%_mingw64_target-*
%prefix/%_mingw64_target/bin/
%prefix/%_mingw64_target/lib/ldscripts

%changelog
* Sat Apr 16 2011 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- initial build for ALT Linux Sisyphus
