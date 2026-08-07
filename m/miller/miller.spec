%define _unpackaged_files_terminate_build 1

Name: miller
Version: 6.20.2
Release: alt1

Summary: Name-indexed data processing tool
License: BSD-2-Clause
Group: Text tools
Url: https://miller.readthedocs.io
Vcs: https://github.com/johnkerl/miller.git

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Miller (mlr) allows name-indexed data such as CSV, TSV and JSON files to be
processed with functions equivalent to sed, awk, cut, join, sort etc. It can
convert between formats, preserves headers when sorting or reversing, and
streams data where possible so its memory requirements stay small. It works
well with pipes and can feed "tail -f".

%prep
%setup -a1

%build
%gobuild ./cmd/mlr

%install
install -Dpm0755 mlr %buildroot%_bindir/mlr
install -Dpm0644 man/mlr.1 %buildroot%_man1dir/mlr.1

mkdir -p %buildroot%_datadir/bash-completion/completions
./mlr completion bash > %buildroot%_datadir/bash-completion/completions/mlr
mkdir -p %buildroot%_datadir/zsh/site-functions
./mlr completion zsh > %buildroot%_datadir/zsh/site-functions/_mlr

%check
%gotest ./pkg/...
%gotest regression_test.go

%files
%doc LICENSE.txt README.md CLAUDE.md
%_bindir/mlr
%_man1dir/mlr.1*
%_datadir/bash-completion/completions/mlr
%_datadir/zsh/site-functions/_mlr

%changelog
* Thu Aug 06 2026 Denis Rastyogin <gerben@altlinux.org> 6.20.2-alt1
- Initial build for ALT Sisyphus.
