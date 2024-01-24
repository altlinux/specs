%define _unpackaged_files_terminate_build 1

Name: hugo
Version: 0.115.2
Release: alt1

Summary: Configurable static site generator
License: Apache-2.0
Group: Development/Other
Url: https://gohugo.io
Vcs: https://github.com/gohugoio/hugo
Packager: Michael Chernigin <chernigin@altlinux.ru>

Source0: %name-%version.tar
ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Hugo is a static HTML and CSS website generator written in Go. It is optimized
for speed, ease of use, and configurability. Hugo takes a directory with
content and templates and renders them into a full HTML website.

%global build_dir .build
%global import_path github.com/mchernigin/hugo

%prep
%setup
export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

%build
export BUILDDIR="$PWD/%build_dir"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
cd %build_dir/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/%build_dir"
export IGNORE_SOURCES=1
%golang_install

%buildroot/usr/bin/%name gen man
mkdir -p %buildroot%_man1dir/
install -Dm 0644 man/* %buildroot%_man1dir/

%buildroot/usr/bin/%name completion bash > %name.bash
%buildroot/usr/bin/%name completion fish > %name.fish
%buildroot/usr/bin/%name completion zsh  > %name.zsh
install -Dm 0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 0644 %name.zsh  %buildroot%_datadir/zsh/site-functions/_%name

%files
%doc LICENSE
%doc README.md
%_bindir/*
%_man1dir/*.1.xz
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Tue Jul 18 2023 Michael Chernigin <chernigin@altlinux.org> 0.115.2-alt1
- Update to 8966424e from upstream, branch release-0.115.2

* Tue Jun 13 2023 Michael Chernigin <chernigin@altlinux.org> 0.113.0-alt1
- Update to 73779707 from upstream, branch release-0.113.0
- Initial build for ALT Linux
