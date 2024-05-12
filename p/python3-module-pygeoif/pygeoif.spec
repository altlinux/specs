%define _unpackaged_files_terminate_build 1
%define oname pygeoif

%def_with check

Name: python3-module-%oname
Version: 1.5.0
Release: alt1

Summary: A basic implementation of the __geo_interface__
License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.org/project/pygeoif
Vcs: https://github.com/cleder/pygeoif.git
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-more-itertools
%endif

%py3_provides %oname


%description
PyGeoIf provides a GeoJSON-like protocol for geo-spatial (GIS) vector
data.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sun May 12 2024 Anton Vyatkin <toni@altlinux.org> 1.5.0-alt1
- New version 1.5.0.

* Tue Mar 26 2024 Anton Vyatkin <toni@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Tue Feb 06 2024 Anton Vyatkin <toni@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Thu Jan 25 2024 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20140924.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20140924
- Initial build for Sisyphus

