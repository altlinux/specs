%define oname js.angular_nvd3_directives

Name: python3-module-%oname
Version: 2.3.11
Release: alt3

Summary: Fanstatic packaging of angularjs-nvd3-directives
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.angular_nvd3_directives/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.angular
BuildRequires: python3-module-js.nvd3
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires js js.angular js.nvd3


%description
This library packages angularjs-nvd3-directives for fanstatic.

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
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.11-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3.11-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.3.11-alt2
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.11-alt1.2.1
- (AUTO) subst_x86_64.

* Tue Mar 15 2016 Denis Medvedev <nbr@altlinux.org> 2.3.11-alt1.2
- NMU just rebuild.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.11-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Initial build for Sisyphus

