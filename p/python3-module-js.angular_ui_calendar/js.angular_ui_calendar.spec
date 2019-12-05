%define oname js.angular_ui_calendar

Name: python3-module-%oname
Version: 0.9.0
Release: alt3

Summary: Fanstatic packaging of angular-ui ui-calendar
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.angular_ui_calendar/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-js.angular
BuildRequires: python3-module-js.fullcalendar
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires js js.angular js.fullcalendar


%description
This library packages angular-ui-calendar for fanstatic.

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
py.test3

%files
%doc *.txt
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/*-nspkg.pth


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt3
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.0-alt2.beta.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.0-alt2.beta
- Fixed build.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.beta.1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.beta.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.beta.1.1
- NMU: Use buildreq for BR.

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.beta.1
- Initial build for Sisyphus

