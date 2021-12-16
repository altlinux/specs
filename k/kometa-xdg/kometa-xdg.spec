Name: kometa-xdg
Summary: XDG desktop settings for Kometa distros
Summary(ru): Настройки рабочего окружения дистрибутивов Комета
License: GPL-3.0
Group: Graphical desktop/Other
Version: 1.2
Release: alt1
Source0: kometa-xdg-%version.tar
Source1: COPYING
BuildArch: noarch
BuildRequires: rpm-macros-systemd

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
%_user_env_gen_dir/10-kometa-xdg.sh
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

%define regex auth[[:space:]]([[:space:]]).*pam_env.so user_envfile=.kometa_env readenv=0 user_readenv=1

%package pam-env
Summary: Hack PAM configs to make Qt5 applications ran by usermode use Kometa icons
Summary(ru): Хак конфигов PAM, чтобы запущенные через usermode приложения на Qt5 использовали иконки Кометы
Group: System/Base
# %%_qt5_plugindir/platformthemes/libqgtk3.so
Requires: libqt5-gui
Requires: pam
Requires(post): /bin/echo
Requires(post): grep
Requires(post): pam-config
Requires(preun): grep
Requires(preun): sed

%description pam-env
Hack PAM configs to make Qt5 applications ran by usermode use Kometa icons.
%description -l ru_RU.UTF-8 pam-env
Некоторые приложения, например, acc (alterator-standalone), запускаются из-под
пользовательской сессии от root через usermode и при этом используют basealt
в качестве иконки. В KDE 5 под X11 приложение само после запуска устанавливает иконку
на панели задач. Темы иконок kometa* в качестве иконки basealt устанавливают логотип
Кометы вместо Базальта, чтобы не создавать ошибочное впечатление, что Комета — продукт
Базальта. Но из-под root Qt5 не узнает тему иконок и использует иконку basealt не из
темы Кометы. Этот пакет при установке подключает выставление переменной окружения
QT_QPA_PLATFORMTHEME=gtk3 для root, благодаря чему Qt5 начинает использовать
пользовательскую тему иконок под root. Удаление пакета отключает выставление переменной.

%files pam-env
# copied to /root/.kometa_env by scriptlet
%_datadir/kometa-pam-env

%post pam-env
# sisyphus_check does not allow to package files inside /root,
# that is why I have to make this hack.
# IMHO it's OK to package /root/* here as in rootfiles.
cp %_datadir/kometa-pam-env /root/.kometa_env

# This scriptlet sees if pam_env.so <...> exists in PAM configuration and adds it to there if it does not.
# It does not add if if a sysadmin manually commented it out.
# /etc/control.d/facilities/ seemed to be too complex and not easy to use for this task, so inventing a bicycle.
TEXT='auth\t\toptional\tpam_env.so user_envfile=.kometa_env readenv=0 user_readenv=1'
# based on /etc/control.d/facilities/pam_access
CONFIG_COMMON=/etc/pam.d/system-auth-common
CONFIG_SYSTEM=/etc/pam.d/system-auth
if [ -f "$CONFIG_COMMON" ]
then
    CONFIG="$CONFIG_COMMON"
else
    CONFIG="$(readlink -e "$CONFIG_SYSTEM")" || CONFIG="$CONFIG_SYSTEM"
fi
if ! grep -qE "%regex" "$CONFIG"
then
    echo "Adding loading ~/.kometa_env into PAM configs..."
    cp "$CONFIG" "$CONFIG".rpmsave
    # do not rely that shell-builtin 'echo' is capable of '-e' (not POSIX sh)
    /bin/echo -e "$TEXT" >> "$CONFIG"
fi

%preun pam-env
# Package removal, not upgrade
if [ "$1" -eq 0 ]; then
    for file in /etc/pam.d/system-auth-common /etc/pam.d/system-auth
    do
        if grep -qE "^%regex" "$file"; then
            echo "Removing loading ~/.kometa_env from PAM config ${file}..."
            sed -i'.rpmsave' -E -e "/^%regex/d" "$file"
        fi
    done
    unlink /root/.kometa_env
fi
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
install -m0755 scripts/systemd.sh %buildroot%_user_env_gen_dir/10-kometa-xdg.sh

mkdir -p %buildroot/etc/xdg/kometa
install -m0644 plasma5/* %buildroot/etc/xdg/kometa

mkdir -p %buildroot%_datadir
echo QT_QPA_PLATFORMTHEME=gtk3 > %buildroot/%_datadir/kometa-pam-env

%check
cd scripts
./test.sh

%changelog
* Thu Dec 16 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.2-alt1
- Hack to make alterator use correct icons (new subpackage kometa-xdg-pam-env)
- Use macro for directory with systemd user environment generators (thanks to ldv@)

* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.1-alt1
- set default icon theme

* Tue Dec 14 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt1
- Init
