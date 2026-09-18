%define _unpackaged_files_terminate_build 1

Name: mprocs
Version: 0.9.6
Release: alt1

Summary: TUI for running multiple processes
License: MIT
Group: Development/Tools
Url: https://github.com/pvolok/mprocs
Vcs: https://github.com/pvolok/mprocs

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires: rpm-macros-rust
BuildRequires: rust-cargo

%description
mprocs is a terminal user interface for running multiple processes in parallel
and viewing their output in separate panes.

%prep
%setup -q -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# These tests require child-process I/O that is unavailable in the hasher.
cargo test --release %{?_smp_mflags} --no-fail-fast -- \
    --skip task::proc_task::tests::log_path_is_resolved_with_real_pid \
    --skip task::proc_task::tests::proc_output_is_logged_via_direct_observer \
    --skip task::proc_task::tests::stop_signal_cmd_runs_shell_command

%files
%doc README.md LICENSE
%_bindir/mprocs

%changelog
* Fri Sep 18 2026 Vladislav Glinkin <smasher@altlinux.org> 0.9.6-alt1
- Initial build for ALT.
