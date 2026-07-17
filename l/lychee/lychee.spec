%define _unpackaged_files_terminate_build 1

%define GIT_DATE %(date +%%Y-%%m-%%d)

Name: lychee
Version: 0.24.2
Release: alt1

Summary: A fast, async, stream-based link checker written in Rust
License: Apache-2.0 or MIT
Group: Development/Tools
Url: https://lychee.cli.rs/
Vcs: https://github.com/lycheeverse/lychee

Source0: %name-%version.tar
Source1: vendor_rust.tar

Patch1: lychee-v0.24.2-fix-build-enviroment.patch
Patch2: lychee-v0.24.2-exclude-octocrab-from-workspace.patch
Patch3: lychee-v0.24.2-turn-off-network-depended-tests.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
lychee is a fast, async link checker written in Rust.
It finds broken hyperlinks and mail addresses in your Markdown and HTML files,
codebases, and websites. It's simple, lightweight, and easy to use.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
export GIT_DATE=%GIT_DATE
%rust_build

%install
%rust_install

%check
export GIT_DATE=%GIT_DATE
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Fri Jul 10 2026 Yaroslav Bahtin <alpacost@altlinux.org> 0.24.2-alt1
- Initial build

