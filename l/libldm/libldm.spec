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
Version:        0.2.3
Release:        alt1_6
Summary:        A tool to manage Windows dynamic disks
Group:		System/Libraries
License:        LGPLv3+ and GPLv3+
URL:            https://github.com/mdbooth/libldm
Source0:        %{url}/downloads/%{name}-%{version}.tar.gz
Patch0:         cast_be64toh.patch
Patch1:         libldm-gtype.patch
Patch2:         libldm-security.patch
Patch3:         fix-build-with-gcc7.patch

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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static --enable-gtk-doc
%make_build V=1

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
* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_6
- update by mgaimport

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_5
- new version

