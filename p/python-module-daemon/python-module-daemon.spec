%define module_name daemon

%def_with python3

Name: python-module-%module_name
Version: 2.0.5
Release: alt1

Summary: Library to implement a well-behaved Unix daemon process


License: Apache-2
Group: Development/Python
Url: http://pypi.python.org/pypi/python-daemon/

Source: python-%module_name-%version.tar

BuildArch: noarch
BuildRequires: python-module-setuptools
BuildRequires: python-module-lockfile > 0.10 python-module-json python-module-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-lockfile > 0.10 python3-module-simplejson python3-module-docutils
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name


%description
Library to implement a well-behaved Unix daemon process.

%package -n python3-module-%module_name
Summary: Library to implement a well-behaved Unix daemon process
Group: Development/Python3
%py3_provides %module_name

%description -n python3-module-%module_name
Library to implement a well-behaved Unix daemon process.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc ChangeLog LICENSE.*
%python_sitelibdir/daemon
%python_sitelibdir/python_daemon*

%if_with python3
%files -n python3-module-%module_name
%doc ChangeLog LICENSE.*
%python3_sitelibdir/daemon
%python3_sitelibdir/python_daemon*
%endif


%changelog
* Wed Aug 19 2015 Terechkov Evgenii <evg@altlinux.org> 2.0.5-alt1
- Update to 2.0.5

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.5-alt2.1
- Rebuild with Python-2.7

* Fri Aug 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.5.5-alt2
- pidlockfile.py: add checking for stale {pid,lock}file

* Sun Apr 04 2010 Denis Klimov <zver@altlinux.org> 1.5.5-alt1
- Initial build for ALT Linux


