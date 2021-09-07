%define _unpackaged_files_terminate_build 1

%define oname sphinxext-opengraph

Name: python3-module-%oname
Version: 0.4.2
Release: alt1
Summary: Sphinx extension to generate unique OpenGraph metadata
License: MIT
Group: Development/Python3
#https://github.com/mplanchard/pydecor
Url: https://sphinxext-opengraph.readthedocs.io

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Sphinx extension to generate OpenGraph metadata

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE.md
%python3_sitelibdir/sphinxext/opengraph
%python3_sitelibdir/sphinxext_opengraph-main-*.egg-info

%changelog
* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 0.4.2-alt1
- Initial build for ALT
