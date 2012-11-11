# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize /usr/bin/mate-keyring-daemon /usr/bin/pkg-config
# END SourceDeps(oneline)
%define gcrypt_version 1.0
%define _libexecdir %_prefix/libexec
Summary:	Framework for managing passwords and other secrets
Name:		libmatekeyring
Version:	1.5.0
Release:	alt1_1
License:	GPLv2+ and LGPLv2+
Group:		System/Libraries
Source:		http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
URL:		http://mate-desktop.org

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	libgcrypt-devel >= %{gcrypt_version}
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(gtk-doc)
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
%configure --disable-gtk-doc
	
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# avoid unneeded direct dependencies
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS NEWS README COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%doc %{_datadir}/gtk-doc/html/*

%changelog
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

