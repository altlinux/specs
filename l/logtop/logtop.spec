Name: logtop
Version: 0.6.1
Release: alt1.git20140901.1.1
Summary: Display real time statistics of whatever you want
License: BSD
Group: Text tools
Url: http://julienpalard.github.io/logtop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/JulienPalard/logtop.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: swig libncurses-devel libuthash-devel
BuildPreReq: python-devel python3-devel

Requires: lib%name = %EVR

%description
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

This package contains shared library of %name.

%package -n python-module-%name
Summary: Python module of %name
Group: Development/Python
AutoReq: yes,nopython

%description -n python-module-%name
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

This package contains Python module of %name.

%package -n python3-module-%name
Summary: Python module of %name
Group: Development/Python3

%description -n python3-module-%name
logtop displays real-time count of strings received in standard input.
It's useful for some cases, like getting the IP flooding your server:
$ tail -f /var/log/apache2/access.log | cut -d ' ' -f1 | logtop

This package contains Python module of %name.

%prep
%setup

%build
%make_build all

%install
%ifarch x86_64
LIB_SUFFIX=64
%endif
%makeinstall_std LIB_SUFFIX=$LIB_SUFFIX

sed -i '/^ogtop_swigregister/d' %buildroot%python_sitelibdir/%name.py
sed -i '/^ogtop_swigregister/d' %buildroot%python3_sitelibdir/%name.py

%files
%doc ChangeLog README examples
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so

%files -n python-module-%name
%python_sitelibdir/*

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.6.1-alt1.git20140901.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.1-alt1.git20140901.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri May 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20140901
- Initial build for Sisyphus

