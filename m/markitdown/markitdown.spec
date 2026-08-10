%define nameD markitdown

Name: %nameD
Version: 0.1.5
Release: alt1

Summary: Python tool for converting files and office documents to Markdown
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/markitdown
Vcs: https://github.com/microsoft/markitdown

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%package -n python3-module-%nameD
Group:   Development/Python3
Requires: %name = %EVR
Summary: Python module for %nameD
%description -n python3-module-%nameD
Python module for %nameD

%prep
%setup

%build
pushd packages/markitdown
%pyproject_build
popd

%install
pushd packages/markitdown
%pyproject_install
popd

%files
%doc *.md
%_bindir/%nameD

%files -n python3-module-%nameD
%python3_sitelibdir/%nameD
%python3_sitelibdir/%{pyproject_distinfo %nameD}

%changelog
* Tue Aug 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.5-alt1
- Initial build for ALT Linux.

