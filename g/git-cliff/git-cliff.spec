%define _unpackaged_files_terminate_build 1

Name: git-cliff
Version: 2.12.0
Release: alt1
Url: https://git-cliff.org
Vcs: https://github.com/orhun/git-cliff.git
Summary: A highly customizable Changelog Generator that follows Conventional Commit specifications
License: Apache-2.0 or MIT
Group: Development/Tools

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust libssl-devel

%description
%summary.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build --no-default-features -F integrations

mkdir -p completions/
OUT_DIR=completions/ "./target/release/%name-completions"
mkdir -p man/
OUT_DIR=man/ "./target/release/%name-mangen"

%install
%rust_install

install -Dm644 -T ./completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 -T ./completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 -T ./completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -Dm644 -T ./man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.md CHANGELOG.md LICENSE-APACHE LICENSE-MIT
%_bindir/git-cliff
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%_man1dir/*

%changelog
* Wed Feb 11 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.12.0-alt1
- Initial build.
