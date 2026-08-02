# SPEC file for QtPass
#

%define _unpackaged_files_terminate_build 1

%define real_name    QtPass

Name:     qtpass
Version:  1.7.0
Release:  alt1

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
BuildRequires(pre): rpm-macros-qt6-webengine


# Automatically added by buildreq on Sun Aug 02 2026
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdouble-conversion3 libgcc15-devel libglvnd-devel libgpg-error libp11-kit libqt6-core libqt6-dbus libqt6-gui libqt6-network libqt6-qml libqt6-test libqt6-widgets libsasl2-3 libstdc++-devel python3 python3-base qt6-base-devel qt6-tools sh5
BuildRequires: qt6-declarative-devel qt6-svg-devel qt6-tools-devel

%ifarch %qt6_qtwebengine_arches
BuildRequires: qt6-webengine-devel
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

mv -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/LICENSE) LICENSE

%build
%qmake_qt6  PREFIX=%buildroot%prefix
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
* Sun Aug 02 2026 Nikolay A. Fetisov <naf@altlinux.org> 1.7.0-alt1
- New version
   - Switch to Qt 6
   - Auto-detect Git in existing password-store
   - Use ed25519 for GPG key generation when available

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

