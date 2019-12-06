%define oname nose_fixes

%def_without docs

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: A plugin to make nose behave better
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose_fixes/
BuildArch: noarch

# https://github.com/cjw296/nose_fixes.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python3-module-pytest
%if_with docs
BuildRequires: python3-module-sphinx
%endif

%py3_provides %oname


%description
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains tests for %oname.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A plugin that changes nose to behave better. Hopefully, these changes
will make their way back into nose...

This package contains documentation for %oname.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
py.test3

%files
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20130214.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3-alt1.git20130214.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20130214.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130214
- Initial build for Sisyphus

