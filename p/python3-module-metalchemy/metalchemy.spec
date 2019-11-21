%define oname metalchemy

%def_disable check

Name: python3-module-%oname
Version: 1.0.0
Release: alt3

Summary: SQLAlchemy hierarchical key/value helper
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/metalchemy/
# https://github.com/paylogic/metalchemy.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
The metalchemy package provides helpers for your SQLAlchemy models to
add dynamic properties.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test-%_python3_version

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2.git20141006.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.git20141006.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)


* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt2.git20141006
- Disable tests and unnecessary dependencies

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141006
- Initial build for Sisyphus

