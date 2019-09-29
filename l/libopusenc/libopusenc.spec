# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		0
%define libname		libopusenc%{major}
%define develname	libopusenc-devel

Name:		libopusenc
Version:	0.2.1
Release:	alt1_1
Summary:	A library that provides an easy way to encode Ogg Opus files
Group:		System/Libraries
License:	BSD
URL:		https://opus-codec.org/
Source0:	https://ftp.osuosl.org/pub/xiph/releases/opus/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	doxygen
BuildRequires:	pkgconfig(opus)
Source44: import.info

%description
A library that provides an easy way to encode Ogg Opus files.

%package -n	%{libname}
Summary:	A library that provides an easy way to encode Ogg Opus files
Group:		System/Libraries

%description -n	%{libname}
A library that provides an easy way to encode Ogg Opus files.

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

rm -rf %{buildroot}%{_datadir}/doc/%{name}/

%check
make check V=1

%files -n %{libname}
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{develname}
%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_1
- new version

