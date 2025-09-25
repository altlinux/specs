Name: altemu-overlayfs
Version: 0.1
Release: alt2

Summary: Merging several dirs with ROM files into one dir

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64
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
install -m 0644 20-%name.preset %buildroot%_presetdir/20-%name.preset

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_unitdir/%name.service
%_presetdir/20-%name.preset

%changelog
* Wed Sep 24 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Fix case with only one card

* Tue Sep 23 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
