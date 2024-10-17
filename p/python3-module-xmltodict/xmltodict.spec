%define _unpackaged_files_terminate_build 1
%define oname xmltodict

%def_with check

Name: python3-module-%oname
Version: 0.14.2
Release: alt1

Summary: Makes working with XML feel like you are working with JSON

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/xmltodict
Vcs: https://github.com/martinblech/xmltodict

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%py3_provides %oname

%description
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v tests/

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Thu Oct 17 2024 Anton Vyatkin <toni@altlinux.org> 0.14.2-alt1
- New version 0.14.2.

* Thu Oct 10 2024 Anton Vyatkin <toni@altlinux.org> 0.14.1-alt1
- New version 0.14.1.

* Wed Oct 09 2024 Anton Vyatkin <toni@altlinux.org> 0.14.0-alt1
- New version 0.14.0.
- Move to pyproject macroses.
- Move to gear remotes.

* Mon Apr 10 2023 Anton Vyatkin <toni@altlinux.org> 0.13.0-alt2
- Fix BuildRequires

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)

* Mon Jul 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.12.0-alt1
- build python3 module separately
- new version (0.12.0) with rpmgs script

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.0-alt1
- Updated to upstream version 0.11.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150118
- Version 0.9.1

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20140727
- Initial build for Sisyphus

