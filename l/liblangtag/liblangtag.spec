Name: liblangtag
Version: 0.6.2
Release: alt1
Summary: An interface library to access tags for identifying languages

Group: System/Libraries
License: (LGPLv3+ or MPLv2.0) and UCD
Url: http://tagoh.bitbucket.org/liblangtag/
Source0: https://bitbucket.org/tagoh/%name/downloads/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Jul 28 2013
# optimized out: gnu-config pkg-config
BuildRequires: gtk-doc libxml2-devel

BuildRequires: glib2-devel

%description
%name is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%{?_isa} = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%configure --disable-static --enable-shared --disable-introspection
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build V=1 \
    LD_LIBRARY_PATH=`pwd`/liblangtag/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

%check
LD_LIBRARY_PATH=`pwd`/liblangtag/.libs make check

%install
make install DESTDIR=%buildroot

%files
%doc AUTHORS COPYING NEWS README
%_libdir/%name.so.*
%_libdir/%name/*.so
%_datadir/%name

%files devel
%doc COPYING
%_includedir/%name
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_datadir/gtk-doc/html/%name

%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.6.2-alt1
- Autobuild version bump to 0.6.2

* Wed Apr 13 2016 Fr. Br. George <george@altlinux.ru> 0.6.0-alt1
- Autobuild version bump to 0.6.0
- Provide "check" section

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 0.5.8-alt1
- Autobuild version bump to 0.5.8

* Tue Jul 14 2015 Fr. Br. George <george@altlinux.ru> 0.5.7-alt1
- Autobuild version bump to 0.5.7

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.5.6-alt1
- Autobuild version bump to 0.5.6

* Mon Jun 09 2014 Fr. Br. George <george@altlinux.ru> 0.5.4-alt1
- Autobuild version bump to 0.5.4

* Wed Apr 09 2014 Fr. Br. George <george@altlinux.ru> 0.5.3-alt1
- Autobuild version bump to 0.5.3

* Thu Oct 17 2013 Fr. Br. George <george@altlinux.ru> 0.5.2-alt2
- Override fcimport release

* Mon Oct 14 2013 Fr. Br. George <george@altlinux.ru> 0.5.2-alt1
- Autobuild version bump to 0.5.2

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_1
- update to new release by fcimport

* Sun Jul 28 2013 Fr. Br. George <george@altlinux.ru> 0.5.1-alt1
- Initial build from FC git

* Thu May 16 2013 Eike Rathke <erack@redhat.com> - 0.5.1-2-UNBUILT
- updated .spec with MPLv2.0 and UCD licenses

* Tue Apr 30 2013 David Tardon <dtardon@redhat.com> - 0.5.1-1
- fix ABI breakage

* Mon Apr 29 2013 David Tardon <dtardon@redhat.com> - 0.5.0-1
- new release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Dec 01 2012 David Tardon <dtardon@redhat.com> - 0.4.0-2
- fix build on ppc

* Sun Nov 25 2012 David Tardon <dtardon@redhat.com> - 0.4.0-1
- new upstream release

* Sun Sep 09 2012 David Tardon <dtardon@redhat.com> - 0.3-1
- initial import
