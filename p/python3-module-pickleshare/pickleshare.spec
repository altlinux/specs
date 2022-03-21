%define _unpackaged_files_terminate_build 1
%define oname pickleshare

%def_with check

Name: python3-module-%oname
Version: 0.7.5
Release: alt2
Summary: File system based database that uses python pickles
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pickleshare/

# https://github.com/pickleshare/pickleshare.git
Source0: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary.
Unlike shelve, many processes can access the database simultaneously.
Changing a value in database is immediately visible to other processes
accessing the same database.

Concurrency is possible because the values are stored in separate files.
Hence the 'database' is a directory where all files are governed by
PickleShare.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/pickleshare.py
%python3_sitelibdir/__pycache__/pickleshare.cpython-*
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 0.7.5-alt2
- Fixed FTBFS (Python 3.10).

* Wed Jul 21 2021 Stanislav Levin <slev@altlinux.org> 0.7.5-alt1
- 0.7.4 -> 0.7.5.
- Reenabled testing.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150422.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5-alt1.git20150422.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150422
- Initial build for Sisyphus

