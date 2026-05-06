%global import_path github.com/element-hq/lk-jwt-service
%global _unpackaged_files_terminate_build 1

Name:           livekit
Version: 1.11.0
Release:        alt1
Summary:        LiveKit Realtime Media Server
License:        Apache-2.0
Group:          System/Servers
Url:            https://github.com/livekit/livekit
Vcs:            https://github.com/livekit/livekit.git
Provides:       %name-server = %EVR
Source:         %name-%version.tar
Source1:        %name.service
Source2:        %name.sysusers
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
%golang_build cmd/server

%install
export BUILDDIR="$PWD/.gopath"
export IGNORE_SOURCES=1
%golang_install
mv %buildroot%_bindir/server %buildroot%_bindir/%name-server
install -p -Dm 644 %SOURCE1 %buildroot%_unitdir/%name.service
install -p -Dm 644 config-sample.yaml %buildroot%_sysconfdir/%name/%name.yaml
install -p -Dm 644 %SOURCE2 %buildroot%_sysusersdir/%name.conf
mkdir -p %buildroot%_localstatedir/%name

%pre
%sysusers_create_package %name %SOURCE2

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE
%_bindir/%name-server
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/%name.yaml
%dir %attr(0750,_%name,_%name) %_localstatedir/%name

%changelog
* Wed May 06 2026 Alexey Shabalin <shaba@altlinux.org> 1.11.0-alt1
- updated from 1.9.12 to 1.11.0

* Mon Mar 23 2026 Alexey Shabalin <shaba@altlinux.org> 1.9.12-alt1
- Initial build.
