%global import_path github.com/kubernetes-incubator/cri-tools

%global _unpackaged_files_terminate_build 1

Name:     cri-tools
Version:  1.26.1
Release:  alt1

Summary:  CLI and validation tools for Kubelet Container Runtime Interface (CRI)
License:  Apache-2.0
Group:    Other
Url:      https://github.com/kubernetes-incubator/cri-tools

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: /usr/bin/go-md2man
# For creating completion
BuildRequires: /proc

%description
CLI and validation tools for Kubelet Container Runtime Interface (CRI).

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

for doc in docs/*.md; do
    go-md2man -in "$doc" -out "${doc%%md}"1
done
pushd .build/src/%import_path
%golang_build cmd/crictl
go test -buildmode=pie -o $BUILDDIR/bin/critest -c "$PWD"/cmd/critest
popd

for shell in bash zsh fish; do
    $BUILDDIR/bin/crictl completion "$shell" > "crictl-$shell-completion"
done

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

install -Dpm 644 docs/*.1 -t %buildroot/%_man1dir
rm docs/*.1
install -Dpm 644 crictl-bash-completion -T %buildroot/%_datadir/bash-completion/completions/crictl
install -Dpm 644 crictl-zsh-completion -T %buildroot/%_datadir/zsh/site-functions/_crictl
install -Dpm 644 crictl-fish-completion -T %buildroot%_datadir/fish/vendor_completions.d/crictl.fish

%files
%_bindir/crictl
%_bindir/critest
%_datadir/bash-completion/completions/crictl
%_datadir/zsh/site-functions/_crictl
%_datadir/fish/vendor_completions.d/crictl.fish
%doc %_man1dir/*
%doc docs

%changelog
* Mon Mar 27 2023 Alexander Stepchenko <geochip@altlinux.org> 1.26.1-alt1
- 1.26.1

* Sat Jun 04 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.24.2-alt1
- new version 1.24.2

* Thu Dec 02 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.0-alt1
- new version 1.22.0
- add zsh and fish completions

* Wed Jun 30 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.21.0-alt1
- new version 1.21.0

* Fri Jan 22 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.20.0-alt1
- new version 1.20.0

* Thu Sep 17 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1.19.0-alt1
- new version 1.19.0

* Thu Aug 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.11.1-alt1
- Initial build for Sisyphus
