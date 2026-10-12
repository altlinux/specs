%global import_path gitea.com/gitea/runner

Name: gitea-runner
Version: 5.0.0
Release: alt1

Summary: Act runner is a runner for Gitea based on Gitea fork of act.
License: MIT
Group: Other
Url: https://gitea.com/gitea/runner
Vcs: https://gitea.com/gitea/runner.git
Source: %name-%version.tar
Source2: %name.service

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.27.1
Requires: sysctl-conf-userns podman systemd-container
Requires: git
Provides: gitea-act = %EVR
Obsoletes: gitea-act < 5.0.0
#Requires: docker-engine

%description
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X %import_path/internal/pkg/ver.version=v%version"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCE=1
mkdir -p %buildroot{%_bindir,%_userunitdir,%_tmpfilesdir,%_sysconfdir/%name,%_sharedstatedir/%name}

%golang_install
mv %buildroot%_bindir/runner %buildroot%_bindir/%name

%buildroot%_bindir/%name config generate > %buildroot%_sysconfdir/%name/config.yaml

install -m 0644 %SOURCE2 %buildroot%_userunitdir/%name.service

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -s /dev/null -c "%name services" -M -d %_sharedstatedir/%name _%name > /dev/null 2>&1 ||:
#usermod -aG docker _%name

%post
%systemd_user_post %name.service
# First install
if [ $1 -ge 1 ] &&  sd_booted; then
#Configure rootless podman for user _%name
# 1. sysctl kernel.unprivileged_userns_clone=1
# depend on sysctl-conf-userns package
# 2. Allow newgidmap and newgidmap for user
  control newgidmap public
  control newuidmap public
# 3. Add subuid and subgid
  usermod --add-subuids 100000-165536 --add-subgids 100000-165536 _%name
# 4. Allow autostart user units
  loginctl enable-linger _%name
# 5. Enable user units
  user_id=$(id -u _%name)
  SYSTEMCTL=systemctl
  $SYSTEMCTL --user -M "$user_id@" enable podman.socket
fi
exit 0

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%doc README.md LICENSE altlinux/altREADME.md
%attr(0750,root,_%name) %dir %_sysconfdir/%name
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name/config.yaml
%attr(0770,root,_%name) %dir %_sharedstatedir/%name
%_bindir/%name
%_userunitdir/%name.service

%changelog
* Mon Oct 12 2026 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- 5.0.0 (Fixed: CVE-2026-73802, CVE-2026-28708).
- Rename act to runner.
- Move systemd unit to user unit dir for rootless podman containers.

* Tue Feb 24 2026 Alexey Shabalin <shaba@altlinux.org> 0.3.0-alt1
- 0.3.0

* Wed Sep 03 2025 Alexey Shabalin <shaba@altlinux.org> 0.2.13-alt1
- 0.2.13
- Update url for altlinux docker images

* Wed Sep 25 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.11-alt1
- 0.2.11

* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.10-alt4
- Update to upstream snapshot 2024-07-26.

* Tue May 28 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.10-alt3
- Update to upstream snapshot 2024-05-27.

* Tue May 07 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.10-alt2
- Fixed service type

* Mon Apr 15 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.10-alt1
- 0.2.10
- add alt linux images to labels to default config

* Wed Mar 27 2024 Alexey Shabalin <shaba@altlinux.org> 0.2.8-alt1
- 0.2.8

* Tue Sep 26 2023 Alexey Shabalin <shaba@altlinux.org> 0.2.6-alt1
- 0.2.6

* Wed Aug 09 2023 Alexey Shabalin <shaba@altlinux.org> 0.2.5-alt1
- 0.2.5

* Fri Aug 04 2023 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- 0.2.4
- Fixed post and preun macros.

* Thu Jun 08 2023 Stepan Paksashvili <paksa@altlinux.org> 0.1.6-alt2
- Update readme

* Thu May 04 2023 Stepan Paksashvili <paksa@altlinux.org> 0.1.6-alt1
- 0.1.6

* Tue May 02 2023 Stepan Paksashvili <paksa@altlinux.org> 0.1.5-alt1
- Initial build for ALT
