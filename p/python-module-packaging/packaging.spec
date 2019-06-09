%define _unpackaged_files_terminate_build 1
%define oname packaging

%def_with docs
%def_with check

Name: python-module-%oname
Version: 19.0
Release: alt1
Summary: Core utilities for Python packages
License: ASLv2.0 or BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/packaging
BuildArch: noarch

# https://github.com/pypa/packaging.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with docs
BuildRequires: python-module-sphinx-devel
%endif

%if_with check
BuildRequires: python2.7(coverage)
BuildRequires: python2.7(pretend)
BuildRequires: python2.7(pyparsing)
BuildRequires: python2.7(pytest)
BuildRequires: python3(coverage)
BuildRequires: python3(pretend)
BuildRequires: python3(pyparsing)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
Core utilities for Python packages.

%package -n python3-module-%oname
Summary: Core utilities for Python packages
Group: Development/Python3

%description -n python3-module-%oname
Core utilities for Python packages.

%if_with docs
%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
%summary
This package contains documentation for %oname

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Core utilities for Python packages.

This package contains pickles for %oname.
%endif

%prep
%setup

cp -fR . ../python3

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%if_with docs
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst LICENSE*
%python_sitelibdir/%oname/
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/
%if_with docs
%exclude %python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/* tasks

%files pickles
%python_sitelibdir/*/pickle
%endif

%files -n python3-module-%oname
%doc *.rst LICENSE*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Thu Jun 06 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt1
- 16.8 -> 19.0.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 16.8-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 16.8-alt1
- Updated to upstream version 16.8.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.4-alt2.dev0.git20150801.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 02 2016 Sergey Alembekov <rt@altlinux.ru> 15.4-alt2.dev0.git20150801
- rebuild with clean buildreq
- disable tests 

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.4-alt1.dev0.git20150801
- Initial build for Sisyphus

