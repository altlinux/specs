%define _unpackaged_files_terminate_build 1
%define bin_name monolith

Name: monolith
Version: 2.10.1
Release: alt1
Summary: CLI tool and library to save web pages as a single HTML file with embedded assets

License: CC0-1.0
Group: Networking/WWW
Url: https://crates.io/crates/monolith
Vcs: https://github.com/Y2Z/monolith.git
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: perl-IPC-Cmd

%description
Monolith is a CLI tool that saves web pages as a single HTML file. It embeds
CSS, images, and JavaScript into an HTML5 document. Unlike "Save page as" or
wget, it uses data URLs for assets. This ensures offline rendering matches the
online view. Ideal for data hoarders to store and share web content.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md
%_bindir/%bin_name

%changelog
* Thu Aug 14 2025 Aleksandr A. Voyt <sobue@altlinux.org> 2.10.1-alt1
- Initial build.

