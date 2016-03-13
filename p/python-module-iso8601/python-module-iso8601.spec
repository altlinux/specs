%global pypi_name iso8601
%def_with python3

Name:		python-module-%{pypi_name}
Version:	0.1.10
Release:	alt1.1
Summary:	Simple module to parse ISO 8601 dates

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/iso8601/
Source0:	%{name}-%{version}.tar

BuildArch:	noarch
BuildRequires:	python-devel python-module-setuptools

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Simple module to parse ISO 8601 dates
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3 python3-module-setuptools

%description -n python3-module-%{pypi_name}
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc LICENSE README.rst
%{python_sitelibdir}/*

%if_with python3
%files -n python3-module-%{pypi_name}
%doc LICENSE README.rst
%{python3_sitelibdir}/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.10-alt1
- 0.1.10
- Enbale python3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.4-alt1
- Initial release for Sisyphus (based on Fedora)
