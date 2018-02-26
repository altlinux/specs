%define sconsopts VERSION=%version PREFIX=%prefix PREFIX_CONF=%_sysconfdir SKIPUTILS='NSIS Menu' STRIP_CP=false

Name: mingw32-nsis
Version: 2.45
Release: alt1
Summary: Nullsoft Scriptable Install System

License: zlib and CPL
Group: System/Libraries
Url: http://nsis.sourceforge.net/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dl.sourceforge.net/sourceforge/nsis/nsis-%version-src.tar.bz2

# This patch fixes NSIS to actually build 64-bit versions.
# Originally from Debian, updated by Kevin Kofler.
Patch: nsis-2.43-64bit-fixes.patch
# Use RPM_OPT_FLAGS for the natively-built parts
Patch1: nsis-2.43-rpm-opt.patch

BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++ cvs flex
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: python
BuildRequires: scons

# Don't build NSIS Menu as it doesn't actually work on POSIX systems: 1. it
# doesn't find its index.html file without patching, 2. it has various links to
# .exe files such as the makensisw.exe W32 GUI which are not available in the
# POSIX version at all and 3. the documentation links have backslashes in the
# URLs and the relative paths are wrong. Almost none of the links worked when I
# tested it (after patching problem 1.).
# Also removes unnecessary wxGTK dependency for this otherwise GUI-less package.
# (Does it really make sense to drag in wxGTK just to display a HTML file?)
# If you really want to reenable this, it needs a lot of fixing. Oh, and it'd
# need a .desktop file too.
# -- Kevin Kofler
# BuildRequires:  wxGTK-devel

# upgrade path for CalcForge users
Obsoletes: nsis < %version-%release
Provides: nsis = %version-%release
Obsoletes: nsis-data < %version-%release
Provides: nsis-data = %version-%release

%description
NSIS, the Nullsoft Scriptable Install System, is a script-driven
Windows installation system.

This package includes native Fedora binaries of makensis (etc.) and
all plugins.

%prep
%setup -q -n nsis-%version-src

%patch0 -p1 -b .64bit
%patch1 -p1 -b .rpmopt

%build
scons %sconsopts

%install
mkdir %buildroot
scons %sconsopts PREFIX_DEST=%buildroot install

mv %buildroot%_docdir/nsis %buildroot%_docdir/%name-%version

%files
%doc %_docdir/%name-%version
%config(noreplace) %_sysconfdir/nsisconf.nsh
%_bindir/*
#{_includedir}/nsis
%_datadir/nsis

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 2.45-alt1
- initial build

* Tue Jul 21 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.45-1
- Update to 2.45 (#512429)

* Tue Jun 30 2009 Stu Tomlinson <stu@nosnilmot.com> - 2.44-2
- Re-enable System.dll plugin, inline Microsoft assembler code was
  replaced in 2.42 (#509234)

* Sat Mar 14 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.44-1
- Update to 2.44 (#488522)

* Tue Mar  3 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-6
- Don't build the MinGW parts with debugging information, NSIS corrupts the
  debugging information in the stubs when building installers from them
- Drop debian-debug-opt patch, all its changes are either taken care of by our
  rpm-opt patch, unwanted (see above) or unneeded

* Wed Feb 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-5
- Use RPM_OPT_FLAGS for the natively-built parts

* Wed Feb 25 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.43-4
- Updated 64bit-fixes patch (remove some more -m32 use)
- Drop ExclusiveArch, not needed with the above
- Obsoletes/Provides nsis and nsis-data for migration path from CalcForge
- Disable NSIS Menu (does not work on *nix, see specfile comment for details)
- Drop BR wxGTK-devel

* Sat Feb 21 2009 Richard W.M. Jones <rjones@redhat.com> - 2.43-3
- Restore ExclusiveArch line (Levente Farkas).

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.43-2
- Rebuild for mingw32-gcc 4.4

* Fri Feb 13 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.43-1
- update to the latest upstream

* Wed Jan 14 2009 Levente Farkas <lfarkas@lfarkas.org> - 2.42-1
- update to the latest upstream
- a few small changes

* Fri Oct 17 2008 Richard W.M. Jones <rjones@redhat.com> - 2.39-5
- Fix the Summary line.

* Wed Oct  8 2008 Richard W.M. Jones <rjones@redhat.com> - 2.39-4
- Initial RPM release.
