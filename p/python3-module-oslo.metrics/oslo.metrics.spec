%define oname oslo.metrics

%def_without check
%def_without docs

Name: python3-module-%oname
Version: 0.4.0
Release: alt1

Summary: Collect metrics data from other Oslo libraries

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/oslo.service

Source: %oname-%version.tar.gz
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.utils >= 3.41.0
BuildRequires: python3-module-oslo.config >= 6.9.0
BuildRequires: python3-module-oslo.log >= 3.44.0

#TODO: fix docs and check
%if_with check
BuildRequires: python3-module-sphinx
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
Summary: Oslo metrics documentation
Group: Development/Documentation

%description doc
Documentation for oslo.metrics
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%files
%doc *.rst LICENSE
%_bindir/oslo-metrics
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc LICENSE html
%endif

%changelog
* Fri May 27 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus.
