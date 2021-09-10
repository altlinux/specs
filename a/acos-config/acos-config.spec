Name: acos-config
Version: 0.1
Release: alt1

Summary: Files for ignition in ACOS
License: GPL-3.0-or-later
Group: System/Configuration/Boot and Init

Source: acos-%version.tar

Requires: ignition dracut bash mount coreutils
BuildArch: noarch

%description
Files for ignition in ACOS

%prep
%setup -n acos-%version

%install
mkdir -p %buildroot/%_unitdir
install -m 0644 ignition-firstboot-complete.service %buildroot/%_unitdir

mkdir -p %buildroot/%prefix/lib/dracut/modules.d/35ignition-acos
install -m 0755 dracut/35ignition-acos/*.sh %buildroot/%prefix/lib/dracut/modules.d/35ignition-acos
install -m 0644 dracut/35ignition-acos/ignition-setup-user.service %buildroot/%prefix/lib/dracut/modules.d/35ignition-acos

%files
%_unitdir/*
%_prefix/lib/dracut/modules.d/*

%changelog
* Fri Sep 10 2021 Andrey Sokolov <keremet@altlinux.org> 0.1-alt1
- Initial release
