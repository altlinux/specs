%global _unpackaged_files_terminate_build 1
%def_with check

Name: hyprscratch
Version: 0.6.5
Release: alt1
Summary: Improved scratchpad functionality for Hyprland
License: MIT
Group: Graphical desktop/Other
URL: https://crates.io/crates/hyprscratch
VCS: https://github.com/sashetophizika/hyprscratch

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Hyprscratch makes scratchpads in Hyprland painless
in a well-integrated and flexible way.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# tests require a live Hyprland session
%rust_test -- \
    --skip daemon::tests::test_auto_reload \
    --skip daemon::tests::test_clean \
    --skip daemon::tests::test_handlers \
    --skip daemon::tests::test_spotless \
    --skip daemon::tests::test_vanish \
    --skip scratchpad::tests::test_attach \
    --skip scratchpad::tests::test_named_workspace \
    --skip scratchpad::tests::test_persist \
    --skip scratchpad::tests::test_pin \
    --skip scratchpad::tests::test_poly \
    --skip scratchpad::tests::test_show_hide \
    --skip scratchpad::tests::test_summon_normal \
    --skip scratchpad::tests::test_summon_special \
    --skip utils::tests::test_autospawn \
    --skip utils::tests::test_move_floating

%files
%_bindir/%name

%changelog
* Fri Jun 26 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.5-alt1
- Initial build for ALT.
