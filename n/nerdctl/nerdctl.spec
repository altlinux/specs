%global import_path github.com/containerd/nerdctl
Name:     nerdctl
Version:  1.7.7
Release:  alt1

Summary:  contaiNERD CTL - Docker-compatible CLI for containerd
License:  Apache-2.0
Group:    System/Configuration/Other
Url:      https://github.com/containerd/nerdctl

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

Patch1:   wrap-selinuxenabled-to-wariable-to-skip-requires.patch
Patch2:   add-sbin-to-path-to-work-in-rootless-mode.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: containerd >= 1.6
Requires: cni-plugins iptables

%description
Docker-compatible CLI for containerd, with support for Compose, Rootless,
eStargz, OCIcrypt, IPFS.

To run rootless need package %name-rootless.

%package rootless
Summary: Use nerdctl rootless
Group: System/Configuration/Other
Requires: rootlesskit %name slirp4netns

%description rootless
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="${LDFLAGS:-} -X github.com/containerd/nerdctl/pkg/version.Version=%version"
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -m 0755 extras/rootless/containerd-rootless-setuptool.sh \
    %buildroot%_bindir/containerd-rootless-setuptool.sh
install -m 0755 extras/rootless/containerd-rootless.sh %buildroot%_bindir/containerd-rootless.sh


mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files rootless
%exclude %_bindir/%name
%_bindir/*

%files
%_bindir/%name
%doc *.md
%doc docs
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Sep 11 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.7-alt1
- new version 1.7.7

* Thu May 02 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.6-alt1
- new version 1.7.6

* Mon Mar 18 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.5-alt1
- new version 1.7.5

* Mon Feb 19 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.4-alt1
- new version 1.7.4

* Thu Feb 01 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.3-alt1
- new version 1.7.3

* Wed Dec 13 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.2-alt1
- new version 1.7.2

* Thu Nov 30 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.1-alt1
- new version 1.7.1

* Tue Nov 07 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.0-alt1
- new version 1.7.0

* Thu Nov 02 2023 Ivan A. Melnikov <iv@altlinux.org> 1.6.2-alt1.1
- NMU: add patch for loongarch64 support

* Sat Oct 28 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.2-alt1
- new version 1.6.2

* Tue Sep 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.0-alt1
- new version 1.6.0

* Mon Jul 31 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.5.0-alt1
- new version 1.5.0

* Mon May 22 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.0-alt1
- new version 1.4.0

* Fri Apr 14 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.1-alt1
- new version 1.3.1

* Thu Apr 06 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Tue Mar 14 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.1-alt2
- Add sbin to path to work in rootless mode (Closes: 44495)

* Wed Mar 01 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.1-alt1
- new version 1.2.1

* Fri Feb 17 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Thu Dec 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Tue Nov 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Thu Sep 15 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.23.0-alt1
- new version 0.23.0

* Fri Sep 09 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.22.2-alt1
- new version 0.22.2

* Wed Jul 20 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.22.0-alt1
- new version 0.22.0

* Wed Jun 22 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.21.0-alt1
- new version 0.21.0

* Thu Jun 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.20.0-alt1
- new version 0.20.0

* Thu May 05 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.19.0-alt1
- new version 0.19.0

* Thu Apr 07 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Mon Mar 14 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.1-alt1
- new version 0.17.1

* Tue Mar 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Tue Feb 01 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.1-alt1
- Initial build for Sisyphus
