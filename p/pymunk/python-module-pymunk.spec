Name: pymunk
Version: 5.0.0
Release: alt1
%setup_python_module %name
Summary: Example files for %packagename
Group: Development/Python
License: MIT
BuildArch: noarch
Source: %name-%version.zip
Source1: libload.py

%add_python_req_skip py2exe ctypeslib

# Automatically added by buildreq on Sun Mar 03 2013
# optimized out: python-base
BuildRequires: unzip

%description
Example files for %packagename

%package -n %packagename
Summary: Python wrapper for the chipmunk 2D physics engine
Group: Development/Python
Requires: libchipmunk
%description -n %packagename
Pymunk is a Python wrapper for the wrapper for the chipmunk 2D physics
engine. It aims to be easy to use, "Pythonic", and non-intrusive.

%prep
%setup
cp %SOURCE1 pymunk/

%build
%install
mkdir -p %buildroot%python_sitelibdir_noarch/%modulename %buildroot%_datadir/%name
install pymunk/*.py %buildroot%python_sitelibdir_noarch/%modulename/
cp -a pymunkoptions %buildroot%python_sitelibdir_noarch/
cp -a examples tests tools %buildroot%_datadir/%name/

%files
%doc *txt docs
%_datadir/%name

%files -n %packagename
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/pymunkoptions

%changelog
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

