%global _unpackaged_files_terminate_build 1
%def_with check

Name: rumdl
Version: 0.2.73
Release: alt1
Summary: A high-performance Markdown linter
License: MIT
Group: Development/Tools
URL: https://rumdl.dev
VCS: https://github.com/rvben/rumdl

Source: %name-%version.tar
Source1: vendor.tar

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
%rust_prep

%build
%rust_build

%install
%rust_install

%check
# Timing-based tests are not stable in a build chroot.
# MDX recovery tests rely on debug_assert in markdown-rs and fail
# in release profile: https://github.com/rvben/rumdl/issues/872
%rust_test -- \
    --test-threads=1 \
    --skip perf:: \
    --skip rules::md074_mkdocs_nav::tests::test_cache_prevents_duplicate_validation \
    --skip lint_context::mdx::tests::a_recovered_parse_leaves_panic_reporting_on \
    --skip lint_context::mdx::tests::unclosed_jsx_in_link_label_uses_recovery_context

%files
%_bindir/%name

%changelog
* Sun Sep 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.73-alt1
- Updated to version 0.2.73.

* Sat Aug 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.62-alt1
- Updated to version 0.2.62.

* Thu Aug 13 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.55-alt1
- Updated to version 0.2.55.

* Sat Aug 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.52-alt1
- Updated to version 0.2.52.

* Mon Aug 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.49-alt1
- Updated to version 0.2.49.

* Sat Aug 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.48-alt1
- Updated to version 0.2.48.

* Sat Aug 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.47-alt1
- Updated to version 0.2.47.

* Thu Jul 30 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.46-alt1
- Updated to version 0.2.46.

* Mon Jul 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.43-alt1
- Updated to version 0.2.43.

* Fri Jul 24 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.41-alt1
- Initial build for ALT.
