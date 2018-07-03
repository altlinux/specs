%define modulename prometheus_client
%def_with python3

Name: python-module-prometheus_client
Version: 0.2.0
Release: alt1

Summary: The Python client for Prometheus

Url: https://github.com/kovidgoyal/html5-parser
License: ASL 2.0
Group: Development/Python

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/prometheus/client_python/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.1.4
BuildRequires: python-devel python-module-setuptools

BuildRequires: python-module-decorator python-module-pytest

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-decorator python3-module-pytest
%endif

%description
The Python client for Prometheus.

%package -n python3-module-%modulename
Summary: The Python client for Prometheus
Group: Development/Python3

%description -n python3-module-%modulename
The Python client for Prometheus.

%prep
%setup
%python3_dirsetup

%build
%python_build_debug
%python3_dirbuild_debug

%install
%python_install
%python3_dirinstall

%check
# uses network
#python_test
#python3_dirtest

%files
%doc README.md MAINTAINERS.md
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc README.md MAINTAINERS.md
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-*.egg-info
%endif


%changelog
* Tue Jul 03 2018 Vitaly Lipatov <lav@altlinux.ru> 0.2.0-alt1
- initial build for ALT Sisyphus

