%define oname js.nvd3

Name: python3-module-%oname
Version: 1.8.1
Release: alt2

Summary: Fanstatic packaging of NVD3
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.nvd3/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.d3
BuildRequires: python3-module-pytest

%py3_requires js js.d3

%description
This library packages NVD3 for fanstatic.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test
rm -fR build
export PYTHONPATH=$PWD
py.test3

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.8.1-alt2
- Porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.1-alt1
- Updated to upstream version 1.8.1.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.15-alt1.beta.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.15-alt1.beta.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.15-alt1.beta.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.15-alt1.beta
- Initial build for Sisyphus

