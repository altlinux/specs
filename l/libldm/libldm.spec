# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xsltproc perl(JSON/PP.pm) pkgconfig(gio-unix-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global api 1.0
%global major 0
%define libname libldm%{api}_%{major}
%define devname libldm%{api}-devel

Name:           libldm
Version:        0.2.5
Release:        alt1_1
Summary:        A tool to manage Windows dynamic disks
Group:		System/Libraries
License:        LGPLv3+ and GPLv3+
URL:            https://github.com/mdbooth/libldm
Source0:        https://github.com/mdbooth/libldm/archive/%{name}-%{version}.tar.gz

BuildRequires:  glib2-devel >= 2.26.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.14.0
BuildRequires:  pkgconfig(devmapper) >= 1.0
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  libreadline-devel
BuildRequires:  gtk-doc
Source44: import.info

%description
libldm is a library for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted. It includes ldmtool, which
exposes this functionality as a command-line tool.

libldm is released under LGPLv3+. ldmtool is released under GPLv3+.

%package        -n %libname
Summary:        A tool to manage Windows dynamic disks
Group:          System/Libraries
Obsoletes:      %{_lib}ldm0 < 0.2.3-6

%description    -n %libname
libldm is a library for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted.

%package        -n %devname
Summary:        Development files for %{name}
Group:		Development/C
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Provides:       libldm-devel = %{version}-%{release}
Provides:       libldm%{api}-devel = %{version}-%{release}
Obsoletes:      %{_lib}ldm-devel < 0.2.3-6

%description    -n %devname
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i -e 's/-Werror //' src/Makefile.*
gtkdocize
autoreconf -i

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static --enable-gtk-doc
%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -delete

%files
%doc COPYING.lgpl COPYING.gpl
%{_bindir}/ldmtool
%{_mandir}/man1/ldmtool.1*

%files -n %libname
%doc COPYING.lgpl COPYING.gpl
%{_libdir}/libldm-%{api}.so.%{major}*

%files -n %devname
%doc %{_datadir}/gtk-doc/*
%{_includedir}/*
%{_libdir}/libldm-%{api}.so
%{_libdir}/pkgconfig/ldm-%{api}.pc




%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.2.5-alt1_1
- update by mgaimport

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_2
- update by mgaimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1_1
- update by mgaimport

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_7
- fixed build

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_6
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_5
- new version

