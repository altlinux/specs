# spec file for package innernet
#

Name: innernet
Version: 1.5.5
Release: alt1

Summary: a private network system that uses WireGuard under the hood
Summary(ru_RU.UTF-8): система построения сетей VPN на базе WireGuard

License: %mit
Group: System/Servers
Url: https://github.com/tonarino/innernet

Packager: Nikolay A. Fetisov <naf@altlinux.org>


Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: vendor.tar
Source2: config.toml

Source11: innernet@.service
Source12: innernet.service
Source13: innernet-server@.service
Source14: innernet-server.service


BuildRequires(pre): rpm-build-licenses
BuildRequires: /proc

# Automatically added by buildreq on Sat Jun 19 2021
# optimized out: ca-trust clang10.0 clang10.0-libs glibc-kernheaders-generic glibc-kernheaders-x86 libsasl2-3 llvm10.0-libs llvm11.0-libs pkg-config python-modules python2-base python3 python3-base python3-module-mpl_toolkits python3-module-paste ruby ruby-stdlibs rust sh4
BuildRequires: clang-devel libsqlite3-devel rust-cargo

# Extra automatic requires, need to remove (no lsb-core on ppc64le)
#BuildRequires: lsb-core

%description
Innernet is a private network system that uses WireGuard
under the hood.

This package contains a client to manage innernet network
interfaces.

%description -l ru_RU.UTF-8
Innernet - система организации частных сетей VPN с использованием
WireGuard.

Данный пакет содержит клиент для управления сетевыми интерфесами
innernet.



%package server
Summary: a server to coordinate innernet networks
Summary(ru_RU.UTF-8): управляющий сервер для сетей innernet
Group: System/Servers

%description server
Innernet is a private network system that uses WireGuard
under the hood.

This package contains a server to coordinate innernet networks.

%description server -l ru_RU.UTF-8
Innernet - система организации частных сетей VPN с использование
WireGuard.

Данный пакет содержит сервер innernet для координации работы
узлов сети.


%define innernet_user  _innernet
%define innernet_group _innernet

%define innernet_data /var/lib/%name

%prep
%setup
%patch0 -p1

# Rust packages, update them before new build!
tar xf %SOURCE1
install -Dm664 -- %SOURCE2 .cargo/config


%build
export CARGO_HOME=`pwd`/cargo

for pkg in client server; do
  pushd ${pkg}
    cargo build --release --offline
  popd
done


%install
# Binary files:
mkdir -p -- %buildroot%_sbindir
cp -a -- target/release/innernet{,-server} %{buildroot}%_sbindir

# Man pages:
mkdir -p -- %buildroot%_mandir/man8/
cp -a -- doc/innernet{,-server}.8 %{buildroot}%_mandir/man8/

# Unit files:
mkdir -p  %buildroot%_unitdir
install -m 0644 %SOURCE11  %buildroot%_unitdir/innernet@.service
install -m 0644 %SOURCE12  %buildroot%_unitdir/innernet.service
install -m 0644 %SOURCE13  %buildroot%_unitdir/innernet-server@.service
install -m 0644 %SOURCE14  %buildroot%_unitdir/innernet-server.service

# Configuration directories:
install -m 0700 -d %buildroot%_sysconfdir/%name
install -m 0700 -d %buildroot%_sysconfdir/%{name}-server
install -m 0700 -d %buildroot/var/lib/%{name}
install -m 0700 -d %buildroot/var/lib/%{name}-server


%pre
# Add the "_innernet" user
%_sbindir/groupadd -r -f %innernet_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %innernet_group -c 'Innernet daemon' \
        -s /dev/null -d /dev/null %innernet_user 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%post server
%post_service %name-server

%preun server
%preun_service %name-server


%files
%doc LICENSE README.md

# 0700 right now is forced in the code
%attr(0700,root,%innernet_group) %dir %_sysconfdir/%name
%attr(0700,root,%innernet_group) %dir /var/lib/%name

%_sbindir/%name
%_mandir/man8/%{name}.*
%_unitdir/innernet@.service
%_unitdir/innernet.service

%files server
%doc LICENSE README.md

# 0700 right now is forced in the code
%attr(0700,root,%innernet_group) %dir %_sysconfdir/%{name}-server
%attr(0700,root,%innernet_group) %dir /var/lib/%{name}-server

%_sbindir/%{name}-server
%_mandir/man8/%{name}-server.*
%_unitdir/innernet-server@.service
%_unitdir/innernet-server.service


%changelog
* Sat Dec 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.5.5-alt1
- New version

* Fri Nov 19 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.5.1-alt1
- New version

* Sun Aug 08 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.4.1-alt1
- New version

* Thu Jul 01 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3.1-alt2
- Update BuildRequires to use clang 11.0

* Thu Jun 24 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus
