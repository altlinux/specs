Name: python3-module-unicode-rbnf
Version: 1.1.0
Release: alt1

Summary: Pure-python RBNF
License: MIT
Group: Development/Python
Url: https://pypi.org/project/unicode-rbnf/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A pure Python implementation of ICU's rule-based number format engine

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/unicode_rbnf
%python3_sitelibdir/unicode_rbnf-%version.dist-info

%changelog
* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.1.0-alt1
- 1.1.0 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released

