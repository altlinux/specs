# TODO : https://github.com/rust-lang/cargo/issues/7058
Name: croc
Version: 9.6.15
Release: alt1

Summary: Easily and securely send things from one computer to another

License: MIT
Group: System/Servers
Url: https://schollz.com/software/croc6

# Source-url: https://github.com/schollz/croc/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExcludeArch: %ix86 ppc64le

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
croc is a tool that allows any two computers to simply and securely transfer files and folders.
AFAIK, croc is the only CLI file-transfer tool that does all of the following:

* allows any two computers to transfer data (using a relay)
* provides end-to-end encryption (using PAKE)
* enables easy cross-platform transfers (Windows, Linux, Mac)
* allows multiple file transfers
* allows resuming transfers that are interrupted
* local server or port-forwarding not needed
* ipv6-first with ipv4 fallback
* can use proxy, like tor

%prep
%setup -a 1

%build
go build -mod=vendor

%install
install -D -m 0755 croc %buildroot%_bindir/croc
install -D -m 0644 croc.service %buildroot%_unitdir/croc.service

%files
%doc README.md
%_bindir/croc
%_unitdir/croc.service

%changelog
* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 9.6.15-alt1
- new version (9.6.15) with rpmgs script

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 0.0.7-alt1
- initial build for ALT Sisyphus
