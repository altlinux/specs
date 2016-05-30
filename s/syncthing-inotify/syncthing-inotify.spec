Name: syncthing-inotify
Version: 0.8
Release: alt1
Summary: File watcher intended for use with Syncthing
License: MPL-2.0
Group: Networking/Other
Url: https://github.com/syncthing/syncthing-inotify

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: golang

%description
Syncthing (core) uses a rescan interval to detect changes in folders.
This application (syncthing-inotify) uses OS primitives to detect changes
as soon as they happen. Therefore, if you save a file, syncthing-inotify
will know about it and pass this information to Syncthing such that near
real-time synchronisation can be achieved.

%prep
%setup
%patch -p1

%build
mkdir -p build/src/ build/vendor/
export GOPATH="$PWD/build:$PWD/build/vendor"

mkdir -p build/src/github.com/syncthing/%name
ls | sed '/^build$/d' | xargs cp -at build/src/github.com/syncthing/%name/

pushd build/src/github.com/syncthing/%name/
go install
popd

%install
install -Dm 0755 build/bin/%name %buildroot%_bindir/%name
install -Dm 0644 etc/linux-systemd/system/%name@.service        \
  %buildroot%_unitdir/%name@.service
install -Dm 0644 etc/linux-systemd/user/%name.service           \
  %buildroot%_libexecdir/systemd/user/%name.service

%files
%doc LICENSE README.md
%_bindir/%name
%_unitdir/%name@.service
%_libexecdir/systemd/user/%name.service

%changelog
* Mon May 30 2016 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- first build for Sisyphus

