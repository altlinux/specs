%define _unpackaged_files_terminate_build 1
%define oname sphinx-gallery

%def_with check

Name: python3-module-%oname
Version: 0.17.0
Release: alt1
Summary: Sphinx extension for automatic generation of an example gallery
License: BSD-3-Clause
Group: Development/Python3
Url: https://sphinx-gallery.github.io
Vcs: https://github.com/sphinx-gallery/sphinx-gallery.git

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: /proc

# install_requires=
BuildRequires: python3(sphinx)

# optional
BuildRequires: python3(matplotlib)
BuildRequires: python3(numpy)
BuildRequires: python3(numpy.testing)
BuildRequires: python3(joblib)
BuildRequires: python3-module-Pillow

BuildRequires: python3(pytest)
BuildRequires: python3(lxml)
%endif

%description
A Sphinx extension that builds an HTML version of any Python script and puts it into an examples gallery.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests need jupyterlite_sphinx which not packaged yet
%pyproject_run_pytest --durations=5 -ra \
 --deselect=sphinx_gallery/tests/test_docs_resolv.py::test_embed_code_links_get_data \
 --deselect=sphinx_gallery/tests/test_full.py \
 --deselect=sphinx_gallery/tests/test_full_noexec.py \
 --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents \
 --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_non_default_contents \
 --deselect=sphinx_gallery/tests/test_gen_gallery.py::test_create_jupyterlite_contents_with_jupyterlite_disabled_via_config

%files
%doc README.rst RELEASES.md CHANGES.rst
%_bindir/sphinx_gallery_py2jupyter
%python3_sitelibdir/sphinx_gallery
%python3_sitelibdir/sphinx_gallery-%version.dist-info
%exclude %python3_sitelibdir/sphinx_gallery/tests

%changelog
* Sun Jul 21 2024 Anton Vyatkin <toni@altlinux.org> 0.17.0-alt1
- New version 0.17.0.

* Mon Apr 29 2024 Anton Vyatkin <toni@altlinux.org> 0.16.0-alt1
- New version 0.16.0.

* Tue Nov 28 2023 Anton Vyatkin <toni@altlinux.org> 0.15.0-alt1
- New version 0.15.0.

* Mon Oct 16 2023 Anton Vyatkin <toni@altlinux.org> 0.14.0-alt1
- New version 0.14.0.

* Tue Mar 01 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9.0 -> 0.10.1.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Updated to upstream version 0.9.0.
- Enabled tests.

* Wed Aug 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
