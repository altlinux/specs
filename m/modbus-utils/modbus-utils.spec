%define unpackaged_files_terminate_build 1

Name: modbus-utils
Version: 1.0.0
Release: alt1

Summary: CLI utilities to work with Modbus devices
License: %mit

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-macros-cmake
Group: Other
Url: https://github.com/Krzysztow/modbus-utils
Source0: %name-%version.tar

BuildRequires: cmake
BuildRequires: libmodbus-devel

%description
Client and server CLI utilities to work with Modbus devices

%prep
%setup -q

%build
%cmake
%install
%cmakeinstall_std
%files
%_bindir/modbus_client
%_bindir/modbus_server

%changelog
* Tue Aug 10 2021 Aleksey Saprunov <sav@altlinux.org> 1.0.0-alt1
- Initial release

