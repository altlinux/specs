Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/mate-keyring-daemon /usr/bin/pkg-config
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary:	Framework for managing passwords and other secrets
Name:		libmatekeyring
Version:	1.6.0
Release:	alt1_1
License:	GPLv2+ and LGPLv2+
Source:		http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
URL:		http://mate-desktop.org

BuildRequires:	libdbus-devel
BuildRequires:	glib2-devel
BuildRequires:  gtk-doc
BuildRequires:	libgcrypt-devel
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
Source44: import.info

%description
libmatekeyring is a program that keep password and other secrets for
users. The library libmatekeyring is used by applications to integrate
with the libmatekeyring system.

%package devel
Summary:	Development files for libmate-keyring
License:	LGPLv2+
Group:		Development/C
Requires:	%name = %{version}-%{release}

%description devel
The libmatekeyring-devel package contains the libraries and
header files needed to develop applications that use libmate-keyring.


%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-gtk-doc-html  
 
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install 
rm %{buildroot}%{_libdir}/*.la

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/*

%changelog
* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Sun Nov 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- build to sisyphus

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

