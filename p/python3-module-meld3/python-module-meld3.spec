%define modulename meld3

Name: python3-module-%modulename
Version: 2.0.0
Release: alt2

Summary: Elementree based templating system
License: ZPL
Group: Development/Python3
Url: http://www.plope.com/software/meld3/
# https://github.com/Supervisor/meld3
BuildArch: noarch

Source: meld3-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires elementtree

%add_python3_req_skip neo_cgi neo_cs neo_util


%description
meld3 is an HTML/XML templating system for Python 2.3+ which keeps template 
markup and dynamic rendering logic separate from one another. 
See http://www.entrian.com/PyMeld for a treatise on the benefits of this pattern.

%prep
%setup -n meld3-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc *.txt


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2
- build for python2 disabled

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
