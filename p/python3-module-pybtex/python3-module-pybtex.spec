%define pypi_name pybtex

Name: python3-module-%pypi_name
Version: 0.25.0
Release: alt1

Summary: Pybtex reads citation from a file and produces a bibliography
License: MIT
Group: Development/Python3
Url: https://pybtex.org/
Vcs: https://bitbucket.org/pybtex-devs/pybtex.git

Source: %name-%version.tar

BuildRequires(Pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-latexcodec
BuildRequires: python3-module-pyyaml-ft
BuildRequires: python3-module-six

BuildArch: noarch

%description
Pybtex reads citation information from a file and
produces a formatted bibliography. BibTeX style files are supported.
Alternatively it is possible to write styles in Python.
Pybtex currently understands the following bibliography formats:
- BibTeX
- BibTeXML
- YAML-based format
The resulting bibliography may be output in one of the following formats
(not supported by legacy BibTeX styles):
- LaTeX
- HTML
- markdown
- plain text

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README
%_bindir/%pypi_name
%_bindir/%{pypi_name}-convert
%_bindir/%{pypi_name}-format
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Apr 02 2026 Ulysses Apokin <ulysses@altlinux.org> 0.25.0-alt1
- Initial build for Sisyphus.
