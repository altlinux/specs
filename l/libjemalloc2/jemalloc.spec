%define title jemalloc
%define sorev 2

%def_with check

Name: libjemalloc2
Version: 5.3.0
Release: alt1.1
Summary: A general-purpose scalable concurrent malloc(3) implementation
Group: System/Libraries
License: BSD
Url: http://jemalloc.net/
VCS: https://github.com/jemalloc/jemalloc

Source: %name-%version.tar
Patch: %name-%version-alt.patch

# Automatically added by buildreq on Mon May 14 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libstdc++-devel python-base
BuildRequires: gcc-c++
BuildRequires: xsltproc docbook-style-xsl

%if_with check
BuildRequires: /proc
%endif

%description
jemalloc is a general-purpose scalable concurrent malloc(3)
implementation. There are several divergent versions of jemalloc in
active use, including:

 * FreeBSD's default system allocator (malloc.c, manual page). This was
    the first public use of jemalloc, and it is still author-maintained.
 * NetBSD's default system allocator (jemalloc.c).
 * Mozilla Firefox's allocator (source code), specifically for
   Microsoft Windows-related platforms, Solaris, and Linux. There is
   Apple Mac OS X support code as well, but it has never been used in a
   release.
 * The stand-alone jemalloc, which currently targets only Linux.
   Thus far I have had no driving need to integrate support for other
   operating systems into this version of jemalloc, but it is probable
   that the stand-alone jemalloc library's platform support will
    broaden over time.

%package -n libjemalloc-tools
Summary: Shell wrapper  for preloading %title
Group: System/Libraries
License: BSD
Requires: %name = %EVR

%description -n libjemalloc-tools
Starting up wrapper for use %title.

%package -n libjemalloc-devel
Summary: Development files of %title
Group: System/Libraries
License: BSD

%description -n libjemalloc-devel
Development files of %title

%prep
%setup
%autopatch -p1

%build
%autoreconf

%configure \
    --with-version='%version-0-g0' \
    --with-xslroot=/usr/share/xml/docbook/xsl-stylesheets \
%ifarch %e2k
    --with-lg-quantum=4 \
%endif
    %nil

%make_build
%make doc

%install
%makeinstall_std

mv %buildroot%_defaultdocdir/jemalloc{,%sorev}

# add so.2 -> so.2.0
mv %buildroot%_libdir/libjemalloc.so.%sorev{,.0}
ln -s libjemalloc.so.%sorev.0 %buildroot%_libdir/libjemalloc.so.%sorev

rm -r %buildroot%_libdir/*.a

%check
%make_build VERBOSE=1 check

%files
%doc %_defaultdocdir/jemalloc2
%doc COPYING README TUNING* VERSION
%_libdir/libjemalloc.so.%sorev
%_libdir/libjemalloc.so.%sorev.0

%files -n libjemalloc-tools
%_bindir/jemalloc.sh

%files -n libjemalloc-devel
%_bindir/*prof
%_includedir/*
%_man3dir/*
%_libdir/libjemalloc.so
%_bindir/*config
%_pkgconfigdir/*.pc

%changelog
* Thu Dec 01 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 5.3.0-alt1.1
- Fixed build for Elbrus

* Wed Oct 12 2022 Stanislav Levin <slev@altlinux.org> 5.3.0-alt1
- 5.2.1 -> 5.3.0.

* Wed Jun 02 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.1-alt1
- Updated to upstream version 5.2.1

* Mon Dec 07 2020 Nikita Ermakov <arei@altlinux.org> 5.2.0-alt2
- Remove the not needed google-perftools requirement in libjemalloc-devel.

* Thu Jul 04 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.0-alt1
- Updated to upstream version 5.2.0

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 5.1.0-alt4
- shell wrapper with LD_PRELOAD moved to package libjemalloc-tools to avoid files
  conflict with previouis libjemalloc build

* Sun Aug 26 2018 Vitaly Lipatov <lav@altlinux.ru> 5.1.0-alt3
- fix soname, fix libname for libjemalloc with prof and stats (ALT bug 31642)
- fix duplicated files
- disable static by default

* Fri Aug 24 2018 Fr. Br. George <george@altlinux.ru> 5.1.0-alt2
- Fix file conflict with libjemalloc1

* Mon May 14 2018 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Grand major version change

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 3.6.0-alt1
- Autobuild version bump to 3.6.0

* Thu Feb 20 2014 Fr. Br. George <george@altlinux.ru> 3.5.0-alt1
- Autobuild version bump to 3.5.0
- Hack out "restrict" keywords (GCC doesn't compile this)

* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 3.4.1-alt1
- Autobuild version bump to 3.4.1

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 3.4.0-alt1
- Autobuild version bump to 3.4.0

* Sun Mar 31 2013 Fr. Br. George <george@altlinux.ru> 3.3.1-alt1
- Autobuild version bump to 3.3.1

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 3.3.0-alt1
- Autobuild version bump to 3.3.0

* Mon Nov 12 2012 Fr. Br. George <george@altlinux.ru> 3.2.0-alt1
- Autobuild version bump to 3.2.0

* Mon Oct 22 2012 Fr. Br. George <george@altlinux.ru> 3.1.0-alt1
- Autobuild version bump to 3.1.0
- Shellcript added

* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 3.0.0-alt1
- Autobuild version bump to 3.0.0

* Tue Jan 10 2012 Fr. Br. George <george@altlinux.ru> 2.2.5-alt1
- Autobuild version bump to 2.2.5
- Documentation rebuilding added

* Wed Sep 07 2011 Fr. Br. George <george@altlinux.ru> 2.2.3-alt1
- Autobuild version bump to 2.2.3

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.2.2-alt1
- Autobuild version bump to 2.2.2

* Tue May 03 2011 Fr. Br. George <george@altlinux.ru> 2.2.1-alt1
- Autobuild version bump to 2.2.1

* Thu Mar 31 2011 Fr. Br. George <george@altlinux.ru> 2.2.0-alt1
- Autobuild version bump to 2.2.0

* Thu Mar 10 2011 Fr. Br. George <george@altlinux.ru> 2.1.2-alt1
- Autobuild version bump to 2.1.2

* Tue Feb 22 2011 Fr. Br. George <george@altlinux.ru> 2.1.1-alt1
- Autobuild version bump to 2.1.1

* Mon Dec 20 2010 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Autobuild version bump to 2.1.0

* Sun Nov 14 2010 Fr. Br. George <george@altlinux.ru> 2.0.1-alt1
- Autobuild version bump to 2.0.1

* Thu Oct 28 2010 Fr. Br. George <george@altlinux.ru> 2.0.0-alt1
- Autobuild version bump to 2.0.0

* Wed Aug 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up

* Wed May 19 2010 Fr. Br. George <george@altlinux.ru> 1.0.2-alt1
- Version up

* Wed Apr 21 2010 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Version up

* Wed Apr 14 2010 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

