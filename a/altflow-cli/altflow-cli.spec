%define _unpackaged_files_terminate_build 1

Name: altflow-cli
Version: 0.1.0
Release: alt1
Summary: Command-line client for Altflow
License: GPL-3.0-only
Group: Development/Other
Url: https://altlinux.space/writers/altflow-cli
Vcs: https://altlinux.space/writers/altflow-cli.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-rust

%description
%summary, a centralized OCI image build system, that
helps create bulk OCI image build requests from YAML files, track build
statuses, and view build logs.

%prep
%setup
%rust_prep

%build
%rust_build

%install
%rust_install -- altflow-cli
install -Dm0644 config/cli.toml %{buildroot}%{_sysconfdir}/altflow/cli.toml
install -Dm0644 completions/altflow-cli.bash %{buildroot}%{_datadir}/bash-completion/completions/altflow-cli
install -Dm0644 completions/altflow-cli.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/altflow-cli.fish

%check
%rust_test --lib

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/altflow/cli.toml
%_bindir/altflow-cli
%{_datadir}/bash-completion/completions/altflow-cli
%{_datadir}/fish/vendor_completions.d/altflow-cli.fish

%changelog
* Mon Sep 28 2026 Artyom Sinyugin <writers@altlinux.org> 0.1.0-alt1
- Initial package.
