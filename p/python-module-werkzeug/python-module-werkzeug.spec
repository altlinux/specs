%define version 0.10.1
%define release alt1
%setup_python_module werkzeug

%def_with python3
%def_disable check

Summary: Werkzeug is one of the most advanced WSGI utility modules
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename.tar
Patch: werkzeug-alt-python3.patch
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://werkzeug.pocoo.org/

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

#BuildRequires: python-module-setuptools-tests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%description
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.

%package -n python3-module-%modulename
Summary: Werkzeug is one of the most advanced WSGI utility modules
Group: Development/Python3

%description -n python3-module-%modulename
Werkzeug started as a simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules. It includes a powerful debugger, fully featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

It does Unicode and doesn't enforce a specific template engine, database
adapter or anything else. It doesn't even enforce a specific way of
handling requests and leaves all that up to the developer.

%prep
%setup -n %modulename
%patch -p2

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
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python ./setup.py test
%if_with python3
pushd ../python3
python3 ./setup.py test
popd
%endif

%files -f INSTALLED_FILES
%doc AUTHORS CHANGES LICENSE

%if_with python3
%files -n python3-module-%modulename
%doc AUTHORS CHANGES LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.10.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Version 0.10.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1
- Version 0.9.6
- Added module for Python 3

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.1
- Fixed build

* Sun Jan 06 2013 Ivan A. Melnikov <iv@altlinux.org> 0.8.3-alt1
- 0.8.3 (ALT #28297);
- minor packaging improvements.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.2-alt1.1
- Rebuild with Python-2.7

* Mon Jun 06 2011 Sergey Alembekov <rt@altlinux.ru> 0.6.2-alt1
- Initial release for ALTLinux
