%define oname oslo.metrics
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 0.6.0
Release: alt1

Summary: OpenStack Oslo Metrics API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.metrics

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-metrics = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 3.1.1
BuildRequires: python3-module-oslo.utils >= 3.41.0
BuildRequires: python3-module-oslo.log >= 3.44.0
BuildRequires: python3-module-oslo.config >= 6.9.0
BuildRequires: python3-module-prometheus_client

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
This Oslo metrics API supports collecting metrics data from other
Oslo libraries and exposing the metrics data to monitoring system.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation
Provides: python3-module-oslo-metrics-doc = %EVR

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%if_with docs
# install man page
install -pDm 644 man/oslometrics.1 %buildroot%_man1dir/oslometrics.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslo-metrics
%python3_sitelibdir/oslo_metrics
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_metrics/tests

%files tests
%python3_sitelibdir/oslo_metrics/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslometrics.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- Automatically updated to 0.6.0.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Automatically updated to 0.5.0.

* Fri May 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
