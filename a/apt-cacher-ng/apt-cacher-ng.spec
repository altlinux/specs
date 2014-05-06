Name: apt-cacher-ng
Version: 0.7.25
Release: alt1

Summary: Caching HTTP download proxy for software packages

License: BSD
Group: Networking/Other
Url: http://www.unix-ag.uni-kl.de/~bloch/acng/

Source: http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%version.orig.tar
Patch0: acng-conf.patch
Patch1: acng-init.patch

# Automatically added by buildreq on Wed May 30 2012
# optimized out: cmake cmake-modules libstdc++-devel pkg-config
BuildRequires: boost-devel-headers bzlib-devel ccmake gcc-c++ libfuse-devel liblzma-devel zlib-devel

BuildRequires: boost-devel bzlib-devel gcc-c++ libfuse-devel zlib-devel liblzma-devel

%description
Apt-Cacher NG is a caching HTTP download proxy for software packages,
primarily for Debian/Ubuntu clients. It's partially based on concepts
of Apt-Cacher but is rewritten with a main focus on performance and low
resource usage.

%prep
%setup
%patch0 -p 1
%patch1 -p 1
echo "-llzma" >> link.flags

%build
%make_build all

%install
mkdir -p %buildroot%_sbindir
install build/apt-cacher-ng %buildroot%_sbindir/
install build/in.acng %buildroot%_sbindir/

mkdir -p %buildroot%_libdir/%name
install expire-caller.pl distkill.pl urlencode-fixer.pl %buildroot%_libdir/%name/

mkdir -p %buildroot%_sysconfdir/%name
cp -a conf/* %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
cat <<'_EOF'_ > %buildroot%_sysconfdir/apt/apt.conf.d/%name
# Uncomment next line to enable %name in apt
# Acquire::http { Proxy "http://localhost:3142"; };
_EOF_

mkdir -p %buildroot%_initdir
install -m755 acng.init %buildroot%_initdir/acng

mkdir -p %buildroot%_man8dir
install -m644 doc/man/*.8 %buildroot%_man8dir

mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_cachedir/%name/

%files
%_sbindir/apt-cacher-ng
%_sbindir/in.acng
%_libdir/%name/
%config %_sysconfdir/%name/
%config %_sysconfdir/apt/apt.conf.d/%name
%_initdir/acng
%_man8dir/*
%doc COPYING README TODO
%doc doc/html
%doc doc/apt-cacher-ng.pdf
%dir %_logdir/%name/
%dir %_cachedir/%name/

%post
%post_service acng

%preun
%preun_service acng

%changelog
* Tue May 06 2014 Vitaly Lipatov <lav@altlinux.ru> 0.7.25-alt1
- new version 0.7.25 (with rpmrb script)

* Mon Aug 06 2012 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt1
- new version 0.7.7 (with rpmrb script)
- apply patches (ALT bug #24731)
- from Vadim Druzhin <cdslow@mail.ru>:
 + removed xinetd stuf
 + added init script
 + added APT proxy config

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1.1
- Fixed build

* Sat Apr 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- initial build for ALT Linux Sisyphus
