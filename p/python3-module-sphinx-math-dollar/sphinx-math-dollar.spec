%define _unpackaged_files_terminate_build 1

%define oname sphinx-math-dollar
%define realname sphinx_math_dollar

Name: python3-module-%oname
Version: 1.2
Release: alt1
Summary: Sphinx extension to let you write LaTeX math using $$
License: MIT
Group: Development/Python3
Url: https://github.com/sympy/sphinx-math-dollar

BuildArch: noarch

# https://github.com/sympy/sphinx-math-dollar.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math using $$.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math using $$.

This package contains tests for %oname.

%prep
%setup

# fix egg-info
sed -i -e 's/\(^\s\+git_refnames = \).*$/\1"%version"/' %realname/_version.py

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc README* CHANGELOG*
%python3_sitelibdir/%realname
%python3_sitelibdir/%realname-%version-py%{_python3_version}.egg-info
%exclude %python3_sitelibdir/%realname/tests

%files tests
%python3_sitelibdir/%realname/tests

%changelog
* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream version 1.2.

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Initial build for ALT.
