%define _unpackaged_files_terminate_build 1

%define bin_name nu
%def_with check

Name: nushell
Version: 0.113.1
Release: alt1

Summary: A new type of shell
License: MIT
Group: Terminals
Url: http://www.nushell.sh/
Vcs: https://github.com/nushell/nushell.git
Source: %name-%version.tar
Source1: vendor.tar
# Not supported by upstream
ExcludeArch: %ix86

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: openssl-devel
BuildRequires: zlib-ng-devel
BuildRequires: libcurl-devel
BuildRequires: libssh2-devel
BuildRequires: libzstd-devel

%description
Nushell (or Nu for short) is a new type of shell that supports structured and typed data.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[env]
ZSTD_SYS_USE_PKG_CONFIG = "1"
LIBSSH2_SYS_USE_PKG_CONFIG = "1"
OPENSSL_NO_VENDOR = "1"
DEP_CURL_STATIC = "1"
EOF

%build
%rust_build

%install
%rust_install %bin_name

#according to the upstream documentation
%check
cargo test --workspace --                                                           \
    --skip commands::move_::umv::errors_if_destination_doesnt_exist                 \
    --skip commands::move_::umv::errors_if_moving_to_itself                         \
    --skip commands::move_::umv::errors_if_renaming_directory_to_an_existing_file   \
    --skip commands::move_::umv::mv_directory_with_same_name                        \
    --skip commands::ucp::copy_identical_file                                       \
    --skip commands::ucp::test_cp_debug_default                                     \
    --skip plugins::stream::echo_interactivity_on_slow_pipelines                    \
    --skip commands::run_external                                                   \
    --skip plugins::stress_internals::test_exit_before_hello_stdio                  \
# Skipped tests depend on uutils-coreutils specific behaviour and not applicable for gnu-coreutils.
# Stress tests skipped due to problems with girar builder. On local machine everything is fine.
# External commands disabled due to instability on builder.

%post
# Add nu to the list of allowed shells in /etc/shells
if ! grep %_bindir/nu %_sysconfdir/shells >/dev/null; then
    echo %_bindir/nu >>%_sysconfdir/shells
fi

%postun
# Remove nu from the list of allowed shells in /etc/shells
if [ $1 -eq 0 ]; then
    grep -v %_bindir/nu %_sysconfdir/shells >%_sysconfdir/nu.tmp
    mv %_sysconfdir/nu.tmp %_sysconfdir/shells
fi

%files
%_bindir/%bin_name
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

%changelog
* Tue Jun 16 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.113.1-alt1
- Updated to upstream version 0.113.1

* Tue Apr 21 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.112.2-alt1
- Updated to upstream version 0.112.2

* Sun Feb 08 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.110.0-alt1
- Updated to upstream version 0.110.0

* Thu Oct 17 2024 Elena Dyatlenko <lenka@altlinux.org> 0.99.0-alt1
- Updated to upstream version 0.96.1
- Add vendor-filter

* Tue Aug 06 2024 Elena Dyatlenko <lenka@altlinux.org> 0.96.1-alt2
- Add nu to the list of allowed shells in /etc/shells (ALT #51040)
- Fix url

* Wed Jul 31 2024 Elena Dyatlenko <lenka@altlinux.org> 0.96.1-alt1
- Updated to upstream version 0.96.1

* Mon Jul 08 2024 Elena Dyatlenko <lenka@altlinux.org> 0.95.0-alt1
- Initial build for Sisyphus
