%define _unpackaged_files_terminate_build 1
%define oname parse_type

%def_with check

Name: python-module-%oname
Version: 0.4.2
Release: alt2
Summary: parse_type extends the parse module (opposite of string.format())
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/parse_type/

# https://github.com/jenisys/parse_type.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(enum34)
BuildRequires: python2.7(parse)
BuildRequires: python2.7(pytest)
BuildRequires: python3(parse)
BuildRequires: python3(tox)
%endif

%py_requires parse enum34

%description
Simplifies to build parse types based on the parse module.

%package -n python3-module-%oname
Summary: parse_type extends the parse module (opposite of string.format())
Group: Development/Python3
%py3_requires parse

%description -n python3-module-%oname
Simplifies to build parse types based on the parse module.

%prep
%setup

rm -rf ../python3
cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
sed -i -e '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%python_sitelibdir/parse_type/
%python_sitelibdir/parse_type-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/parse_type/
%python3_sitelibdir/parse_type-%version-py%_python3_version.egg-info/

%changelog
* Tue Jan 29 2019 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2
- Dropped BR on argparse.

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.2-alt1
- Updated to upstream version 0.4.2.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.5-alt1.dev.git20140505.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.5-alt1.dev.git20140505.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.dev.git20140505.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.dev.git20140505
- Initial build for Sisyphus

