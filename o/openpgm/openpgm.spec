# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/python3 gcc-c++ perl(JSON.pm) perl(Net/SSH.pm) unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 5.3.128
%define uver    %(echo %{version}|sed 's/\\./-/g')

%define api     5.3
%define major   0
%define libname libpgm%{api}_%{major}
%define devname libpgm-devel

Name:          openpgm
Version:       5.3.128
Release:       alt1_4
Summary:       An implementation of the PGM reliable multicast protocol
Group:         System/Libraries
# The license is LGPLv2.1
License:       LGPLv2
URL:           https://github.com/steve-o/openpgm
Source0:       https://github.com/steve-o/%{name}/archive/release-%{uver}.zip
Patch1:        openpgm-autoconf.patch
BuildRequires: perl
BuildRequires: bash sh
Source44: import.info

%description
OpenPGM is an open source implementation of the Pragmatic General
Multicast (PGM) specification in RFC 3208.

%package -n %{libname}
Summary:       Library files for %{name}
Group:         System/Libraries
Obsoletes:     %{_lib}%{name}0 < %{version}-%{release}

%description -n %{libname}
This package contains OpenPGM libraries.

%package -n %{devname}
Summary:       Development files for %{name}
Group:         System/Libraries
Requires:      %{libname} = %{version}-%{release}
Provides:      %{name}%{api}-devel = %{version}-%{release}
Provides:      %{name}-devel = %{version}-%{release}
Obsoletes:     %{_lib}%{name}-devel < %{version}-%{release}

%description -n %{devname}
This package contains OpenPGM related development libraries and header files.

%prep
%setup -q -n %{name}-release-%{uver}/%{name}/pgm
%patch1 -p1


%build
# Fix .pc.in version (already fixed in upstream git)
mv %{name}-5.2.pc.in %{name}-5.3.pc.in
./bootstrap.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc COPYING LICENSE
%{_libdir}/libpgm-%{api}.so.%{major}
%{_libdir}/libpgm-%{api}.so.%{major}.*

%files -n %{devname}
%doc examples/
%{_includedir}/*
%{_libdir}/libpgm.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc


%changelog
* Thu Aug 31 2023 Igor Vlasenko <viy@altlinux.org> 5.3.128-alt1_4
- update by mgaimport

* Mon Dec 28 2020 Igor Vlasenko <viy@altlinux.ru> 5.3.128-alt1_2
- new version

* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 5.2.122-alt1_21
- fixed build

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 5.2.122-alt1_3
- new version

