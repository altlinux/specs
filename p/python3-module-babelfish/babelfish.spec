%define oname babelfish

Name:       python3-module-%oname
Version:    0.5.5
Release:    alt4

Summary:    A module to work with countries and languages
License:    BSD
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/babelfish/

BuildArch:  noarch

#           https://github.com/Diaoul/babelfish.git
Source:     %name-%version.tar
Patch1:     %oname-%version-alt-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%py3_provides %oname


%description
BabelFish is a Python library to work with countries and languages.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
BabelFish is a Python library to work with countries and languages.

This package contains tests for %oname.

%prep
%setup
%patch1 -p1

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.5-alt4
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.5-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.5-alt3
- Updated to upstream release version 0.5.5.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.5-alt2.dev.git20150124.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 03 2016 Sergey Alembekov <rt@altlinux.ru> 0.5.5-alt2.dev.git20150124
- Delete unnecessary dependens

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

