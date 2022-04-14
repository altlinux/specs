%define _unpackaged_files_terminate_build 1

%define oname sphinx-inline-tabs

Name: python3-module-%oname
Version: 2022.01.02.beta11
Release: alt1
Summary: Add inline tabbed content to your Sphinx documentation. 
License: MIT
Group: Development/Python3
Url: https://sphinx-inline-tabs.readthedocs.io

BuildArch: noarch

# https://github.com/pradyunsg/sphinx-inline-tabs
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flit
BuildRequires: python3-module-sphinx

%description
Add inline tabbed content to your Sphinx documentation.

%prep
%setup

%build
flit build

%install
pip%{_python3_version} install -I dist/sphinx_inline_tabs-*-none-any.whl --root %buildroot --prefix %prefix --no-deps

%files
%doc LICENSE README.md
%python3_sitelibdir/sphinx_inline_tabs
%python3_sitelibdir/sphinx_inline_tabs-*dist-info

%changelog
* Thu Apr 14 2022 Egor Ignatov <egori@altlinux.org> 2022.01.02.beta11-alt1
- new version 2022.01.02.beta11

* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 2021.08.17.beta10-alt1
- Initial build for ALT
