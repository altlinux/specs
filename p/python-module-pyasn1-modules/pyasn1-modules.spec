%define _unpackaged_files_terminate_build 1
%define mname pyasn1-modules

%def_with check

Name: python-module-%mname
Version: 0.2.8
Release: alt1

Summary: ASN.1 modules for Python
License: BSD-2-Clause
Group: Development/Python
# Source-git: https://github.com/etingof/pyasn1-modules.git
Url: https://pypi.python.org/pypi/pyasn1-modules

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python2.7(pyasn1)
BuildRequires: python3(pyasn1)

%if_with check
BuildRequires: python2.7(pytest)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

Requires: python-module-pyasn1 >= 0.4.6
BuildArch: noarch

%description
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%package -n python3-module-%mname
Summary: ASN.1 modules for Python 3
Group: Development/Python3
Requires: python3-module-pyasn1 >= 0.4.6

%description -n python3-module-%mname
This is a small but growing collection of ASN.1 data structures
expressed in Python terms using pyasn1 data model.

It's thought to be useful to protocol developers and testers.

%prep
%setup
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF

export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc LICENSE.txt README.md
%python_sitelibdir/pyasn1_modules/
%python_sitelibdir/pyasn1_modules-%version-*.egg-info/

%files -n python3-module-%mname
%doc LICENSE.txt README.md
%python3_sitelibdir/pyasn1_modules/
%python3_sitelibdir/pyasn1_modules-%version-*.egg-info/

%changelog
* Sat Nov 23 2019 Stanislav Levin <slev@altlinux.org> 0.2.8-alt1
- 0.2.4 -> 0.2.8.

* Mon Feb 11 2019 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1
- 0.2.3 -> 0.2.4.

* Thu Jan 17 2019 Stanislav Levin <slev@altlinux.org> 0.2.3-alt1
- 0.2.2 -> 0.2.3.

* Tue Jul 24 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1
- 0.2.1 -> 0.2.2

* Tue Mar 13 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1
- 0.1.5 -> 0.2.1

* Thu Nov 09 2017 Stanislav Levin <slev@altlinux.org> 0.1.5-alt1
- 0.0.8 -> 0.1.5

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Version 0.0.7

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Version 0.0.5

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt2
- Version 0.0.4

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.4-alt1.rc0.1
- Rebuild with Python-3.3

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.rc0
- Initial build for Sisyphus

