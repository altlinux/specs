%global _unpackaged_files_terminate_build 1

Name: phaser
Version: 3.90.0
Release: alt1
Summary: Phaser - HTML5 Game Framework
License: MIT
Group: Development/Tools
Url: https://phaser.io/
VCS: https://github.com/phaserjs/phaser
Source: %name-%version.tar
Source1: node_modules.tar

BuildArch: noarch

BuildRequires: npm
BuildRequires: node-webpack
BuildRequires: node-webpack-cli

%description
Phaser is a fun, free and fast 2D game framework for making HTML5
games for desktop and mobile web browsers, supporting Canvas and
WebGL rendering.

%prep
%setup -a 1

%build
npm run distfull

%install
install -d %buildroot%_datadir/%name
cp -a dist types %buildroot%_datadir/%name

%files
%doc LICENSE.md
%_datadir/%name

%changelog
* Mon Feb 16 2026 Vladislav Eliseev <general@altlinux.org> 3.90.0-alt1
- Initial build for Sisyphus.
