Name: iced_comet
Version: 0.14.0
Release: alt1.10.g4b4eb891

Summary: Debugger for iced apps
License: MIT
Group: Development/Debuggers
Url: https://github.com/iced-rs/comet
Vcs: https://github.com/iced-rs/comet

BuildRequires(pre): rpm-build-rust

Source0: %name-%version.tar
Source1: vendor.tar

%description
Comet is a debugging tool for iced applications. It
receives telemetry from an attached app and shows
performance metrics and message history. It also
supports time-travel debugging.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc LICENSE

%changelog
* Fri Nov 20 2026 Vsevolod Myalitsin <r4nc@altlinux.org> 0.14.0-alt1.10.g4b4eb891
- Initial build for Sisyphus.

