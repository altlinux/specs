%define _unpackaged_files_terminate_build 1

Name: forgejo-runner
Version: 12.12.0
Release: alt1

%global import_path code.forgejo.org/forgejo/runner/v%(echo %{version} | cut -d. -f1)

Summary: Forgejo Runner
License: GPL-3.0-or-later
Group: Other
Url: https://forgejo.org/docs/latest/admin/actions/#forgejo-runner
Vcs: https://code.forgejo.org/forgejo/runner.git

Source: %name-%version.tar
Source2: %name.service
Source3: README-alt.md
Source4: cache-config.yml
Source5: %name-cache.service
Source6: README-alt-cache.md

Patch: %name-%version.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.25.0

#Requires: docker-engine
Requires: sysctl-conf-userns podman systemd-container

# https://code.forgejo.org/forgejo/runner/releases/tag/v12.0.0
Requires: git

%description
A runner for Forgejo Actions.

%package cache
Summary: Cache server settings for forgejo runner
Group: Other

Requires: %name = %EVR

%description cache
Cache server settings for forgejo runner.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X %import_path/internal/pkg/ver.version=v%version"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
cp %SOURCE3 ./
cp %SOURCE6 ./
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
mkdir -p %buildroot{%_bindir,%_userunitdir,%_sysconfdir/%name,%_sysconfdir/%name-cache,%_sharedstatedir/%name}

%golang_install

mv %buildroot%_bindir/runner %buildroot%_bindir/%name

%buildroot%_bindir/%name generate-config > %buildroot%_sysconfdir/%name/config.yaml
install -m 0640 %SOURCE4 %buildroot%_sysconfdir/%name-cache/config.yaml

install -m 0644 %SOURCE2 %buildroot%_userunitdir/%name.service
install -m 0644 %SOURCE5 %buildroot%_userunitdir/%name-cache.service

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

%post cache
%systemd_user_post %name-cache.service
if [ ! -f %_sysconfdir/%name-cache/secret ]; then
  openssl rand -hex 32 > %_sysconfdir/%name-cache/secret
  chown root:_%name %_sysconfdir/%name-cache/secret
  chmod 640 %_sysconfdir/%name-cache/secret
fi

%preun
%systemd_user_preun %name.service

%postun
%systemd_user_postun_with_restart %name.service

%preun cache
%systemd_user_preun %name-cache.service

%postun cache
%systemd_user_postun_with_restart %name-cache.service

%files
%doc README.md LICENSE RELEASE-NOTES.md README-alt.md
%attr(0750,root,_%name) %dir %_sysconfdir/%name
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name/config.yaml
%attr(0770,root,_%name) %dir %_sharedstatedir/%name
%_bindir/%name
%_userunitdir/%name.service

%files cache
%doc README-alt-cache.md
%attr(0750,root,_%name) %dir   %_sysconfdir/%name-cache
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name-cache/config.yaml
%_userunitdir/%name-cache.service

%changelog
* Sat Jun 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.12.0-alt1
- New version 12.12.0.

* Fri Jun 12 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.11.1-alt1
- New version 12.11.1.

* Wed May 27 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.10.2-alt1
- New version 12.10.2.

* Tue May 05 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.10.1-alt1
- New version 12.10.1.

* Thu Apr 23 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.9.0-alt1
- New version 12.9.0.

* Wed Apr 08 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.8.2-alt1
- New version 12.8.2.

* Mon Apr 06 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.8.0-alt1
- New version 12.8.0.
- Changed /etc/forgejo-runner permissions from 0770 to 0750.
- Add forgejo-runner-cache subpackage (thx respublica@).

* Mon Mar 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.7.2-alt1
- New version 12.7.2.

* Fri Mar 06 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.7.1-alt1
- New version 12.7.1.

* Thu Feb 19 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.7.0-alt1
- New version 12.7.0.

* Mon Feb 09 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.6.4-alt1
- New version 12.6.4.

* Thu Jan 29 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.6.3-alt1
- New version 12.6.3.

* Mon Jan 26 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.6.2-alt1
- New version 12.6.2.

* Tue Jan 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.5.3-alt1
- New version 12.5.3.

* Sat Jan 17 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.5.2-alt1
- New version 12.5.2.

* Sun Jan 11 2026 Maxim Slipenko <maks1ms@altlinux.org> 12.5.0-alt1
- New version 12.5.0.

* Mon Dec 29 2025 Maxim Slipenko <maks1ms@altlinux.org> 12.3.1-alt1
- New version 12.3.1.

* Wed Dec 10 2025 Maxim Slipenko <maks1ms@altlinux.org> 12.1.2-alt1
- New version 12.1.2.

* Thu Nov 27 2025 Maxim Slipenko <maks1ms@altlinux.org> 12.0.1-alt1
- New version 12.0.1.

* Mon Nov 17 2025 Maxim Slipenko <maks1ms@altlinux.org> 11.3.1-alt1
- New version 11.3.1.

* Wed Nov 05 2025 Maxim Slipenko <maks1ms@altlinux.org> 11.3.0-alt1
- New version 11.3.0.
- Corrected license tag.

* Mon Oct 06 2025 Maxim Slipenko <maks1ms@altlinux.org> 11.1.2-alt1
- New version 11.1.2.

* Tue Sep 16 2025 Maxim Slipenko <maks1ms@altlinux.org> 11.0.0-alt1
- New version 11.0.0.

* Mon Sep 01 2025 Alexey Shabalin <shaba@altlinux.org> 10.0.0-alt1
- New version 10.0.0.

* Tue Aug 12 2025 Alexey Shabalin <shaba@altlinux.org> 9.0.3-alt1
- New version 9.0.3.

* Fri Jul 18 2025 Alexey Shabalin <shaba@altlinux.org> 7.0.0-alt1
- New version 7.0.0.

* Tue May 27 2025 Alexey Shabalin <shaba@altlinux.org> 6.3.1-alt2
- not define User and Group for user unit (ALT#54407).

* Tue Apr 22 2025 Alexey Shabalin <shaba@altlinux.org> 6.3.1-alt1
- New version 6.3.1.

* Fri Jan 31 2025 Alexey Shabalin <shaba@altlinux.org> 6.2.2-alt1
- New version 6.2.2.

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

