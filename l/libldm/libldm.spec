# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/xsltproc perl(JSON/PP.pm) pkgconfig(gio-unix-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global major 0
%define libname libldm%{major}
%define devname libldm-devel
Name:           libldm
Version:        0.2.3
Release:        alt1_5
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
Group:		System/Libraries

%description    -n %libname
libldm is a library for managing Microsoft Windows dynamic disks, which use
Microsoft's LDM metadata. It can inspect them, and also create and remove
device-mapper block devices which can be mounted.

%package        -n %devname
Summary:        Development files for %{name}
Group:		Development/C
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Provides:	libldm-devel = %{version}-%{release}

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
%configure --disable-static --enable-gtk-doc
%make V=1


%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'




%files
%doc COPYING.lgpl COPYING.gpl
%{_bindir}/ldmtool
%{_mandir}/man1/ldmtool.1*

%files -n %libname
%doc COPYING.lgpl COPYING.gpl
%{_libdir}/*.so.*


%files -n %devname
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/ldm-1.0.pc
%{_datadir}/gtk-doc




%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_5
- new version

