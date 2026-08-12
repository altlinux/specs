%define _unpackaged_files_terminate_build 1

Name: desktopify-lite
Version: 1.0.6
Release: alt1

Summary: Turn any website into a desktop app launcher
License: MIT
Group: Networking/Other
Url: https://github.com/miniguys/desktopify-lite
Vcs: https://github.com/miniguys/desktopify-lite.git

Source: %name-%version.tar

BuildRequires: golang

%description
Turn any website into a desktop app launcher. Supported chromium-style
browsers, others require specific settings.

%prep
%setup

%build
%make_build build

%install
install -Dm0755 %name %buildroot%_bindir/%name

%files
%doc README.md
%doc LICENSE
%_bindir/%name

%changelog
* Tue Aug 11 2026 Mikhail Nogin <joycap@altlinux.org> 1.0.6-alt1
- Initial built for Sisyphus.
