%define _unpackaged_files_terminate_build 1
%define oname dirty-models

%def_with check

Name: python3-module-%oname
Version: 0.12.4
Release: alt1
Summary: Dirty models for python 3
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/dirty-models/

# https://github.com/alfred82santa/dirty-models.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(dateutil)

BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(nose2)
BuildRequires: python3(iso8601)
%endif

# PEP503 normalized name
%py3_provides %oname

%description
Dirty models for python 3.


Features:

* Python 3 package.
* Easy to create a model.
* Non destructive modifications.
* Non false positive modifications.
* Able to restore original data for each field or whole model.
* Access to original data.
* Read only fields.
* Alias for fields.
* Custom getters and setters for each fields.
* Automatic cast value.
* Easy import from/export to dict.
* Basic field type implemented.
* HashMap model. It could be used instead of DynamicModel.
* FastDynamicModel. It could be used instead of DynamicModel. Same
  behavior, better performance.
* Pickable models.
* Datetime fields can use any datetime format using parser and formatter
  functions.
* No database dependent.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    nose2
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc *.rst
%python3_sitelibdir/dirty_models/
%python3_sitelibdir/dirty_models-%version-py%_python3_version.egg-info/

%changelog
* Tue Feb 08 2022 Stanislav Levin <slev@altlinux.org> 0.12.4-alt1
- 0.9.2 -> 0.12.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jan 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.2-alt1
- automated PyPI update

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150420
- Initial build for Sisyphus

