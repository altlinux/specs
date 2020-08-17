%define oname plugml

Name: python3-module-%oname
Version: 0.2.4
Release: alt3

Summary: Easy-to-use and highly modular machine learning framework
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/plugml/
# https://github.com/mkraemer67/plugml.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: fix-deprecated-import.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nltk python3-module-numpy
BuildRequires: python3-module-psycopg2 python3-module-scikit-learn
BuildRequires: python3-module-scipy

%py3_provides %oname
%py3_requires nltk numpy psycopg2 sklearn scipy


%description
Easy-to-use and highly modular machine learning framework based on
scikit-learn with postgresql data bindings.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Mon Aug 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt3
- Deprecated import fixed.

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.git20150215.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.4-alt1.git20150215.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.git20150215
- Version 0.2.4

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150211
- Initial build for Sisyphus

