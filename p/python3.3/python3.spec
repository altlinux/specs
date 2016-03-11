%define shortdesc Setup the compatibility %ext_basename/site-packages directory
%define desc This is a customization of the %std_basename site\
which makes python3 use the additional\
%ext_basename/site-packages directory as the search path\
for modules, too.\
\
This package is needed for the transition only.

# %%std_site is a place where we can put *.py
# to be read and executed by the system python3
# (in the target "output" system).
#
# %%std_basename is some kind of unique name
# we use to name the specific version of the system python3.
# (Here, it happens to occur in the path to %%std_site,
# but in the general case this might not hold.)
%global std_basename %(basename %(dirname %python3_sitelibdir))
%global std_site %python3_sitelibdir

# %%ext_sitelibdir{,_noarch} is the extension we are adding to the
# system python search path.
#
# %%ext_basename is its "base" path component.
# It also appears in the name of the package.
%global ext_basename python%_python3_version
%global ext_sitelibdir %_libdir/%ext_basename/site-packages
%global ext_sitelibdir_noarch %_libexecdir/%ext_basename/site-packages

# To make this package an exception for sisyphus_check,
# its SRPM name must be like a "base" python package;
# cf. 220-check-python (%%s is to avoid RPM warnings):
#
#	# python base packages are exception.
#	if printf %%s "$rpm_sourcerpm" |
#	   egrep -qx 'python([2-9](\.[0-9])?)?-[^-]+-[^-]+'; then
#		return 0
#	fi
#
# Hopefully, we can take 0 as a non-conflicting minor version.
Summary: %shortdesc (with the only built subpkg)
Name: %ext_basename
Version: %_python3_version.1
Release: alt200
License: Python
Group: Development/Python3

BuildRequires(pre): rpm-build-python3 >= 0.1.9
# Possibly, our autoprovs make no sense:
#AutoProv: no

%package -n %ext_basename-site-packages
Summary: %shortdesc
Group: %group

# If we allow to install a package with a module in %%ext_sitelibdir
# (i.e., the old path for modules, with the minor version),
# then we must guarantee that they can work.
# This can be guaranteed only by a python with the same ABI.
%if "%_lib" == "lib64"
Requires: %ext_basename-ABI(64bit)
%else
Requires: %ext_basename-ABI
%endif

# Obsoletes would be not very honest here... hopefully, it works this way:
Conflicts: python3-base < 3.3.1-alt6

%description
ONLY %ext_basename-site-packages PACKAGE IS BUILT AND USED!

%desc

%description -n %ext_basename-site-packages
%desc

%install

mkdir -p %buildroot%ext_sitelibdir/__pycache__
%if "%_lib" == "lib64"
mkdir -p %buildroot%ext_sitelibdir_noarch/__pycache__
%endif

mkdir -p %buildroot%std_site/
cat <<\EOF >%buildroot%std_site/sitecustomize.py
import sys
import os
import site

known_paths = set()
for prefix in site.PREFIXES:
    site.addsitedir(os.path.join("%ext_sitelibdir"),
                    known_paths)
%if "%_lib" == "lib64"
    site.addsitedir(os.path.join("%ext_sitelibdir_noarch"),
                    known_paths)
%endif
EOF

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%ext_basename-site-packages-files.req.list
# %ext_basename-site-packages-%EVR dirlist for %_rpmlibdir/files.req
%ext_sitelibdir/			%ext_basename-site-packages
%ext_sitelibdir/__pycache__/		%ext_basename-site-packages
%if "%_lib" == "lib64"
%ext_sitelibdir_noarch/			%ext_basename-site-packages
%ext_sitelibdir_noarch/__pycache__/	%ext_basename-site-packages
%endif
EOF

%files -n %ext_basename-site-packages
%_rpmlibdir/%ext_basename-site-packages-files.req.list

%dir %ext_sitelibdir/
%dir %ext_sitelibdir/__pycache__/

%if "%_lib" == "lib64"
%attr(0755,root,root) %dir %ext_sitelibdir_noarch
%attr(0755,root,root) %dir %ext_sitelibdir_noarch/__pycache__/
%endif

%std_site/*
%exclude %dir %std_site/__pycache__

%changelog
* Fri Mar 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt200
- customize to look for modules under the old path (python3.3/site-packages)

* Fri Mar 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt107
- (.spec) The summary of the main (non-built)/source package made nicer.

* Thu Mar 10 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt106
- (cosmetic tweak) _-files.req.list: no duplicate entries on non-lib64.

* Fri Mar  4 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt105
- (.spec) simplify: substitute the macros into sitecustomize.py

* Fri Mar  4 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt104
- (.spec) macro code cleanup (easier to understand and extend)

* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt103
- fill out python3-site-packages-files.req.list to make other pkgs
  depend on the listed directories (like in the real python3-base)

* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt102
- workaround the missing dep on rpm-build-python3 in
  python3-3.3.1-alt4 (required by the ALT Sisyphus RPM Macros
  Packaging policy)

* Fri Feb 26 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.1-alt101
- don't loose __pycache__.
- .spec: avoid RPM warnings (because of a macro in comments).

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
