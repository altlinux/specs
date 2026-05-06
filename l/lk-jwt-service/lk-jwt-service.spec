%global import_path github.com/element-hq/lk-jwt-service
%global _unpackaged_files_terminate_build 1

Name:           lk-jwt-service
Version: 0.4.4
Release:        alt1
Summary:        Minimal service to issue LiveKit JWTs for MatrixRTC
License:        AGPL-3.0
Group:          System/Servers
Url:            https://github.com/element-hq/lk-jwt-service
Vcs:            https://github.com/element-hq/lk-jwt-service.git
Source:         %name-%version.tar
Source1:        %name.service
Source2:        %name.env
Source3:        %name.sysusers
Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.3

%description
This service is part of the MatrixRTC stack and is primarily used
when the LiveKit RTC backend (MSC4195) is in use.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
pushd $BUILDDIR/src/%import_path
%gobuild -o %name
popd

%install
export BUILDDIR="$PWD/.gopath"
pushd $BUILDDIR/src/%import_path
install -p -Dm 755 %name %buildroot%_bindir/%name
popd

install -p -Dm 644 %SOURCE1 %buildroot%_unitdir/%name.service
install -p -Dm 644 %SOURCE2 %buildroot%_sysconfdir/%name/%name.env
install -p -Dm 644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
mkdir -p %buildroot%_localstatedir/%name

%pre
%sysusers_create_package %name %SOURCE3

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE
%_bindir/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/%name.env
%dir %attr(0750,_%name,_%name) %_localstatedir/%name

%changelog
* Wed May 06 2026 Alexey Shabalin <shaba@altlinux.org> 0.4.4-alt1
- updated from 0.4.1 to 0.4.4

* Mon Mar 23 2026 Alexey Shabalin <shaba@altlinux.org> 0.4.1-alt1
- Initial build.
