%define pypname sphinx_reredirects

Name: python3-module-sphinx-reredirects

Version: 0.1.6
Release: alt1

Summary: The extension for Sphinx documentation projects that handles redirects for moved pages
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/sphinx-reredirects
Vcs: https://github.com/documatt/sphinx-reredirects

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

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

%files
%doc LICENSE README.rst *.md
%python3_sitelibdir/%pypname/
%python3_sitelibdir/%{pyproject_distinfo %pypname}

%changelog
* Sun Mar 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.6-alt1
- 0.1.5 -> 0.1.6

* Thu Feb 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.5-alt1
- Initial build for ALT Linux
