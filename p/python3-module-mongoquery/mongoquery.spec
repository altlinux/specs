%define _unpackaged_files_terminate_build 1
%define oname mongoquery

Name: python3-module-%oname
Version: 1.3.5
Release: alt1

Summary: A python implementation of mongodb queries
License: Public domain
Group: Development/Python3
Url: https://pypi.python.org/pypi/mongoquery/
BuildArch: noarch

# https://github.com/kapouille/mongoquery.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-unittest2

%py3_provides %oname


%description
A utility library that provides a MongoDB-like query language for
querying python collections. It's mainly intended to parse objects
structured as fundamental types in a similar fashion to what is produced
by JSON or YAML parsers.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Jan 23 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.5-alt1
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.2-alt1.git20170921.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.2-alt1.git20170921
- Updated to current upstream version.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1
- automated PyPI update

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20150105
- Initial build for Sisyphus

