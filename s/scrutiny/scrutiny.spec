%global _unpackaged_files_terminate_build 1
%global import_path github.com/AnalogJ/scrutiny

Name: scrutiny
Version: 0.8.1
Release: alt1
Summary: Hard Drive S.M.A.R.T Monitoring
License: MIT
Group: Monitoring
Url: https://github.com/AnalogJ/scrutiny

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: scrutiny-web.service
Source4: scrutiny-collector.service
Source5: scrutiny-collector.timer
Patch: alt-fix-hardcoded-paths.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: npm

%description
Scrutiny is a Hard Drive Health Dashboard & Monitoring solution,
merging manufacturer provided S.M.A.R.T metrics with real-world failure rates.

%package web
Summary: Scrutiny Web UI and API
Group: Monitoring
Requires: scrutiny-common

%description web
Scrutiny Web UI and API.

%package collector
Summary: Scrutiny data collector
Group: Monitoring
Requires: scrutiny-common
Requires: /usr/sbin/smartctl

%description collector
Scrutiny data collector.

%package common
Summary: Common files and directories for scrutiny package
Group: Monitoring
BuildArch: noarch

%description common
Common files and directories for scrutiny package.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix webapp/frontend install
# git add webapp/frontend/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2
%patch -p1

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor

npm --prefix webapp/frontend run build

%golang_prepare
cd .gopath/src/%import_path
go build -o=scrutiny-web ./webapp/backend/cmd/scrutiny
go build -o=scrutiny-collector ./collector/cmd/collector-metrics

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_logdir/scrutiny \
         %buildroot%_sysconfdir/scrutiny \
         %buildroot%_datadir/scrutiny/web \
         %buildroot%_sharedstatedir/scrutiny
install -m 0755 .gopath/src/%import_path/scrutiny-web %buildroot%_bindir/scrutiny-web
install -m 0755 .gopath/src/%import_path/scrutiny-collector %buildroot%_bindir/scrutiny-collector
install -m 0644 %SOURCE3 %buildroot%_unitdir/scrutiny-web.service
install -m 0644 %SOURCE4 %buildroot%_unitdir/scrutiny-collector.service
install -m 0644 %SOURCE5 %buildroot%_unitdir/scrutiny-collector.timer
install -m 0644 example.scrutiny.yaml %buildroot%_sysconfdir/scrutiny/scrutiny.yaml
install -m 0644 example.collector.yaml %buildroot%_sysconfdir/scrutiny/collector.yaml
cp -r .gopath/src/%import_path/webapp/frontend/dist/treo/* %buildroot%_datadir/scrutiny/web

%post web
%post_service scrutiny-web

%post collector
%post_service scrutiny-collector

%preun web
%preun_service scrutiny-web

%preun collector
%preun_service scrutiny-collector

%files web
%_datadir/scrutiny
%_bindir/scrutiny-web
%_unitdir/scrutiny-web.service
%config(noreplace) %_sysconfdir/scrutiny/scrutiny.yaml

%files collector
%_bindir/scrutiny-collector
%_unitdir/scrutiny-collector.timer
%_unitdir/scrutiny-collector.service
%config(noreplace) %_sysconfdir/scrutiny/collector.yaml

%files common
%_logdir/scrutiny
%_sharedstatedir/scrutiny
%dir %_sysconfdir/scrutiny
%doc LICENSE

%changelog
* Sun Feb 23 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.1-alt1
- Initial build for ALT.
