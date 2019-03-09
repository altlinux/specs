# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api 1.0
%define major 1
%define libname libzeitgeist%{api}_%{major}
%define develname libzeitgeist-devel

Name: libzeitgeist
Version: 0.3.18
Release: alt2_7
Summary: Client library for applications that want to interact with the Zeitgeist daemon
Group: System/Libraries
License: LGPLv3 and GPLv3
URL: https://launchpad.net/libzeitgeist
Source0: http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires: pkgconfig(gio-2.0) >= 2.26
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.26
BuildRequires: pkgconfig(gobject-2.0) >= 2.26
BuildRequires: gtk-doc
# for tests:
BuildRequires: dbus-tools dbus-tools-gui
# zeitgeist is just a runtime and the reason to install libzeitgeist
Requires: python-module-zeitgeist2.0 zeitgeist
Source44: import.info

%description
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package -n %libname
Summary: Shared library for %name
Group: System/Libraries

%description -n %libname
This project provides a client library for applications that want to interact
with the Zeitgeist daemon. The library is written in C using glib and provides
an asynchronous GObject oriented API.

%package -n %develname
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}

%description -n %develname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall_std

install -d -p -m 755 %{buildroot}%{_datadir}/vala/vapi
install -D -p -m 644 bindings/zeitgeist-1.0.{vapi,deps} %{buildroot}%{_datadir}/vala/vapi
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove duplicate documentation
rm -fr %{buildroot}%{_defaultdocdir}/%{name}

%files -n %libname
%doc COPYING COPYING.GPL README
%{_libdir}/libzeitgeist-%{api}.so.%{major}
%{_libdir}/libzeitgeist-%{api}.so.%{major}.*

%files -n %develname
%doc AUTHORS ChangeLog COPYING COPYING.GPL MAINTAINERS NEWS 
%doc examples/*.vala examples/*.c
%{_datadir}/gtk-doc/html/zeitgeist-1.0/
%{_includedir}/zeitgeist-1.0/
%{_libdir}/pkgconfig/zeitgeist-1.0.pc
%{_libdir}/*.so
%{_datadir}/vala/vapi/


%changelog
* Sat Mar 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.18-alt2_7
- do not delete - autoimports dependency

* Fri Mar 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.18-alt1_7
- autoimports dep

* Thu Jul 26 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3.18-alt1
- new version 0.3.18 (with rpmrb script) (ALT bug #27571)

* Tue Jan 24 2012 Vitaly Lipatov <lav@altlinux.ru> 0.3.12-alt1
- new version 0.3.12 (with rpmrb script)

* Tue Jul 12 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.10-alt1
- initial build for ALT Linux Sisyphus

* Wed Apr 06 2011 Renich Bon ciric <renich@woralelandia.com> - 0.3.10-1
- Updated to version 0.3.10
- Fixed bugs:
    https://bugs.launchpad.net/ubuntu/+source/libzeitgeist/+bug/742438
- Renamed log fix patch to something more appropriate

* Sat Apr 02 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-4
- Added -p to install statements (forgot some)
- Moved README to the main package from devel

* Fri Mar 25 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-3
- Removed Rubys geo2 dependency since is not needed; it's provided by glibc-devel

* Thu Mar 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-2
- Log test failure repaired by patch from Mamoru Tasaka

* Mon Mar 21 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.6-1
- Updated to 0.3.6
- Implemented the isa macro for the devel subpackage.
- Eliminated the doc macro from gtk-doc since it gets marked automatically

* Sat Mar 12 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-3
- Removed mistaken isa macro from zeitgeist require

* Thu Mar 10 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-2
- Cleaned up old stuff (BuildRoot, Clean and stuff of sorts)
    https://fedoraproject.org/wiki/Packaging/Guidelines#BuildRoot_tag
    https://fedoraproject.org/wiki/Packaging/Guidelines#.25clean
- Added glib2-devel and gtk-doc as a BuildRequires
- Added GPLv3 since it covers the documentation examples
- Updated Requires to use the new arch specification macro when accordingly
    https://fedoraproject.org/wiki/Packaging/Guidelines#Requires
- Configured install to preserve timestamps
- Added V=1 to the make flags for more verbosity on build
- Added a check section
- Removed disable-module from configure statement since it's not needed anymore:
    https://bugs.launchpad.net/libzeitgeist/+bug/683805

* Thu Feb 24 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.4-1
- updated to latest version

* Sun Feb 06 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-3
- got rid of INSTALL from docs
- got rid ot dorcdir and used doc to include html docs

* Sat Feb 05 2011 Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-2
- removed duplicate documentation
- added the use of macros for everything; including source and build dir.
- revised path syntax

* Thu Jan 27 2011 - Renich Bon Ciric <renich@woralelandia.com> - 0.3.2-1
- First buildName: libzeitgeist
