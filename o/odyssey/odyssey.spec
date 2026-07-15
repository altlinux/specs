Name:		odyssey
Version:	1.5.1
Release:	alt1
Summary:	Advanced multi-threaded PostgreSQL connection pooler and request router
Group:		Databases
License:	BSD-3-Clause
URL:		https://github.com/yandex/odyssey
Source0:	%name-%version.tar

BuildRequires: cmake libldap-devel libpam-devel libssl-devel libsystemd-devel
ExcludeArch: %ix86

%description
Advanced multi-threaded PostgreSQL connection pooler and request router

%prep
%setup -q

%build
#    -DBUILD_COMPRESSION=ON \

%cmake \
    -DBUILD_TYPE=build_release

%cmake_build

%install
%cmakeinstall_std

install -D -m 640 odyssey.conf %buildroot%_sysconfdir/%name/odyssey.conf
install -D -m 644 scripts/systemd/odyssey.service %buildroot%_unitdir/odyssey.service
install -D -m 644 scripts/systemd/odyssey@.service %buildroot%_unitdir/odyssey@.service

# Delete trash
rm %buildroot/usr/share/doc/odyssey/changelog.Debian.gz

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd  -r -g %name -s /sbin/nologin -c "Odyssey Server" -M -d /run/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS LICENSE README.md docs
%_bindir/*
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/%{name}.conf
%_unitdir/*

%changelog
* Wed Jul 15 2026 Alexei Takaseev <taf@altlinux.org> 1.5.1-alt1
- Initial build.
