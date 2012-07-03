%define __strip %_mingw32_strip
%define __objdump %_mingw32_objdump

%define realname dlfcn-win32

%define alphatag r11

Name: mingw32-dlfcn
Version: 0
Release: alt1.0.5.%alphatag
Summary: Implements a wrapper for dlfcn (dlopen dlclose dlsym dlerror)

License: LGPLv2+
Group: System/Libraries
Url: http://code.google.com/p/dlfcn-win32/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://dlfcn-win32.googlecode.com/files/%realname-%alphatag.tar.bz2

BuildArch: noarch

BuildRequires: rpm-build-mingw32
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
#BuildRequires: dos2unix

Patch1: dlfcn_configure.patch

%description
This library implements a wrapper for dlfcn, as specified in POSIX and SUS,
around the dynamic link library functions found in the Windows API.

%prep
%setup -q -n %realname-%alphatag

sed -i 's/\r//' configure
sed -i 's/\r//' README
sed -i 's/\r//' COPYING

%patch1 -p1

%build
%_mingw32_configure \
  --incdir=%_mingw32_includedir \
  --cc=%_mingw32_cc \
  --enable-shared=yes \
  --enable-static=no \
  --enable-strip=%_mingw32_strip
%make_build

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README COPYING
%_mingw32_bindir/libdl.dll
%_mingw32_libdir/libdl.dll.a
%_mingw32_includedir/dlfcn.h

%changelog
* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 0-alt1.0.5.r11
- initial build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.r11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0-0.4.r11
- Rebuild for mingw32-gcc 4.4

* Wed Jan 14 2009 Richard W.M. Jones <rjones@redhat.com> - 0-0.3.r11
- Use Version 0
  (https://www.redhat.com/archives/fedora-packaging/2009-January/msg00064.html)
- Revert use of dos2unix for now
  (https://www.redhat.com/archives/fedora-packaging/2009-January/msg00066.html)
- Use _smp_mflags.

* Tue Jan 13 2009 Richard W.M. Jones <rjones@redhat.com> - 0.1-0.2.r11
- Import into fedora-mingw temporary repository because there are packages
  which will depend on this.
- Fix the version/release according to packaging guidelines.
- Tidy up the spec file.
- Use dos2unix and keep the timestamps.

* Fri Jan 02 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - r11-1
- Initial RPM release.
