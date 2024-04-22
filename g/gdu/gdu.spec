Name: gdu
Version: 5.27.0
Release: alt2

Summary: Fast disk usage analyzer with console interface written in Go

Group: File tools
License: MIT
Url: https://github.com/dundee/gdu

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/dundee/gdu/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExclusiveArch: %go_arches
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-golang

BuildRequires: rpm-build-golang

%description
GDU is a fast disk usage analyzer with console interface written in Go for Unix/Linux systems.

Gdu is intended primarily for SSD disks where it can fully utilize parallel processing.
However HDDs work as well, but the performance gain is not so huge.

%prep
%setup -a1

%build
export GOFLAGS="-mod=vendor -trimpath -modcacherw -pgo=default.pgo"
export LDFLAGS="-s -w -X 'github.com/dundee/gdu/v5/build.Version=%version-%release'"
#export CGO_ENABLED=0
%gobuild github.com/dundee/gdu/v5/cmd/gdu
#go build -o dist/%name

%install
install -D -p -m 755 %name %buildroot%_bindir/%name
install -Dpm 0755 %name.1 %buildroot%_man1dir/gdu.1

%files
%doc LICENSE.md README.md
%_man1dir/*
%_bindir/%name

%changelog
* Mon Apr 22 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.27.0-alt2
- NMU: fixed FTBFS on LoongArch (don't try to build a static binary)

* Wed Apr 17 2024 Vitaly Lipatov <lav@altlinux.ru> 5.27.0-alt1
- initial build for ALT Sisyphus
