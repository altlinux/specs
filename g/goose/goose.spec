%global _unpackaged_files_terminate_build 1

Name: goose
Version: 1.15.0
Release: alt1
Summary: An open source, extensible AI agent
License: Apache-2.0
Group: Development/Tools
Url: https://block.github.io/goose
VCS: https://github.com/block/goose

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libsqlite3-devel
BuildRequires: libxcb-devel

%description
goose is your on-machine AI agent, capable of automating complex
development tasks from start to finish. More than just code
suggestions, goose can build entire projects from scratch,
write and execute code, debug failures, orchestrate workflows,
and interact with external APIs - autonomously.

%prep
%setup -a 1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/nmathewson/crunchy?branch=cross-compilation-fix"]
git = "https://github.com/nmathewson/crunchy"
branch = "cross-compilation-fix"
replace-with = "vendored-sources"
EOF

%build
%rust_build -p goose-cli

%install
%rust_install

%files
%_bindir/goose
%doc LICENSE

%changelog
* Thu Nov 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.15.0-alt1
- Initial build for ALT.

