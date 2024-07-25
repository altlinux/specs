%global   import_path go.senan.xyz/cliphist

Name:     cliphist
Version:  0.5.0
Release:  alt1

Summary:  Wayland clipboard manager with support for multimedia
License:  GPLv3
Group:    Text tools
Url:      https://github.com/sentriz/cliphist

ExclusiveArch: %go_arches

# Source-url: https://github.com/sentriz/cliphist/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# auto predownloaded go modules during update version with rpmgs from etersoft-build-utils
# see for more information:
# https://www.altlinux.org/Etersoft-build-utils
# https://www.altlinux.org/Etersoft-build-utils/extra_sources

Source1: %name-development-%version.tar

Requires: wl-clipboard xdg-utils

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%prep
%setup -a1

%build
%gobuild %import_path

%install
install -D -p -m 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Thu Jul 25 2024 Roman Alifanov <ximper@altlinux.org> 0.5.0-alt1
- initial build
