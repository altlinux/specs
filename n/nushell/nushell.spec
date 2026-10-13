%define _unpackaged_files_terminate_build 1

%define bin_name nu
%def_with check

Name: nushell
Version: 0.116.1
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
Nushell (or Nu for short) is a new type of shell that supports
structured and typed data.

%package -n nu_plugin_inc
Summary: Nushell nu_plugin_inc plugin
Group: Development/Tools

%description -n nu_plugin_inc
Increment a value or version (e.g., semver). This plugin acts as both
an end-user plugin as well as a simple developer example of how to
create a plugin.

%package -n nu_plugin_polars
Summary: Nushell nu_plugin_polars plugin
Group: Development/Tools

%description -n nu_plugin_polars
Extremely fast columnar operations using DataFrames via the Polars
Library.

%package -n nu_plugin_gstat
Summary: Nushell nu_plugin_gstat plugin
Group: Development/Tools

%description -n nu_plugin_gstat
Returns information on the status of a Git repository as Nushell
structured data.

%package -n nu_plugin_formats
Summary: Nushell nu_plugin_formats plugin
Group: Development/Tools

%description -n nu_plugin_formats
Support for several additional data formats - EML, ICS, INI, plist,
and VCF.

%package -n nu_plugin_query
Summary: Nushell nu_plugin_query plugin
Group: Development/Tools

%description -n nu_plugin_query
Support for querying XML (via XPath), JSON, HTML (via CSS selectors),
and web page metadata.

%prep
%setup -a 1
%rust_prep
cat >> .cargo/config.toml <<EOF

[env]
ZSTD_SYS_USE_PKG_CONFIG = "1"
LIBSSH2_SYS_USE_PKG_CONFIG = "1"
OPENSSL_NO_VENDOR = "1"
DEP_CURL_STATIC = "1"
EOF

%build
%rust_build                 \
    -p nu                   \
    -p nu_plugin_inc        \
    -p nu_plugin_polars     \
    -p nu_plugin_gstat      \
    -p nu_plugin_formats    \
    -p nu_plugin_query 

%install
%rust_install nu nu_plugin_inc nu_plugin_polars nu_plugin_gstat nu_plugin_formats nu_plugin_query


%check
%rust_test \
    -p nu                   \
    -p nu_plugin_inc        \
    -p nu_plugin_polars     \
    -p nu_plugin_gstat      \
    -p nu_plugin_formats    \
    -p nu_plugin_query      \
    --                      \
    --skip integration::cli::ide_check_missing_file_reports_error                   \
    --skip integration::cli::ide_flags_accept_values                                \
    --skip commands::move_::umv::errors_if_destination_doesnt_exist                 \
    --skip commands::move_::umv::errors_if_moving_to_itself                         \
    --skip commands::move_::umv::errors_if_renaming_directory_to_an_existing_file   \
    --skip commands::move_::umv::mv_directory_with_same_name                        \
    --skip commands::ucp::copy_identical_file                                       \
    --skip commands::ucp::test_cp_debug_default                                     \
    --skip commands::utouch                                                         \
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
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md LICENSE
%_bindir/%bin_name

%files -n nu_plugin_inc
%doc LICENSE
%_bindir/nu_plugin_inc

%files -n nu_plugin_polars
%doc LICENSE
%_bindir/nu_plugin_polars

%files -n nu_plugin_gstat
%doc LICENSE
%_bindir/nu_plugin_gstat

%files -n nu_plugin_formats
%doc LICENSE
%_bindir/nu_plugin_formats

%files -n nu_plugin_query
%doc LICENSE
%_bindir/nu_plugin_query

%changelog
* Tue Oct 13 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.116.1-alt1
- Updated to upstream version 0.116.1
- Packaged MIT License
- Added core plugins (Closes: 60508)

* Mon Jul 13 2026 Sergey Zhidkih <rx1513@altlinux.org> 0.114.1-alt1
- Updated to upstream version 0.114.1

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
