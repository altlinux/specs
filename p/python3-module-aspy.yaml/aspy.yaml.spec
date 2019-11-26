%define _unpackaged_files_terminate_build 1

%define mname aspy
%define oname %mname.yaml

Name: python3-module-%oname
Version: 1.1.1
Release: alt2

Summary: Some extensions to pyyaml
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/aspy.yaml/

# https://github.com/asottile/aspy.yaml.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml python3-module-coverage
BuildRequires: python3-module-flake8 pylint-py3
BuildRequires: python3-module-pytest

%py3_provides %oname
Requires: python3-module-%mname = %EVR
%py3_requires yaml


%description
A few extensions to pyyaml.

%package -n python3-module-%mname
Summary: Core files of %mname
Group: Development/Python3
%py3_provides %mname

%description -n python3-module-%mname
Core files of %mname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 %mname/__init__.py \
	%buildroot%python3_sitelibdir/%mname/

%check
%__python3 setup.py test
py.test3 -vv

%files
%doc *.md
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth
%exclude %python3_sitelibdir/%mname/__init__.py
%exclude %python3_sitelibdir/%mname/__pycache__

%files -n python3-module-%mname
%dir %python3_sitelibdir/%mname
%dir %python3_sitelibdir/%mname/__pycache__
%python3_sitelibdir/%mname/__init__.py
%python3_sitelibdir/%mname/__pycache__


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt2
- python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1.qa1
- NMU: applied repocop patch

* Wed May 30 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150111.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.git20150111.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.git20150111
- Initial build for Sisyphus

