# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed
%define import_path github.com/mikefarah/yq/v4

Name: yq-go
Version: 4.53.3
Release: alt1

Summary: A portable command-line YAML, JSON, XML, CSV, TOML and properties processor
License: MIT
Group: Development/Tools
Url: https://mikefarah.gitbook.io/yq
VCS: https://github.com/mikefarah/yq

Source: %name-%version.tar
Source1: vendor.tar

Provides: yq = %EVR
Conflicts: yq < %EVR

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A lightweight and portable command-line YAML processor. yq uses jq-like
syntax but works with YAML files as well as JSON. It doesn't yet support
everything jq does - but it does support the most common operations and
functions, and more is being added continuously.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%golang_build .
./.build/bin/yq completion bash > yq.bash
./.build/bin/yq completion fish > yq.fish
./.build/bin/yq completion zsh  > yq.zsh

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
install -Dpm644 yq.bash -T %buildroot%_datadir/bash-completion/completions/yq
install -Dpm644 yq.fish -T %buildroot%_datadir/fish/vendor_completions.d/yq.fish
install -Dpm644 yq.zsh  -T %buildroot%_datadir/zsh/site-functions/_yq

%check
%buildroot%_bindir/yq --version |& grep -Px 'yq .* version v\Q%version\E'
%gotest ./...

%files
%doc LICENSE README.md how-it-works.md release_notes.txt examples
%_bindir/yq
%_datadir/bash-completion/completions/yq
%_datadir/fish/vendor_completions.d/yq.fish
%_datadir/zsh/site-functions/_yq

%changelog
* Fri Jul 17 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 4.53.3-alt1
- Updated to version 4.53.3.

* Fri Nov 28 2025 Vitaly Chikunov <vt@altlinux.org> 4.49.2-alt1
- Update to v4.49.2 (2025-11-25).

* Thu Nov 14 2024 Vitaly Chikunov <vt@altlinux.org> 4.44.3-alt1
- First import v4.44.3-18-g39a81da1 (2024-10-10).
