Name: apt-cacher-ng
Version: 3.7.5
Release: alt1

Summary: Caching HTTP download proxy for software packages

License: BSD-4-Clause
Group: Networking/Other
Url: https://www.unix-ag.uni-kl.de/~bloch/acng/

# Source-url: https://deb.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%version.orig.tar.xz
Source: %name-%version.tar
Source2: acng.init
Patch0: acng-conf.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ pkg-config
BuildRequires: bzlib-devel liblzma-devel zlib-devel
BuildRequires: libevent-devel libcares-devel
BuildRequires: libssl-devel
BuildRequires: libsystemd-devel

# workaround for sysvinit: see ALT bugs 11359 and 32101:
Requires: su

%description
Apt-Cacher NG is a caching HTTP download proxy for software packages,
primarily for Debian/Ubuntu clients. It's partially based on concepts
of Apt-Cacher but is rewritten with a main focus on performance and low
resource usage.

%prep
%setup
%patch0 -p 1

%build
%cmake \
    -DACNG_CACHE_DIR=%_cachedir/%name \
    -DACNG_LOG_DIR=%_logdir/%name \
    -DSDINSTALL=ON
%cmake_build

%install
%cmake_install

mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
cat <<'_EOF_' > %buildroot%_sysconfdir/apt/apt.conf.d/%name.conf
// Uncomment next line to enable %name in apt
// Acquire::http { Proxy "http://localhost:3142"; };
_EOF_

mkdir -p %buildroot%_initdir
install -p -m755 %SOURCE2 %buildroot%_initdir/acng

mkdir -p %buildroot%_logdir/%name/
mkdir -p %buildroot%_cachedir/%name/

%pre
/usr/sbin/groupadd -r -f %name ||:
/usr/sbin/useradd -g %name -c '%name pseudouser' \
	-d %_cachedir/%name -s /dev/null -r %name >/dev/null 2>&1 ||:

%files
/lib/systemd/system/%name.service
%_prefix/lib/tmpfiles.d/%name.conf
%_sbindir/apt-cacher-ng
%_libdir/libsupacng.so
%_prefix/lib/%name/
%config(noreplace) %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%name.conf
%_sysconfdir/avahi/services/%name.service
%_initdir/acng
%_man8dir/*
%_datadir/doc/%name/
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
* Wed Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 3.7.5-alt1
- new version 3.7.5 (major update from 0.8.5)
- switch to cmake build with proper paths
- drop obsolete patches (vfilepattern, perl_tobase64)
- update dependencies: drop boost/fuse, add libevent/libcares
- use upstream systemd service
- remove in.acng binary (dropped upstream)

* Tue Apr 08 2025 Vitaly Lipatov <lav@altlinux.ru> 0.8.5-alt5
- use %%cmake macros for build

* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 0.8.5-alt4.1
- NMU: Rebuild with new openssl 1.1.0.

* Mon Jun 27 2016 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt4
- Add release.debuginfo to vfilepattern

* Fri May 20 2016 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt3
- Add manual Requires: su

* Thu Feb 18 2016 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt2
- Add git.alt task support in vfilepattern

* Mon Aug 31 2015 Terechkov Evgenii <evg@altlinux.org> 0.8.5-alt1
- 0.8.5
- vfilepattern patch updated
- TOBASE64 patch for fix perl deparsing in perl.req
- Replace %%_libdir to %%_libexecdir

* Fri Nov 21 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt2
- 0.8.0
- %%name pseudouser/group (just as in upstream) for daemon
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
