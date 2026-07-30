%global _unpackaged_files_terminate_build 1
%def_with check

Name: rumdl
Version: 0.2.46
Release: alt1
Summary: A high-performance Markdown linter
License: MIT
Group: Development/Tools
URL: https://rumdl.dev
VCS: https://github.com/rvben/rumdl

Source: %name-%version.tar
Source1: vendor.tar
Patch: 0001-avoid-changing-cwd-in-init-test.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: git-core
%endif

%description
rumdl is a high-performance Markdown linter and formatter that
helps ensure consistency and best practices in your Markdown files.
Inspired by ruff's approach to Python linting, rumdl brings similar
speed and developer experience improvements to the Markdown ecosystem.

%prep
%setup -a1
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# Timing-based tests are not stable in a build chroot.
%rust_test -- \
    --test-threads=1 \
    --skip perf:: \
    --skip rules::md074_mkdocs_nav::tests::test_cache_prevents_duplicate_validation

%files
%_bindir/%name

%changelog
* Thu Jul 30 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.46-alt1
- Updated to version 0.2.46.

* Mon Jul 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.43-alt1
- Updated to version 0.2.43.

* Fri Jul 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.41-alt1
- Initial build for ALT.
