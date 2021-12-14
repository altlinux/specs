Name: kometa-xdg
Summary: XDG desktop settings for Kometa distros
Summary(ru): Настройки рабочего окружения дистрибутивов Комета
License: GPL-3.0
Group: Graphical desktop/Other
Version: 1.1
Release: alt1
Source0: kometa-xdg-%version.tar
Source1: COPYING
BuildArch: noarch

%description
XDG desktop settings for Kometa distros
%description -l ru_RU.UTF-8
Настройки рабочего окружения дистрибутивов Комета

#--------------------------------------------------------------

%package core
Summary: DE-agnostic desktop settings for Kometa distros
Summary(ru): DE-независимые настройки рабочих окружений дистрибутивов Комета
Group: Graphical desktop/Other
Requires: sed

%description core
DE-agnostic desktop settings for Kometa distros
%description -l ru_RU.UTF-8 core
DE-независимые настройки рабочих окружений дистрибутивов Комета

%files core
%doc COPYING
%dir /etc/xdg/kometa
%_bindir/kometa-xdg-env
# XXX ALT has no macro for /usr/lib/systemd/...
/usr/lib/systemd/user-environment-generators/10-kometa-xdg.sh
/etc/profile.d/10-kometa-xdg.sh

#--------------------------------------------------------------

# alternatives between plasma5-classic, plasma5-foo etc. can be added later

%package plasma5-classic
Summary: KDE 5 desktop settings for classic variant of Kometa
Summary(ru): Настройки KDE 5 для классического варианта Кометы
Group: Graphical desktop/KDE
Requires: %name-core = %EVR
Requires: kometa-icons-theme-classic

%description plasma5-classic
KDE 5 desktop settings for classic variant of Kometa
%description -l ru_RU.UTF-8 plasma5-classic
Настройки KDE 5 для классического варианта Кометы

%files plasma5-classic
%doc COPYING
/etc/xdg/kometa/dolphinrc
#/etc/xdg/kometa/kcminputrc
/etc/xdg/kometa/kdeglobals
/etc/xdg/kometa/kxkbrc

#--------------------------------------------------------------

%prep
%setup -q
cp %SOURCE1 .

%build
:

%install

mkdir -p %buildroot%_bindir
mkdir -p %buildroot/etc/profile.d
mkdir -p %buildroot/usr/lib/systemd/user-environment-generators
install -m0755 scripts/kometa-xdg-env %buildroot%_bindir/kometa-xdg-env
# for console
install -m0755 scripts/profile.sh %buildroot/etc/profile.d/10-kometa-xdg.sh
# for dbus services
install -m0755 scripts/systemd.sh %buildroot/usr/lib/systemd/user-environment-generators/10-kometa-xdg.sh

mkdir -p %buildroot/etc/xdg/kometa
install -m0644 plasma5/* %buildroot/etc/xdg/kometa

%check
cd scripts
./test.sh

%changelog
* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.1-alt1
- set default icon theme

* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt1
- Init
