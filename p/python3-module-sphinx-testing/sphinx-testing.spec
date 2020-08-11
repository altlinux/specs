%define _unpackaged_files_terminate_build 1

%define oname sphinx-testing

Name: python3-module-%oname
Version: 1.0.1
Release: alt1
Summary: Testing utility classes and functions for Sphinx extensions
License: BSD-2-Clause
Group: Development/Python3
Url: https://github.com/sphinx-doc/sphinx-testing

BuildArch: noarch

# https://github.com/sphinx-doc/sphinx-testing.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
sphinx-testing provides testing utility classes and functions for Sphinx extensions.

Important
This package has been deprecated. Please use sphinx.testing package instead. It is bundled with Sphinx.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE
%doc AUTHORS CHANGES.rst README.rst Sphinx-AUTHORS
%python3_sitelibdir/sphinx_testing
%python3_sitelibdir/sphinx_testing-%version-py%{_python3_version}.egg-info

%changelog
* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.
