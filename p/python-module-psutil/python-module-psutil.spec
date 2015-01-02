%define oname psutil

%def_with python3

Name: python-module-%oname
Version: 2.1.3
Release: alt1

Summary: A process utilities module for Python

License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/psutil/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://psutil.googlecode.com/files/%oname-%version.tar.gz
Source: %oname-%version.tar

%add_python_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com
%add_python_req_skip _psutil_sunos _psutil_windows

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%setup_python_module %oname

%description
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%package -n python3-module-%oname
Summary: A process utilities module for Python
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com
%add_python3_req_skip _psutil_sunos _psutil_windows

%description -n python3-module-%oname
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%prep
%setup -n %oname-%version

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
%doc CREDITS *.rst LICENSE TODO docs/*.rst examples
%python_sitelibdir/%oname/
%python_sitelibdir/_*.so
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc CREDITS *.rst LICENSE TODO docs/*.rst examples
%python3_sitelibdir/%oname/
%python3_sitelibdir/_*.so
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Version 2.1.3
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Sat Feb 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1 (ALT #28561)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 23 2012 Alexey Morsov <swi@altlinux.ru> 0.4.1-alt1
- new version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Linux Sisyphus
