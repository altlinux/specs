Name: rest-server
Version: 0.12.0
Release: alt1

Summary: Rest Server is a high performance HTTP server that implements restic's REST backend API

Group: Development/Tools
License: BSD-2-Clause license
Url: https://github.com/restic/rest-server

# Source-url: https://github.com/restic/rest-server/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

Source2: %name.service

BuildRequires(pre): rpm-macros-golang
ExclusiveArch: %go_arches

BuildRequires: golang >= 1.17

%description
Rest Server is a high performance HTTP server that implements restic's REST backend API.
It provides secure and efficient way to backup data remotely, using restic backup client via the rest: URL.

%prep
%setup -a1

%build
export GOFLAGS=-mod=vendor
go build -o %name ./cmd/rest-server

%install
install -D -p -m 755 %name %buildroot%_sbindir/%name
install -D -m 644 %SOURCE2 %buildroot%_unitdir/%name.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md
%_sbindir/%name
%_unitdir/%name.service

%changelog
* Wed Jun 07 2023 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- new version 0.12.0 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- initial build for ALT Sisyphus
