%define _unpackaged_files_terminate_build 1

%define oname sphinx-gallery

Name: python3-module-%oname
Version: 0.9.0
Release: alt1
Summary: Sphinx extension for automatic generation of an example gallery
License: BSD-3-Clause
Group: Development/Python3
Url: https://sphinx-gallery.github.io

BuildArch: noarch

# https://github.com/sphinx-gallery/sphinx-gallery.git
Source: %name-%version.tar

Patch1: %oname-alt-python3-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: /usr/bin/pytest-3 python3-module-pytest-cov python3(numpy.testing) python3(matplotlib) python3(joblib)

%description
A Sphinx extension that builds an HTML version of any Python script and puts it into an examples gallery.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Sphinx extension that builds an HTML version of any Python script and puts it into an examples gallery.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%check
pytest-3 -vv \
	--deselect=sphinx_gallery/tests/test_docs_resolv.py::test_embed_code_links_get_data \
	--deselect=sphinx_gallery/tests/test_full.py \
	%nil

%files
%doc LICENSE
%doc README.rst RELEASES.md CHANGES.rst
%_bindir/*
%python3_sitelibdir/sphinx_gallery
%python3_sitelibdir/sphinx_gallery-%version-*.egg-info
%exclude %python3_sitelibdir/sphinx_gallery/tests

%files tests
%python3_sitelibdir/sphinx_gallery/tests

%changelog
* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Updated to upstream version 0.9.0.
- Enabled tests.

* Wed Aug 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
