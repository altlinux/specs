%define _unpackaged_files_terminate_build 1

%define oname fake-factory

%def_with check

Name: python3-module-%oname
Version: 4.14.0
Release: alt1
Summary: Faker is a Python package that generates fake data for you
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fake-factory/

# https://github.com/joke2k/faker.git
Source: %name-%version.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(dateutil)
BuildRequires: python3(freezegun)
BuildRequires: python3(pytest)
BuildRequires: python3(random2)
BuildRequires: python3(tox)
BuildRequires: python3(text_unidecode)
BuildRequires: python3(validators)
%endif

%description
Faker is a Python package that generates fake data for you. Whether you
need to bootstrap your database, create good-looking XML documents,
fill-in your persistence to stress test it, or anonymize data taken from
a production service, Faker is for you.

%prep
%setup
%autopatch -p1

%build
%python3_build_debug

%install
%python3_install

pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

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
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
* Fri Oct 16 2020 Stanislav Levin <slev@altlinux.org> 4.14.0-alt1
- 0.8.17 -> 4.14.0.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.17-alt1
- Updated to upstream version 0.8.17.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150222.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.git20150222.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.git20150222.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.git20150222
- Version 0.5.0

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141015
- Initial build for Sisyphus

