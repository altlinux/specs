Name: acl
Version: 2.2.51
Release: alt1

Summary: ACL manipulation utilities
License: GPLv2+
Group: File tools
Url: http://savannah.nongnu.org/projects/acl
# git://git.altlinux.org/gears/a/acl.git
Source: %name-%version-%release.tar

Requires: lib%name = %version-%release
BuildRequires: libattr-devel
BuildConflicts: libacl-devel

%define _libexecdir %_libdir
%def_disable static

%description
This package contains chacl, getfacl, and setfacl utilities for
manipulating POSIX access control lists.

%package -n lib%name
Summary: Dynamic library for ACL support
License: LGPLv2+
Group: System/Libraries

%package -n lib%name-devel
Summary: ACL header files
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: ACL static library
License: LGPLv2+
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with lib%name.

%description -n lib%name-devel
This package contains header files needed to develop programs which
make use of POSIX access control lists.

%description -n lib%name-devel-static
This package contains the static library needed to develop statically
linked programs which make use of POSIX access control lists.

%prep
%setup

%build
make configure
%configure %{subst_enable static}
%make_build DEBUG= OPTIMIZER=

%install
make install install-lib install-dev \
    DIST_ROOT=%buildroot

# Workaround bug in makefiles
rm -rf %buildroot%_datadir/doc/%name

# Relocate shared libraries from %_libdir/ to /%_lib/.
mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/*.so; do
	t=$(readlink -v "$f")
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/*.so.* %buildroot/%_lib/

# Relocate chacl.
mkdir %buildroot/bin
mv %buildroot%_bindir/chacl %buildroot/bin/

%find_lang %name

%check
if ./setfacl/setfacl -m u:`id -u`:rwx .; then
	make tests
else
	echo 'ACLs are probably not supported by the file system'
fi

%files -f %name.lang
/bin/*
%_bindir/*
%_mandir/man[15]/*
%doc doc/CHANGES.gz README

%files -n lib%name
/%_lib/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_mandir/man[23]/*
%_includedir/acl/
%_includedir/sys/acl.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Tue Sep 20 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.51-alt1
- Updated to v2.2.51-1-g3d80b8f.

* Mon Mar 07 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.49-alt3
- Updated to v2.2.49-10-gcd31baf.
- Fixed compilation warnings.
- Cleaned up specfile.
- Disabled build and packaging of the static library.

* Wed Nov 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.49-alt2
- rebuilt with set-versioned rpm

* Wed Dec 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.49-alt1
- 2.2.49 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.47-alt2
- obsolete by filetriggers macros removed

* Mon Mar 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.47-alt1
- 2.2.47

* Tue Sep 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.45-alt1
- 2.2.45

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.39-alt1.0
- Automated rebuild.

* Thu Sep 14 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.39-alt1
- 2.2.39

* Mon Aug 30 2004 Anton D. Kachalov <mouse@altlinux.org> 2.2.23-alt2
- Multilib support

* Sat May 15 2004 Alexander Bokovoy <ab@altlinux.ru> 2.2.23-alt1
- 2.2.23

* Thu Dec 11 2003 Alexander Bokovoy <ab@altlinux.ru> 2.2.21-alt1
- 2.2.21

* Thu Aug 21 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt2
- Explicitly use old libtool for build.
- Fixed -devel packaging.

* Tue May 20 2003 Alexander Bokovoy <ab@altlinux.ru> 2.2.4-alt1
- 2.2.4, changed maintainer
- Updated buildrequires
- Fixed mess with static libraries

* Fri Dec 27 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.11-alt1
- 2.0.11
- Added buildrequires

* Wed Apr 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.5-alt0.1cvs
- 2.0.5

* Wed Dec 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt2
- Rebuild with new kernel

* Wed Nov 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt1
- First build for Sisyphus

* Sat Sep 29 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.3-1mdk
- 1.1.3.

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.2-2mdk
- Fix provides.

* Fri Sep  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1.2-1mdk
- Rework the .spec.
- Make libs in subpackage.
- 1.1.2.

* Wed May  2 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-1mdk
- First attempt.

# end of file



