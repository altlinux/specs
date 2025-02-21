Name: darkhttpd
Version: 1.16
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
%summary.
When you need a web server in a hurry.
Features:
* simple to set up:
  - single binary, no other files, no installation needed,
  - standalone, doesn't need inetd or ucspi-tcp,
  - no messing around with config files;
* written in C - efficient and portable;
* small memory footprint;
* event loop, single threaded - no fork() or pthreads;
* generates directory listings;
* supports HTTP GET and HEAD requests;
* supports Range / partial content;
* supports If-Modified-Since;
* supports Keep-Alive connections;
* supports IPv6;
* can serve 301 redirects based on Host header;
* uses sendfile() on FreeBSD, Solaris and Linux;
* can use acceptfilter on FreeBSD;
* at some point worked on FreeBSD, Linux, OpenBSD, Solaris;
* ISC license.
Security:
* can log accesses, including Referer and User-Agent;
* can chroot;
* can drop privileges;
* impervious to /../ sniffing;
* times out idle connections;
* drops overly long requests.
Limitations:
* Only serves static content - no CGI.

%prep
%setup
cp %SOURCE1 .

%build
%make
scdoc < %name.1.scd > %name.1
xz %name.1

%install
mkdir -p %buildroot%_datadir/doc/%name-%version
install -Dpm 0751 darkhttpd %buildroot%_bindir/%name
install -Dpm 0644 README.md %buildroot%_datadir/doc/%name-%version
install -Dpm 0644 Dockerfile %buildroot%_datadir/doc/%name-%version
mkdir -p %buildroot%_datadir/doc/%name-%version/docker
install -Dpm 0644 group %buildroot%_datadir/doc/%name-%version/docker
install -Dpm 0644 passwd %buildroot%_datadir/doc/%name-%version/docker
mkdir -p %buildroot%_man1dir
install -Dpm 0644 %name.1.xz %buildroot%_man1dir

%files
%doc README.md Dockerfile group passwd
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Tue Feb 18 2025 Ulysses Apokin <ulysses@altlinux.org> 1.16-alt1
- Initial build for Sisyphus.
