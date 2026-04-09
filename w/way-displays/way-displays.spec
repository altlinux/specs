Name: way-displays
Version: 1.15.0
Release: alt1
Summary: Auto Manage Your Wayland Displays
License: MIT
Group: Graphical desktop/Other

Source: %name-%version.tar

BuildRequires: libinput-devel libwlroots0.18-devel libyaml-cpp-devel gcc gcc-c++ wayland-devel libwayland-client-devel
Requires: libinput-gestures

%description
%summary

%prep
%setup -n %name-%version

%build
%make_build

%install
mkdir -p %buildroot%_sysconfdir/%name
%makeinstall_std PREFIX=%_prefix PREFIX_ETC=/

%files
%_bindir/%name
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/cfg.yaml
%_man1dir/%name.1.xz
%changelog
* Thu Apr  9 2026 Artyom Bystrov <arbars@altlinux.org> 1.15.0-alt1
- Initial build for ALT.
