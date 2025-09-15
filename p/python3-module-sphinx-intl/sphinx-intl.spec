%define pypi_name sphinx-intl
%define mod_name sphinx_intl

%def_with check
%def_with docs

Name: python3-module-%pypi_name
Version: 2.3.2
Release: alt1

Summary: A Sphinx utility that make it easy to translate and to apply translations

License: BSD-2-Clause
Group: Development/Python3
URL: https://pypi.org/project/sphinx-intl
VCS: https://github.com/sphinx-doc/sphinx-intl
# Documentation: https://sphinx-intl.readthedocs.io

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-click
BuildRequires: python3-module-sphinx
%endif

%if_with docs
BuildRequires: python3-module-sphinx-click
BuildRequires: python3-module-sphinx_rtd_theme
%endif

%description
sphinx-intl is a utility tool that provides several features
that make it easy to translate and to apply translation to
Sphinx generated document. Optional: support the Transifex
service for translation with Sphinx.

%package docs
Summary: Documentation for %pypi_name
Group: Development/Documentation

%description docs
sphinx-intl is a utility tool that provides several features
that make it easy to translate and to apply translation to
Sphinx generated document. Optional: support the Transifex
service for translation with Sphinx.

This package contains documentation for %pypi_name.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc man
%make -C doc html
# remove the sphinx-build leftovers
rm -rv doc/_build/html/{.buildinfo,objects.inv}
%endif

%if_with docs
mkdir -p %buildroot%_man1dir
install -m0644 doc/_build/man/%pypi_name.1 %buildroot%_man1dir
%endif

%check
%pyproject_run_pytest -k "not test_update_txconfig_resources"

%files
%doc *.rst LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %mod_name}
%if_with docs
%_man1dir/*

%files docs
%doc doc/_build/html
%endif

%changelog
* Sat Sep 13 2025 Alexander Kovalev <alexvk@altlinux.org> 2.3.2-alt1
- Initial build for ALT.
