%define _unpackaged_files_terminate_build 1

%define oname sphinx-inline-tabs

Name: python3-module-%oname
Version: 2021.08.17.beta10
Release: alt1
Summary: Add inline tabbed content to your Sphinx documentation. 
License: MIT
Group: Development/Python3
Url: https://sphinx-inline-tabs.readthedocs.io

BuildArch: noarch

# https://github.com/pradyunsg/sphinx-inline-tabs
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx

%description
Add inline tabbed content to your Sphinx documentation.

%prep
%setup

%install
mkdir -p %buildroot/%python3_sitelibdir/sphinx_inline_tabs
cp -r src/sphinx_inline_tabs/* %buildroot/%python3_sitelibdir/sphinx_inline_tabs

%files
%doc LICENSE README.md
%python3_sitelibdir/sphinx_inline_tabs

%changelog
* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 2021.08.17.beta10-alt1
- Initial build for ALT
