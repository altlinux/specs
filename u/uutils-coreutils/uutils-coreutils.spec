%define _unpackaged_files_terminate_build 1

%def_enable selinux
%def_disable multicall

%define prog_prefix uu-

Name: uutils-coreutils
Version: 0.9.0
Release: alt1

Summary: Cross-platform Rust rewrite of the GNU coreutils

License: MIT
Group: System/Base
Url: https://uutils.github.io/coreutils/
Vcs: https://github.com/uutils/coreutils.git

BuildRequires: /sys
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: rust
BuildRequires: rust-cargo

BuildRequires: gcc-c++
BuildRequires: clang-devel

%{?_enable_selinux:BuildRequires: libselinux-devel}

Source: %name-%version.tar
Source1: vendor.tar

Patch0: debian-fix-locale-path.patch

%description
%summary

%prep
%setup -a1

%patch0 -p1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF

%ifarch aarch64
sed -i 's/linker = "aarch64-linux-gnu-gcc"/linker = "aarch64-alt-linux-gcc"/' .cargo/config.toml
%endif

%build
%make_build \
    PROFILE=release \
    %{?_enable_multicall:MULTICALL=y} \
    %{?!_enable_selinux:SKIP_UTILS="runcon chcon"}

%install
%makeinstall_std \
    PROFILE=release \
    %{?_enable_multicall:MULTICALL=y} \
    %{?!_enable_selinux:SKIP_UTILS="runcon chcon"} \
    PROG_PREFIX=%prog_prefix \
    PREFIX=%_prefix \
    DESTDIR=%buildroot \
    LIBSTDBUF_DIR=%_libexecdir/%{prog_prefix}coreutils

%check
# Disabled tests:
# - test_stdbuf::test_stdbuf_no_fork_regression
#   Seems that 'sleep' command doesn't work properly
# - test_nproc
#   Fails to run on girar-builder
# - test_logname
#   Fails to get information about logged in user
# - test_stat::test_percent_escaping
# - test_stdbuf::test_stdbuf_search_order_exe_dir_first
#   Tries to execute file that being modified?
# - test_touch::test_touch_device_files
#   Tries to touch /dev/random
# - test_stat::test_mount_point_basic
#   test_stat::test_mount_point_combined_with_other_specifiers
#   Fails to find mountpoints
# - tests about localization and colors
#   These features work on a normal install (as of last manual check)
# - test_cat::test_write_fast_fallthrough_uses_flush
#   Tries to access /proc/1/cmdline which doesn't exist
# - test_df and test_ls::test_ls_allocation_size
#   stderr = df: no file systems processed
#   Cannot detect filesystems inside hasher
# - test_stat
#   Fails to find mountpoints and panics
# - test_chgrp
#   Fails as hasher users and groups are not the same as
#   in actual system
# - test_who
#   Fails to get system boot time

# Tests are skipped (for now) for these platforms as they fail diferrently
# on each consecutive build
%ifnarch i586 aarch64
%make_build test \
    PROFILE=release \
    %{?!_enable_selinux:SKIP_UTILS="runcon chcon"} \
    TEST_NO_FAIL_FAST="--no-fail-fast -- \
    --skip test_stdbuf::test_stdbuf_no_fork_regression \
    \
    --skip test_nproc::test_nproc_all_omp \
    --skip test_nproc::test_nproc_omp_limit \
    \
    --skip test_logname::test_output_format \
    --skip test_logname::test_normal \
    \
    --skip test_stat::test_percent_escaping \
    --skip test_stdbuf::test_stdbuf_search_order_exe_dir_first \
    \
    --skip test_touch::test_touch_device_files \
    --skip test_stat::test_mount_point_basic \
    --skip test_stat::test_mount_point_combined_with_other_specifiers \
    \
    --skip test_help_messages_french_translation \
    --skip test_french_colored_error_messages \
    --skip test_error_messages_french_translation \
    --skip test_sort::test_clap_localization_invalid_value \
    --skip test_chmod::test_chmod_colored_output \
    --skip test_env::test_env_french \
    --skip test_ls::test_localized_possible_values \
    --skip test_ls::test_ls_long_symlink_color \
    --skip test_sort::test_argument_suggestion \
    --skip test_sort::test_clap_localization_help_message \
    --skip test_sort::test_clap_localization_unknown_argument \
    --skip test_sort::test_error_colors_enabled \
    --skip test_sort::test_error_colors_disabled \
    --skip test_sort::test_french_translations \
    --skip test_sort::test_help_colors_disabled \
    --skip test_sort::test_help_colors_enabled \
    \
    --skip test_cat::test_write_fast_fallthrough_uses_flush \
    --skip test_df::test_file_column_width_if_filename_contains_unicode_chars \
    --skip test_df::test_nonexistent_file \
    --skip test_df::test_output_file_specific_files \
    --skip test_df::test_output_mp_repeat \
    --skip test_df::test_output_option_without_equals_sign \
    --skip test_df::test_total_label_in_correct_column \
    --skip test_df::test_type_option_with_file \
    --skip test_ls::test_ls_allocation_size \
    --skip test_chgrp::test_from_with_invalid_group \
    --skip test_chgrp::test_reference \
    --skip test_stat::test_symlinks \
    --skip test_stat::test_printf \
    --skip test_stat::test_normal_format \
    --skip test_stat::test_multi_files \
    --skip test_who::test_boot"
%endif

%files
%_bindir/%{prog_prefix}*
%_libexecdir/%{prog_prefix}coreutils/*
# This path is currently hardcoded in patch from Debian
%_datadir/uu-coreutils/locales/*
%_datadir/bash-completion/completions/%{prog_prefix}*
%_datadir/zsh/site-functions/_%{prog_prefix}*
%_datadir/fish/vendor_completions.d/%{prog_prefix}*.fish
%_man1dir/%{prog_prefix}*
%doc README.md
%doc SECURITY.md

%changelog
* Tue Jul 28 2026 Ivan Korytov <toreonify@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
