%def_with check

Name:    serie
Version: 0.8.0
Release: alt1

Summary: A rich git commit graph in your terminal, like magic
License: MIT
Group:   Development/Other
URL:     https://lusingander.github.io/serie/
VCS:     https://github.com/lusingander/serie.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
%if_with check
BuildRequires: git
%endif

%description
Serie is a TUI application that uses the terminal emulators' image
display protocol to render commit graphs like git log --graph --all

%prep
# For vendoring use cargo-vendor-alt from cargo-vendor-filterer
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md
%_bindir/serie

%changelog
* Fri May 15 2026 Ilya Sorochan <k0tran@altlinux.org> 0.8.0-alt1
- Update version.

* Tue Mar 03 2026 Ilya Sorochan <k0tran@altlinux.org> 0.6.1-alt1
- Update version.

* Mon Feb 02 2026 Ilya Sorochan <k0tran@altlinux.org> 0.6.0-alt1
- Update version.

* Tue Jan 13 2026 Ilya Sorochan <k0tran@altlinux.org> 0.5.7-alt1
- Initial build for Sisyphus.
