%define oname psutil

Name: python-module-%oname
Version: 0.4.1
Release: alt1.1

Summary: A process utilities module for Python

License: BSD
Group: Development/Python
Url: http://code.google.com/p/psutil/

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://psutil.googlecode.com/files/%oname-%version.tar.gz
Source: %oname-%version.tar

%add_python_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com

# Automatically added by buildreq on Wed Sep 08 2010
BuildRequires: python-devel

BuildPreReq: rpm-build-python


%setup_python_module %oname

%description
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%doc README LICENSE
%python_sitelibdir/%oname/
%python_sitelibdir/_*.so
%python_sitelibdir/*.egg-info

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 23 2012 Alexey Morsov <swi@altlinux.ru> 0.4.1-alt1
- new version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Linux Sisyphus
