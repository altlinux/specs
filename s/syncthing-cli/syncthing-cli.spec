%define basename syncthing
Name: syncthing-cli
Version: 0.1
Release: alt1.20150923.1
Summary: The Syncthing command line interface
Summary(ru_RU.UTF-8): Интерфейс командной строки для Syncthing
License: MPL-2.0
Group: Networking/Other
Url: https://syncthing.net/
#https://github.com/syncthing/syncthing
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires: go >= 1.3

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
mkdir -p build/src/ build/vendor/
export GOPATH="$PWD/build:$PWD/build/vendor"

mkdir -p build/src/github.com/%basename/%name
ls | sed '/^build$/d' | xargs cp -at build/src/github.com/%basename/%name
cp -a Godeps/_workspace/src build/vendor
pushd build/src/github.com/%basename/%name/

go install
popd

%install
install -Dm 0755 build/bin/%name %buildroot%_bindir/%name

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Tue May 31 2016 Anton Midyukov <antohami@altlinux.org> 0.1-alt1.20150923.1
- Initial build for ALT Linux Sisyphus.
