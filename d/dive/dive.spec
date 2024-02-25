%define gobuild go build

# TODO: build with external sources

Name: dive
Version: 0.12.0
Release: alt2

Summary: A tool for exploring each layer in a docker image

Group: Development/Tools
License: MIT
Url: https://github.com/wagoodman/dive

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/wagoodman/dive/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang

ExclusiveArch: x86_64 aarch64

BuildRequires: golang >= 1.7

%description
A tool for exploring a docker image, layer contents, and discovering ways to shrink the size of your Docker/OCI image.

%prep
%setup -a1

%build
export GOFLAGS=-mod=vendor
#make
#go fmt -x ./...
go build -o dist/%name

%check
export GOFLAGS=-mod=vendor
# skip coverage tests as for now
#make test


%install
install -D -p -m 755 ./dist/dive %buildroot%_bindir/%name

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Sun Feb 25 2024 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt2
- skip coverage tests

* Sun Feb 18 2024 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)
- build only for x86_64 and aarch64

* Mon Jan 02 2023 Vitaly Lipatov <lav@altlinux.ru> 0.10.0-alt1
- initial build for ALT Sisyphus
