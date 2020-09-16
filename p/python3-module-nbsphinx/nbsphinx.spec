%define _unpackaged_files_terminate_build 1

%define oname nbsphinx

%def_without docs

Name: python3-module-%oname
Version: 0.7.1
Release: alt1
Summary: Jupyter Notebook Tools for Sphinx
License: MIT
Group: Development/Python3
Url: http://nbsphinx.rtfd.io/

BuildArch: noarch

# https://github.com/spatialaudio/nbsphinx.git
Source: %name-%version.tar

# Fedora patch
Patch0: 0001-Allow-errors-and-add-a-note-in-one-doc-notebook.patch
Patch1: %oname-%version-alt-docversion.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-jupyter_client
BuildRequires: python3-module-nbconvert
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-pathlib2

%if_with docs
BuildRequires: pandoc
%endif

%description
nbsphinx is a Sphinx extension that provides a source parser for *.ipynb
files. Custom Sphinx directives are used to show Jupyter Notebook code cells
(and of course their results) in both HTML and LaTeX output. Unevaluated
notebooks, i.e. notebooks without stored output cells, will be automatically
executed during the Sphinx build process.

%if_with docs
%package doc
Summary: nbsphinx documentation
Group: Development/Documentation
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-doc
Documentation for nbsphinx
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1
echo %version > version.txt

%build
%python3_build

%if_with docs
PYTHONPATH=. py3_sphinx-build doc html
# remove the sphinx-build leftovers
rm -rf html/{.doctrees,.buildinfo,conf.py}
%endif

%install
%python3_install

%files
%doc LICENSE README.rst
%python3_sitelibdir/__pycache__/%{oname}*
%python3_sitelibdir/%oname.py*
%python3_sitelibdir/%oname-%version-py3*.egg-info

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.1-alt1
- Updated to upstream version 0.7.1.

* Thu Apr 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.15-alt2
- Build for python2 disabled.

* Tue Nov 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.15-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Miro Hrončok <mhroncok@redhat.com> - 0.2.13-1
- Initial package
