%define _unpackaged_files_terminate_build 1
%define pypi_name fortls

%def_with check

Name: python3-module-%pypi_name
Version: 3.1.2
Release: alt1

Summary: Fortran Language Server for the Language Server Protocol
License: MIT
Group: Development/Tools
URL: https://github.com/fortran-lang/fortls

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-json5

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %pypi_name-%version.tar

Patch: %name-%version-%release.patch

%description
Fortran Language Server (fortls) is an implementation of the Language
Server Protocol. It can be used with editors that supports the
protocol (e.g. Emacs with elpa-lsp-mode) to offer support for code
completion and documentation.

Supported LSP features include:
* Document symbols (textDocument/documentSymbol)
* Auto-complete (textDocument/completion)
* Signature help (textDocument/signatureHelp)
* GoTo/Peek definition (textDocument/definition)
* Hover (textDocument/hover)
* GoTo implementation (textDocument/implementation)
* Find/Peek references (textDocument/references)
* Project-wide symbol search (workspace/symbol)
* Symbol renaming (textDocument/rename)
* Documentation parsing (Doxygen and FORD styles)
* Diagnostics

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%if_with check
%check
%pyproject_run_pytest
%endif

%files
%doc CHANGELOG.md CITATION.cff LICENSE README.md SECURITY.md
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%dir %python3_sitelibdir/%{pypi_name}*dist-info
%python3_sitelibdir/%{pypi_name}*dist-info/*

%changelog
* Sun Feb 23 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.2-alt1
- Initial build for Sisyphus
