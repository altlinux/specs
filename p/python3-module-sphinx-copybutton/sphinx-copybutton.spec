%define _unpackaged_files_terminate_build 1

%define oname sphinx-copybutton

Name: python3-module-%oname
Version: 0.4.0
Release: alt1
Summary: A small sphinx extension to add a "copy" button to code blocks
License: MIT
Group: Development/Python3
Url: https://github.com/executablebooks/sphinx-copybutton

BuildArch: noarch

# https://github.com/executablebooks/sphinx-copybutton.git
Source: %name-%version.tar

# git submodules
Source1: %name-%version-clipboard.js.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-sphinx

%description
A small sphinx extension to add a "copy" button to code blocks.

%prep
%setup -a1

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README.md CHANGELOG.md
%python3_sitelibdir/sphinx_copybutton
%python3_sitelibdir/sphinx_copybutton-%version-*.egg-info

%changelog
* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.0-alt1
- Updated to upstream version 0.4.0.

* Wed Aug 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.0-alt1
- Initial build for ALT.
