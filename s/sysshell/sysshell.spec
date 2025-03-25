Name: sysshell
Version: 9.9.9
Release: alt1
Summary: Sysshell is a generic shell for wayland written in gtkmm 4
Group: Graphical desktop/Other
License: WTFPL
Url: https://github.com/System64fumo/sysshell

Source: %name-%version.tar

BuildRequires: gcc-c++ make
BuildRequires: libgtkmm4-devel libgtk4-layer-shell-devel

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
%doc README.md
%_bindir/%name
%_datadir/sys64/shell/*.conf

%changelog

* Tue Mar 25 2025 Artyom Bystrov <arbars@altlinux.org> 9.9.9-alt1
- initial build for ALT Sisyphus
