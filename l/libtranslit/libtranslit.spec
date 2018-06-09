# BEGIN SourceDeps(oneline):
BuildRequires: glib2-devel pkgconfig(gio-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libtranslit
Version:	0.0.3
Release:	alt1_18
Summary:	ASCII to Unicode transliteration library with multiple backends

License:	GPLv3+
Group:		System/Libraries
URL:		http://github.com/ueno/libtranslit
Source0:	http://du-a.org/files/libtranslit/%{name}-%{version}.tar.gz

BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
BuildRequires:	libvala-devel, vala-tools
Source44: import.info

%description
ASCII to Unicode transliteration library with multiple backends.

%package	devel
Group: System/Libraries
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	vala vala-tools

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	m17n
Group: System/Libraries
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(m17n-shell)
Requires:	%{name} = %{version}-%{release}

%description	m17n
The %{name}-m17n package contains a transliteration module using
m17n-lib for %{name}.

%package	icu
Group: System/Libraries
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(icu-io)
Requires:	%{name} = %{version}-%{release}

%description	icu
The %{name}-icu package contains a transliteration module using
ICU for %{name}.


%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%files
%{_libdir}/*.so.*
%dir %{_libdir}/libtranslit
%dir %{_libdir}/libtranslit/modules
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*.vapi
%{_datadir}/vala/vapi/*.deps

%files m17n
%{_libdir}/libtranslit/modules/*m17n.so*

%files icu
%{_libdir}/libtranslit/modules/*icu.so*


%changelog
* Sat Jun 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_18
- rebuild with new icu

* Fri Feb 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.3-alt1_11
- rebuild with new icu

* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_3
- initial fc import

