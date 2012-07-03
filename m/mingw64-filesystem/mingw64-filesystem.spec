Name: mingw64-filesystem
Version: 23
Release: alt2

Summary: MinGW base filesystem and environment

Group: Development/Other
License: GPLv2+
Url: http://git.annexia.org/?p=fedora-mingw.git

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: COPYING
Source2: mingw64.sh
#Source3: mingw64.csh

#BuildPreReq: sisyphus_check > 0.8.22-alt1

BuildRequires: rpm-build-mingw64

# Note about 'Provides: mingw64(foo.dll)'
# ------------------------------------------------------------
#
# We want to be able to build & install mingw64 libraries without
# necessarily needing to install wine.  (And certainly not needing to
# install Windows!)  There is no requirement to have wine installed in
# order to use the mingw toolchain to develop software (ie. to
# compile more stuff on top of it), so why require that?
#
# So for expediency, this base package provides the "missing" DLLs
# from Windows.  Another way to do it would be to exclude these
# proprietary DLLs in our find-requires checking script - essentially
# it comes out the same either way.
#
Provides: mingw64(kernel32.dll)
Provides: mingw64(msvcrt.dll)
Provides: mingw64(advapi32.dll)
Provides: mingw64(user32.dll)
Provides: mingw64(dnsapi.dll)
Provides: mingw64(ole32.dll)
Provides: mingw64(shell32.dll)
Provides: mingw64(shlwapi.dll)
Provides: mingw64(ws2_32.dll)
Provides: mingw64(gdi32.dll)
Provides: mingw64(msimg32.dll)
Provides: mingw64(comctl32.dll)
Provides: mingw64(comdlg32.dll)
Provides: mingw64(imm32.dll)
Provides: mingw64(crypt32.dll)
Provides: mingw64(oleaut32.dll)
Provides: mingw64(opengl32.dll)
Provides: mingw64(version.dll)
Provides: mingw64(winmm.dll)
Provides: mingw64(rpcrt4.dll)

%description
This package contains the base filesystem layout
for all ALT Linux MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW

%prep
%setup -c -T
cp %SOURCE0 COPYING

%install
mkdir -p %buildroot%_sysconfdir/profile.d
install -m 644 %SOURCE2 %buildroot%_sysconfdir/profile.d/
# install -m 644 {SOURCE3} %buildroot%_sysconfdir/profile.d/

# GCC requires these directories, even though they contain links
# to binaries which are also installed in /usr/bin etc.  These
# contain Fedora native binaries.
mkdir -p %buildroot%prefix/%_mingw64_target/bin
mkdir -p %buildroot%prefix/%_mingw64_target/lib

# The MinGW system root which will contain Windows native binaries
# and Windows-specific header files, pkgconfig, etc.
mkdir -p %buildroot%_mingw64_bindir
mkdir -p %buildroot%_mingw64_includedir
mkdir -p %buildroot%_mingw64_includedir/sys/
mkdir -p %buildroot%_mingw64_libdir
mkdir -p %buildroot%_mingw64_libdir/pkgconfig/

cd %buildroot%_mingw64_prefix

# GCC wants to look in include64/ directory for some reason.
ln -s include include64

# We don't normally package manual pages and info files, except
# where those are not supplied by a ALT Linux native package.  So we
# need to create the directories.
#
# Note that some packages try to install stuff in
#   /usr/%_mingw64_target/sys-root/mingw/man and
#   /usr/%_mingw64_target/sys-root/mingw/doc
# but those are both packaging bugs.
mkdir -p share/
mkdir -p share/doc/
mkdir -p share/info/
mkdir -p share/man/
mkdir -p share/man/man{1,2,3,4,5,6,7,8,l,n}
mkdir -p share/aclocal/

cd -

%files
%doc COPYING
%config(noreplace) %_sysconfdir/profile.d/mingw64.sh
#%config(noreplace) %_sysconfdir/profile.d/mingw64.csh
%_mingw64_prefix/

%changelog
* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 23-alt2
- use only /usr/x86_64-pc-mingw64 sysroot

* Sat Apr 16 2011 Vitaly Lipatov <lav@altlinux.ru> 23-alt1
- build for x86_64-pc-mingw64

* Sun Sep 20 2009 Boris Savelev <boris@altlinux.org> 52-alt2
- add provides rpcrt4.dll for wxGTK

* Fri Jul 17 2009 Boris Savelev <boris@altlinux.org> 52-alt1
- build for Sisyphus from Fedora

