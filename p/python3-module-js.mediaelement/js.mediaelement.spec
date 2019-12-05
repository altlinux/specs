%define mname js
%define oname %mname.mediaelement

Name: python3-module-%oname
Version: 2.13.1
Release: alt3

Summary: Fanstatic packaging of MediaElement.js
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.mediaelement/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic python3-module-js.jquery
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires %mname fanstatic js.jquery


%description
This library packages MediaElement.js for fanstatic.

This requires integration between your web framework and fanstatic, and
making sure that the original resources (shipped in the resources
directory in js.mediaelement) are published to some URL.

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
export PYTHONPATH=$PWD
py.test3 -vv

%files
%doc *.txt
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.13.1-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.13.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13.1-alt2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13.1-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.13.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus

