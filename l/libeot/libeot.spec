# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 0
%define libname libeot%{major}
%define devname libeot-devel

Name: libeot
Version: 0.01
Release: alt1_6
Summary: A library for parsing Embedded OpenType font files

Group: System/Libraries
License: MPLv2.0
URL: https://github.com/umanwizard/libeot
Source: http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.bz2
Source44: import.info

%description
%{name} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package -n %libname
Summary: A library for parsing Embedded OpenType font files
Group: System/Libraries

%description -n %libname
%{libname} is a library for parsing Embedded OpenType files (Microsoft
embedded font "standard") and converting them to other formats.

%package -n %devname
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: libeot-devel

%description -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tools
Summary: Tools to transform EOT font files into other formats
Group: Office
Requires: %{libname} = %{version}-%{release}

%description tools
Tools to transform EOT font files into other formats. Only TTF is
supported currently.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make

%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la



%files -n %libname
%doc LICENSE PATENTS
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %devname
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files tools
%{_bindir}/eot2ttf



%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_6
- new version

* Sat Jun 07 2014 Alexey Shabalin <shaba@altlinux.ru> 0.01-alt1
- initial build
