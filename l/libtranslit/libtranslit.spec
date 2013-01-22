# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize glib2-devel pkgconfig(gio-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-2.0)
# END SourceDeps(oneline)
Name:		libtranslit
Version:	0.0.2
Release:	alt1_3
Summary:	ASCII to Unicode transliteration library with multiple backends

License:	GPLv3+
Group:		System/Libraries
URL:		http://github.com/ueno/libtranslit
Source0:	http://cloud.github.com/downloads/ueno/libtranslit/%{name}-%{version}.tar.gz

BuildRequires:	gobject-introspection-devel
BuildRequires:	intltool
Source44: import.info

%description
ASCII to Unicode transliteration library with multiple backends.

%package	devel
Group: System/Libraries
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %%{name}-devel package contains libraries and header files for
developing applications that use %%{name}.

%package	m17n
Group: System/Libraries
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(m17n-shell)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	m17n
The %%{name}-m17n package contains a transliteration module using
m17n-lib for %%{name}.

%package	icu
Group: System/Libraries
Summary:	Transliteration module using m17n-lib for %{name}
BuildRequires:	pkgconfig(icu-io)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	icu
The %%{name}-icu package contains a transliteration module using
ICU for %%{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f '{}' ';'


%files
%{_libdir}/*.so.*
%dir %{_libdir}/libtranslit/modules
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

%files m17n
%{_libdir}/libtranslit/modules/*m17n.so*

%files icu
%{_libdir}/libtranslit/modules/*icu.so*


%changelog
* Tue Jan 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1_3
- initial fc import

