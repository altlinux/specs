BuildRequires: rpm-build-mingw32
%global __strip %{_mingw32_strip}
%global __objdump %{_mingw32_objdump}

Name:           mingw32-celt051
Version:        0.5.1.3
Release:        alt1_4
Summary:        An audio codec for use in low-delay speech and audio communication

Group:          System/Libraries
License:        BSD
# Files without license header are confirmed to be BSD. Will be fixed in later release
# http://lists.xiph.org/pipermail/celt-dev/2009-February/000063.html
URL:            http://www.celt-codec.org/
Source0:        http://downloads.us.xiph.org/releases/celt/celt-%{version}.tar.gz

# Some tests need libcelt but are not explicitly linked against it.
# Windows cross builds fail because of that (native linux builds
# don't for some mysterious reason).  Fix it.
Patch1:         celt051-tests-makefile-fix.patch

# Fixes "libtool: link: warning: undefined symbols not allowed in
# i686-pc-mingw32 shared libraries"
Patch2:         celt051-build-a-dll-for-win32.patch

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 49
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  pkgconfig autoconf automake libtool
Requires:       pkgconfig

BuildRequires:  mingw32-libogg libogg-devel
Requires:       mingw32-libogg
Source44: import.info

%description
CELT (Constrained Energy Lapped Transform) is an ultra-low delay audio 
codec designed for realtime transmission of high quality speech and audio. 
This is meant to close the gap between traditional speech codecs 
(such as Speex) and traditional audio codecs (such as Vorbis). 

%prep
%setup -q -n celt-%{version}
%patch1 -p1
%patch2 -p1

%build
autoreconf -i -f
%{_mingw32_configure}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_mingw32_libdir}/libcelt051.a

%files
%doc COPYING README TODO
%{_mingw32_bindir}/celtenc051.exe
%{_mingw32_bindir}/celtdec051.exe
%{_mingw32_bindir}/libcelt051-0.dll
%{_mingw32_includedir}/celt051
%{_mingw32_libdir}/libcelt051.la
%{_mingw32_libdir}/libcelt051.dll.a
%{_mingw32_libdir}/pkgconfig/celt051.pc

%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1.3-alt1_4
- initial release by fcimport

