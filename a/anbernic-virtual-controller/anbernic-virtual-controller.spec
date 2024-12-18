Name: anbernic-virtual-controller
Version: 0.1
Release: alt1

Summary: Set of tools to combine several input devices into one virtual controller on Anbernic handhelds

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64
BuildRequires(pre): rpm-macros-systemd

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Requires: evsieve

%description
%summary

%prep
%setup -n %name-%version

%install
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-%name.preset %buildroot%_presetdir/20-%name.preset

mkdir -p %buildroot%_udevrulesdir
install -m 0644 99-%name.rules %buildroot%_udevrulesdir/99-%name.rules


%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_unitdir/%name.service
%_udevrulesdir/99-%name.rules
%_presetdir/20-%name.preset


%changelog
* Wed Dec 18 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
