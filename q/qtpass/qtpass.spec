# SPEC file for QtPass
#

%define real_name    QtPass

Name:     qtpass
Version:  1.4.0
Release:  alt1.1

Summary: a multi-platform GUI for pass, the standard unix password manager
Summary(ru_RU.UTF-8): кросс-платформенный интерфейс к менеджеру паролей pass

Group:    Text tools
License:  %gpl3plus
URL:      https://qtpass.org/
# URL: https://github.com/IJHack/qtpass

Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version-%release.patch

Patch1:  %name-1.1.6-alt-desktop.patch

Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png

BuildRequires(pre): rpm-build-licenses desktop-file-utils
BuildRequires(pre): rpm-macros-qt5-webengine


# Automatically added by buildreq on Tue Jan 28 2020
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-test libqt5-widgets libqt5-xml libstdc++-devel python-modules python2-base python3 python3-base python3-dev qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel ruby ruby-stdlibs sh4
BuildRequires: kf5-kwallet-devel python3-module-mpl_toolkits qt5-multimedia-devel qt5-phonon-devel qt5-script-devel qt5-svg-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
%ifarch %qt5_qtwebengine_arches
BuildRequires: qt5-webengine-devel
%endif

Requires: gnupg gnupg2 git-core pwgen

%description
QtPass is a multi-platform GUI for pass, the standard unix
password manager, with the following features:

* Reading pass password stores
* Displaying the password and related info
* Editing and adding of passwords and information
* Per-folder user selection for multi-user password stores
* Updating to and from a git repository
* Copying password to clipboard
* Using pass or git and gpg2 directly
* And other

%description -l ru_RU.UTF-8
QtPass -  кроссплатформенный графический интерфейс к менеджеру
паролей pass, с поддержкой:

* чтение хранилищ паролей pass,
* отображение паролей и сопутствующей информации
* редактирование и добавление паролей в хранилище
* поддержка выбора пользоваталей для многопользовательских хранилищ
* поддержка размещения хранилища паролей в репозитории git,
* копирование паролей в буфер обмена,
* работа с использованием pass или напрямую через git и gpg2
* и прочее.


%prep
%setup  -n %real_name-%version
%patch0 -p1

%patch1

## TEMPORARY FIX program version - 1.3.3 not released yet:
sed -e 's#1\.3\.3#1.3.2-371-gcfac4db8#' -i Doxyfile
sed -e 's#1\.3\.3#1.3.2-371-gcfac4db8#' -i qtpass.iss
sed -e 's#1\.3\.3#1.3.2-371-gcfac4db8#' -i qtpass.pri
sed -e 's#1\.3\.3#1.3.2-371-gcfac4db8#' -i qtpass.plist

mv -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/LICENSE) LICENSE

%build
%qmake_qt5  PREFIX=%buildroot%prefix
%make_build

%install
%makeinstall

install -D -m0644 -- qtpass.desktop %buildroot%_desktopdir/%name.desktop

install -D -m0644 -- artwork/icon.svg   %buildroot%_iconsdir/hicolor/scalable/apps/qtpass-icon.svg
install -D -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -D -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

install -D -m0644 -- qtpass.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml

%files
%doc README.md CHANGELOG.md FAQ.md
%doc --no-dereference LICENSE

%_bindir/%name

%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_datadir/appdata/%name.appdata.xml

%changelog
* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 1.4.0-alt1.1
- NMU: Use rpm-macros-qt5-webengine (fixes build on loongarch64)

* Sun Oct 29 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.4.0-alt1
- New version
- ppc64le: avoid webengine (missing)

* Tue Aug 03 2021 Michael Shigorin <mike@altlinux.org> 1.3.2-alt3.gitcfac4db8.1
- E2K: avoid webengine (missing)
- Enable parallel build

* Fri Jun 18 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3.2-alt3.gitcfac4db8
- Fix GPG keys info in the users dialog window

* Sun Mar 14 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3.2-alt2.gitcfac4db8
- Update to current development state
  - Fix renaming passwords and directories failures
  - Fix support for passwords names contained dots
  - Update translations
  - Other bugfixes

* Tue Jan 28 2020 Nikolay A. Fetisov <naf@altlinux.org> 1.3.2-alt1
- New version

* Mon Jun 11 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.3-alt1
- New version

* Sat May 12 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.2-alt1
- New version

* Mon Jan 08 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.2.1-alt1
- New version
  - Insecure password generation fixed

* Sat Dec 09 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.2.0-alt1
- New version

* Thu Jan 26 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.1.6-alt1
- Initial build for ALT Linux Sisyphus

