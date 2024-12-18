%if "%(rpmquery --qf '%%{VERSION}' libssl-devel)" >= "3"
%def_enable providers
%endif

%define _unitdir %_prefix/lib/systemd/system

Name: dnsdist
Version: 1.9.8
Release: alt1

Summary: Highly DNS-, DoS- and abuse-aware loadbalancer

License: GPL-2.0-only
Group: Networking/DNS
Url: https://dnsdist.org

Source: https://downloads.powerdns.com/releases/%name-%version.tar.bz2

# Automatically added by buildreq on Fri Nov 08 2024
# optimized out: boost-devel-headers glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libabseil-cpp-devel libabseil-cpp2407.0.0 libgpg-error libstdc++-devel node perl pkg-config sh5 systemd
BuildRequires: boost-devel boost-lockfree-devel gcc-c++ libcap-devel libcdb-devel libedit-devel libfstrm-devel liblmdb-devel libnghttp2-devel libre2-devel libsodium-devel libssl-devel libsystemd-devel node-uglify-js perl-parent
BuildRequires: systemd libxdp-devel libbpf-devel
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

# run as dnsdist user
sed -i '/^ExecStart/ s/dnsdist/dnsdist -u dnsdist -g dnsdist/' dnsdist.service.in

%build
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
    --with-re2

rm html/js/*
make min_js

%make_build
cp dnsdist.conf-dist dnsdist.conf.sample

%install
%makeinstall_std

# install systemd unit file
install -D -p -m 644 %name.service %buildroot%_unitdir/%name.service
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
%doc dnsdist.conf.sample
%doc README.md
%doc COPYING
%_bindir/%name
%_man1dir/%name.1*
%_unitdir/%name.service
%_unitdir/%name@.service
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/dnsdist.conf

%changelog
* Wed Dec 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.8-alt1
- New version (1.9.8) with rpmgs script.

* Wed Nov 20 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt3
- Fixed service startup (ALT #52112).

* Mon Nov 11 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt2
- Enabled tls providers with OpenSSL >= 3.0 only.

* Fri Nov 08 2024 Leontiy Volodin <lvol@altlinux.org> 1.9.7-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
