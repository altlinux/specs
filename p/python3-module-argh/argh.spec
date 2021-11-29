%define _unpackaged_files_terminate_build 1

%define oname argh
%def_with check

Name: python3-module-%oname
Version: 0.26.2
Release: alt2
Summary: An unobtrusive argparse wrapper with natural syntax
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/argh/

# https://github.com/neithere/argh.git
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(mock)
BuildRequires: python3(tox)
%endif

%description
An argparse wrapper that doesn't make you say "argh" each time you deal
with it.

http://argh.rtfd.org

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} -m pytest {posargs:-vra}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr

%files
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*

%changelog
* Mon Nov 29 2021 Stanislav Levin <slev@altlinux.org> 0.26.2-alt2
- Fixed FTBFS.

* Tue Sep 08 2020 Stanislav Levin <slev@altlinux.org> 0.26.2-alt1
- 0.26.1 -> 0.26.2.
- Stopped Python2 package build.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.26.1-alt1.git20141030.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Jul 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.26.1-alt1.git20141030.2
- Fixed build spec with pytest3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.26.1-alt1.git20141030.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.26.1-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.26.1-alt1.git20141030
- Initial build for Sisyphus

