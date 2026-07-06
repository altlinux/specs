%if "%(rpmquery --qf '%%{VERSION}' libssl-devel)" >= "3"
%def_enable providers
%endif

%if "%(rpmquery --qf '%%{VERSION}' libbpf-devel)" < "1"
%def_disable xsk
%else
%def_enable xsk
%endif

%def_enable meson

%define _unitdir %_prefix/lib/systemd/system

Name: dnsdist
Version: 2.1.0
Release: alt1

Summary: Highly DNS-, DoS- and abuse-aware loadbalancer

License: GPL-2.0-only
Group: Networking/DNS
Url: https://dnsdist.org
VCS: https://github.com/PowerDNS/pdns
# NOTE: see https://www.dnsdist.org/changelog.html for CVEs.

Source0: %name-%version.tar.xz
Source1: dnsdist.1
Patch: %name-%version-%release.patch

ExcludeArch: i586

# Automatically added by buildreq on Fri Nov 08 2024
# optimized out: boost-devel-headers glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libabseil-cpp-devel libabseil-cpp2407.0.0 libgpg-error libstdc++-devel node perl pkg-config sh5 systemd
# libstdc++-devel-static: -lstdc++fs
BuildRequires: boost-devel boost-lockfree-devel gcc-c++ libstdc++-devel-static libcap-devel libcdb-devel libedit-devel libfstrm-devel liblmdb-devel libnghttp2-devel libre2-devel libsodium-devel libssl-devel libsystemd-devel node-uglify-js perl-parent python3-module-yaml libgnutls-devel
BuildRequires: systemd libbpf-devel ragel
%if_enabled meson
BuildRequires: meson
%endif
%if_enabled xsk
BuildRequires: libxdp-devel
%endif
%ifarch %ix86 x86_64 %mips aarch64 loongarch64
BuildRequires: libluajit-devel
%else
BuildRequires: lua-devel
%endif

%description
dnsdist is a highly DNS-, DoS- and abuse-aware loadbalancer. Its goal in life
is to route traffic to the best server, delivering top performance to
legitimate users while shunting or blocking abusive traffic.

%prep
%setup
%patch -p1

cd pdns/dnsdistdist

# run as dnsdist user
sed -i '/^ExecStart/ s/dnsdist/dnsdist -u dnsdist -g dnsdist/' \
    dnsdist.service.in \
    dnsdist.service.meson.in

# fix version detection
sed -i "s|version: run_command.*|version: '%version',|" \
    meson.build

%build
cd pdns/dnsdistdist

%if_enabled meson

%meson \
    --sysconfdir=%_sysconfdir/%name \
    -Ddnscrypt=enabled \
    -Ddns-over-https=enabled \
    -Ddns-over-tls=enabled \
%if_enabled providers
    -Dtls-libssl-providers=true \
%endif
    -Dunit-tests=true \
    -Dcdb=enabled \
    -Dlmdb=enabled \
    -Dnghttp2=enabled \
    -Dre2=enabled \
    -Dtls-gnutls=enabled \
    -Dman-pages=false \
%if_disabled xsk
    -Debpf=disabled \
    -Dxsk=disabled \
%endif
#
%meson_build

%else

%autoreconf
%configure \
    --sysconfdir=%_sysconfdir/%name \
    --disable-static \
    --disable-dependency-tracking \
    --disable-silent-rules \
    --enable-dnscrypt \
    --enable-dns-over-https \
    --enable-dns-over-tls \
%if_enabled providers
    --enable-tls-providers \
%endif
    --enable-unit-tests \
    --with-cdb \
    --with-lmdb \
    --with-nghttp2 \
    --with-re2 \
    --with-gnutls \
%if_disabled xsk
    --with-ebpf=no \
    --with-xsk=no \
%endif
#

rm html/js/*
make min_js

%make_build
%endif

cp dnsdist.conf-dist dnsdist.conf.sample

%install
cd pdns/dnsdistdist
%if_enabled meson
%meson_install
%else
%makeinstall_std
%endif

# install systemd unit file
install -D -p -m 644 %_target_platform/%name.service %buildroot%_unitdir/%name.service
install -d %buildroot%_man1dir/
install -D -p %SOURCE1 %buildroot%_man1dir/%name.1
install -d %buildroot%_sysconfdir/%name/
mv %buildroot%_sysconfdir/%name/dnsdist.conf-dist %buildroot%_sysconfdir/%name/dnsdist.conf

%pre
getent group dnsdist >/dev/null || groupadd -r dnsdist
getent passwd dnsdist >/dev/null || \
    useradd -r -g dnsdist -d / -s /sbin/nologin \
    -c "dnsdist user" dnsdist
exit 0

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%doc pdns/dnsdistdist/dnsdist.conf.sample
%doc README.md
%doc COPYING
%_bindir/%name
%_man1dir/%name.1*
%_unitdir/%name.service
%_unitdir/%name@.service
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/dnsdist.conf

%changelog
* Mon Jul 06 2026 Leontiy Volodin <lvol@altlinux.org> 2.1.0-alt1
- New version 2.1.0.

* Mon Jun 29 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.7-alt1
- New version 2.0.7 (Fixes: CVE-2026-40210, CVE-2026-40209,
  CVE-2026-42004, CVE-2026-40211, CVE-2026-40208, CVE-2026-42005,
  CVE-2026-40011).

* Mon Jun 01 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.6-alt1
- New version 2.0.6.

* Thu Apr 23 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.5-alt1
- New version 2.0.5 (Fixes: CVE-2026-33257, CVE-2026-33260,
  CVE-2026-33593, CVE-2026-33596, CVE-2026-33597,
  CVE-2026-33598, CVE-2026-33599, CVE-2026-33602,
  CVE-2026-33254, CVE-2026-33595, CVE-2026-33594).

* Fri Apr 10 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt2
- Fixed version detection (ALT #58639).

* Thu Apr 09 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt1.2
- Listed closed CVEs for older versions (backport).

* Thu Apr 09 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt1.1
- Listed closed CVEs (Fixes: CVE-2026-0396, CVE-2026-0397,
  CVE-2026-24028, CVE-2026-24029, CVE-2026-24030,
  CVE-2026-27853, CVE-2026-27854).

* Wed Apr 01 2026 Leontiy Volodin <lvol@altlinux.org> 2.0.3-alt1
- New version 2.0.3.
- Added VCS tag.
- Built using meson.

* Thu Dec 04 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.2-alt1
- New version (2.0.2) with rpmgs script.
- Enabled gnutls support.

* Thu Sep 18 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.1-alt1
- New version (2.0.1) with rpmgs script (Fixes: CVE-2025-4820,
  CVE-2025-4821, CVE-2025-7054, CVE-2025-8671, CVE-2025-30187).

* Wed Jul 23 2025 Leontiy Volodin <lvol@altlinux.org> 2.0.0-alt1
- New version (2.0.0) with rpmgs script.

* Tue May 27 2025 Leontiy Volodin <lvol@altlinux.org> 1.9.10-alt1
- New version (1.9.10) with rpmgs script.
- Excluded build on i586.

* Mon May 05 2025 Leontiy Volodin <lvol@altlinux.org> 1.9.9-alt1
- New version (1.9.9) with rpmgs script.

* Tue Jan 21 2025 Leontiy Volodin <lvol@altlinux.org> 1.9.8-alt2
- Simplified backport to older branches (XSK support).

* Wed Dec 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.8-alt1
- New version (1.9.8) with rpmgs script.

* Wed Nov 20 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt3
- Fixed service startup (ALT #52112).

* Mon Nov 11 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt2
- Enabled tls providers with OpenSSL >= 3.0 only.

* Fri Nov 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
