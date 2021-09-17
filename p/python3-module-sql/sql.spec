%define _unpackaged_files_terminate_build 1

%define oname sql

%def_with check

Name: python3-module-%oname
Version: 1.3.0
Release: alt1

Summary: Library to write SQL queries
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/python-sql/
BuildArch: noarch

# https://github.com/Tyba/python-sql.git
Source0: python-%oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(tox)
%endif

# PyPI name
%py3_provides python-sql

%description
python-sql is a library to write SQL queries in a pythonic way.

%prep
%setup -n python-%oname-%version

%build
%python3_build_debug

%install
%python3_install

# don't ship tests
rm -r %buildroot%python3_sitelibdir/%oname/tests/

%check
# `test` command of setuptools is deprecated
sed -i 's/{envpython} setup.py test/python -m unittest discover/' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc CHANGELOG README
%python3_sitelibdir/%oname/
%python3_sitelibdir/python_sql-%version-py%_python3_version.egg-info/

%changelog
* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1
- 0.8 -> 1.3.0.

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20140911
- Initial build for Sisyphus

