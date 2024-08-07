%define pypi_name html5tagger

Name:    python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Create HTML documents from Python
License: Unlicense
Group:   Development/Python3
URL:     https://github.com/sanic-org/html5tagger

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-0.0.0.dist-info/

%changelog
* Sat Jul 20 2024 Alexander Burmatov <thatman@altlinux.org> 1.3.0-alt1
- Initial build for Sisyphus.
