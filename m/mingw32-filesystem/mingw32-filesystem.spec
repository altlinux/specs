%define debug_package %nil

Name: mingw32-filesystem
Version: 68
Release: alt1
Summary: MinGW base filesystem and environment

Group: Development/Other
License: GPLv2+
Url: http://hg.et.redhat.com/misc/fedora-mingw--devel/
BuildArch: noarch

Packager: Boris Savelev <boris@altlinux.org>

Source: COPYING
Source2: mingw32.sh
#Source3: mingw32.csh

BuildRequires: rpm-macros-mingw32

# Note about 'Provides: mingw32(foo.dll)'
# ------------------------------------------------------------
#
# We want to be able to build & install mingw32 libraries without
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
Provides:       mingw32(advapi32.dll)
Provides:       mingw32(cfgmgr32.dll)
Provides:       mingw32(comctl32.dll)
Provides:       mingw32(comdlg32.dll)
Provides:       mingw32(crypt32.dll)
Provides:       mingw32(ddraw.dll)
Provides:       mingw32(dnsapi.dll)
Provides:       mingw32(dsound.dll)
Provides:       mingw32(gdi32.dll)
Provides:       mingw32(gdiplus.dll)
Provides:       mingw32(glu32.dll)
Provides:       mingw32(glut32.dll)
Provides:       mingw32(imm32.dll)
Provides:       mingw32(kernel32.dll)
Provides:       mingw32(mscoree.dll)
Provides:       mingw32(msdmo.dll)
Provides:       mingw32(msimg32.dll)
Provides:       mingw32(msvcrt.dll)
Provides:       mingw32(netapi32.dll)
Provides:       mingw32(odbc32.dll)
Provides:       mingw32(ole32.dll)
Provides:       mingw32(oleaut32.dll)
Provides:       mingw32(opengl32.dll)
Provides:       mingw32(rpcrt4.dll)
Provides:       mingw32(secur32.dll)
Provides:       mingw32(setupapi.dll)
Provides:       mingw32(shell32.dll)
Provides:       mingw32(shlwapi.dll)
Provides:       mingw32(user32.dll)
Provides:       mingw32(usp10.dll)
Provides:       mingw32(version.dll)
Provides:       mingw32(winmm.dll)
Provides:       mingw32(wldap32.dll)
Provides:       mingw32(ws2_32.dll)
Provides:       mingw32(wsock32.dll)


%description
This package contains the base filesystem layout, RPM macros and
environment for all Fedora MinGW packages.

This environment is maintained by the Fedora MinGW SIG at:

  http://fedoraproject.org/wiki/SIGs/MinGW


%prep
%setup -q -c -T
cp %SOURCE0 COPYING

%build
# nothing


%install
mkdir -p %buildroot

mkdir -p %buildroot%_sysconfdir/profile.d
install -m 644 %SOURCE2 %buildroot%_sysconfdir/profile.d/
# install -m 644 {SOURCE3} %buildroot%_sysconfdir/profile.d/

# GCC requires these directories, even though they contain links
# to binaries which are also installed in /usr/bin etc.  These
# contain Fedora native binaries.
mkdir -p %buildroot%prefix/%_mingw32_target/bin
mkdir -p %buildroot%prefix/%_mingw32_target/lib

# The MinGW system root which will contain Windows native binaries
# and Windows-specific header files, pkgconfig, etc.
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/bin
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/include
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/include/sys
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/lib
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/lib/pkgconfig
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/sbin

mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/aclocal
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/cmake
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/pkgconfig
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/xml

# We don't normally package manual pages and info files, except
# where those are not supplied by a Fedora native package.  So we
# need to create the directories.
#
# Note that some packages try to install stuff in
#   /usr/%_mingw32_target/sys-root/mingw/man and
#   /usr/%_mingw32_target/sys-root/mingw/doc
# but those are both packaging bugs.
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/doc
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/info
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/man
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/man/man{1,2,3,4,5,6,7,8,l,n}
mkdir -p %buildroot%prefix/%_mingw32_target/sys-root/mingw/share/themes

%files
%doc COPYING
%config(noreplace) %_sysconfdir/profile.d/mingw32.sh
#%config(noreplace) %_sysconfdir/profile.d/mingw32.csh
%prefix/%_mingw32_target

%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 68-alt1
- bumped version to 68
- sync with Fedora mingw32-filesystem-69-7

* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 61-alt1
- sync with Fedora:
  + bumped version to 61
  + syncronized Windows system dll provides
  + syncronized filesystem hierarchy

* Sun Sep 20 2009 Boris Savelev <boris@altlinux.org> 52-alt2
- add provides rpcrt4.dll for wxGTK

* Fri Jul 17 2009 Boris Savelev <boris@altlinux.org> 52-alt1
- build for Sisyphus from Fedora

* Wed Jun 24 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 52-2
- Updated ChangeLog comment from previous version as the RPM variable
  __debug_install_post needs to be overridden instead of __os_install_post
  for -debuginfo subpackage generation

* Mon Jun 22 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 52-1
- Add script to create -debuginfo subpackages
  This script was created by Fridrich Strba
- All mingw32 packages now need to add these lines to their .spec files:
%%define __debug_install_post %%{_mingw32_debug_install_post}
%%{_mingw32_debug_package}

* Thu Jun  4 2009 Adam Goode <adam@spicenitz.org> - 51-1
- Add CMake rules

* Tue Apr 21 2009 Richard W.M. Jones <rjones@redhat.com> - 50-4
- Fix dependency problem with + in DLL name (Thomas Sailer).

* Fri Mar 27 2009 Richard W.M. Jones <rjones@redhat.com> - 50-3
- Fix up and test mingw32-pkg-config changes.

* Thu Mar 26 2009 Levente Farkas <lfarkas@lfarkas.org> - 50-1
- Add mingw32-pkg-config.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 49-2
- Rebuild for mingw32-gcc 4.4

* Thu Feb 19 2009 Richard W.M. Jones <rjones@redhat.com> - 49-1
- Added virtual provides for mingw32(cfgmgr32.dll) and mingw32(setupapi.dll).

* Wed Feb 18 2009 Richard W.M. Jones <rjones@redhat.com> - 48-1
- Fix _mingw32_configure.

* Tue Feb 17 2009 Richard W.M. Jones <rjones@redhat.com> - 47-1
- Rename mingw32-COPYING to COPYING.
- Rename mingw32-macros.mingw32 to macros.mingw32.
- _mingw32_configure looks for configure in "." and ".." dirs.
- Added _mingw32_description.
- Added mingw32(version.dll) virtual provides (rhbz#485842).

* Sun Feb  1 2009 Richard W.M. Jones <rjones@redhat.com> - 46-1
- Unset PKG_CONFIG_PATH because %_libdir/rpm/macros sets it (Erik van
  Pienbroek).

* Wed Jan 28 2009 Richard W.M. Jones <rjones@redhat.com> - 45-1
- Use PKG_CONFIG_LIBDIR instead of PKG_CONFIG_PATH so that native pkgconfig
  is never searched.

* Mon Jan 26 2009 Richard W.M. Jones <rjones@redhat.com> - 44-1
- Install rpmlint overrides file to suppress some rpmlint warnings.

* Sat Jan 24 2009 Richard W.M. Jones <rjones@redhat.com> - 43-6
- Don't claim C++ compiler exists if it's not installed, as this
  breaks autoconf and (in particular) libtool.

* Wed Jan 14 2009 Richard W.M. Jones <rjones@redhat.com> - 42-1
- Add pseudo-provides secur32.dll

* Wed Dec 17 2008 Levente Farkas <lfarkas@lfarkas.org> - 41-1
- Re-add mingw32-make

* Sat Dec  6 2008 Levente Farkas <lfarkas@lfarkas.org> - 40-2
- Rewrite mingw32-scripts to run in the current shell
- (Re-add mingw32-make) - Removed by RWMJ.
- Add mingw32-env to mingw32.sh

* Mon Nov 24 2008 Richard W.M. Jones <rjones@redhat.com> - 39-3
- Unify mingw32-filesystem packages from all three branches again, and test.
- Fix mingw32-scripts so it can handle extra parameters correctly.
- Remove mingw32-env & mingw32-make since neither of them actually work.

* Sun Nov 23 2008 Richard Jones <rjones@redhat.com> - 38-1
- Added mingw32(glut32.dll).

* Wed Nov 19 2008 Richard Jones <rjones@redhat.com> - 37-1
- Revert part of the 36-1 patch.  --build option to configure was wrong.

* Wed Nov 19 2008 Richard Jones <rjones@redhat.com> - 36-1
- Greatly improved macros (Levente Farkas).
- Added -mms-bitfields.

* Thu Nov 13 2008 Richard Jones <rjones@redhat.com> - 35-1
- Added mingw32(wldap32.dll) pseudo-provides.

* Wed Oct 29 2008 Richard Jones <rjones@redhat.com> - 34-1
- Set --prefix correctly.

* Wed Oct 29 2008 Richard Jones <rjones@redhat.com> - 33-1
- Remove mingw32.{sh,csh} which are unused.

* Mon Oct 27 2008 Richard Jones <rjones@redhat.com> - 32-1
- Add mingw32-configure script.

* Mon Oct 27 2008 Richard Jones <rjones@redhat.com> - 31-1
- Update the spec file with explanation of the 'Provides: mingw32(...)'
  lines for Windows system DLLs.

* Mon Oct  6 2008 Richard Jones <rjones@redhat.com> - 30-1
- Added _mingw32_cxx.

* Thu Sep 25 2008 Richard Jones <rjones@redhat.com> - 29-1
- Added _mingw32_as, _mingw32_dlltool, _mingw32_windres.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 27-1
- Begin the grand renaming of mingw -> mingw32.
- Added mingw32(mscoree.dll).

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 25-1
- Add shared aclocal directory.

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 24-1
- Remove mingw-defs, since no longer used.
- Add _mingw_infodir.

* Thu Sep 11 2008 Daniel P. Berrange <berrange@redhat.com> - 23-1
- Add macros for find-provides/requires scripts

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 22-1
- Windows provides OLE32.DLL.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 21-1
- Allow '.' in dll names for find-requires
- Windows provides GDI32.DLL.

* Fri Sep  5 2008 Richard W.M. Jones <rjones@redhat.com> - 20-1
- On 64 bit install in %_libdir/rpm always.

* Thu Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 19-1
- 'user32.dll' is provided by Windows.
- Allow '-' in DLL names.
- More accurate detection of DLLs in requires/provides scripts.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 17-1
- Automatically add mingw-filesystem and mingw-runtime requires.
- Add --prefix to _mingw_configure macro.
- Three backslashes required on each continuation line in RPM macros.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 14-1
- Fix path to mingw-find-requires/provides scripts.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 12-1
- Put CFLAGS on a single line to avoid problems in some configure scripts.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 10-1
- Provides certain base Windows DLLs (not literally).

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 9-1
- Include RPM dependency generators and definitions.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 4-1
- Add _mingw_cc/cflags/etc. and _mingw_configure macros.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 3-1
- Add _mingw_host macro.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 2-1
- Add _mingw_sysroot macro.
- Add _mingw_target macro.

* Mon Sep  4 2008 Richard W.M. Jones <rjones@redhat.com> - 1-1
- Basic filesystem layout.
