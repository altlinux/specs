%global _unpackaged_files_terminate_build 1

Name: weathr
Version: 1.4.0
Release: alt1
Summary: A terminal weather app with ascii animation
License: GPL-3.0
Group: Other
Url: https://github.com/Veirt/weathr
VCS: https://github.com/Veirt/weathr

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
A terminal weather app with ASCII animations driven by real-time
weather data.
Features real-time weather from Open-Meteo with animated rain, snow,
thunderstorms, flying airplanes, day/night cycles, and auto-location
detection.

%prep
%setup -a 1
%rust_prep

%build
%rust_build
./target/release/%name --completions bash > %name.bash
./target/release/%name --completions zsh > _%name
./target/release/%name --completions fish > %name.fish

%install
%rust_install
mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d

install -m 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name.bash
install -m 0644 _%name %buildroot%_datadir/zsh/site-functions/_%name
install -m 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%doc LICENSE README.md

%_datadir/bash-completion/completions/%name.bash
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Mar 13 2026 Vladislav Eliseev <general@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
