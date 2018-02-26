%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump
# Patented bytecode interpreter and patented subpixel rendering
# disabled by default.  Pass '--with bytecode_interpreter' and '--with
# subpixel_rendering' on rpmbuild command-line to enable them.

%define _with_subpixel_rendering 1}
%define _without_subpixel_rendering 0}
%{!?_with_bytecode_interpreter: %{!?_without_bytecode_interpreter: %define _without_bytecode_interpreter --without-bytecode_interpreter}}
%{!?_with_subpixel_rendering: %{!?_without_subpixel_rendering: %define _without_subpixel_rendering --without-subpixel_rendering}}

%define with_xfree86 0

Name: mingw32-freetype
Version: 2.3.8
Release: alt1
Summary: Free and portable font rendering engine

License: FTL or GPLv2+
Url: http://www.freetype.org
Packager: Boris Savelev <boris@altlinux.org>

Source: http://download.savannah.gnu.org/releases/freetype/freetype-%version.tar.bz2
Source1: http://download.savannah.gnu.org/releases/freetype/freetype-doc-%version.tar.bz2
#Source2:        http://download.savannah.gnu.org/releases/freetype/ft2demos-%version.tar.bz2
Group: System/Libraries

# Patches from native Fedora package.
#Patch5:         ft2demos-2.1.9-mathlib.patch
Patch20: freetype-2.1.10-enable-ft2-bci.patch
Patch21: freetype-2.3.0-enable-spr.patch
Patch46: freetype-2.2.1-enable-valid.patch
Patch88: freetype-multilib.patch
Patch89: freetype-2.2.1-memcpy-fix.patch

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-zlib
BuildRequires: mingw32-dlfcn

Requires: pkgconfig

%description
MinGW Windows Freetype library.

%prep
%setup -q -n freetype-%version -b 1 -a 1

#pushd ft2demos-%version
#%patch5 -p1 -b .mathlib
#popd

%if %{?_with_bytecode_interpreter:1}%{!?_with_bytecode_interpreter:0}
%patch20  -p1 -b .enable-ft2-bci
%endif

%if %{?_with_subpixel_rendering:1}%{!?_with_subpixel_rendering:0}
%patch21  -p1 -b .enable-spr
%endif

%patch46  -p1 -b .enable-valid

%patch88 -p1 -b .multilib
%patch89 -p1 -b .memcpy

%build
%_mingw32_configure --disable-static
%make_build

# The ft2demos Makefile is hacky and doesn't understand
# cross-compilation.  This nearly works, but not quite, so
# disable. it.
#pushd ft2demos-%version
#make TOP_DIR=".." PLATFORM=win32
#popd

%install
%makeinstall_std

%files
%doc docs/LICENSE.TXT
%_mingw32_bindir/freetype-config
%_mingw32_bindir/libfreetype-6.dll
%_mingw32_includedir/freetype2
%_mingw32_includedir/ft2build.h
%_mingw32_libdir/libfreetype.dll.a
%_mingw32_libdir/libfreetype.la
%_mingw32_libdir/pkgconfig/freetype2.pc
%_mingw32_datadir/aclocal/freetype2.m4

%changelog
* Tue Jul 28 2009 Boris Savelev <boris@altlinux.org> 2.3.8-alt1
- initial build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 2.3.8-2
- Rebuild for mingw32-gcc 4.4

* Fri Jan 16 2009 Richard W.M. Jones <rjones@redhat.com> - 2.3.8-1
- New upstream version 2.3.8.
- Use the patches from the Fedora native package.
- Disable patented code.
- Don't build the static library.
- Use _smp_mflags.
- BR mingw32-dlfcn (not required, but uses it if installed).
- Add license file to doc section.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 2.3.7-6
- Requires pkgconfig.

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 2.3.7-5
- Rename mingw -> mingw32.

* Mon Sep 22 2008 Daniel P. Berrange <berrange@redhat.com> - 2.3.7-4
- Import patches from rawhide  & add docs

* Sun Sep 21 2008 Richard W.M. Jones <rjones@redhat.com> - 2.3.7-3
- Depends on filesystem >= 25.

* Wed Sep 10 2008 Richard W.M. Jones <rjones@redhat.com> - 2.3.7-2
- Fix source URL.
- Remove static libraries.

* Tue Sep  9 2008 Daniel P. Berrange <berrange@redhat.com> - 2.3.7-1
- Initial RPM release
