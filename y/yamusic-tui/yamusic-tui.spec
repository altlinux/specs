Name: yamusic-tui
Version: 0.7.1
Release: alt1
License: GPL-3.0

Summary: An unofficial Yandex Music terminal client

Group: Sound

Url: https://github.com/DECE2183/yamusic-tui
Vcs: https://github.com/DECE2183/yamusic-tui.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

BuildRequires: pkgconfig(alsa)

%description
%summary.

To use this client, you should have a valid Yandex account and an access token.

%prep
%setup -a1

%build
%gobuild -mod=vendor

%install
install -D -m 0755 ./%name %buildroot/%_bindir/%name

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Sun Jun 15 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.7.1-alt1
- Initial build
