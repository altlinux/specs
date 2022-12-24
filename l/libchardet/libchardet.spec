# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define _name     chardet

%define major     1
%define libname   lib%{_name}%{major}
%define develname lib%{_name}-devel

Name:           libchardet
Version:        1.0.6
Release:        alt1_1
Summary:        Mozilla Universal Chardet library
License:        MPL
Group:          Development/C++
Url:            http://mirror.oops.org/pub/oops/libchardet
Source:         https://github.com/Joungkyun/libchardet/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

Requires:       %{libname} = %{version}
Source44: import.info

%description
Mozilla's Universal Charset Detector C/C++ API.

%package -n     %{libname}
Summary:        Mozilla Universal Chardet library
Group:          System/Libraries

%description -n %{libname}
Mozilla's Universal Charset Detector C/C++ API.

%package -n     %{develname}
Summary:        Development files of libchardet
Group:          Development/C++
Requires:       %{libname} = %{version}-%{release}
Provides:       %{_name}-devel = %{version}-%{release}

%description -n %{develname}
The libchardet development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libchardet.

%prep
%setup -q

sed -i 's/^\(AM_MAINTAINER\)/m4_ifdef([AM_PROG_AR], [AM_PROG_AR])\n\1/' configure.ac
sed -i '/^dist_doc/d' Makefile.am

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files
%doc Changelog LICENSE README.md
%{_bindir}/%{_name}-config

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{develname}
%{_includedir}/%{_name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{_name}.pc
%dir %{_mandir}/ko/
%dir %{_mandir}/ko/man3/
%{_mandir}/*/man?/detect*.*
%{_mandir}/man?/detect*.*


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.6-alt1_1
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_1
- new version

