Name: acos-config
Version: 0.1.1
Release: alt1

Summary: Files for ignition in ALTCOS
License: GPL-3.0-or-later
Group: System/Configuration/Boot and Init

Source: altcos-%version.tar

Requires: ignition dracut bash mount coreutils
BuildArch: noarch

%description
Files for ignition in ALTCOS

%prep
%setup -n altcos-%version

%install
mkdir -p %buildroot/%_unitdir
install -m 0644 ignition-firstboot-complete.service %buildroot/%_unitdir

mkdir -p %buildroot/%prefix/lib/dracut/modules.d/35ignition-altcos
install -m 0755 dracut/35ignition-altcos/*.sh %buildroot/%prefix/lib/dracut/modules.d/35ignition-altcos
install -m 0644 dracut/35ignition-altcos/ignition-setup-user.service %buildroot/%prefix/lib/dracut/modules.d/35ignition-altcos

%files
%_unitdir/*
%_prefix/lib/dracut/modules.d/*

%changelog
* Wed Sep 29 2021 Andrey Sokolov <keremet@altlinux.org> 0.1.1-alt1
- Rename ACOS to ALTCOS

* Fri Sep 10 2021 Andrey Sokolov <keremet@altlinux.org> 0.1-alt1
- Initial release
