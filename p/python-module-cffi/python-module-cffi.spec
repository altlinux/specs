%define _unpackaged_files_terminate_build 1
%define modulename cffi

%def_with check

Name: python-module-cffi
Version: 1.12.3
Release: alt1

Summary: Foreign Function Interface for Python calling C code

Group: Development/Python
License: MIT
Url: https://pypi.org/project/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://files.pythonhosted.org/packages/93/1a/ab8c62b5838722f29f3daffcc8d4bd61844aa9b5f437341cc890ceee483b/%modulename-%version.tar.gz
Patch: cffi-0.8.6-alt-link.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libffi-devel

%if_with check
BuildRequires: gcc-c++
BuildRequires: python2.7(json)
BuildRequires: python2.7(pycparser)
BuildRequires: python2.7(pytest)
BuildRequires: python3(pycparser)
BuildRequires: python3(tox)
%endif
%py_requires pycparser

%description
Foreign Function Interface for Python calling C code.

%package -n python3-module-cffi
Summary: Foreign Function Interface for Python calling C code
Group: Development/Python3
%py3_requires pycparser

%description -n python3-module-cffi
Foreign Function Interface for Python calling C code.

%prep
%setup -n %modulename-%version
%patch -p2

# unpin pycparser (2.19 brokes Python2.6, but we don't care about old Python)
grep -qsF 'pycparser<2.19' setup.py || exit 1
sed -i 's/pycparser<2\.19/pycparser/g' setup.py

cp -fR . ../python3

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
cat > tox.ini <<EOF
[testenv]
commands = {envpython} -m pytest {posargs:.}
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -vr

%files
%python_sitelibdir/_cffi_backend.so
%python_sitelibdir/%modulename/
%python_sitelibdir/%modulename-%version-py%_python_version.egg-info/

%files -n python3-module-cffi
%python3_sitelibdir/_cffi_backend.cpython-%{python_version_nodots python3}m.so
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/

%changelog
* Mon May 06 2019 Stanislav Levin <slev@altlinux.org> 1.12.3-alt1
- 1.10.0 -> 1.12.3.
- Enabled testing.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Jun 8 2017 Vladimir Didenko <cow@altlinux.ru> 1.10.0-alt1
- Version 1.10.0

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Jan 10 2016 Vladimir Didenko <cow@altlinux.ru> 1.4.2-alt1
- Version 1.4.2

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1
- Version 1.1.2

* Mon Aug 04 2014 Lenar Shakirov <snejok@altlinux.ru> 0.8.6-alt2
- python{3,}-module-pycparser added to Requires
- Because find-requires script /usr/lib/rpm/python3.req.py says:
  * cffi/cparser.py: line=2 possible relative import from ., UNIMPLEMENTED

* Fri Jul 11 2014 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt1
- new version 0.8.6 (with rpmrb script) (ALT bug #30174)

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt3
- Added module for Python3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt2
- fix packing

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus
