Name: foreman-discovery-image-service
Version: 1.0.0
Release: alt1
Summary: Metapackage with dependencies for FDI

Group: System/Servers
License: GPLv2+
URL: https://github.com/theforeman/foreman-discovery-image

BuildArch: noarch

BuildRequires: ruby
BuildRequires: ruby-devel

Requires: smart-proxy
Requires: gem-smart-proxy-discovery

%description
Metapackage with dependencies for FDI

%package tui
Summary: Metapackage with dependencies for FDI TUI
Group: System/Servers
Requires: ruby
Requires: gem(newt)
Requires: gem(fast_gettext)

%description tui
Metapackage with dependencies for FDI text-user interface

%prep

%files

%files tui

%changelog
* Thu Nov 19 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus.
