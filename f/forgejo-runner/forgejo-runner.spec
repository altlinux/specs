%global import_path gitea.com/gitea/act_runner

Name: forgejo-runner
Version: 6.0.1
Release: alt1

Summary: Forgejo Runner
License: MIT
Group: Other
Url: https://forgejo.org/docs/latest/admin/actions/#forgejo-runner
Vcs: https://code.forgejo.org/forgejo/runner.git

Source: %name-%version.tar
Source2: %name.service
Source3: README-alt.md
Patch: %name-%version.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.23.3

#Requires: docker-engine
Requires: sysctl-conf-userns podman systemd-container

%description
A runner for Forgejo Actions.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X gitea.com/gitea/act_runner/internal/pkg/ver.version=%version"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
cp %SOURCE3 ./
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot{%_bindir,%_userunitdir,%_sysconfdir/%name,%_sharedstatedir/%name}

%golang_install

mv %buildroot%_bindir/act_runner %buildroot%_bindir/%name

%buildroot%_bindir/%name generate-config > %buildroot%_sysconfdir/%name/config.yaml

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
  $SYSTEMCTL --user -M "$user_id@" enable %name.service
fi
exit 0

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%files
%doc README.md LICENSE RELEASE-NOTES.md README-alt.md
%attr(0770,root,_%name) %dir %_sysconfdir/%name
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name/config.yaml
%attr(0770,root,_%name) %dir %_sharedstatedir/%name
%_bindir/%name
%_userunitdir/%name.service

%changelog
* Mon Jan 13 2025 Alexey Shabalin <shaba@altlinux.org> 6.0.1-alt1
- 6.0.1

* Fri Dec 06 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.3-alt2
- move systemd unit from system to user
- adapt systemd unit for run as user service and rootless podman
- configure rootless podman for first install

* Tue Dec 03 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.3-alt1
- 5.0.3

* Mon Nov 18 2024 Alexey Shabalin <shaba@altlinux.org> 5.0.0-alt1
- 5.0.0

* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.1-alt1
- 3.5.1

* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- Initial build.

