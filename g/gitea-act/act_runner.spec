%global import_path gitea.com/gitea/act_runner

Name: gitea-act
Version: 0.2.10
Release: alt3

Summary: Act runner is a runner for Gitea based on Gitea fork of act.
License: MIT
Group: Other
Url: https://%import_path

Source: %name-%version.tar
Source2: %name.service

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.21

#Requires: docker-engine

%description
%summary.

%prep
%setup

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
mkdir -p %buildroot{%_bindir,%_unitdir,%_tmpfilesdir,%_sysconfdir/%name,%_sharedstatedir/%name}

pushd $BUILDDIR/src/$IMPORT_PATH
%golang_install
popd

mv %buildroot%_bindir/act_runner %buildroot%_bindir/%name
rm -rf %buildroot%go_root

%buildroot%_bindir/%name generate-config > %buildroot%_sysconfdir/%name/config.yaml

install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -r -g _%name -s /dev/null -c "gitea-act services" -M -d %_sharedstatedir/%name _%name > /dev/null 2>&1 ||:
#usermod -aG docker _%name

%post
%post_systemd %name.service

%preun
%preun_systemd %name.service

%files
%doc README.md LICENSE altlinux/altREADME.md
%attr(0770,root,_%name) %dir %_sysconfdir/%name
%attr(0640,root,_%name) %config(noreplace) %_sysconfdir/%name/config.yaml
%attr(0770,root,_%name) %dir %_sharedstatedir/%name
%_bindir/%name
%_unitdir/%name.service

%changelog
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
