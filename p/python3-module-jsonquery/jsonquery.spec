%define _unpackaged_files_terminate_build 1
%define oname jsonquery

Name: python3-module-%oname
Version: 1.0.2
Release: alt3

Summary: Basic json -> sqlalchemy query builder
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonquery/
# https://github.com/numberoverzero/jsonquery.git

Source: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-SQLAlchemy
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires json sqlalchemy


%description
Basic json -> sqlalchemy query builder.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150117
- Initial build for Sisyphus

