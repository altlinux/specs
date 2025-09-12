Name: darkhttpd
Version: 1.17
Release: alt1

Summary: Darkhttpd is a simple, fast HTTP 1.1 web server for static content
License: ISC
Group: System/Servers
Url: https://unix4lyfe.org/darkhttpd/
Vcs: https://github.com/emikulic/darkhttpd

Source0: %name-%version.tar
Source1: %name.1.scd

# To generate a man page
BuildRequires: scdoc

%description
A single binary HTTP server written in C, with a single-threaded, standalone
design that does not require inetd or ucspi-tcp. The server does not require
any configuration files and is designed to host static content (no CGI).

%prep
%setup
cp %SOURCE1 .

%build
%make
scdoc < %name.1.scd > %name.1
xz %name.1

%install
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/%name/docker
mkdir -p %buildroot%_man1dir
install -Dpm 0751 darkhttpd %buildroot%_bindir/%name
install -Dpm 0644 Dockerfile %buildroot%_datadir/%name
install -Dpm 0644 docker/group %buildroot%_datadir/%name/docker
install -Dpm 0644 docker/passwd %buildroot%_datadir/%name/docker
install -Dpm 0644 %name.1.xz %buildroot%_man1dir

%files
%doc README.md
%_datadir/%name
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Tue Sep 09 2025 Ulysses Apokin <ulysses@altlinux.org> 1.17-alt1
- New version.

* Tue Feb 18 2025 Ulysses Apokin <ulysses@altlinux.org> 1.16-alt1
- Initial build for Sisyphus.
