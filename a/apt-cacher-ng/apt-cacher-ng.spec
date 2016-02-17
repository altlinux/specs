Name: apt-cacher-ng
Version: 0.8.5
Release: alt2

Summary: Caching HTTP download proxy for software packages

License: BSD
Group: Networking/Other
Url: http://www.unix-ag.uni-kl.de/~bloch/acng/

Source: http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%version.orig.tar
Source1: acng.service
Source2: acng.init
Patch0: acng-conf.patch
Patch1: acng-0.8.5-alt-vfilepattern.patch
Patch2: acng-0.8.5-alt-perl_tobase64.patch

# Automatically added by buildreq on Wed May 30 2012
# optimized out: cmake cmake-modules libstdc++-devel pkg-config
BuildRequires: boost-devel boost-devel-headers bzlib-devel ccmake gcc-c++ libfuse-devel liblzma-devel zlib-devel openssl-devel

%description
Apt-Cacher NG is a caching HTTP download proxy for software packages,
primarily for Debian/Ubuntu clients. It's partially based on concepts
of Apt-Cacher but is rewritten with a main focus on performance and low
resource usage.

%prep
%setup
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1
echo "-llzma" >> link.flags

%build
%make_build all

%install
mkdir -p %buildroot%_sbindir
install -p -m 755 build/apt-cacher-ng %buildroot%_sbindir/
install -p -m 755 build/in.acng %buildroot%_sbindir/

mkdir -p %buildroot%_libexecdir/%name
install -p -m 755 scripts/{expire-caller.pl,distkill.pl,urlencode-fixer.pl} %buildroot%_libexecdir/%name/
install -p -m 755 build/acngtool %buildroot%_libexecdir/%name/

mkdir -p %buildroot%_sysconfdir/%name
cp -a conf/* %buildroot%_sysconfdir/%name/

mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
cat <<'_EOF'_ > %buildroot%_sysconfdir/apt/apt.conf.d/%name.conf
// Uncomment next line to enable %name in apt
// Acquire::http { Proxy "http://localhost:3142"; };
_EOF_

mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE2 %buildroot%_initdir/acng

mkdir -p %buildroot%_man8dir
install -p -m644 doc/man/*.8 %buildroot%_man8dir

mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_cachedir/%name/

install -pDm 644 %SOURCE1 %buildroot%_unitdir/acng.service
install -pDm 644 systemd/%name.conf %buildroot/lib/tmpfiles.d/%name.conf

%pre
/usr/sbin/groupadd -r -f %name ||:
/usr/sbin/useradd -g %name -c '%name pseudouser' \
	-d %_cachedir/%name -s /dev/null -r %name >/dev/null 2>&1 ||:

%files
%_unitdir/acng.service
/lib/tmpfiles.d/*
%_sbindir/apt-cacher-ng
%_sbindir/in.acng
%_libexecdir/%name/
%config(noreplace) %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%name.conf
%_initdir/acng
%_man8dir/*
%doc COPYING README TODO
%doc doc/html
%doc doc/apt-cacher-ng.pdf
%dir %attr(0775,root,%name) %_logdir/%name/
%dir %attr(0770,root,%name) %_cachedir/%name/

%post
chown -R root:%name %_cachedir/%name ||:
chmod -R ug+rw %_cachedir/%name ||:
chown root:%name %_logdir/%name/* ||:
chmod ug+rw %_logdir/%name/* ||:
%post_service acng

%preun
%preun_service acng

%changelog
* Thu Feb 18 2016 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt2
- Add git.alt task support in vfilepattern

* Mon Aug 31 2015 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt1
- 0.8.5
- vfilepattern patch updated
- TOBASE64 patch for fix perl deparsing in perl.req
- Replace %%_libdir to %%_libexecdir

* Fri Nov 21 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt2
- 0.8.0
- %name pseudouser/group (just as in upstream) for daemon
- vfilepattern patch updated
- Cleanup BuildRequires
- Update sysv init script to run as pseudouser and extract it from patch

* Sun Aug 17 2014 Terechkov Evgenii <evg@altlinux.org> 0.7.27-alt2
- Set (noreplace) on config files

* Fri Aug 15 2014 Terechkov Evgenii <evg@altlinux.org> 0.7.27-alt1
- 0.7.27 (includes fix for CVE-2014-4510)

* Fri Aug 15 2014 Terechkov Evgenii <evg@altlinux.org> 0.7.25-alt2
- Rename/rewrite apt.conf.d/apt-cacher-ng (ALT bug #30212)
- Patch2 added with alt-specific volatile file patterns
- Systemd unit file added

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
