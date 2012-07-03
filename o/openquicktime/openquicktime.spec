# $Id: openquicktime.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag

%define prerel a1

Summary: Portable library for handling Apples QuickTime(tm) format
Name: openquicktime
Version: 2.0.0
Release: alt5.%prerel
License: LGPL
Group: Video
URL: http://www.openquicktime.org/

Packager: Igor Vlasenko <viy@altlinux.org>

Source: http://dl.sf.net/openquicktime/openquicktime-%{version}%{prerel}.tar.gz
Patch: openquicktime-2.0.0-a1-alt-minolta-crashfix.patch
Patch1:openquicktime-2.0.0-a1-forum-twos8bit-fix.patch
Patch2:openquicktime-2.0.0a1-alt-gcc41.patch

# lazy work
Patch3: openquicktime-2.0.0-a1-dirty-hack.patch

# Automatically added by buildreq on Tue Jul 19 2005
BuildRequires: xorg-x11-libs esound glibc-devel-static hostinfo libSDL-devel libaudiofile-devel libdv-devel libjpeg-devel liblame-devel libogg-devel libpng-devel libshout-devel libtiff-devel libvorbis-devel zlib-devel
# TODO: add build with
# libcurl-devel libfaac-devel libfaad-devel xvid-devel

%description
OpenQuicktime aims to be a portable library for handling Apples QuickTime
popular media files on Unix-like environments. It is aim is to provide
encoding, authoring and editing support as well as video playback.

%package devel
Summary: Header files and development documentation for libopenquicktime
Group: Development/C
Requires: %name = %version-%release
Requires: libaudiofile-devel 
Requires: liblame-devel 
Requires: libshout-devel 
Requires: libtiff-devel
Requires: libpng-devel
Requires: libjpeg-devel
Requires: libdv-devel
Requires: libogg-devel
Requires: libvorbis-devel

%description devel
Header files and development documentation for libopenquicktime.

%package utils
Summary: Useful tools to operate at QuickTime files
Group: Video
Requires: %name = %version-%release

%description utils
Useful tools to operate on QuickTime files.


%prep
%setup -q -n %{name}-%{version}%{prerel}
%patch -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1

%build
#  --enable-debug=no
autoreconf -fisv
%configure
%{__make} %{_smp_mflags}

%install
### FIXME: Makefile doesn't create %{_libdir}
#%{__install} -d -m0755 %{buildroot}%{_libdir}
%makeinstall

## FIXME: Add a libmajor to libraries
for lib in %{buildroot}%{_libdir}/*.so; do
	%{__mv} -f $lib $lib.0
	%{__ln_s} -f $(basename $lib).0 $lib
done

# remove non-packaged files
# %__rm -f %buildroot%_libdir/%name/*.la


%files 
%doc AUTHORS ChangeLog CHANGES DEPENDENCIES INSTALL COPYING README TODO
%{_libdir}/%{name}
%{_libdir}/*.so.*

%files utils
%_bindir/*

%files devel
%_includedir/*
%{_libdir}/*.so

%changelog
* Thu Apr 17 2008 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt5.a1
- autoreconf'ed

* Tue May 16 2006 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt4.a1
- added *.so to -devel
- C fixes for gcc 4

* Thu Sep 15 2005 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt3.a1
- removed *.so* from -devel (#7808)

* Fri Aug 26 2005 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt2.a1
- fixed crash on some MOVs

* Tue Jul 19 2005 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1.a1
- first altlinux build

* Thu Jul 08 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Added provides for libopenquicktime.so. (Fridrich Strba)

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.0-0
- Initial package. (using DAR)
