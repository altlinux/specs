Name: rpm-build-mingw64
Version: 23
Release: alt3

Summary: MinGW RPM build helper files and macros

Group: Development/Other
License: GPLv2+
Url: http://git.annexia.org/?p=fedora-mingw.git

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

%description
This package contains the RPM macros and
environment for all ALT Linux MinGW 64 packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW

%prep
%setup
%__subst 's/@VERSION@/%version/' mingw64-find-requires.sh

%install
mkdir -p %buildroot%_rpmmacrosdir
install -m 644 macros.mingw64 %buildroot%_rpmmacrosdir/mingw64

mkdir -p %buildroot%_libexecdir
install -m 755 mingw64-scripts.sh %buildroot%_libexecdir/mingw64-scripts

mkdir -p %buildroot%_bindir
pushd %buildroot%_bindir
for i in mingw64-configure mingw64-make; do
  ln -s %_libexecdir/mingw64-scripts $i
done
popd

#mkdir -p %buildroot%_sysconfdir/rpmlint
#install -m 644 SOURCE7 %buildroot%_sysconfdir/rpmlint/

mkdir -p %buildroot%_rpmlibdir/
install -m 0755 mingw64-find-debuginfo.sh %buildroot%_rpmlibdir/
install -m 0755 mingw64-find-requires.sh %buildroot%_rpmlibdir/
install -m 0755 mingw64-find-provides.sh %buildroot%_rpmlibdir/

mkdir -p %buildroot%_datadir/mingw64/
install -m 0755 Toolchain-mingw64.cmake %buildroot%_datadir/mingw64/
install -m 0644 Makefile.mingw64 %buildroot%_datadir/mingw64/

%files
%doc COPYING
%_rpmmacrosdir/mingw64
%_rpmlibdir/mingw64-*
%_datadir/mingw64/
#%config(noreplace) %_sysconfdir/rpmlint/mingw64-rpmlint.config
%_bindir/mingw64-configure
%_bindir/mingw64-make
%_libexecdir/mingw64-scripts

%changelog
* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 23-alt3
- drop out sysroot using (use /usr/x86_64-mc-mingw32 only)

* Sat Apr 16 2011 Vitaly Lipatov <lav@altlinux.ru> 23-alt2
- use target x86_64-pc-mingw32 (mingw64 does not supported by autotools yet)

* Sat Apr 16 2011 Vitaly Lipatov <lav@altlinux.ru> 23-alt1
- initial build for ALT Linux Sisyphus
- use target x86_64-pc-mingw64
