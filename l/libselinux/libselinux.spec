Name: libselinux
Version: 2.0.98
Release: alt2.1

Summary: SELinux library
License: Public Domain
Group: System/Libraries
Url: http://userspace.selinuxproject.org/

# http://userspace.selinuxproject.org/releases/current/devel/
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libsepol-devel-static >= 2.0.36-alt1

%description
libselinux provides an API for SELinux applications to get and set
process and file security contexts and to obtain security policy
decisions.

%package devel
Summary: SELinux development library and header files
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development library and header files needed
for developing SELinux applications.

%package devel-static
Summary: Static SELinux library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static SELinux library needed for developing
statically linked SELinux applications.

%package utils
Summary: SELinux utilities
Group: System/Configuration/Other

%description utils
This package provides utility programs to get and set process and
file security contexts and to obtain security policy decisions.

%package -n python-module-selinux
%setup_python_module selinux
Summary: Python module for %name
Group: System/Configuration/Other

%description -n python-module-selinux
This package contains SELinux python bindings.

%prep
%setup
%patch -p1

%build
%make_build all pywrap \
	CFLAGS='%optflags -W -Wundef -Wshadow -Wmissing-noreturn -Wmissing-format-attribute' \
	LIBDIR=%_libdir PYTHON_VERSION=%__python_version

%install
%makeinstall_std install-pywrap \
	LIBDIR=%buildroot/%_libdir \
	SHLIBDIR=%buildroot/%_lib
mkdir -p %buildroot/var/run/setrans

%post
telinit=/sbin/telinit
[ -x $telinit -a -L /proc/1/exe -a -L /proc/1/root ] && $telinit u ||:

%files
/%_lib/*.so.*
%_man8dir/*
/sbin/matchpathcon
%dir /var/run/setrans

%files devel
%_libdir/*.so
%_includedir/selinux/
%_pkgconfigdir/*.pc
%_man3dir/*
%_man5dir/*

%files devel-static
%_libdir/*.a

%files utils
%_sbindir/*

%files -n python-module-selinux
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.98-alt2.1
- Rebuild with Python-2.7

* Fri Feb 25 2011 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt2
- Fix License.
- Rebuilt for debuginfo.

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.98-alt1
- Updated to 2.0.98.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt6
- .pc file: use Libs.private instead of Requires.private.

* Mon Sep 13 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt5
- Add /var/run/setrans directory.

* Tue Aug 31 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt4
- Cleanup is_selinux_enabled() (by Dmitry V. Levin).
- Fix %%post to avoid circular dependence on SysVinit (by Dmitry V. Levin).

* Mon Aug 30 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt3
- utils: fix is_selinux_enabled() return value handling.
- Run 'telinit u' in %%post (closes #23987).

* Thu Aug 26 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt2
- Fix errors messages.

* Wed Aug 25 2010 Mikhail Efremov <sem@altlinux.org> 2.0.96-alt1
- Updated to 2.0.96.
- Made 10 symbols hidden (by Dmitry V. Levin).
- Relocated load_setlocaldefs definition (by Dmitry V. Levin).
- Fixed specfile to use %%optflags for build.

* Mon Jun 28 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt2
- Ugly hackaround for 'load policy' bug.
- fix selinuxenabled.

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.94-alt1
- new version

* Wed Mar 10 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt2
- devel package: fix description and group.
- package the static libraries.

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.90-alt1
- new version

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.80-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.80-alt1
- new version

* Tue Jan 13 2009 Anton Farygin <rider@altlinux.ru> 2.0.77-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.76-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2.0.65-alt1
- new (development) version
- specfile cleanup
- use static libsepol for build (mainstream)
- move man3 and man5 to devel package

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.34.15-alt1
- Initial build
