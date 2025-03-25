Name: syslock
Version: 9.9.9
Release: alt1
Summary: Syslock is a simple lockscreen for wayland written in gtkmm4
Group: Graphical desktop/Other
License: WTFPL
Url: https://github.com/System64fumo/syslock

Source: %name-%version.tar

BuildRequires: gcc-c++ make
BuildRequires: libgtkmm4-devel libgtk4-layer-shell-devel
BuildRequires: libpam0-devel libevdev-devel
BuildRequires: wayland-protocols libwayland-client-devel

%description
%summary

%prep
%setup -n %name-%version

%build
%make_build

%install

%makeinstall_std PREFIX=%_prefix

%files
%doc LICENSE README.md
%_bindir/%name
%_libexecdir/libsyslock.so
%_datadir/sys64/lock/*.css
%_datadir/sys64/lock/*.conf

%changelog

* Tue Mar 25 2025 Artyom Bystrov <arbars@altlinux.org> 9.9.9-alt1
- initial build for ALT Sisyphus
