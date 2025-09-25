%define _unpackaged_files_terminate_build 1
%global import_path github.com/go-graphite/carbonapi

%define carbon_user carbon
%define carbon_group carbon
%define carbon_loggroup adm

Name:    carbonapi
Version: 0.17.0
Release: alt1

Summary: Implementation of graphite API (graphite-web) in golang
License: BSD-2-Clause
Group:   Other
Url:     https://github.com/go-graphite/carbonapi

Source0: %name-%version.tar
Source1: carbonapi.service
Source2: logrotate
Source3: tmpfiles
Source4: carbonapi.yaml

# Exclude 32-bit x86 architecture due to gocairo dependency
# causing "type [1073741824] too large" errors on 32-bit builds.
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang /proc
BuildRequires: libcairo-devel

%description
CarbonAPI supports a significant subset of graphite functions. 
In our testing it has shown to be 5x-10x faster than 
requesting data from graphite-web.

%prep
%setup

%build
export VERSION=%version
%make_build VERSION=%version

%install
%makeinstall_std

rm -f %buildroot%_datadir/%name/%name.example.yaml

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_runtimedir/%name

install -Dp -m0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -Dp -m0644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
install -Dp -m0644 %SOURCE3 %buildroot%_sysconfdir/tmpfiles.d/%name.conf
install -Dp -m0644 %SOURCE4 %buildroot%_sysconfdir/%name.yaml
touch %buildroot%_logdir/%name/%name.log

%pre
# Add the "carbon" user
getent group %carbon_group >/dev/null || groupadd -r %carbon_group
getent passwd %carbon_user >/dev/null || \
    useradd -r -g %carbon_group -s /sbin/nologin \
    --no-create-home -c "carbon user"  %carbon_user
exit 0

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md LICENSE
%defattr(-,root,root,-)
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.yaml
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf
%attr(0755, root, root) %dir %_logdir/%name
%attr(0755, %carbon_user, %carbon_group) %dir %_runtimedir/%name
%attr(0640, %carbon_user, %carbon_group) %_logdir/%name/%name.log
%_unitdir/%name.service


%changelog
* Tue Sep 23 2025 Nikita Shmatko <nash@altlinux.org> 0.17.0-alt1
- Initial build for Sisyphus.
