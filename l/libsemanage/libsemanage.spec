Name: libsemanage
Version: 2.0.46
Release: alt1.1
License: %lgpl2plus
Url: http://userspace.selinuxproject.org/trac/

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Summary: This package contains the libsemanage library, which provides an interface for SELinux management.
Group: System/Libraries

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue May 12 2009
BuildRequires: bzlib-devel flex libselinux-devel >= 2.0.80-alt1 libsepol-devel >= 2.0.36-alt1 libustr-devel python-devel

%description
This package provides the shared libraries for the manipulation of
SELinux binary policies. It is used by checkpolicy (the policy compiler)
and similar tools, as well as by programs like load_policy that need
to perform specific transformations on binary policies such as
customizing policy boolean settings. This contains the run-time
libraries needed by such tools.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version
%description devel
Header files and libraries for SELinux policy manipulation tools
This package provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as
well as by programs like load_policy that need to perform specific
transformations on binary policies such as customizing policy boolean
settings. It contains the static libraries and header files needed
for developing applications that manipulate SELinux binary policies.

%package -n python-module-semanage
Summary: Python module for %name
Group: System/Configuration/Other
%description -n python-module-semanage
Python bindings  for SELinux policy manipulation tools
This package provides python bindings for the manipulation of SELinux
binary policies.

%prep
%setup
%patch -p1

%build
%make_build all pywrap \
        CFLAGS='%optflags -W -Wundef -Wshadow -Wmissing-noreturn -Wmissing-format-attribute -Wno-unused-parameter' \
        LIBDIR=%buildroot/%_libdir SHLIBDIR=%buildroot/%_lib

%install
%makeinstall_std install-pywrap LIBDIR=%buildroot/%_libdir SHLIBDIR=%buildroot/%_lib
ln -sf /%_lib/libsemanage.so.1 %buildroot/%_libdir/libsemanage.so

%files
%dir %_sysconfdir/selinux
%config(noreplace) %_sysconfdir/selinux/semanage.conf
/%_lib/*.so.*
%_man3dir/*

%files devel
%_libdir/*.so
%exclude %_libdir/*.a
%_includedir/semanage
%_pkgconfigdir/*.pc

%files -n python-module-semanage
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.46-alt1.1
- Rebuild with Python-2.7

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.46-alt1
- Updated to 2.0.46.
- Drop unused variable.

* Mon Nov 15 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt3
- Add /srv/home and /var/srv/home to home directories list.
- Use rpm-build-licenses.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt2
- .pc file: use Libs.private instead of Requires.private.
- fix build and install sections.
- use tar instead of tgz for sources.
- Drop redundant information from description.
- fix Url.
- drop Packager from spec.

* Wed Jun 09 2010 Mikhail Efremov <sem@altlinux.org> 2.0.45-alt1
- new version

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.44-alt1
- new version

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.31-alt1.1
- Rebuilt with python 2.6

* Tue Jan 13 2009 Anton Farygin <rider@altlinux.ru> 2.0.31-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.30-alt1
- new version
- fixed python-module name

* Sat Dec 20 2008 Anton Farygin <rider@altlinux.ru> 2.0.25-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.10.9-alt1
- Initial build
