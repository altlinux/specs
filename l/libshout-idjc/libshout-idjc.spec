# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(theora)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	3
%define libname	libshout-idjc%{major}
%define devname	libshout-idjc-devel

Name:		libshout-idjc
Version:	2.4.1
Release:	alt1_1
Summary:	Libshout with extensions for IDJC
Source:		http://downloads.sf.net/idjc/libshout-idjc-%{version}.tar.gz
URL:		http://sourceforge.net/projects/idjc/
Group:		System/Libraries
License:	LGPL-2.1+
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libspeex-devel
Source44: import.info

%description
This is a modified version of libshout, with extensions for IDJC.

%package -n %{libname}
Summary:	Libshout with extensions for IDJC
Group:		System/Libraries

%description -n %{libname}
This is a modified version of libshout, with extensions for IDJC.

%package -n %{devname}
Summary:	Development files for libshout with extensions for IDJC
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Libshout-idjc is a modified version of libshout, with extensions for IDJC.
This package contains the development files for the library.

%prep
%setup -q

%build
autoreconf -vfi
%configure
%make_build LDFLAGS+="-lspeex -logg"

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/libshout-idjc.{a,la}
rm -rf %{buildroot}%{_datadir}/doc/libshout-idjc

%files -n %{libname}
%{_libdir}/libshout-idjc.so.%{major}
%{_libdir}/libshout-idjc.so.%{major}.*

%files -n %{devname}
%doc COPYING NEWS README
%{_datadir}/aclocal/shout.m4
%{_includedir}/shoutidjc
%{_libdir}/libshout-idjc.so
%{_libdir}/pkgconfig/shout-idjc.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1
- new version

