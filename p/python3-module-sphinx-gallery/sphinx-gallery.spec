%define _unpackaged_files_terminate_build 1
%define oname sphinx-gallery

%def_with check

Name: python3-module-%oname
Version: 0.10.1
Release: alt1
Summary: Sphinx extension for automatic generation of an example gallery
License: BSD-3-Clause
Group: Development/Python3
Url: https://sphinx-gallery.github.io

BuildArch: noarch

# https://github.com/sphinx-gallery/sphinx-gallery.git
Source: %name-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

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
%endif

%description
A Sphinx extension that builds an HTML version of any Python script and puts it into an examples gallery.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

# outdated script requiring dropped easy_install
rm %buildroot%_bindir/copy_sphinxgallery.sh

# drop `.py` suffix to avoid clash as Python module
mv %buildroot%_bindir/sphx_glr_python_to_jupyter{.py,}

%check
py.test3 -vra \
	--deselect=sphinx_gallery/tests/test_docs_resolv.py::test_embed_code_links_get_data \
	--deselect=sphinx_gallery/tests/test_full.py \
	%nil

%files
%doc LICENSE
%doc README.rst RELEASES.md CHANGES.rst
%_bindir/sphx_glr_python_to_jupyter
%python3_sitelibdir/sphinx_gallery
%python3_sitelibdir/sphinx_gallery-%version-*.egg-info
%exclude %python3_sitelibdir/sphinx_gallery/tests

%changelog
* Tue Mar 01 2022 Stanislav Levin <slev@altlinux.org> 0.10.1-alt1
- 0.9.0 -> 0.10.1.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt1
- Updated to upstream version 0.9.0.
- Enabled tests.

* Wed Aug 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.0-alt1
- Initial build for ALT.
