%define bname jellyfin

Name:    %bname-web
Version: 10.11.8
Release: alt1

Summary: The Free Software Media System - Official Web Client
License: GPL-2.0
Group:   Video
Url:     https://jellyfin.org
Vcs:     https://github.com/jellyfin/jellyfin-web.git

Source0: %name-%version.tar
Source1: node_modules.tar

BuildRequires: /proc
BuildRequires: npm

ExclusiveArch: x86_64

%description
%summary.

%prep
%setup -a1

%build
npm_config_offline=true \
npm run build:production

%install
install -d %buildroot%_libexecdir/%bname/%name
cp -Rfv dist/* %buildroot%_libexecdir/%bname/%name

%files
%doc *.md
%_libexecdir/%bname/%name

%changelog
* Mon Apr 06 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 10.11.8-alt1
- Initial build for Sisyphus.
