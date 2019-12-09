%define _unpackaged_files_terminate_build 1
%define oname pytest-tornado

Name: python3-module-%oname
Version: 0.8.0
Release: alt2

Summary: Fixtures and markers to simplify testing of asynchronous tornado applications
License: ASLv2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/pytest-tornado/

# https://github.com/eugeniy/pytest-tornado.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(pytest)
BuildRequires: python3(tornado)
BuildRequires: python3(tox)

%py3_provides %oname


%description
A py.test plugin providing fixtures and markers to simplify testing of
asynchronous tornado applications.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    python test/create_cert.py --cert test/testcert.pem
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc README.rst
%python3_sitelibdir/pytest_tornado/
%python3_sitelibdir/*.egg-info/


%changelog
* Mon Dec 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.8.0-alt2
- python2 disabled

* Fri May 31 2019 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.5.0 -> 0.8.0.

* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- 0.4.5 -> 0.5.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.5-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.5-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150219.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150219
- Initial build for Sisyphus

