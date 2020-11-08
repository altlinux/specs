%define oname packaging

%def_with docs
%def_with check

Name: python3-module-%oname
Version: 19.0
Release: alt3

Summary: Core utilities for Python packages

License: ASLv2.0 or BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/packaging

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch0: packaging-19.0-Fix-testsuite-for-pytest-5.x.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: python3(coverage)
BuildRequires: python3(pretend)
BuildRequires: python3(pyparsing)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
%endif

%description
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
%patch0 -p1

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if_with docs
export PYTHONPATH=$PWD
%make -C docs html SPHINXBUILD=sphinx-build-3
%endif

%check
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst LICENSE*
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%if_with docs
%files docs
%doc docs/_build/html/* tasks
%endif

%changelog
* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 19.0-alt3
- build python3 package separately, cleanup spec

* Fri Aug 09 2019 Stanislav Levin <slev@altlinux.org> 19.0-alt2
- Fixed testing against Pytest 5.

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

