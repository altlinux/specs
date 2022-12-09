
%define oname node_exporter
%global import_path github.com/prometheus/node_exporter

%global _unpackaged_files_terminate_build 1

Name: prometheus-%oname
Version: 1.5.0
Release: alt1
Summary: Prometheus exporter for hardware and OS metrics exposed by *NIX kernels.

Group: Development/Other
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar

Source2: %name.sysconfig
Source3: %name.init
Source4: %name.service

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang
BuildRequires: glibc-devel-static
#BuildRequires: promu
BuildRequires: /proc

Requires(pre): prometheus-common

%description
There is varying support for collectors on each operating system.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
#promu build
export BUILDTAGS="netgo,osusergo,static_build"
export LDFLAGS="-X github.com/prometheus/common/version.Version=%version \
         -X github.com/prometheus/common/version.Revision=%release \
         -X github.com/prometheus/common/version.Branch=tarball \
         -X github.com/prometheus/common/version.BuildDate=$(date -u +%%Y%%m%%d)"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
#export GOPATH="%go_path"
%golang_install
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root
mkdir -p %buildroot{%_bindir,%_initdir,%_unitdir,%_sysconfdir/sysconfig}

#install -m0755 %oname %buildroot%_bindir/%oname
install -m0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0755 %SOURCE3 %buildroot%_initdir/%name
install -m0644 %SOURCE4 %buildroot%_unitdir/%name.service
install -Dpm0644 example-rules.yml %buildroot%_datadir/prometheus/node-exporter/example-rules.yml
mkdir -p %buildroot%_sharedstatedir/prometheus/node-exporter
ln -r -s %buildroot%_bindir/%oname %buildroot%_bindir/%name
# Build man pages.
mkdir -p %buildroot%_man1dir
%buildroot%_bindir/%name --help-man > \
    %buildroot%_man1dir/%name.1
sed -i '/^  /d; /^.SH "NAME"/,+1c.SH "NAME"\nprometheus-node-exporter \\- The Prometheus Node-Exporter' \
    %buildroot%_man1dir/%name.1


%post
%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE README.md docs/* example-rules.yml
%_bindir/*
%_unitdir/%name.service
%_initdir/%name
%_man1dir/*.1*
%_datadir/prometheus/node-exporter/example-rules.yml
%dir %attr(0755,root,prometheus) %_sharedstatedir/prometheus/node-exporter
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Thu Dec 08 2022 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt1
- 1.5.0 (Fixes: CVE-2022-46146)

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Jan 26 2021 Alexey Shabalin <shaba@altlinux.org> 1.0.1-alt1
- 1.0.1.

* Sun May 31 2020 Alexey Shabalin <shaba@altlinux.org> 1.0.0-alt1
- 1.0.0

* Wed Jul 17 2019 Alexey Shabalin <shaba@altlinux.org> 0.18.1-alt1
- 0.18.1

* Fri Jan 18 2019 Alexey Shabalin <shaba@altlinux.org> 0.17.0-alt1
- 0.17.0

* Tue May 08 2018 Alexey Shabalin <shaba@altlinux.ru> 0.16.0-alt0.rc3
- Initial build for ALT.
