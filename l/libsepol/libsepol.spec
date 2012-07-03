Name: libsepol
Version: 2.0.42
Release: alt1.1

Summary: SELinux binary policy manipulation library
License: LGPLv2+
Group: System/Libraries
Url: http://userspace.selinuxproject.org/trac/
# http://www.nsa.gov/selinux/archives/libsepol-%version.tgz
Source: %name-%version.tar

%description
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
%description devel
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

This package contains development library and header files for %name.

%package devel-static
Summary: Static development files for %name
Group: Development/C
Requires: %name-devel = %version-%release
%description devel-static
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

This package contains static library.

%package utils
Summary: Utils for checking and mainplating policy binaries Security-enhanced Linux
Group: System/Configuration/Other
Requires: %name = %version-%release
%description utils
libsepol provides an API for the manipulation of SELinux binary policies.
It is used by checkpolicy (the policy compiler) and similar tools, as well
as by programs like load_policy that need to perform specific transformations
on binary policies such as customizing policy boolean settings.

%prep
%setup

%build
%make_build LIBDIR=%buildroot%_libdir SHLIBDIR=%buildroot/%_lib \
        CFLAGS='%optflags -W -Wundef -Wshadow -Wmissing-noreturn -Wmissing-format-attribute'

%install
%makeinstall_std LIBDIR=%buildroot%_libdir SHLIBDIR=%buildroot/%_lib

%files
/%_lib/*.so.*

%files devel
%_libdir/*.so
%_includedir/sepol
%_pkgconfigdir/*.pc
%_man3dir/*

%files devel-static
%_libdir/*.a

%files utils
%_bindir/chkcon
%_man8dir/chkcon.*
%exclude %_man8dir/genpol*

%changelog
* Thu Nov 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.42-alt1.1
- Fixed packaging of manpages.
- Rebuilt for debuginfo.

* Wed Dec 29 2010 Mikhail Efremov <sem@altlinux.org> 2.0.42-alt1
- Updated to 2.0.42.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.41-alt2
- fix build and install sections.
- Set LIBDIR and SHLIBDIR for make while build.
- use tar instead of tgz for sources.
- fix Url.
- Drop redundant information from description.

* Wed Feb 03 2010 Mikhail Efremov <sem@altlinux.org> 2.0.41-alt1
- new version

* Thu May 07 2009 Anton Farygin <rider@altlinux.ru> 2.0.36-alt1
- new version

* Mon Dec 22 2008 Anton Farygin <rider@altlinux.ru> 2.0.34-alt1
- new version

* Fri Dec 19 2008 Anton Farygin <rider@altlinux.ru> 2.0.30-alt1
- new (development) version
- specfile cleanup

* Sun Mar 09 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.16.12-alt1
- Initial build
