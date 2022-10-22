%define alterator_libexecdir %_prefix/libexec/alterator

Name: alterator-manager
Version: 0.0.3
Release: alt1

Summary: Modular tool for system configuration via D-Bus
License: GPL-2
Group: System/Configuration/Other

BuildRequires: cmake gcc
BuildRequires: libgio-devel libsystemd-devel

Source: %name-%version.tar

%description
Modular tool for system configuration via D-Bus.

%package devel
Summary: Headers for developing alterator-manager modules
Group: Development/Other
Requires: libgio-devel

%description devel
Headers for developing alterator-manager modules.


%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std
mkdir -p %buildroot%alterator_libexecdir

%files
%_sbindir/%name
%_datadir/dbus-1/system.d/ru.basealt.alterator_manager.conf
%_unitdir/alterator-manager.service
%dir %alterator_libexecdir

%files devel
%_includedir/alterator

%changelog
* Sat Oct 22 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.0.3-alt1
- Improve errors treatment.
- Rename source files from plugin to modules in common style.
- Add support loading backends prototype with interfaces from
  alterator_manager_interface in modules.

* Thu Oct 13 2022 Ivan Savin <svn17@altlinux.org> 0.0.2-alt1
- Add devel.

* Fri Aug 19 2022 Ivan Savin <svn17@altlinux.org> 0.0.1-alt1
- Initial commit.

