%global pybasever 3
%global old_pybasever 3.3

%global pylibdir %_libdir/python%pybasever
%global pylibdir_noarch %_libexecdir/python%pybasever
%global old_pylibdir %_libdir/python%old_pybasever
%global old_pylibdir_noarch %_libexecdir/python%old_pybasever

# To make this package an exception for sisyphus_check,
# its SRPM name must be like a "base" python package;
# cf. 220-check-python :
#
#	# python base packages are exception.
#	if printf %s "$rpm_sourcerpm" |
#	   egrep -qx 'python([2-9](\.[0-9])?)?-[^-]+-[^-]+'; then
#		return 0
#	fi
#
# Hopefully, we can take 0 as a non-conflicting minor version.
Summary: ONLY site-packages SUBPACKAGE IS BUILT
Name: python%pybasever.0
Version: %old_pybasever.1
Release: alt100
License: Python
Group: Development/Python3

BuildRequires(pre): rpm-build-python3 >= 0.1.7
# Possibly, our autoprovs make no sense:
#AutoProv: no

Source: sitecustomize.py
Patch: sitecustomize-lib64.patch

%package -n python%pybasever-site-packages
Summary: Setup the common python%pybasever/site-packages directory
Group: Development/Python3

%description
ONLY %name-site-packages PACKAGE IS BUILT AND USED!

%description -n python%pybasever-site-packages
This is a customization of the python%pybasever site
which makes python%old_pybasever use the new common
python%pybasever/site-packages directory as the search path
for modules.

New releases of python%pybasever in Sisyphus will do this by default.

This package is needed for the transition only.

%prep
cp %SOURCE0 ./
%if "%_lib" == "lib64"
%patch0 -p1
%endif

%install

install -d -m 0755 $RPM_BUILD_ROOT%pylibdir/site-packages/__pycache__

%if "%_lib" == "lib64"
install -d -m 0755 %buildroot/usr/lib/python%pybasever/site-packages/__pycache__
%endif

install -d -m 0755 $RPM_BUILD_ROOT%old_pylibdir/site-packages/
install -m 0644 sitecustomize.py $RPM_BUILD_ROOT%old_pylibdir/site-packages/

%files -n python%pybasever-site-packages

%dir %pylibdir
%dir %pylibdir/site-packages/
%dir %pylibdir/site-packages/__pycache__/

%if "%_lib" == "lib64"
%attr(0755,root,root) %dir %prefix/lib/python%pybasever
%attr(0755,root,root) %dir %prefix/lib/python%pybasever/site-packages
%attr(0755,root,root) %dir %prefix/lib/python%pybasever/site-packages/__pycache__/
%endif

%old_pylibdir/site-packages/*
%exclude %old_pylibdir/site-packages/__pycache__

%changelog
* Fri Feb 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt100
- Stripped everything from python3 packages, but left only the
  site-packages dirs (at the new common location).
- Put sitecustomize.py for python3.3 to look into these new dirs.

* Tue Apr 16 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt4
- remove subpackage %%name-modules-idlelib (moved to
  %%name-modules-tkinter)
- move %%_libdir/python*/Tools/scripts/run_tests.py to subpackage
  %%name-test

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt3
- add subpackage %%name-modules-idlelib

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt2
- fix gcc 4.8 incompatibility (rhbz#927358); regenerate autotool
  intermediates
- fix error in platform.platform() when non-ascii byte strings are
  decoded to unicode (rhbz#922149)

* Fri Apr 12 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.1-alt1
- version up to 3.3.1
- skip test_posix_fadvise: RLIMIT_CPU 1000000 unavailable in hasher

* Fri Mar 29 2013 Aleksey Avdeev <solo@altlinux.ru> 3.3.0-alt1
- version up to 3.3.0
- add support for Bluetooth

* Wed May 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt3
- base: add python3.x(builtins) to Provides

* Thu Apr 19 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt2
- python-3.2.3-autoconf-sem_open_check-alt.patch

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Mon Mar 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt4
- build python3 binary with static libpython3
- split up independent libpython3 subpackage with shared library
- change optimization to -O3

* Thu Jan 26 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt3
- repair build with fresh rpm-build-python3
- enable check

* Wed Dec 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt2
- rebuild with rpm-build-python3
- split up, rename subpackages

* Tue Dec 06 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.2-alt1
- initial Python3 port from Fedora
