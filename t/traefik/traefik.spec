%global import_path github.com/traefik/traefik

%global _unpackaged_files_terminate_build 1
%def_with prebuild_webui

Name: traefik
Version: 2.9.8
Release: alt1
Summary: The Cloud Native Edge Router

License: MIT
Group: System/Servers
Url: https://traefik.io/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang rpm-macros-nodejs
%if_without prebuild_webui
BuildRequires: npm yarn
BuildRequires: node node-devel node-gyp node-sass
%endif

%description
Traefik listens to your service registry/orchestrator API and instantly
generates the routes so your microservices are connected to the outside
world -- without further intervention from your part.

Traefik is a modern HTTP reverse proxy and load balancer that makes
deploying microservices easy. Traefik integrates with your existing
infrastructure components (Docker, Swarm mode, Kubernetes, Marathon,
Consul, Etcd, Rancher, Amazon ECS, ...) and configures itself
automatically and dynamically.

Pointing Traefik at your orchestrator should be the only configuration
step you need.

Documentation: http://docs.traefik.io/

%prep
#%%if_without prebuild_webui
# Build the Front-end Assets
# $ cd webui
# $ git rm -r node_modules
# $ npm install
# $ rm -rf node_modules/node-sass
# $ rm -rf node_modules/node-gyp
# $ git add -f node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"
#%%endif

# Vendorized go modules
# $ go generate
# $ GO111MODULE=on go mod vendor -v
# $ git add -f vendor
# $ git commit -n --no-post-rewrite -m "add go vendor modules"

%setup
%patch -p1

%if_without prebuild_webui
rm -rf webui/static

# add symlink to node headers
node_ver=$(node -v | sed -e "s/v//")
mkdir -p webui/node_modules/.node-gyp/$node_ver/include
ln -s %_includedir/node webui/node_modules/.node-gyp/$node_ver/include/node
echo "9" > webui/node_modules/.node-gyp/$node_ver/installVersion

ln -sf %nodejs_sitelib/node-gyp webui/node_modules/node-gyp
ln -sf %nodejs_sitelib/node-sass webui/node_modules/node-sass
%else
rm -rf webui/node_modules
%endif

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export PATH="$PATH:$PWD/webui/node_modules/.bin"
export npm_config_devdir="$PWD/webui/node_modules/.node-gyp"

%golang_prepare

cd .gopath/src/%import_path

export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux
export CODENAME=livarot
export DATE=$(date -u '+%%Y-%%m-%%d')
export GOFLAGS="-mod=vendor"

%if_without prebuild_webui
pushd webui
yarn build:nc
echo 'For more information see `webui/readme.md`' > static/DONT-EDIT-FILES-IN-THIS-DIRECTORY.md
popd
%endif

mkdir -p dist

go generate
CGO_ENABLED=0 GOGC=off go build -ldflags " -w  \
    -X github.com/traefik/traefik/v2/pkg/version.Version=$VERSION \
    -X github.com/traefik/traefik/v2/pkg/version.Codename=$CODENAME \
    -X github.com/traefik/traefik/v2/pkg/version.BuildDate=$DATE \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.branch=$BRANCH \
    " -a -installsuffix nocgo -o dist/traefik ./cmd/traefik

%install
install -p -D -m 0755 .gopath/src/%import_path/dist/traefik %buildroot%_bindir/%name
install -p -D -m 0644 contrib/systemd/traefik.service %buildroot%_unitdir/%name.service
install -d -m 750 %buildroot%_sysconfdir/%name
install -d -m 750 %buildroot%_sysconfdir/%name/%name.d
touch %buildroot%_sysconfdir/%name/acme.json
install -p -D -m 0644 traefik.sample.toml %buildroot%_sysconfdir/%name/%name.toml
# Setup directories
install -d -m 755 %buildroot%_logdir/%name
install -d -m 755 %buildroot%_sharedstatedir/%name
# Install logrotate
#install -p -D -m 644 %%SOURCE10 %%buildroot%%_logrotatedir/%%name

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -G %name -c 'Traefik reverse proxy and load balancer daemon' \
        -s /sbin/nologin  -d %_sharedstatedir/%name %name 2>/dev/null ||:
%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE.md
%_bindir/%name
%dir %attr(750, root, %name) %_sysconfdir/%name
%dir %attr(750, root, %name) %_sysconfdir/%name/%name.d
%config(noreplace) %attr(640, root, %name) %_sysconfdir/%name/traefik.toml
%config(noreplace) %attr(600, %name, %name) %_sysconfdir/%name/acme.json
%_unitdir/%name.service
%dir %attr(0770, root, %name) %_logdir/%name
%dir %attr(0750, %name, %name) %_sharedstatedir/%name

%changelog
* Thu Feb 16 2023 Alexey Shabalin <shaba@altlinux.org> 2.9.8-alt1
- 2.9.8 (Fixes: CVE-2022-23469, CVE-2022-46153, CVE-2022-41717)

* Mon Oct 24 2022 Alexey Shabalin <shaba@altlinux.org> 2.9.1-alt1
- 2.9.1

* Sun Sep 04 2022 Alexey Shabalin <shaba@altlinux.org> 2.8.4-alt1
- 2.8.4

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 2.7.1-alt1
- 2.7.1

* Thu Jan 27 2022 Alexey Shabalin <shaba@altlinux.org> 2.6.0-alt1
- 2.6.0

* Mon Dec 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.5-alt1
- 2.5.5

* Fri Nov 12 2021 Alexey Shabalin <shaba@altlinux.org> 2.5.4-alt1
- 2.5.4
- Build with prebuilded js static files

* Tue Aug 17 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.14-alt1
- 2.4.14

* Tue Aug 10 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.13-alt1
- 2.4.13

* Thu Jun 24 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.9-alt1
- 2.4.9

* Tue Feb 16 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.3-alt1
- 2.4.3

* Sat Feb 13 2021 Alexey Shabalin <shaba@altlinux.org> 2.4.2-alt1
- 2.4.2

* Tue Nov 10 2020 Alexey Shabalin <shaba@altlinux.org> 2.3.2-alt1
- 2.3.2
- fix perm of acme.json

* Tue Aug 04 2020 Alexey Shabalin <shaba@altlinux.org> 2.2.8-alt1
- 2.2.8

* Sun Mar 15 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.7-alt1
- 2.0.7

* Thu Oct 10 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.2-alt1
- 2.0.2
- update systemd unit for allow write to logfile

* Wed Oct 02 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- 2.0.1

* Mon Sep 30 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.18-alt1
- 1.7.18

* Fri Aug 23 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.14-alt1
- 1.7.14
- build with golang-1.12.9 (Fixes: CVE-2019-9512, CVE-2019-9514)

* Tue May 07 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.11-alt1
- 1.7.11

* Fri Mar 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.10-alt1
- 1.7.10

* Thu Feb 28 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.9-alt2
- build webui
- update sample config
- listen api entryPoint on localhost by default for security reason
- update systemd unit

* Mon Feb 25 2019 Alexey Shabalin <shaba@altlinux.org> 1.7.9-alt1
- Initial build

