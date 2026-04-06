%define _unpackaged_files_terminate_build 1
%global import_path github.com/mr-karan/doggo

Name: doggo
Version: 1.1.5
Release: alt1
Summary: Command-line DNS Client for Humans.
License: GPL-3.0-only
Group: Monitoring
Url: https://github.com/mr-karan/doggo
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%package %name-web
Summary: Web UI for %name
Group: Networking/DNS

%description %name-web
HTTP server for %name that provides a web browser UI for making DNS queries.

%description
Doggo is a modern command-line DNS client (like dig) written in Golang.
It outputs information in a neat concise manner and supports protocols like DoH,
DoT, DoQ, and DNSCrypt as well.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name/ ./web/

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install
mv -f %buildroot%_bindir/web %buildroot%_bindir/%name-web

# Completions
%buildroot%_bindir/%name completions bash > %name.bash
install -Dm644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
%buildroot%_bindir/%name completions fish > %name.fish
install -Dm644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
%buildroot%_bindir/%name completions zsh > %name.zsh
install -Dm644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name

%files
%doc *.md LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%files %name-web
%doc config-api-sample.toml
%_bindir/%name-web

%changelog
* Mon Apr 06 2026 Pavel Shilov <zerospirit@altlinux.org> 1.1.5-alt1
- Update to new version and close ALT #58527

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.1.4-alt1
- 1.1.3 -> 1.1.4

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 1.1.3-alt1
- 1.1.2 -> 1.1.3

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.1.2-alt1
- 1.0.5 -> 1.1.2

* Wed Jul 30 2025 Pavel Shilov <zerospirit@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus.
