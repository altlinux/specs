%define _unpackaged_files_terminate_build 1

%define oname sh
%def_with check

Name: python3-module-%oname
Version: 1.12.14
Release: alt6
Summary: Python subprocess interface
License: MIT
BuildArch: noarch
Group: Development/Python3
Url: https://pypi.org/project/sh/

# https://github.com/amoffat/sh.git
Source: %name-%version.tar
Patch1: pep-0538-test-fix.patch
Patch2: 1.12.14-sh-alt-fix-test_piped_exceptionX.patch
Patch3: 1.12.14-sh-alt-fix-test_general_signal.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-coverage
BuildRequires: python3(tox)
%endif

%description
sh (previously pbs) is a full-fledged subprocess replacement for python
2.6 - 3.2 that allows you to call any program as if it were a function:

  from sh import ifconfig
  print ifconfig("eth0")

sh is not a collection of system commands implemented in python.

%prep
%setup
%autopatch -p1

sed -i -e 's:==:>=:g' \
	requirements*.txt

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} sh.py travis
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc *.md
%python3_sitelibdir/sh.py
%python3_sitelibdir/__pycache__/sh.cpython-*.py*
%python3_sitelibdir/sh-%version-py*.egg-info/

%changelog
* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.12.14-alt6
- Built Python3 package from its ows src.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.12.14-alt5
- Fixed FTBFS.

* Tue Jan 22 2019 Stanislav Levin <slev@altlinux.org> 1.12.14-alt4
- Fixed build.

* Tue Jan 15 2019 Stanislav Levin <slev@altlinux.org> 1.12.14-alt3
- Fixed build.

* Wed Sep 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt2
- Fixed build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.12.14-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.14-alt1
- Updated to upstream release 1.12.14.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150211
- Version 1.11

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2.git20141230
- Fixed Group

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt1.git20141230
- Version 1.10

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.09-alt1.git20130908
- Initial build for Sisyphus

