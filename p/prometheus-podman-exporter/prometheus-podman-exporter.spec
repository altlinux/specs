%global goipath github.com/containers/prometheus-podman-exporter
%{!?_userunitdir: %global _userunitdir /usr/lib/systemd/user}

Name: prometheus-podman-exporter
Version: 1.14.0
Release: alt1.2

Summary: Prometheus exporter for podman environment

License: Apache-2.0 and MPL-2.0 and BSD-3-Clause and BSD-2-Clause and MIT and CC-BY-SA-4.0 and ISC
Group: System/Configuration/Other
Url: https://github.com/containers/prometheus-podman-exporter
Vcs: git://github.com/containers/prometheus-podman-exporter.git

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre):  rpm-build-golang /proc
BuildRequires: git-core libdevmapper-devel glib2-devel libgpgme-devel libassuan-devel libbtrfs-devel libsystemd-devel
BuildRequires: libselinux-utils
Requires: conmon crun
%ifnarch i586
Requires: netavark
%endif

%description
Prometheus exporter for podman environments exposing containers, pods, images,
volumes and networks information.

%prep
%setup
sed -i 's| selinuxenabled| %_sbindir/selinuxenabled|' \
  Makefile
sed -i 's|$(DESTDIR)/$(TARGET)|$(DESTDIR)%_bindir/$(TARGET)|' \
  Makefile

%build
%make_build

%install
%makeinstall_std
install -Dm644 contrib/systemd/system/%name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -Dm644 contrib/systemd/system/%name.service -t %buildroot%_unitdir/
install -Dm644 contrib/systemd/user/%name.service -t %buildroot%_userunitdir/

%files
%doc LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md MAINTAINERS.md README.md SECURITY.md
%_bindir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_userunitdir/%name.service

%changelog
* Fri Dec 20 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1.2
- Fixed userunitdir path.

* Thu Dec 19 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1.1
- Fixed backporting to older branches.

* Wed Dec 18 2024 Leontiy Volodin <lvol@altlinux.org> 1.14.0-alt1
- Initial build for ALT Sisyphus.
