%define _unpackaged_files_terminate_build 1

%define pypi_name pylatexenc

%def_with check

Name: python3-module-%pypi_name
Version: 2.10
Release: alt1

Summary: Simple LaTeX parser providing latex-to-unicode and unicode-to-latex conversion
License: MIT
Group: Development/Python3
URL: https://github.com/phfaist/pylatexenc

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_issues)

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Provides a "unicode_to_latex()" function which converts a unicode
string into LaTeX text and escape sequences, and a module with a
series of routines that parse the LaTeX structure of given LaTeX code
and return a logical structure of objects suitable for converting
into another format such as plain text. The functionality is
also exposed via command-line scripts (latexencode, latex2text,
latexwalker).

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build
%make SPHINXBUILD="sphinx-build-3" -C doc html

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.txt README.rst doc/_build/html
%_bindir/latex2text
%_bindir/latexencode
%_bindir/latexwalker
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 2.10-alt1
- Initial build for Sisyphus
