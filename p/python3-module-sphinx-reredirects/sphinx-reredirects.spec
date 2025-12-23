%define pypname sphinx_reredirects
%def_with check

Name: python3-module-sphinx-reredirects

Version: 1.1.0
Release: alt1

Summary: The extension for Sphinx documentation projects that handles redirects for moved pages
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/sphinx-reredirects
Vcs: https://github.com/documatt/sphinx-reredirects

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-flit-core

%if_with check
BuildRequires: python3-module-sphinx python3-module-sphinx-tests
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
The extension for Sphinx documentation projects that handles redirects for moved pages. 
Based on the its configuration, the extension generates HTML pages with meta refresh redirects 
to the new page location. 

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests -k 'not test_linkcheck'

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypname/
%python3_sitelibdir/%{pyproject_distinfo %pypname}

%changelog
* Tue Dec 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.1.0-alt1
- 1.0.0 -> 1.1.0

* Sun Jun 01 2025 Aleksandr Shamaraev <shad@altlinux.org> 1.0.0-alt1
- 0.1.6 -> 1.0.0

* Sun Mar 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6

* Thu Feb 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.5-alt1
- Initial build for ALT Linux
