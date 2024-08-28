%global import_path gitea.com/gitea/act_runner

Name: forgejo-runner
Version: 3.5.1
Release: alt1

Summary: Forgejo Runner
License: MIT
Group: Other
Url: https://forgejo.org/docs/latest/admin/actions/#forgejo-runner
Vcs: https://code.forgejo.org/forgejo/runner.git

Source: %name-%version.tar
Source2: %name.service
Patch: %name-%version.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

#Requires: docker-engine

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
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCE=1
mkdir -p %buildroot{%_bindir,%_unitdir,%_sysconfdir/%name,%_sharedstatedir/%name}

pushd $BUILDDIR/src/$IMPORT_PATH
%golang_install
popd

mv %buildroot%_bindir/act_runner %buildroot%_bindir/%name
rm -rf %buildroot%go_root

%buildroot%_bindir/%name generate-config > %buildroot%_sysconfdir/%name/config.yaml

install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -s /dev/null -c "%name services" -M -d %_sharedstatedir/%name _%name > /dev/null 2>&1 ||:
#usermod -aG docker _%name

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE RELEASE-NOTES.md
%attr(0770,root,_%name) %dir %_sysconfdir/%name
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name/config.yaml
%attr(0770,root,_%name) %dir %_sharedstatedir/%name
%_bindir/%name
%_unitdir/%name.service

%changelog
* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.1-alt1
- 3.5.1

* Tue Jul 02 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- Initial build.

