%define _unpackaged_files_terminate_build 1

%define oname hypothesis

%def_with check

Name: python3-module-%oname
Version: 5.41.2
Release: alt1

Summary: A library for property based testing

License: MPL-2.0-no-copyleft-exception
Group: Development/Python3
Url: https://pypi.org/project/hypothesis/

BuildArch: noarch

# Source-url: %__pypi_url hypothesis
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3(attr)
BuildRequires: python3(black)
BuildRequires: python3(dateutil)
BuildRequires: python3(fakeredis)
BuildRequires: python3(numpy)
BuildRequires: python3(pandas)
BuildRequires: python3(pytz)
BuildRequires: python3(pexpect)
BuildRequires: python3(redis)
BuildRequires: python3(sortedcontainers)
BuildRequires: python3(pytest_xdist)
BuildRequires: python3(tox)
%endif

%description
Hypothesis is an advanced testing library for Python. It lets you write tests
which are parametrized by a source of examples, and then generates simple and
comprehensible examples that make your tests fail. This lets you find more bugs
in your code with less work.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
whitelist_externals =
    /bin/cp
    /bin/sed
commands_pre =
    /bin/cp %_bindir/py.test3 {envbindir}/py.test
    /bin/sed -i '1c #!{envpython}' {envbindir}/py.test
commands =
    {envbindir}/py.test {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -- --numprocesses auto tests

%files
%doc LICENSE.txt README.rst
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 5.41.2-alt1
- new version 5.41.2

* Thu Oct 15 2020 Stanislav Levin <slev@altlinux.org> 5.37.3-alt1
- 5.7.0 -> 5.37.3.

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script)
- separated build python3 module

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.66.30-alt1
- Updated to upstream version 3.66.30.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.18.1-alt1
- Updated to upstream version 3.18.1.

* Thu Jan 19 2017 Anton Midyukov <antohami@altlinux.org> 3.6.1-alt1
- Initial build for ALT Linux Sisyphus.
