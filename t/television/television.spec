%global _unpackaged_files_terminate_build 1
%global bin_name tv

%def_with check

Name: television
Version: 0.15.3
Release: alt1
Summary: A fast, portable and hackable fuzzy finder for the terminal
License: MIT
Group: File tools
Url: https://alexpasmantier.github.io/television
VCS: https://github.com/alexpasmantier/television

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: /dev/pts
%endif

%description
Television is a fuzzy finder that lets you search through any kind
of data in real-time. It comes with built-in channels for common
tasks like finding files, searching git repositories, browsing
environment variables, and more. You can also create your own
custom channels to search through any data source you need.

%prep
%setup -a 1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/alexpasmantier/nucleo.git?branch=television"]
git = "https://github.com/alexpasmantier/nucleo.git"
branch = "television"
replace-with = "vendored-sources"
EOF

%build
%rust_build

%install
%rust_install %bin_name
install -Dm 0644 man/%bin_name.1 %buildroot%_man1dir/%bin_name.1

%check
export TV_BIN_PATH=./target/release/tv
%rust_test --lib --bin tv --test app --test channels

%files
%_bindir/%bin_name
%_man1dir/%bin_name.1.*
%doc LICENSE

%changelog
* Sat Mar 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.15.3-alt1
- Initial build for ALT.
