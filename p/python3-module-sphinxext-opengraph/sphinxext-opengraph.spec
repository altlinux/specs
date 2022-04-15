%define _unpackaged_files_terminate_build 1

%define oname sphinxext-opengraph

Name: python3-module-%oname
Version: 0.6.3
Release: alt1
Summary: Sphinx extension to generate unique OpenGraph metadata
License: MIT
Group: Development/Python3
#https://github.com/wpilibsuite/sphinxext-opengraph
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
* Fri Apr 15 2022 Egor Ignatov <egori@altlinux.org> 0.6.3-alt1
- new version 0.6.3

* Mon Jan 10 2022 Egor Ignatov <egori@altlinux.org> 0.5.1-alt1
- 0.5.1

* Wed Dec 01 2021 Egor Ignatov <egori@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Sep 01 2021 Egor Ignatov <egori@altlinux.org> 0.4.2-alt1
- Initial build for ALT
