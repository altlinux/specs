Name: syncthing
Version: 0.12.22
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
облачные сервисы на открытый, надежный и децентрализованный сервис. Ваши данные
это ваши данные и вы должны иметь возможность выбрать, где им храниться,
совместно с какой-то третьей стороной или нет, и как им передаваться через
Интернет.

%prep
%setup

%build
export GOPATH="$PWD/build"
mkdir -p build/src/github.com/%name/%name
ls | sed '/^build$/d' | xargs cp -at build/src/github.com/%name/%name
go run build.go -no-upgrade

%install
install -Dm 0755 bin/%name %buildroot%_bindir/%name
install -Dm 0644 etc/linux-systemd/system/%name@.service       \
%buildroot%_unitdir/%name@.service
install -Dm 0644 etc/linux-systemd/system/%name-resume.service \
%buildroot%_unitdir/%name-resume.service
install -Dm 0644 etc/linux-systemd/user/%name.service \
%buildroot%_sysconfdir/systemd/user/%name.service

%files
%doc AUTHORS CONDUCT.md CONTRIBUTING.md LICENSE README.md
%_bindir/%name
%_unitdir/%name@.service
%_unitdir/%name-resume.service
%_sysconfdir/systemd/user/%name.service

%changelog
* Tue Apr 26 2016 Anton Midyukov <antohami@altlinux.org> 0.12.22-alt1
- Initial build for ALT Linux Sisyphus.
