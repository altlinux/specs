%define _unpackaged_files_terminate_build 1
%define _localstatedir /var

%def_disable dnstap
%def_disable doc

Name: knot-resolver
Version: 5.6.0
Release: alt1
Summary: Caching full DNS Resolver
Group: System/Servers

License: GPLv3
Url: https://www.knot-resolver.cz/
Source0: %name-%version.tar
Source11: lua-aho-corasick.tar

Patch0: %name-%version.patch

ExclusiveArch: %luajit_arches

BuildRequires(pre): meson >= 0.49 rpm-macros-luajit rpm-macros-systemd
BuildRequires: gcc-c++ luajit
BuildRequires: pkgconfig(cmocka)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(libknot) >= 3.0.2
BuildRequires: pkgconfig(libzscanner) >= 3.0.2
BuildRequires: pkgconfig(libdnssec) >= 3.0.2
BuildRequires: pkgconfig(libnghttp2)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libcap-ng)
BuildRequires: pkgconfig(libuv) >= 1.7
BuildRequires: pkgconfig(luajit) >= 2.0
BuildRequires: pkgconfig(openssl)
BuildRequires: liblmdb-devel
%{?_enable_dnstap:BuildRequires: /usr/bin/protoc-c pkgconfig(libfstrm) pkgconfig(libprotobuf-c) >= 1.0.0}
%{?_enable_doc:BuildRequires: /usr/bin/sphinx-build-3}
Requires: lua5.1-module-basexx
Requires: lua5.1-module-cqueues
Requires: lua5.1-module-http
Requires: lua5.1-module-psl

%description
The Knot Resolver is a DNSSEC-enabled caching full resolver implementation
written in C and LuaJIT, including both a resolver library and a daemon.
Modular architecture of the library keeps the core tiny and efficient, and
provides a state-machine like API for extensions.

The package is pre-configured as local caching resolver.
To start using it, start a single kresd instance:
$ systemctl start kresd@1.service


%package -n libkres
Summary: Library for Knot Resolver
Group: System/Libraries

%description -n libkres
This package contains shared libraries used by %name's daemons
and clients.

%package -n libkres-devel
Summary: Development headers for Knot Resolver
Group: Development/C

%description -n libkres-devel
The package contains development headers for Knot Resolver.

%package doc
Summary: Documentation for Knot Resolver
BuildArch: noarch
Group: Documentation

%description doc
Documentation for Knot Resolver

%package module-http
Summary: HTTP module for Knot Resolver
Group: System/Servers
Requires: %name = %EVR
Requires: lua5.1-module-http
Requires: lua5.1-module-mmdblua

%description module-http
HTTP module for Knot Resolver can serve as API endpoint for other modules or
provide a web interface for local visualization of the resolver cache and
queries. It can also serve DNS-over-HTTPS, but it is deprecated in favor of
native C implementation, which doesn't require this package.

%prep
%setup
tar -xf %SOURCE11 -C modules/policy/lua-aho-corasick
%patch0 -p1

%build
%meson \
    %{?_enable_doc:-Ddoc=enabled} \
    -Dsystemd_files=enabled \
    -Dclient=enabled \
    -Dunit_tests=enabled \
    -Dmanaged_ta=enabled \
    -Dkeyfile_default="%_sharedstatedir/%name/root.keys" \
    -Dinstall_root_keys=enabled \
    -Dinstall_kresd_conf=enabled \
    %{?_enable_dnstap:-Ddnstap=enabled}

%meson_build

%install
%meson_install

# add kresd.target to multi-user.target.wants to support enabling kresd services
install -m 0755 -d %buildroot%_unitdir/multi-user.target.wants
ln -s ../kresd.target %buildroot%_unitdir/multi-user.target.wants/kresd.target

# remove modules with missing dependencies
#rm %buildroot%_libdir/%name/kres_modules/etcd.lua
#rm %buildroot%_libdir/%name/kres_modules/experimental_dot_auth.lua
#rm -r %buildroot%_libdir/%name/kres_modules/http
#rm %buildroot%_libdir/%name/kres_modules/http*.lua
#rm %buildroot%_libdir/%name/kres_modules/prometheus.lua

mkdir -p %buildroot%_cachedir/%name
rm -rf %buildroot%_defaultdocdir/*

%check
export LD_LIBRARY_PATH=$(pwd)/%{__builddir}/lib:$(pwd)/%{__builddir}
%meson_test

%pre
groupadd -r -f %name >/dev/null 2>&1 ||:
useradd -M -r -d %_sharedstatedir/%name -s /bin/false -c "Knot Resolver" -g %name %name >/dev/null 2>&1 ||:

%post
%post_systemd_postponed kresd@*.service kres-cache-gc.service kresd.target

%preun
%systemd_preun kresd@*.service kres-cache-gc.service kresd.target

%files
%doc COPYING AUTHORS NEWS etc/config/config.*
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/kresd.conf
%config(noreplace) %_sysconfdir/%name/root.hints
%_sysconfdir/%name/icann-ca.pem
%attr(750,%name,%name) %dir %_sharedstatedir/%name
%attr(640,%name,%name) %_sharedstatedir/%name/root.keys
%attr(750,%name,%name) %dir %_cachedir/%name
%_unitdir/kresd@.service
%_unitdir/kres-cache-gc.service
%_unitdir/kresd.target
%_unitdir/multi-user.target.wants/kresd.target
/lib/sysusers.d/knot-resolver.conf
%_tmpfilesdir/%name.conf
%_man7dir/*
%_sbindir/kresd
%_sbindir/kresc
%_sbindir/kres-cache-gc
%_libdir/%name
%_man8dir/*
%exclude %_libdir/%name/debug_opensslkeylog.so
%exclude %_libdir/%name/kres_modules/http
%exclude %_libdir/%name/kres_modules/http*.lua
%exclude %_libdir/%name/kres_modules/prometheus.lua

%files -n libkres
%_libdir/libkres.so.*

%files -n libkres-devel
%_includedir/libkres
%_pkgconfigdir/libkres.pc
%_libdir/libkres.so

%if_enabled doc
%files doc
%doc html
%endif

%files module-http
%_libdir/%name/debug_opensslkeylog.so
%_libdir/%name/kres_modules/http
%_libdir/%name/kres_modules/http*.lua
%_libdir/%name/kres_modules/prometheus.lua

%changelog
* Fri Mar 24 2023 Alexey Shabalin <shaba@altlinux.org> 5.6.0-alt1
- 5.6.0

* Thu Sep 29 2022 Alexey Shabalin <shaba@altlinux.org> 5.5.3-alt1
- 5.5.3

* Mon Aug 08 2022 Alexey Shabalin <shaba@altlinux.org> 5.5.1-alt1
- 5.5.1

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 5.5.0-alt1
- 5.5.0

* Fri Jan 07 2022 Alexey Shabalin <shaba@altlinux.org> 5.4.4-alt1
- 5.4.4

* Thu Dec 23 2021 Alexey Shabalin <shaba@altlinux.org> 5.4.3-alt1
- 5.4.3
- Switch to systemd macros int post and preun.

* Mon Nov 01 2021 Alexey Shabalin <shaba@altlinux.org> 5.4.2-alt1
- 5.4.2

* Mon Sep 13 2021 Alexey Shabalin <shaba@altlinux.org> 5.4.1-alt1
- 5.4.1

* Fri Aug 06 2021 Alexey Shabalin <shaba@altlinux.org> 5.4.0-alt1
- 5.4.0

* Tue May 18 2021 Alexey Shabalin <shaba@altlinux.org> 5.3.2-alt1
- 5.3.2

* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 5.3.1-alt1
- 5.3.1

* Wed Dec 16 2020 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt1
- 5.2.1

* Wed Nov 25 2020 Alexey Shabalin <shaba@altlinux.org> 5.2.0-alt1
- 5.2.0

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.3-alt1
- 5.1.3

* Fri Aug 07 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.2-alt1
- 5.1.2

* Fri May 22 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.1-alt1
- 5.1.1 (Fixes: CVE-2020-12667)

* Fri May 08 2020 Alexey Shabalin <shaba@altlinux.org> 5.1.0-alt1
- 5.1.0

* Sun Mar 29 2020 Alexey Shabalin <shaba@altlinux.org> 5.0.1-alt2
- add requires on lua5.1 modules

* Thu Mar 19 2020 Alexey Shabalin <shaba@altlinux.org> 5.0.1-alt1
- Initial build.

