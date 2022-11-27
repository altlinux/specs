%define clang_arches %ix86 x86_64 aarch64 ppc64el armh mipsel

Name: mk-configure
Version: 0.38.1
Release: alt1

Summary: Lightweight replacement for GNU autotools
License: BSD-2-Clause and MIT and ISC
Group: Development/Tools

Url: http://sourceforge.net/projects/mk-configure/
# Source-url: http://prdownloads.sf.net/%name-%version/%name-%version.tar.bz2
Source: %name-%version.tar
Source1: %name.macros

Packager: Aleksey Cheusov <cheusov@altlinux.org>

BuildArch: noarch

Requires:      bmake bmkdep
BuildRequires: bmake mk-files binutils

Requires: rpm-macros-%name = %version-%release

%filter_from_requires /xpg4/d

# required for %%check
BuildRequires: flex bison gcc-c++ glib2-devel groff-base zlib-devel libbsd-devel bmkdep
BuildRequires: perl-podlators perl-devel lua-devel info-install makeinfo m4

%ifarch %clang_arches
BuildRequires: clang
%define cc_compilers gcc clang
%define cxx_compilers g++ clang++
%else
%define cc_compilers gcc
%define cxx_compilers g++
%endif

%define pkgdocdir %_docdir/%name-%version

%description
mk-configure is a lightweight replacement for GNU autotools, written in
bmake (portable version of NetBSD make) and POSIX tools.

%package doc
Summary: %name documentation
Group: Development/Documentation

%description doc
Examples and presentation for %name package.

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging applications that use mk-configure
Group: Development/Other

%description -n rpm-macros-%name
Set of RPM macros for packaging applications that use mk-configure.

%prep
%setup

%define env \
  unset MAKEFLAGS; \
  export USE_NM=%_bindir/nm \
  export USE_INSTALL=%__install \
  export USE_AWK=%_bindir/awk \
  export USE_ID=%_bindir/id \
  export USE_CC_COMPILERS='%cc_compilers' \
  export USE_CXX_COMPILERS='%cxx_compilers' \
  export PREFIX=%_prefix \
  export SYSCONFDIR=%_sysconfdir \
  export MANDIR=%_mandir

# examples are built and tested either,
# let's keep a pristine copy
cp -al examples doc

%build
%env
bmake all

%install
%env
bmake install DESTDIR=%buildroot
install -pD -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name
rm -rf %buildroot%_docdir/%name

# instead of proper %%doc (share docdir among subpackages)
mkdir -p %buildroot%pkgdocdir
cp -at %buildroot%pkgdocdir -- \
	doc/FAQ doc/LICENSE doc/NEWS doc/NOTES README* \
	doc/examples/ presentation/presentation.pdf

%check
export PATH="/sbin:$PATH" # /sbin/info-install
unset MAKEFLAGS
# The following tests are disabled because
# lua.pc does not provide INSTALL_{C,L}MOD
export NOSUBDIR='hello_lua hello_lua2 hello_lua3 lua_dirs'
bmake test
bmake nodeps-cleandir-examples
bmake nodeps-cleandir-tests

%files
%dir %pkgdocdir
%pkgdocdir/[A-Z]*
%_bindir/*
%_datadir/%name/
%_man1dir/*
%_man7dir/*
%_prefix/libexec/%name

%files doc
%dir %pkgdocdir
%pkgdocdir/examples/
%pkgdocdir/presentation.pdf

%files -n rpm-macros-%name
%_rpmmacrosdir/%name

# TODO:
# - add %%config %%_sysconfdir/rpm/macros.mkcmake (extra source)

%changelog
* Sun Nov 27 2022 Aleksey Cheusov <cheusov@altlinux.org> 0.38.1-alt1
- 0.38.1

* Sun Nov 27 2022 Aleksey Cheusov <cheusov@altlinux.org> 0.38.0-alt1
- 0.38.0

* Wed Nov 17 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.37.0-alt2
- Add -ffat-lto-objects to COPTS unconditionally in order to unbreak
  building static libraries

* Wed Apr 14 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.37.0-alt1
- 0.37.0

* Wed Jan 6 2021 Aleksey Cheusov <cheusov@altlinux.org> 0.36.0-alt1
- 0.36.0

* Thu May 21 2020 Aleksey Cheusov <cheusov@altlinux.org> 0.34.2-alt4
- Add rpm macro for packages that use mk-configure

* Thu May 14 2020 Aleksey Cheusov <cheusov@altlinux.org> 0.34.2-alt3
- Remove AutoReq

* Thu May 14 2020 Aleksey Cheusov <cheusov@altlinux.org> 0.34.2-alt2
- Fix incorrect dependency from /usr/xpg4/bin/sh

* Thu May 14 2020 Aleksey Cheusov <cheusov@altlinux.org> 0.34.2-alt1
- new version 0.34.2

* Fri May 01 2020 Michael Shigorin <mike@altlinux.org> 0.34.1-alt1
- 0.34.1
  + added mk-files to BR: (thx cheusov@)
  + merged useful opensuse specfile bits
  + added clang support where available
  + separate doc subpackage
* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.32.1-alt1
- new version 0.32.1 (with rpmrb script)

* Wed May 08 2019 Vitaly Lipatov <lav@altlinux.ru> 0.31.0-alt1
- new version 0.31.0 (with rpmrb script)

* Sun Mar 03 2019 Vitaly Lipatov <lav@altlinux.ru> 0.30.0-alt2
- build with mk-files (ALT bug 36211)

* Wed Dec 26 2018 Vitaly Lipatov <lav@altlinux.ru> 0.30.0-alt1
- new version 0.30.0 (with rpmrb script)

* Tue Feb 16 2016 Michael Shigorin <mike@altlinux.org> 0.29.1-alt1
- new version 0.29.1

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt5
- Fix .gear/rules

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt4
- Remove bad requirement "install"

* Sat Nov 29 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt3
- Make hasher(1) happy

* Thu Nov 27 2014 Aleksey Cheusov <cheusov@altlinux.org> 0.28.0-alt2
- 0.28.0-alt2

* Thu Nov 27 2014 Aleksey Cheusov <vle@gmx.net> 0.28.0-alt1
- 0.28.0

* Mon Mar 11 2013 Michael Shigorin <mike@altlinux.org> 0.24.0-alt1
- 0.24.0

* Sun Mar 10 2013 Michael Shigorin <mike@altlinux.org> 0.23.0-alt2
- fixed build (thx upstream)

* Fri Sep 07 2012 Michael Shigorin <mike@altlinux.org> 0.23.0-alt1
- 0.23.0

* Tue Dec 27 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt5
- tweak examples so that they're built as well but packaged pristine

* Mon Dec 26 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt4
- don't install just-built examples as docs

* Sat Dec 24 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt3
- further spec cleanup
- check fixup (thx upstream)
- extended BR: properly

* Mon Nov 21 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt2
- dropped MKCATPAGES (thx upstream)

* Mon Nov 07 2011 Michael Shigorin <mike@altlinux.org> 0.21.2-alt1
- 0.21.2
- minor spec cleanup

* Tue Jun 29 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt4
- add check section

* Fri Jun 25 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt3
- disable examples build

* Thu Jun 24 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt2
- fix install, disable lua test, enable all tests
- update buildreqs

* Fri Jun 18 2010 Vitaly Lipatov <lav@altlinux.ru> 0.16.0-alt1
- new version 0.16.0 (with rpmrb script)

* Tue Nov 17 2009 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt3
- build for Sisyphus

* Thu Jul 23 2009 Aleksey Cheusov <vle@gmx.net> 0.10.0-alt2
- Not it depends on pkgsrc-mk-files, fixes and clean-ups

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Linux Sisyphus
