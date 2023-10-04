%def_with check

Name:    cargo-cache
Version: 0.8.3
Release: alt2

Summary: manage cargo cache (${CARGO_HOME}, ~/.cargo/), print sizes of dirs and remove dirs selectively
License: Apache-2.0 or MIT
Group:   Development/Tools
Url:     https://github.com/matthiaskrgr/cargo-cache.git

# Some tests require the source code directory name in form of %name instead
# of %name-%version
Source: %name.tar

BuildRequires(pre): rpm-build-rust

%if_with check
BuildRequires: git-core
%endif

%description
Display information on the cargo cache (~/.cargo/ or $CARGO_HOME).
Optional cache pruning.

%prep
# Some tests require the source code directory name in form of %name instead
# of %name-%version
%setup -n %name

%build
%rust_build

%install
%rust_install

%check
# Skip tests that use network
%rust_test --all -- --skip CARGO_HOME_subdirs_are_known \
    --skip alternative_registry_works \
    --skip test_clean_unref \
    --skip remove_dirs \
    --skip build_and_check_size_test \
    --skip spurious_files_in_cache_test

%files
%doc *.md LICENSE-APACHE LICENSE-MIT COPYRIGHT
%_bindir/%name

%changelog
* Mon Jul 03 2023 Alexander Stepchenko <geochip@altlinux.org> 0.8.3-alt2
- Remove explicit BuildRequires for /proc

* Thu May 04 2023 Alexander Stepchenko <geochip@altlinux.org> 0.8.3-alt1
- Initial build for ALT.
