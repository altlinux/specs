# BEGIN SourceDeps(oneline):
BuildRequires: libcares-devel
# END SourceDeps(oneline)
BuildRequires: chrpath
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		12
%define libname		libexosip2_%{major}
%define libname_devel	libexosip2-devel

Summary: 	Extended osip library
Name: 	 	exosip
Version:	5.1.0
Release: 	alt1_1
License:	GPLv2+
Group:		System/Libraries
URL:		https://savannah.nongnu.org/projects/exosip/
Source0:	https://download.savannah.gnu.org/releases/exosip/libexosip2-%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libosip2) >= 3.5
Source44: import.info

%description
Exosip is a library that hides the complexity of using the SIP protocol for
multimedia session establishment. This protocol is mainly to be used by VoIP
telephony applications (endpoints or conference server) but might be also
useful for any application that wish to establish sessions like multiplayer
games.

%package -n 	%{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n 	%{libname_devel}
Summary: 	Header files and static libraries from %name
Group: 		Development/C
Requires: 	%{libname} = %{version}-%{release}
Provides:	libexosip2-devel = %{version}-%{release}
Provides: 	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname_devel}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q -n libexosip2-%{version}


%build
%configure --disable-static
%make_build

%install
%makeinstall_std

# don't ship .a, .la
find %{buildroot} -name '*.la' -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done

%files
%doc README
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{libname_devel}
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- new version

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 5.0.0-alt1_4
- update by mgaimport

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1_2
- new version

