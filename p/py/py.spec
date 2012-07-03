%def_with python3

Name: py
Version: 1.4.7
Release: alt2.hg20120217
Summary: Testing and distributed programming library
License: MIT
Group: Development/Tools
Url: http://pylib.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

# hg clone https://bitbucket.org/hpk42/py
Source: %name-%version.tar.gz

Requires: python-module-%name = %version-%release

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

%if_with python3
%package -n python3-module-%name
Summary: Python 3 module of testing and distributed programming library
Group: Development/Python3
%add_python3_req_skip compiler

%description -n python3-module-%name
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains python module of py lib.

%package -n python3-module-%name-testing
Summary: Testing for py (Python 3)
Group: Development/Python3

%description -n python3-module-%name-testing
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains testing for py lib.
%endif

%package -n python-module-%name
Summary: Python module of testing and distributed programming library
Group: Development/Python
Conflicts: %name

%description -n python-module-%name
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains python module of py lib.

%package -n python-module-%name-testing
Summary: Testing for py
Group: Development/Python

%description -n python-module-%name-testing
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains testing for py lib.

%package doc
Summary: Documentation for testing and distributed programming library
Group: Development/Documentation

%description doc
The py lib has several namespaces which help with testing, generating
and distributing code across machines.

This package contains documentation for py lib.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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
rm -fR %buildroot%python_sitelibdir/%name/bin/win32 \
	%buildroot%python_sitelibdir/%name/execnet/script/socketserverservice.py*
cp -fR testing %buildroot%python_sitelibdir/%name/

for i in $(find %buildroot%python_sitelibdir/%name -type d)
do
	touch $i/__init__.py
done

%if_with python3
pushd ../python3
%python3_install
popd
rm -fR %buildroot%python3_sitelibdir/%name/bin/win32 \
	%buildroot%python3_sitelibdir/%name/execnet/script/socketserverservice.py*
cp -fR testing %buildroot%python3_sitelibdir/%name/

for i in $(find %buildroot%python3_sitelibdir/%name -type d)
do
	touch $i/__init__.py
done
%endif

#files
#_bindir/*

%files -n python-module-%name
%doc AUTHORS CHANGELOG LICENSE *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%name/testing
%exclude %python_sitelibdir/%name/test.py*

%files -n python-module-%name-testing
%python_sitelibdir/%name/testing
%python_sitelibdir/%name/test.py*

%files doc
%doc doc
#doc hacking

%if_with python3
%files -n python3-module-%name
%doc AUTHORS CHANGELOG LICENSE *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%name/testing
%exclude %python3_sitelibdir/%name/test.py*

%files -n python3-module-%name-testing
%python3_sitelibdir/%name/testing
%python3_sitelibdir/%name/test.py*
%endif

%changelog
* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt2.hg20120217
- Added module for Python 3

* Fri Mar 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.7-alt1.hg20120217
- Version 1.4.7

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.6-alt1.hg20111120
- Version 1.4.6 (dev1)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.0-alt1.a1.hg20101007.1
- Rebuild with Python-2.7

* Sun Nov 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.a1.hg20101007
- Version 1.4.0a1

* Wed Jun 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.hg20100628.a1
- Version 1.3.2
- Added testing package (ALT #23695)

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20090913.1
- Rebuilt with python 2.6

* Sun Sep 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.svn20090913
- Initial build for Sisyphus

