Name: syncthing
Version: 0.14.13
Release: alt1
Summary: FOSS Continuous File Synchronisation
Summary(ru_RU.UTF-8): Свободная программа непрерывной синхронизации файлов
License: MPL-2.0
Group: Networking/Other
Url: https://syncthing.net/
#https://github.com/syncthing/syncthing
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires: go >= 1.3
BuildRequires: udev-rules

%description
Syncthing replaces proprietary sync and cloud services with
something open, trustworthy and decentralised. Your data is your
data alone and you deserve to choose where it is stored, if it is
shared with some third party and how it's transmitted over the
Internet.

%description -l ru_RU.UTF-8
Syncthing призван заменить собой проприетарные программы синхронизации и
облачные сервисы на открытый, надёжный и децентрализованный сервис. Ваши данные
это ваши данные и вы должны иметь возможность выбрать, где им храниться,
совместно с какой-то третьей стороной или нет, и как им передаваться через
Интернет.

%prep
%setup

%build
mkdir -p build/src/ build/vendor/
export GOPATH="$PWD/build:$PWD/build/vendor"

mkdir -p build/src/github.com/%name/%name
ls | sed '/^build$/d' | xargs cp -at build/src/github.com/%name/%name
cp -a vendor build/vendor/src

pushd build/src/github.com/%name/%name/
go run build.go -version v%version -no-upgrade
popd

%install
install -Dm 0755 build/src/github.com/%name/%name/bin/%name \
  %buildroot%_bindir/%name
install -Dm 0644 etc/linux-systemd/system/%name@.service        \
  %buildroot%_unitdir/%name@.service
install -Dm 0644 etc/linux-systemd/system/%name-resume.service  \
  %buildroot%_unitdir/%name-resume.service
install -Dm 0644 etc/linux-systemd/user/%name.service           \
  %buildroot%_libexecdir/systemd/user/%name.service

%files
%doc AUTHORS CONDUCT.md CONTRIBUTING.md LICENSE README.md
%_bindir/%name
%dir /lib/systemd
%dir %_unitdir/
%_unitdir/%name@.service
%_unitdir/%name-resume.service
%dir %_libexecdir/systemd
%dir %_libexecdir/systemd/user
%_libexecdir/systemd/user/%name.service

%changelog
* Mon Dec 05 2016 Denis Smirnov <mithraen@altlinux.ru> 0.14.13-alt1
- new version 0.14.13

* Wed Nov 23 2016 Anton Midyukov <antohami@altlinux.org> 0.14.12-alt1
- new version 0.14.12

* Thu Nov 10 2016 Anton Midyukov <antohami@altlinux.org> 0.14.10-alt1
- new version 0.14.10

* Sun Oct 09 2016 Anton Midyukov <antohami@altlinux.org> 0.14.8-alt1
- new version 0.14.8

* Sun Sep 04 2016 Anton Midyukov <antohami@altlinux.org> 0.14.5-alt1
- new version 0.14.5
- added cronbuild-update-source

* Sun Aug 21 2016 Denis Smirnov <mithraen@altlinux.ru> 0.14.4-alt1
- new version 0.14.4
- disable auto update

* Mon Jul 18 2016 Anton Midyukov <antohami@altlinux.org> 0.13.10-alt1
- new version 0.13.10

* Wed Jun 08 2016 Denis Medvedev <nbr@altlinux.org> 0.13.5-alt1
- new version 0.13.5

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 0.13.4-alt1
- New version (Closes: 32138).

* Tue Apr 26 2016 Anton Midyukov <antohami@altlinux.org> 0.12.22-alt1
- Initial build for ALT Linux Sisyphus.
