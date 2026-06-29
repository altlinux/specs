%global import_path github.com/cue-lang/cue
Name:    cue
Version: 0.17.0
Release: alt1

Summary: Validate and define text-based and dynamic configuration
License: Apache-2.0
Group:   Other
Url:     https://github.com/cue-lang/cue

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Configure, Unify, Execute

CUE is an open source data constraint language which aims to simplify tasks
involving defining and using data.

It is a superset of JSON, allowing users familiar with JSON to get started
quickly.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="${LDFLAGS:-} -X cuelang.org/go/cmd/cue/cmd.version=%version"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/cue

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
go test -v -run='!(^TestGenerate$)' ./...

%files
%doc *.md
%_bindir/*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Mon Jun 29 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Wed Apr 22 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.1-alt1
- new version 0.16.1

* Wed Mar 04 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Wed Jan 28 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.4-alt1
- new version 0.15.4

* Tue Dec 30 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.3-alt1
- new version 0.15.3

* Mon Dec 15 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.1-alt1
- new version 0.15.1

* Thu Nov 06 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Thu Oct 23 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.2-alt1
- new version 0.14.2

* Tue Aug 12 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Fri Aug 01 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.14.0-alt1
- new version 0.14.0

* Wed Jun 25 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.2-alt1
- new version 0.13.2

* Wed Jun 11 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.1-alt1
- new version 0.13.1

* Mon May 26 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Mon Apr 14 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.1-alt1
- new version 0.12.1

* Thu Jan 30 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.12.0-alt1
- new version 0.12.0

* Wed Jan 22 2025 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.2-alt1
- new version 0.11.2

* Fri Dec 20 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.1-alt1
- new version 0.11.1

* Wed Nov 20 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.11.0-alt1
- new version 0.11.0

* Thu Oct 24 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.10.1-alt1
- new version 0.10.1

* Mon Aug 19 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.10.0-alt1
- new version 0.10.0

* Thu Jun 27 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.2-alt1
- new version 0.9.2

* Thu Jun 13 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.1-alt1
- new version 0.9.1

* Mon Jun 10 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.0-alt1
- new version 0.9.0

* Fri Apr 26 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.2-alt1
- new version 0.8.2

* Wed Apr 03 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.1-alt1
- new version 0.8.1

* Wed Feb 14 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.7.1-alt1
- new version 0.7.1

* Wed Dec 06 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.7.0-alt1
- new version 0.7.0

* Wed Aug 09 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.6.0-alt1
- new version 0.6.0

* Thu May 18 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
