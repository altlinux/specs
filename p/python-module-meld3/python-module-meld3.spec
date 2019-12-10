%define modulename meld3

Name: python-module-%modulename
Version: 2.0.0
Release: alt1

Summary: Elementree based templating system
License: ZPL
Group: Development/Python

Url: http://www.plope.com/software/meld3/
# https://github.com/Supervisor/meld3
Packager: Maxim Ivanov <redbaron at altlinux.org>
BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-module-setuptools
BuildRequires: time

%py_requires elementtree

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools

Source: meld3-%version.tar


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
%setup -n meld3-%version

cp -fR . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*
%doc *.txt

%files -n python3-module-%modulename
%python3_sitelibdir/*
%doc *.txt


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1
- Version updated to 2.0.0

* Thu Mar 22 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt1
- Version 1.0.2
  
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.5-alt1.2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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
