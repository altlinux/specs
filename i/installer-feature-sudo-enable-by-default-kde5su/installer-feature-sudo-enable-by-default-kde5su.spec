
Name: installer-feature-sudo-enable-by-default-kde5su
Version: 1.0
Release: alt1%ubt

Group: System/Configuration/Other
Summary: Setup kdesu for using sudo by default
Summary(ru_RU.UTF8): Настройка утилиты kdesu для использования sudo
License: GPL
Url: http://wiki.sisyphus.ru/devel/installer/features

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt

%description
Setup kdesu for using sudo by default.
%description -l ru_RU.UTF8
Настройка утилиты kdesu для использования sudo.

%package stage3
Group: System/Configuration/Other
Summary: Setup kdesu for using sudo by default
Summary(ru_RU.UTF8): Настройка утилиты kdesu для использования sudo
Requires: sudo
%description stage3
Setup kdesu for using sudo by default.
%description stage3 -l ru_RU.UTF8
Настройка утилиты kdesu для использования sudo.

%prep
%setup -q

%install
%makeinstall

%files stage3
%_datadir/install2/postinstall.d/*

%changelog
* Fri Apr 28 2017 Sergey V Turchin <zerg@altlinux.org> 1.0-alt1%ubt
- initial build
