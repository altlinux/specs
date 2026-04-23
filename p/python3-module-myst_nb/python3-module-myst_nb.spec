%define pypi_name myst_nb
%define oname mystnb

Name: python3-module-%pypi_name
Version: 1.4.0
Release: alt1

Summary: Parse and execute ipynb files in Sphinx
License: BSD-3-Clause
Group: Development/Python3
Url: myst-nb.readthedocs.io
Vcs: https://github.com/executablebooks/MyST-NB.git

BuildArch: noarch

Source: %name-%version.tar
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-ipython
BuildRequires: python3-module-nbclient
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-flit
BuildRequires: python3-module-nbconvert

%description
A collection of tools for working with Jupyter Notebooks in Sphinx.
The primary tool this package provides is a Sphinx parser for ipynb files.
This allows you to directly convert Jupyter Notebooks into Sphinx documents.
It relies heavily on the MyST parser.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/%{oname}-docutils-html
%_bindir/%{oname}-docutils-html5
%_bindir/%{oname}-docutils-latex
%_bindir/%{oname}-docutils-pseudoxml
%_bindir/%{oname}-docutils-xml
%_bindir/%{oname}-quickstart
%_bindir/%{oname}-to-jupyter
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Mar 30 2026 Ulysses Apokin <ulysses@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus.
