%define pypi_name opencensus-context
%define mod_name opencensus

%def_with check

Name:    python3-module-%pypi_name
Version: 0.1.3
Release: alt1

Summary: The OpenCensus Runtime Context provides in-process context propagation
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/census-instrumentation/opencensus-python

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
The OpenCensus Runtime Context provides in-process context propagation.

%prep
%setup -n %name-%version/context/opencensus-context

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/opencensus/__init__.*
rm -rf %buildroot%python3_sitelibdir/opencensus/__pycache__
rm -rf %buildroot%python3_sitelibdir/opencensus/common/__init__.*
rm -rf %buildroot%python3_sitelibdir/opencensus/common/__pycache__

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Alexander Burmatov <thatman@altlinux.org> 0.1.3-alt1
- Initial build for Sisyphus.
