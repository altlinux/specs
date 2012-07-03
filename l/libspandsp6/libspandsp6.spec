%def_without v17

# soname changed, conflicts don't needed
%define oldconflict() \
Conflicts: libspandsp-%1 < %version-%release \
Conflicts: libspandsp-%1 > %version-%release \
Conflicts: libspandsp3-%1 \
Conflicts: libspandsp4-%1 \
Conflicts: libspandsp5-%1 \
%nil

Name: libspandsp6
Summary: DSP library for VoIP, FAX and T.38 support
Version: 0.0.6
Release: alt0.19.1
License: LGPL
Group: System/Libraries

Url: http://soft-switch.org/downloads/spandsp/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: spandsp.tar

BuildRequires: doxygen libaudiofile-devel libtiff-devel libxml2-devel xsltproc docbook-style-xsl

%description
%summary

%package devel
Summary: %summary
Group: Development/C
Requires: %name = %version-%release
Provides: libspandsp-devel = %version-%release

%oldconflict devel

%description devel
%summary

%package docs
Summary: %summary
Group: Development/Documentation
BuildArch: noarch

%oldconflict docs

%description docs
%summary

%prep
%setup -c

%build
# if this enabled, it _must_ be enabled in all binaries built with this lib
%if_with v17
export CCFLAGS=-DENABLE_V17
export CPPFLAGS=-DENABLE_V17
%endif
%autoreconf
%configure --enable-doc \
%ifarch %ix86 x86_64
	--enable-sse2 \
%endif
	--enable-shared \
	--disable-static
make

%install
%makeinstall_std

mkdir -p %buildroot%_docdir/%name/api
cp -a doc/api/html/* %buildroot%_docdir/%name/api/
cp -a doc/t38_manual %buildroot%_docdir/%name/t38_manual

%files
%_libdir/libspandsp.so.2
%_libdir/libspandsp.so.2.0.0

%files docs
%_docdir/%name

%files devel
%_libdir/libspandsp.so
%_includedir/spandsp
%_includedir/spandsp.h
%_pkgconfigdir/spandsp.pc

%changelog
* Fri Feb 03 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.6-alt0.19.1
- 0.0.6-pre19

* Sat Aug 06 2011 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.17.2
- rebuild

* Thu Dec  9 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.6-alt0.17.1
- updated to spandsp snapshot 20100831

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.7
- auto rebuild

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.6
- auto rebuild

* Mon Oct 11 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.5
- auto rebuild

* Wed Jul 29 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.4
- really fix conflicts

* Sat Jul 25 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.3
- fix conflicts to older libspandsp versions
- remove symbol versioing (sbolshakov@)

* Thu Jul 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.12.2
- rebuild

* Sat Jul 04 2009 Eugene Prokopiev <enp@altlinux.ru> 0.0.6-alt0.12.1
- updated to 0.0.6-pre12

* Thu Feb 12 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.3.2
- spec cleanup

* Thu Feb 12 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt0.3.1
- rename to libspandsp6

* Sun Jan 18 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.6-alt0.3
- updated to 0.0.6-pre3

* Sat Dec 13 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt3.pre4
- build %name-docs as noarch
- cleanup specfile

* Fri Aug 22 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt2.pre4
- update to 0.0.5-pre4

* Mon Jul 21 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1.20080718
- update to 20080718
- change license to LGPL (upstream)
- change name to libspandsp5

* Tue Apr 15 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20080402
- update to 20080402

* Sun Mar 30 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20080318
- update to 20080318
- package T.38 docs

* Thu Mar 06 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20080110
- update to 20080110

* Thu Dec 27 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20071214
- update to 20071214

* Wed Oct 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20071014
- update to 20071014

* Fri Sep 28 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20070802
- update to 20070802

* Sun Jul 08 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20070708
- update to 20070708

* Mon Jun 11 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20070608
- update to 20070608
- make libspandsp4-devel provides more nice for upgrading

* Mon May 14 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1.20070513
- update to 0.0.4

* Fri Apr 27 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.3pre28.2007.04.05-alt1
- version update

* Mon Feb 19 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.3pre27.2007.01.23-alt1
- version update, add symbol versioning

* Thu Jan 11 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.3pre27-alt1
- version update

* Tue Oct 24 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.3pre24-alt1
- version update

* Wed Sep 06 2006 Denis Smirnov <mithraen@altlinux.ru> 0.0.3pre22-alt1.svn20060903
- first build for Sisyphus
- T.38 support
