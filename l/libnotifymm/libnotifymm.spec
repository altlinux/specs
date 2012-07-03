%define apiver 1.0
%define docdeveldir %_docdir/%name-devel-%version

Name: libnotifymm
Version: 0.6.1
Release: alt2
Summary: C++ interface for libnotify

Group: System/Libraries
License: LGPLv2+
Url: http://www.gtkmm.org/
Packager: Mykola Grechukh <gns@altlinux.ru>

Source: http://ftp.gnome.org/pub/GNOME/sources/libnotifymm/0.6/%name-%version.tar.bz2
Patch1: libnotifymm-0.6.1-pkgconfig.patch
Patch2: libnotifymm-0.6.1-bodgenewapi.patch

BuildRequires: gcc-c++
BuildRequires: libglibmm-devel >= 2.12.8
BuildRequires: libgtkmm2-devel >= 2.10
BuildRequires: libnotify-devel >= 0.4.3
BuildRequires: doxygen graphviz

%description
libnotifymm provides a C++ interface to the libnotify
library. Highlights include typesafe callbacks, widgets extensible via
inheritance and a comprehensive set of widget classes that can be
freely combined to quickly create complex user interfaces.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/Other
Requires: %name = %version-%release
Requires: libgtkmm2-devel
Requires: libnotify-devel
Requires: pkgconfig

%description devel
This package contains the libraries and header files needed for
developing %name applications.

%prep
%setup
%patch1 -p1 -b .pkgconfig
%patch2 -p2 -b .bodgenewapi

%build
%configure --disable-static --enable-reference --disable-dependency-tracking
%__subst 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build

%install
%makeinstall_std INSTALL="install -p" \
        referencedir=%docdeveldir/html
find %buildroot -type f -name "*.la" -exec rm -f {} ';'
# Remove code-generation related files
rm -rf %buildroot%_libdir/%name-%apiver

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_libdir/*.so.*

%files devel
%doc %docdeveldir
%_includedir/%name-%apiver
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Sep 01 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.1-alt2
- add patch for remove old libnotify api

* Sat Feb 26 2011 Mykola Grechukh <gns@altlinux.ru> 0.6.1-alt1
- initial build for ALT Linux Sisyphus

* Sun Apr 11 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.6.1-8
- Rebuilt for F-13

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Denis Leroy <denis@poolshark.org> - 0.6.1-5
- Fixed unowned directory issue (#483467)

* Wed Jan 14 2009 Denis Leroy <denis@poolshark.org> - 0.6.1-4
- Removed closesig patch

* Fri Dec 26 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-3
- Added sed line to quiet rpmlint

* Fri Sep  5 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-2
- Added patch to address libnotify rawhide API breakage

* Thu Sep  4 2008 Denis Leroy <denis@poolshark.org> - 0.6.1-1
- Initial version

