%define _unpackaged_files_terminate_build 1
%define oname gettext

%def_with check

Name: python3-module-%oname
Version: 4.0
Release: alt1
Summary: Python Gettext po to mo file compiler
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/python-gettext/

# https://github.com/hannosch/python-gettext.git
Source0: python-%oname-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

# pypi name
%py3_provides python-%oname

%description
This implementation of Gettext for Python includes a Msgfmt class which
can be used to generate compiled mo files from Gettext po files and
includes support for the newer msgctxt keyword.

%prep
%setup -n python-%oname-%version

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python -m unittest -v
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr --develop

%files
%doc *.rst
%python3_sitelibdir/python_gettext-%version-py%_python3_version.egg-info/
%python3_sitelibdir/pythongettext/
%exclude %python3_sitelibdir/pythongettext/tests/

%changelog
* Thu Apr 07 2022 Stanislav Levin <slev@altlinux.org> 4.0-alt1
- 3.0 -> 4.0.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt2
- Drop python2 support.

* Sat Jul 03 2021 Grigory Ustinov <grenka@altlinux.org> 3.0-alt1.2
- NMU: Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2-alt1.dev.git20130210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.dev.git20130210
- Initial build for Sisyphus

