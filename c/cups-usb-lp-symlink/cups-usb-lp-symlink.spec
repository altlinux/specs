Name: cups-usb-lp-symlink
Version: 0.1
Release: alt2

Summary(ru_RU.UTF-8): Создание симлинка на /dev/usb/lp0
Summary: Symlink /dev/usb/lp0

License: GPLv3
Group: System/Configuration/Other
Url: http://os.mos.ru
BuildArch: noarch
Requires: cups
Source: %name-%version.tar

%description
%summary https://bugzilla.altlinux.org/41736

%description -l ru_RU.UTF-8
Решение проблемы https://bugzilla.altlinux.org/41736 созданием ссылки /dev/lp0

%prep
%setup

%install
mkdir -p %buildroot%_unitdir
mkdir -p %buildroot%_presetdir

install -pm644 usb-lp-wa.path %buildroot%_unitdir/usb-lp-wa.path
install -pm644 usb-lp-wa.service %buildroot%_unitdir/usb-lp-wa.service
cat > %buildroot%_presetdir/80-%name.preset << 'EOF'
enable usb-lp-wa.path
EOF

%post
%post_service usb-lp-wa.path

%preun
%preun_service usb-lp-wa.path

%files
%_unitdir/usb-lp-wa.path
%_unitdir/usb-lp-wa.service
%_presetdir/80-%name.preset

%changelog
* Thu Jan 19 2023 Artem Proskurnev <tema@altlinux.org> 0.1-alt2
- changing RemainAfterExit to avoid multiple startup

* Wed Jan 18 2023 Artem Proskurnev <tema@altlinux.org> 0.1-alt1
- Init

