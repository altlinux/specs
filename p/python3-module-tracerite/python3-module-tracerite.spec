%define pypi_name tracerite

Name:    python3-module-%pypi_name
Version: 1.1.3
Release: alt2

Summary: Tracebacks for Humans (in Jupyter notebooks)
License: Unlicense
Group:   Development/Python3
URL:     https://github.com/sanic-org/tracerite

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install
mv ./%pypi_name/style.css %buildroot%python3_sitelibdir/%pypi_name/

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 16 2025 Alexander Burmatov <thatman@altlinux.org> 1.1.3-alt2
- Fix version.

* Wed Aug 13 2025 Alexander Burmatov <thatman@altlinux.org> 1.1.3-alt1
- New 1.1.3 version.

* Sat Jul 20 2024 Alexander Burmatov <thatman@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
