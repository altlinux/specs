Name:    mandown
Version: 0.1.5
Release: alt1

Summary: Create man pages from markdown markup

License: Apache-2.0
Group:   Documentation
URL:     https://gitlab.com/kornelski/mandown
VCS:     https://gitlab.com/kornelski/mandown

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
install -vpD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

# No tests for now
# %check
# %rust_test

%files
%doc README.md LICENSE
%_bindir/mandown

%changelog
* Mon Nov 11 2024 Ilya Sorochan <k0tran@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus.
