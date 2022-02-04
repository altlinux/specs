%define _unpackaged_files_terminate_build 1
%define oname clize

%def_with check

Name: python3-module-%oname
Version: 4.2.1
Release: alt1

Summary: Command-line argument parsing for Python, without the effort

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/clize/

# https://github.com/epsy/clize.git
# Source-url: https://pypi.io/packages/source/c/%oname/%oname-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(sigtools)
BuildRequires: python3(six)
BuildRequires: python3(attr)
BuildRequires: python3(od)
BuildRequires: python3(docutils)

BuildRequires: python3(repeated_test)
BuildRequires: python3(dateutil)
BuildRequires: python3(pygments)
BuildRequires: python3(tox)
%endif

%description
Clize procedurally turns your functions into convenient command-line
interfaces.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/clize/tests/

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    python -m unittest {posargs:-v}
EOF
tox.py3 --sitepackages -vvr

%files
%doc *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Feb 04 2022 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1
- 4.1.1 -> 4.2.1.

* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 4.1.1-alt2
- Drop python2 support.

* Mon Apr 20 2020 Pavel Vasenkov <pav@altlinux.org> 4.1.1-alt1
- new version 4.1.1

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0.3-alt1
- new version 4.0.3 (with rpmrb script)
- build python3 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0-alt1.a2.git20150111.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.0-alt1.a2.git20150111.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.0-alt1.a2.git20150111.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.a2.git20150111
- Initial build for Sisyphus

