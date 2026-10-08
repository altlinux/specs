%global _unpackaged_files_terminate_build 1
%def_with check

Name: raffi
Version: 0.23.0
Release: alt1
Summary: Flexible application launcher
License: Apache-2.0
Group: Graphical desktop/Other
URL: https://chmouel.github.io/raffi
VCS: https://github.com/chmouel/raffi

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

# fuzzel - default ui-type
Requires: fuzzel

%description
Raffi is a flexible application launcher designed for
Wayland environments that lets you define commands, scripts,
and workflows in a simple YAML configuration file.
Raffi is an application launcher that sits on top of Fuzzel
or operates using its own built-in native interface.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# tests depends on firefox
sed -i \
    '/fn test_v0_config_migrated_in_memory()/,/fn test_migrate_v0_to_v1_moves_keys()/ {
        s/binary: firefox/binary: sh/
    }' src/lib.rs
%rust_test

%files
%_bindir/%name

%changelog
* Thu Oct 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.23.0-alt1
- Initial build for ALT.
