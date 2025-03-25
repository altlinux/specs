Name: sysbar
Version: 9.9.9
Release: alt1
Summary: Sysbar is a modular status bar for wayland written in gtkmm4
Group: Graphical desktop/Other
License: WTFPL
Url: https://github.com/System64fumo/sysbar

Source: %name-%version.tar

BuildRequires: gcc-c++ make
BuildRequires: libgtkmm4-devel libgtk4-layer-shell-devel
BuildRequires: jsoncpp-devel libcurl-devel libwireplumber-0.5-devel libdbus-devel playerctl-devel libnl-devel

%description
%summary

%prep
%setup -n %name-%version

%build
%make_build

%install
mkdir -p %buildroot%prefix
%makeinstall_std PREFIX=%_prefix

%files
%doc LICENSE README.md
%_bindir/%name
%_libexecdir/libsysbar.so
%_datadir/sys64/bar/*.css
%_datadir/sys64/bar/*.conf

%changelog

* Tue Mar 25 2025 Artyom Bystrov <arbars@altlinux.org> 9.9.9-alt1
- initial build for ALT Sisyphus
