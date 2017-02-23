%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define _name dleyna
%define api_ver 1.0

Name: %_name-connector-dbus
Version: 0.2.0
Release: alt1

Summary: D-Bus connector for dLeyna services
Group: System/Servers
License: LGPLv2.1
Url: https://01.org/%_name/

%if_disabled snapshot
Source: https://01.org/%_name/sites/default/files/downloads/%name-%version.tar.gz
%else
#VCS: https://github.com/01org/dleyna-connector-dbus.git
Source: %name-%version.tar
%endif

BuildRequires: libgio-devel libdbus-devel libdleyna-core-devel

%description
%summary

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains pc-file for developing applications that
use %name.

%prep
%setup

%build
%autoreconf
%configure  --disable-static
%make_build

%install
%makeinstall_std

%files
%dir %_libdir/%_name-%api_ver/connectors
%_libdir/%_name-%api_ver/connectors/lib%name.so
%doc AUTHORS ChangeLog README

%files devel
%_pkgconfigdir/%name-%api_ver.pc

%exclude %_libdir/%_name-%api_ver/connectors/*.la


%changelog
* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus

