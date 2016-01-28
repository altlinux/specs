%define modulename meld3

%def_with python3

Name: python-module-%modulename
Version: 0.6.5
Release: alt1.2.1

Summary: Elementree based templating system
License: ZPL
Group: Development/Python
Url: http://www.plope.com/software/meld3/
Packager: Maxim Ivanov <redbaron at altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

#BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif
Requires: python-module-elementtree
Source: %modulename-%version.tar
Patch: meld3-0.6.5-alt-hotshot.patch
Patch1: meld3-0.6.5-alt-mimetools.patch

%setup_python_module %modulename

%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template 
markup and dynamic rendering logic separate from one another. 
See http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%package -n python3-module-%modulename
Summary: Elementree based templating system
Group: Development/Python3
%add_python3_req_skip neo_cgi neo_cs neo_util

%description -n python3-module-%modulename
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template 
markup and dynamic rendering logic separate from one another. 
See http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch -p0
%patch1 -p0
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
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
%python_sitelibdir/*
%doc *.txt

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/*
%doc *.txt
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.5-alt1.2.1
- NMU: Use buildreq for BR.

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.5-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.5-alt1.1
- Rebuilt with python 2.6

* Fri May 22 2009 Maxim Ivanov <redbaron at altlinux.org> 0.6.5-alt1
- Initial build for ALTLinux

