%define _unpackaged_files_terminate_build 1
%def_with check

%python3_set_limited_api

Name: pdf-inspector
Version: 0.1.7
Release: alt1

Summary: Fast Rust library for PDF inspection, classification, and text extraction
License: MIT
Group: Development/Tools
Url: https://firecrawl.github.io/pdf-inspector/
Vcs: https://github.com/firecrawl/pdf-inspector

Source: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
Source3: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
BuildRequires: rust-cargo

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%package -n python3-module-%name
Version: 0.2.7
Summary: Python module for %name
Group: Development/Python3

%description
Fast Rust library for PDF classification and text extraction. Detects whether a
PDF is text-based or scanned, extracts text with position awareness, and
converts to clean Markdown - all without OCR. Includes bindings for Python,
Node.js, and browser WebAssembly.

%description -n python3-module-%name
%{summary}.

%prep
%setup -a1
%patch -p1
install -vD %SOURCE2 .cargo/config.toml
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build
cargo build --release %{?_smp_mflags} --offline --bins

%install
install -pD -m0755 -t %buildroot%_bindir/ target/release/{pdf2md,detect-pdf,dump_ops}
%pyproject_install

%check
%pyproject_run -- python3 tests/test_python.py

%files
%doc README.md
%_bindir/pdf2md
%_bindir/detect-pdf
%_bindir/dump_ops

%files -n python3-module-%name
%python3_sitelibdir/pdf_inspector
%python3_sitelibdir/%{pyproject_distinfo pdf-inspector}/

%changelog
* Tue Aug 11 2026 Artem Krasovskiy <aibure@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus
