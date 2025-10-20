%define pypi_name branca

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.2
Release: alt1

Summary: Generate complex HTML+JS pages with Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/branca
Vcs: https://github.com/python-visualization/branca

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-selenium
BuildRequires: python3-module-numpy
%endif

%description
This library is a spinoff from folium, that would host the non-map-specific features.

%prep
%setup -n %pypi_name-%version

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k "\
not test_rendering_utf8_iframe \
and not test_rendering_figure_notebook \
and not test_color_brewer_extendability"

%files
%doc README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Oct 20 2025 Anton Vyatkin <toni@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Sat May 03 2025 Anton Vyatkin <toni@altlinux.org> 0.8.1-alt1
- Initial build for Sisyphus.
