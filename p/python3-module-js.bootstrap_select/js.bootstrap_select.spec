%define oname js.bootstrap_select

Name: python3-module-%oname
Version: 1.5.2
Release: alt2

Summary: Fanstatic packaging of bootstrap-select.js
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.bootstrap_select/

# https://github.com/tmassman/js.bootstrap_select.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.bootstrap
BuildRequires: python3-module-pytest

%py3_requires js js.bootstrap


%description
This library packages bootstrap select for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test
export PYTHONPATH=$PWD
py.test3

%files
%doc *.rst
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.2-alt1.git20140516.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1.git20140516.2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.2-alt1.git20140516.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.2-alt1.git20140516.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.2-alt1.git20140516.1
- NMU: Use buildreq for BR.

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140516
- Initial build for Sisyphus

