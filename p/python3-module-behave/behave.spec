%define _unpackaged_files_terminate_build 1
%define oname behave

%def_with check

Name: python3-module-%oname
Version: 1.2.6
Release: alt7
Summary: behave is behaviour-driven development, Python style
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/behave/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/behave/behave.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
Patch1: drop-distutils.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(hamcrest)
BuildRequires: python3(mock)
BuildRequires: python3(parse)
BuildRequires: python3(parse_type)
BuildRequires: python3(path)
%endif

Requires: %oname-common = %EVR
%add_python3_req_skip gherkin
%add_python3_req_skip gherkin.formatter
%add_python3_req_skip gherkin.tag_expression
# this provide does not exist
%add_python3_req_skip behave.contrib.steps

%description
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%package -n %oname-common
Summary: Common files for Python modules
Group: Development/Python3

%description -n %oname-common
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains common files for Python 2 & 3 modules.

%prep
%setup
%patch -p1
%patch1 -p2

%build
%pyproject_build

%install
%pyproject_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

install -d %buildroot%_sysconfdir
cp -fR etc/* %buildroot%_sysconfdir/

%check
%pyproject_run_pytest -v tests/

%files
%doc *.rst *features
%_bindir/behave.py3
%python3_sitelibdir/behave/
%python3_sitelibdir/setuptools_behave.py
%python3_sitelibdir/__pycache__/setuptools_behave.cpython-*.py*
%python3_sitelibdir/behave-%version.dist-info/

%files -n %oname-common
%dir %_sysconfdir/json
%_sysconfdir/json/behave.json-schema
%dir %_sysconfdir/junit.xml
%_sysconfdir/junit.xml/behave_junit.xsd
%_sysconfdir/junit.xml/junit-4.xsd

%changelog
* Tue Oct 24 2023 Anton Vyatkin <toni@altlinux.org> 1.2.6-alt7
- NMU: Dropped dependency on distuils.

* Tue Aug 15 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 1.2.6-alt6.1
- NMU: ignored unmet dependency

* Mon Apr 17 2023 Anton Vyatkin <toni@altlinux.org> 1.2.6-alt6
- Fix BuildRequires

* Wed Sep 15 2021 Stanislav Levin <slev@altlinux.org> 1.2.6-alt5
- Fixed FTBFS (setuptools 58).

* Mon Oct 05 2020 Stanislav Levin <slev@altlinux.org> 1.2.6-alt4
- Stopped Python2 package build.
- Applied upstream patches.

* Tue Aug 06 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt3
- Fixed testing against Pytest 5.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt2
- Added missing dep on Pytest.

* Fri Jan 25 2019 Stanislav Levin <slev@altlinux.org> 1.2.6-alt1
- 1.2.5 -> 1.2.6.
- Dropped BR on python argparse.

* Sat Feb 03 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1.1
- (NMU) Fix Requires to gherkin

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.5-alt1.a1.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.a1.git20141018
- Initial build for Sisyphus

