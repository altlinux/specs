Name: f3-qt
Version: 2.1.0
Release: alt1

Summary: A simple GUI for F3 - Fight Flash Fraud.
License: GPLv3
Group: System/Configuration/Other
Url: https://github.com/zwpwjwtz/f3-qt

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires: gcc-c++ libxml2-devel libglade-devel
BuildRequires: qt5-base-devel qt5-tools-devel
Requires: f3

%description
%summary

%prep
%setup

%build
qmake-qt5
%make_build

%install
install -Dm0755 %name %buildroot%_bindir/%name
install -Dm0644 f3.png %buildroot%_liconsdir/%name.png
mkdir -p  %buildroot%_desktopdir && cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=F3-qt
Type=Application
Terminal=false
Exec=beesu %name
Icon=%name
Categories=System;
Comment=Detect flash cards capacity with f3 utility
Comment[fr]=Détecte la capacité des cartes flash avec l'utilitaire f3
Comment[ru_RU]=Проверка ёмкости флеш-накопителей чере утилиту F3
Comment[zh_CN]=使用f3测试闪存卡的容量
Comment[zh_TW]=使用f3實用程序檢測閃存卡容量
GenericName=Flash capacity test
GenericName[fr]=Test de capacité de flash
GenericName[ru_RU]=Тест флеш-накопителей
GenericName[zh_CN]=闪存容量测试
GenericName[zh_TW]=閃存容量測試
EOF

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Thu Dec 12 2024 Artyom Bystrov <arbars@altlinux.org> 2.1.0-alt1
- Initial commit