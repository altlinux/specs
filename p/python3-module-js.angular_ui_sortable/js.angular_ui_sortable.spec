%define oname js.angular_ui_sortable

Name: python3-module-%oname
Version: 0.13.4
Release: alt2

Summary: Fanstatic packaging of Angular UI Sortable
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.angular_ui_sortable/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic python3-module-js.jquery
BuildRequires: python3-module-js.jqueryui python3-module-js.angular
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires js js.jquery js.jqueryui js.angular


%description
This library packages Angular UI Sortable for fanstatic.

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
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.13.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.13.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13.4-alt1
- Updated to upstream version 0.13.4.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus

