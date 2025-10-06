Name: altemu-overlayfs
Version: 0.1
Release: alt9

Summary: Merging several dirs with ROM files into one dir

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64 x86_64
BuildRequires(pre): rpm-macros-systemd

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%install
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 95-%name.preset %buildroot%_presetdir/95-%name.preset

mkdir -p %buildroot%_datadir/altemu
install -m 0644 dir-list %buildroot%_datadir/altemu/

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_datadir/altemu/dir-list
%_unitdir/%name.service
%_presetdir/95-%name.preset

%changelog
* Mon Oct 6 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt9
- Change method of check external storage

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt8
- Fix access rights

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt7
- Fix name of user
- Fix check if dir structure exist
- Change number of preset

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt6
- Improove script

* Tue Sep 30 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt5
- Update overlayfs mechanism

* Mon Sep 29 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt4
- Fix path for user data

* Fri Sep 25 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt3
- Add function for creating dirs of game systems
- Fix overlay creation

* Wed Sep 24 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Fix case with only one card

* Tue Sep 23 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
