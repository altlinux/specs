%define _unpackaged_files_terminate_build 1

%define pypi_name sphinxnotes-mock

Name: python3-module-%pypi_name
Version: 1.1
Release: alt1

Summary: Sphinx extension for mocking directives and roles without modifying documents
License: BSD
Group: Development/Python3
URL: https://github.com/sphinx-notes/mock

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-distutils-extra
BuildRequires: python3(sphinx)

BuildArch: noarch

Source: %pypi_name-%version.tar

Patch: %name-%version-%release.patch

%description
%summary

%prep
%setup -n %pypi_name-%version
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%dir %python3_sitelibdir/sphinxnotes
%python3_sitelibdir/sphinxnotes/mock/
%dir %python3_sitelibdir/*.dist-info
%python3_sitelibdir/*.dist-info/METADATA

%changelog
* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.1-alt1
- New version 1.1.

* Sun Mar 09 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
