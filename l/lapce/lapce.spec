%define _unpackaged_files_terminate_build 1

Name: lapce
Version: 0.2.7
Release: alt1

Summary: Lightning-fast and Powerful Code Editor written in Rust
License: Apache-2.0
Group: Development/Other
Url: https://lapce.dev
Vcs: https://github.com/lapce/lapce

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): /proc
BuildRequires: rust-cargo
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: libgio-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: libcairo-devel
BuildRequires: libcairo-gobject-devel
BuildRequires: libpango-devel
BuildRequires: libatk-devel
BuildRequires: libgtk+3-devel
BuildRequires: libssl-devel
BuildRequires: perl-Pod-Usage

# build only for supported architectures
ExclusiveArch: x86_64 aarch64

%description
Lapce is written in pure Rust with a UI in Druid (which is also written
in Rust). It is designed with Rope Science from the Xi-Editor which
makes for lightning-fast computation, and leverages OpenGL for
rendering. More information about the features of Lapce can be found on
the main website and user documentation can be found on GitBook.

%prep
%setup
mkdir .cargo
cp {.gear,.cargo}/config.toml

%build
%rust_build

%install
%rust_install

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/*

%changelog
* Thu May 11 2023 Anton Zhukharev <ancieg@altlinux.org> 0.2.7-alt1
- Initial build for ALT Sisyphus.

