%global import_path github.com/prabhatsharma/zinc

%global _unpackaged_files_terminate_build 1
%def_without prebuild_webui
%define oname zinc

Name: ZincSearch
Version: 0.3.6
Release: alt1
Summary: Zinc Search engine

License: Apache-2.0
Group: System/Servers
Url: https://github.com/prabhatsharma/zinc
Vcs: https://github.com/prabhatsharma/zinc
Source: %name-%version.tar
Source2: zinc.sysconfig
Source3: zinc.service
Patch: %name-%version-%release.patch

Provides: zincsearch = %EVR
ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
%if_without prebuild_webui
BuildRequires: npm
BuildRequires: node node-devel node-gyp
BuildRequires: esbuild
BuildRequires: /proc
%endif

%description
Zinc is a search engine that does full text indexing.
It is a lightweight alternative to Elasticsearch and runs in less than 100 MB of RAM.
It uses bluge as the underlying indexing library.

It is very simple and easy to operate as opposed to Elasticsearch
which requires a couple dozen knobs to understand and tune.

It is a drop-in replacement for Elasticsearch if you are just ingesting
data using APIs and searching using kibana
(Kibana is not supported with zinc. Zinc provides its own UI).

%prep
#%%if_without prebuild_webui
# Build the Front-end Assets
# $ cd webui
# $ git rm -r node_modules
# $ npm install
# $ rm -rf node_modules/esbuild-linux-*
# $ rm -f node_modules/esbuild/bin/esbuild
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
mkdir -p web/node_modules/esbuild/bin
#ln -sf %_bindir/esbuild web/node_modules/esbuild/bin/esbuild
cp -p %_bindir/esbuild web/node_modules/esbuild/bin/esbuild
ln -srf web/node_modules/esbuild/bin/esbuild web/node_modules/.bin/esbuild
%else
rm -rf web/node_modules
%endif

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export PATH="$PATH:$PWD/web/node_modules/.bin"
export ESBUILD_BINARY_PATH="%_bindir/esbuild"
%golang_prepare

cd .gopath/src/%import_path

export GOFLAGS="-mod=vendor"

%if_without prebuild_webui
pushd web
#npm rebuild
npm run build
popd
%endif

export BUILD_DATE=`date -u '+%%Y-%%m-%%d_%%I:%%M:%%S%%p-GMT'`
export ZINC_LDFLAGS=" -X github.com/zinclabs/zinc/pkg/meta.Version=%version -X github.com/zinclabs/zinc/pkg/meta.BuildDate=$BUILD_DATE -X github.com/zinclabs/zinc/pkg/meta.CommitHash=%release -X github.com/zinclabs/zinc/pkg/meta.Build=%release -X github.com/zinclabs/zinc/pkg/meta.Branch=main"


CGO_ENABLED=0 GOGC=off go build -ldflags "$ZINC_LDFLAGS"  \
    -o %oname cmd/zinc/main.go

%install
install -p -D -m 0755 .gopath/src/%import_path/%oname %buildroot%_bindir/%oname
install -p -D -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%oname
install -p -D -m 0644 %SOURCE3 %buildroot%_unitdir/%oname.service

# Setup directories
#install -d -m 755 %%buildroot%%_logdir/%%oname
install -d -m 755 %buildroot%_sharedstatedir/%oname
# Install logrotate
#install -p -D -m 644 %%SOURCE10 %%buildroot%%_logrotatedir/%%oname

%pre
groupadd -r -f %oname 2>/dev/null ||:
useradd -r -g %oname -c 'Zinc Search engine' \
        -s /sbin/nologin  -d %_sharedstatedir/%oname %oname 2>/dev/null ||:
%post
%post_service %oname

%preun
%preun_service %oname

%files
%doc README.md
%_bindir/%oname
%config(noreplace) %attr(640, root, %oname) %_sysconfdir/sysconfig/%oname
%_unitdir/%oname.service
#%dir %attr(0770, root, %oname) %_logdir/%oname
%dir %attr(0750, %oname, %oname) %_sharedstatedir/%oname

%changelog
* Fri Jan 27 2023 Alexey Shabalin <shaba@altlinux.org> 0.3.6-alt1
- new version 0.3.6

* Thu Dec 01 2022 Alexey Shabalin <shaba@altlinux.org> 0.3.5-alt1
- new version 0.3.5

* Sat Jul 02 2022 Alexey Shabalin <shaba@altlinux.org> 0.2.5-alt2
- update systemd unit

* Wed Jun 29 2022 Alexey Shabalin <shaba@altlinux.org> 0.2.5-alt1
- 0.2.5
- update env for zinc service
- fix perm on /var/lib/zinc

* Sun Jun 12 2022 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- 0.2.4

* Tue Dec 14 2021 Alexey Shabalin <shaba@altlinux.org> 0.1.1-alt1
- Initial build

