%define _unpackaged_files_terminate_build 1
%define pypi_name exceptionite
%define mod_name exceptionite

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.0
Release: alt1
 
Summary: Python exception library for exception handling
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/exceptionite/
Vcs: https://github.com/MasoniteFramework/exceptionite
 
BuildArch: noarch
 
Source: %name-%version.tar
 
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-colorama
BuildRequires: python3-module-requests
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-dotty-dict
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-mock
%endif
 
%description
A Python exception library designed to make handling and
displaying exceptions a cinch. Exceptions can be rendered
into a beautiful HTML exception page.

%prep
%setup

%build
%pyproject_build
 
%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
 
%changelog
* Tue Feb 10 2026 Tatyana Gagina <treza@altlinux.org> 3.0.0-alt1
- Packaged for ALT Sisyphus.
