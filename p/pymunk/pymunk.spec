%define packagename python3-module-pymunk

Name: pymunk
Version: 5.5.0
Release: alt2

Summary: Empty package %packagename
License: MIT
Group: Development/Python3

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%add_python3_req_skip py2exe ctypeslib

%description
Empty package

%package -n %packagename
Summary: Python wrapper for the chipmunk 2D physics engine
Group: Development/Python3
Requires: libchipmunk

%description -n %packagename
Pymunk is a Python wrapper for the wrapper for the chipmunk 2D physics
engine. It aims to be easy to use, "Pythonic", and non-intrusive.

%package examples
Summary: Example files for %name
Group: Development/Python3
BuildArch: noarch
Obsoletes: %name

%description examples
Example files for %packagename

%prep
%setup

%build
export CFLAGS="-fPIC -O2 -g"
%python3_build_debug

make -C docs/src SPHINXBUILD=sphinx-build-3 BUILDDIR=../../build html

%install
%python3_install

%check
%__python3 setup.py check

%files examples
%doc examples

%files -n %packagename
%doc *txt build/html
%python3_sitelibdir/%name
%python3_sitelibdir/%name-*
%python3_sitelibdir/pymunkoptions

%changelog
* Tue Apr 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 5.5.0-alt2
- Build for python2 disabled.

* Mon Oct 28 2019 Fr. Br. George <george@altlinux.ru> 5.5.0-alt1
- Autobuild version bump to 5.5.0
- Introduce Python3 package
- Rename %name to %name-examples, as it is

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Fix still queer _libload.py

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 5.0.0-alt1
- Autobuild version bump to 5.0.0

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0
- Drop inactual patch

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 3.0.0-alt1
- Autobuild version bump to 3.0.0
- Provide clean version of libload.py
- Add required internal libchipmunk functions

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Initial build from scratch

