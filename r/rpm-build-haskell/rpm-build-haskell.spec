Name: rpm-build-haskell
Version: 1
Release: alt21
BuildArch: noarch

Summary: RPM helpers to rebuild Haskell packages
License: Public domain
Group: Development/Haskell
Packager: Alex V. Myltsev <avm@altlinux.ru>

Source: scripts-%version.tar
Source1: macros
Source2: buildreq-ignore

# Uses the modular reqprov subsystem
Requires: rpm-build >= 4.0.4-alt78

%description
RPM macros and reqprov helpers to be used in Haskell packages.

There is currently no support for compilers other than GHC.

%prep
%setup -n scripts-%version

%install
%define rpmdir %prefix/lib/rpm
mkdir -p %buildroot%rpmdir
cp haskell.* %buildroot%rpmdir/
install -D %SOURCE1 %buildroot%_sysconfdir/rpm/macros.d/haskell
install -D %SOURCE2 \
	%buildroot%_sysconfdir/buildreqs/files/ignore.d/rpm-build-haskell
install -D -m 755 hs_gen_filelist.sh %buildroot%_libexecdir/%name/hs_gen_filelist.sh

%files
%rpmdir/haskell.*
%_sysconfdir/rpm/macros.d/haskell
%_sysconfdir/buildreqs/files/ignore.d/rpm-build-haskell
%_libexecdir/%name/hs_gen_filelist.sh

%changelog
* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt21
- fix filelist for packaging

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt20
- not try to package /usr/bin

* Sun Jul 01 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt19
- create filelist for all files that can be build from cabal package

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt18
- remove unneeded requires

* Sat Mar 17 2012 Denis Smirnov <mithraen@altlinux.ru> 1-alt17
- remove ghc(package) provides, use only provides with ghc version

* Thu Aug 04 2011 Denis Smirnov <mithraen@altlinux.ru> 1-alt16
- fix install for non-library packages

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt15
- enable build shared libraries

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt14
- fix filelist creation for profiling libs build

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt13
- more strict requires

* Mon Sep 13 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt12
- build all libs with profiling versions

* Sat Sep 11 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt11
- add some useful macros

* Fri Sep 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt10
- ignore builtin_ffi/builtin_rts requires

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt9
- add requires to haskell-filetrigger

* Thu Sep 09 2010 Denis Smirnov <mithraen@altlinux.ru> 1-alt8
- ghc 6.12 support

* Thu Mar 18 2010 Alexander Myltsev <avm@altlinux.ru> 1-alt7
- Fix the hs_package_register macro for ghc 6.10.4.

* Mon Nov 17 2008 Alexander Myltsev <avm@altlinux.ru> 1-alt6
- Stop using the 'configure --user' hack.

* Thu Jun 19 2008 Alexander Myltsev <avm@altlinux.ru> 1-alt5
- Use versionless build-deps.
- Add a buildreq ignore rule (fixes #17878).

* Fri Jan 18 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt4
- Accept *.package.conf files (that's what gtk2hs uses, maybe it's right).
- Fix errors when "depends:" lines contain commas or versionless items.

* Mon Jan 14 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt3
- More useful macros: %hs_package_register, %hs_setup etc.

* Sat Jan 12 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt2
- Fix bug with multiline values in *.pkg files.

* Tue Jan 08 2008 Alex V. Myltsev <avm@altlinux.ru> 1-alt1
- Initial build for Sisyphus.
