Name: portainer
Version: 2.28.1
Release: alt1

Summary: A lightweight docker management UI

License: Zlib
Group: System/Configuration/Other
Url: https://www.portainer.io
Vcs: https://github.com/portainer/portainer.git

Source: %url/archive/%version/%name-%version.tar.gz
# go mod vendor
Source1: vendor.tar
#Source2-url: https://github.com/portainer/portainer/releases/download/%version/portainer-%{version}-linux-amd64.tar.gz
Source2: %name-amd64.tar
#Source3-url: https://github.com/portainer/portainer/releases/download/%version/portainer-%{version}-linux-arm64.tar.gz
Source3: %name-arm64.tar
Source4: portainer.desktop
Source5: portainer.png
Source6: portainer.service

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): golang
BuildRequires: rpm-build-golang /proc

Requires: docker-compose-v2

# The specified file is in docker-compose-v2 but it is not detected.
%filter_from_requires \/usr\/lib\/docker\/cli-plugins\/docker-compose/d

%if "%(rpmquery --qf '%%{VERSION}' golang)" >= "1.23.5"
%def_enable genbin
%else
%def_disable genbin
%endif

%define gover %(rpmquery --qf '%%{VERSION}' golang)

%description
%summary.

%prep
%setup -a1
%ifarch x86_64
    tar -xf %SOURCE2
%endif
%ifarch aarch64
    tar -xf %SOURCE3
%endif

%build
%if_enabled genbin
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   --installsuffix cgo \
   --ldflags="-s -X 'github.com/portainer/liblicense.LicenseServerBaseURL=https://api.portainer.io' \
   -X 'github.com/portainer/portainer/pkg/build.BuildNumber=%release' \
   -X 'github.com/portainer/portainer/pkg/build.GitCommit=c4ca049ab8f11b4966dbb077bc1875971a16cadf' \
   -X 'github.com/portainer/portainer/pkg/build.GoVersion=%gover'" \
   -o "bin/portainer" ./api/cmd/portainer
%endif

%install
%if_enabled genbin
install -Dm755 bin/portainer %buildroot%_bindir/portainer
%else
install -Dm755 portainer/portainer %buildroot%_bindir/portainer
%endif

mkdir -p %buildroot%_datadir/portainer
cp -rip portainer/public %buildroot%_datadir/portainer/public

install -Dm644 %SOURCE5 %buildroot%_iconsdir/hicolor/scalable/apps/portainer.png
install -Dm644 %SOURCE4 %buildroot%_desktopdir/portainer.desktop
install -Dm644 %SOURCE6 %buildroot%_unitdir/portainer.service

ln -s %_libexecdir/docker/cli-plugins/docker-compose %buildroot%_datadir/portainer/docker-compose
ln -s %_bindir/docker %buildroot%_datadir/portainer/docker

mkdir -p %buildroot%_localstatedir/portainer/

%pre
getent group portainer >/dev/null || groupadd -r portainer
getent passwd portainer >/dev/null || \
    useradd -r -g portainer -d %_localstatedir/portainer -s /sbin/nologin \
    -c "portainer user" portainer
exit 0

%post
%post_service portainer.service

%preun
%preun_service portainer.service

%files
%doc LICENSE
%_bindir/portainer
%_unitdir/portainer.service
%_desktopdir/portainer.desktop
%_datadir/portainer/
%_iconsdir/hicolor/scalable/apps/portainer.png
%attr(700,portainer,portainer) %dir %_localstatedir/portainer/

%changelog
* Thu Mar 20 2025 Leontiy Volodin <lvol@altlinux.org> 2.28.1-alt1
- New version 2.28.1.
- Prevented install conflict between docker-cli and podman-docker.
- Fixes:
  + CVE-2024-45338.
  + CVE-2025-21613.
  + CVE-2024-50338.
  + CVE-2025-22869.

* Wed Mar 19 2025 Leontiy Volodin <lvol@altlinux.org> 2.27.1-alt1
- Initial build for ALT Sisyphus.


