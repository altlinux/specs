%define oname paginate_sqlalchemy

%def_with check

Name: python3-module-%oname
Version: 0.3.1
Release: alt1

Summary: Extension to paginate.Page that supports SQLAlchemy queries
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/paginate_sqlalchemy/
Vcs: https://github.com/Pylons/paginate_sqlalchemy.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-paginate
%endif

%py3_provides %oname

%description
This module helps divide up large result sets into pages or chunks. The
user gets displayed one page at a time and can navigate to other pages.
It is especially useful when developing web interfaces and showing the
users only a selection of information at a time.

This module uses and extends the functionality of the paginate module to
support SQLAlchemy queries.

%prep
%setup

sed -i "s/version='0.3.0',/version='0.3.1',/" setup.py

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -k 'not test_select'

%files
%doc CHANGELOG README TODO
%python3_sitelibdir/*


%changelog
* Fri Mar 24 2023 Anton Vyatkin <toni@altlinux.org> 0.3.1-alt1
- new version 0.3.1

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt2.git20140911.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.2.0-alt2.git20140911
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20140911
- Initial build for Sisyphus

