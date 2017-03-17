Name: asterisk-build-sounds
Summary: Helper scripts for build packages with asterisk sounds
Version: 0.0.1
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

%description
%summary

%prep
%setup
%install
install -m755 -D ast-install-core-sounds %buildroot%_bindir/ast-install-core-sounds
install -m755 -D ast-install-extra-sounds %buildroot%_bindir/ast-install-extra-sounds
%files
%_bindir/ast-install-core-sounds
%_bindir/ast-install-extra-sounds

%changelog
* Fri Mar 17 2017 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
