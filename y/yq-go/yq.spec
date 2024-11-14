# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: yq-go
Version: 4.44.3
Release: alt1
Summary: A portable command-line YAML, JSON, XML, CSV, TOML and properties processor
License: MIT
Group: Development/Tools
Url: https://mikefarah.gitbook.io/yq/
Vcs: https://github.com/mikefarah/yq

Provides: yq = %EVR
Conflicts: yq < %EVR

Source: %name-%version.tar
BuildRequires: golang

%description
A lightweight and portable command-line YAML processor. yq uses jq-like
syntax but works with YAML files as well as JSON. It doesn't yet support
everything jq does - but it does support the most common operations and
functions, and more is being added continuously.

%prep
%setup

%build
go build -v -buildmode=pie yq.go
./yq completion bash > yq.bash
./yq completion zsh  > yq.zsh
./yq completion fish > yq.fish

%install
install -Dp yq %buildroot%_bindir/yq
install -Dpm644 yq.bash -T %buildroot%_datadir/bash-completion/completions/yq
install -Dpm644 yq.zsh  -T %buildroot%_datadir/zsh/vendor-completions/_yq
install -Dpm644 yq.fish -T %buildroot%_datadir/fish/vendor_completions.d/yq.fish

%check
%buildroot%_bindir/yq --version |& grep -Px 'yq .* version v\Q%version\E'
go test ./...

%files
%doc LICENSE README.md how-it-works.md release_notes.txt examples
%_bindir/yq
%_datadir/bash-completion/completions/yq
%_datadir/zsh/vendor-completions/_yq
%_datadir/fish/vendor_completions.d/yq.fish

%changelog
* Thu Nov 14 2024 Vitaly Chikunov <vt@altlinux.org> 4.44.3-alt1
- First import v4.44.3-18-g39a81da1 (2024-10-10).
