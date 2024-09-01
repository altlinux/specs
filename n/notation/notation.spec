%global import_path github.com/notaryproject/notation
Name:    notation
Version: 1.2.0
Release: alt1

Summary: A CLI tool to sign and verify artifacts
License: Apache-2.0
Group:   Security/Networking
Url:     https://github.com/notaryproject/notation

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Notation is a CLI project to add signatures as standard items in the OCI
registry ecosystem, and to build a set of simple tooling for signing and
verifying these signatures. This should be viewed as similar security to
checking git commit signatures, although the signatures are generic and can be
used for additional purposes.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
export LDFLAGS="${LDFLAGS:-} -X github.com/notaryproject/notation/internal/version.BuildMetadata="
%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh > %buildroot%_datadir/zsh/site-functions/_%name
mkdir -p %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
go test -v -coverprofile=coverage.txt -covermode=atomic ./...

%files
%doc *.md
%_bindir/*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sat Aug 31 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Wed Jun 12 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- new version 1.1.1

* Thu Feb 08 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Wed Nov 22 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
