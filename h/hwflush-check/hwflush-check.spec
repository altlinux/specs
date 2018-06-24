Name: hwflush-check
Version: 0.1
Release: alt1

Summary: Tool to check how data is flushed on disk

Group: System/Configuration/Hardware
License: BSD like
Url: https://github.com/vitlav/hwflush-check

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/vitlav/hwflush-check.git
Source: %name-%version.tar

%description
hwflush-check is a tool to check how data is flushed on disk.
hwflush-check tests filesystem consystency under power failure conditions.
It does write; fsync; power-cut, and then checks that the data
it has written is actully on disk after bootup.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README.md LICENSE
%_sbindir/%name

%changelog
* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
