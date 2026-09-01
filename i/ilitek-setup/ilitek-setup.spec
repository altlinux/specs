Name: ilitek-setup
Version: 0.1
Release: alt1
Summary: Set Phosh for Baikal M-based stand
License: GPL-2.0-or-later
Group: System/Configuration/Hardware
BuildRequires(pre): rpm-macros-systemd
AutoReq: no

Source: %name-%version.tar
BuildArch: noarch

%description
%summary

%prep
%setup -n %name-%version

%install

install -Dm0755 %name.sh %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-%name.preset %buildroot%_presetdir/

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_unitdir/%name.service
%_presetdir/20-%name.preset

%changelog
* Mon Aug 31 2026 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus