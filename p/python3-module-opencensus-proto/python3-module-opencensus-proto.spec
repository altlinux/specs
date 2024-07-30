%define pypi_name opencensus-proto
%define mod_name opencensus

Name:    python3-module-%pypi_name
Version: 0.4.1
Release: alt1

Summary: Language Independent Interface Types For OpenCensus
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/census-instrumentation/opencensus-proto

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version/gen-python

sed -r -i 's/^__version__[[:blank:]]*=/# &/' version.py
cat >> version.py <<EOF
__version__ = '%{version}'  # Correct release version
EOF

%build
%pyproject_build

%install
%pyproject_install

%files
%doc *.rst
%exclude %python3_sitelibdir/%mod_name/*.py
%exclude %python3_sitelibdir/%mod_name/__pycache__/
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jul 27 2024 Alexander Burmatov <thatman@altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus.
