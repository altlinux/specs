%define oname pyxattr

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt2

Summary: A python module for accessing filesystem Extended Attributes

License: LGPLv2.1
Group: Development/Python
Url: http://pyxattr.sourceforge.net/

# https://github.com/iustin/pyxattr.git
Source: %name-%version.tar

%setup_python_module %oname

BuildPreReq: libattr-devel python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
This is the pyxattr module, a Python extension module which gives access
to the extended attributes for filesystem objects available in some
operating systems.

%package -n python3-module-%oname
Summary: A python module for accessing filesystem Extended Attributes
Group: Development/Python3

%description -n python3-module-%oname
This is the pyxattr module, a Python extension module which gives access
to the extended attributes for filesystem objects available in some
operating systems.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%add_optflags -Wno-error=cpp
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make doc

%files
%python_sitelibdir/*
%doc NEWS README doc/html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%doc NEWS README doc/html
%endif

%changelog
* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.5.3-alt2
- Fix includes. Bug in includes.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Version 0.5.3
- Added module for Python 3

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt for debuginfo

* Sun Jul 11 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.5.0-alt1
- 0.5.0
- spec fixes

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt2
- Rebuilt with python 2.6

* Tue Jan 29 2008 Grigory Batalov <bga@altlinux.ru> 0.2.1-alt1.1
- Rebuilt with python-2.5.

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux Sisyphus
