%define _unpackaged_files_terminate_build 1

%define oname glob2

%def_with check

Name: python3-module-%oname
Version: 0.7
Release: alt3

Summary: Extended version of Python's builtin glob module
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/glob2/
Vcs: https://github.com/miracle2k/python-glob2.git

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
%endif

%py3_provides %oname


%description
Version of the glob module that can capture patterns and supports
recursive wildcards.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -W ignore::pytest.PytestRemovedIn8Warning test.py

%files
%doc CHANGES *.rst PKG-INFO
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Mon Feb 12 2024 Anton Vyatkin <toni@altlinux.org> 0.7-alt3
- Fixed FTBFS.

* Wed Mar 29 2023 Anton Vyatkin <toni@altlinux.org> 0.7-alt2
- Fix BuildRequires.

* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7-alt1
- Version updated to 0.7
- build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20140122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20140122
- Initial build for Sisyphus

