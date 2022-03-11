%define _unpackaged_files_terminate_build 1
%define oname shiftschema

%def_without check

Name: python3-module-%oname
Version: 0.3.0
Release: alt1
Summary: Python3 filtering and validation library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/shiftschema/

# https://github.com/projectshift/shift-schema.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# bad pattern in upstream for reading its own version (self-import)
BuildRequires: python3(bleach)
BuildRequires: python3(slugify)

%if_with check
BuildRequires: python3(flask_wtf)
BuildRequires: python3(nose)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Filtering and validation library for Python3. Can filter and validate
data in model objects and simple dictionaries with flexible schemas.

Main idea: decouple filtering and validation rules from web forms into
flexible schemas, then reuse those schemas in forms as well as apis and
cli. Model validation and filtering rules should be part of the model
and your domain logic, not your views or forms logic.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/nosetests -v {posargs:tests}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false --develop

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Mar 10 2022 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- 0.0.11 -> 0.3.0.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 0.0.11-alt2
- Dropped dependency on coveralls.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.11-alt1
- Updated to upstream version 0.0.11.

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.9-alt1.git20150218.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.9-alt1.git20150218
- Version 0.0.9

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20150211
- Version 0.0.7

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20150205
- Initial build for Sisyphus

