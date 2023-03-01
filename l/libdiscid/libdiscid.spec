%def_disable static
%define _name discid

Name: lib%_name
Version: 0.6.3
Release: alt1

Summary: A Library for creating MusicBrainz DiscIDs
Group: System/Libraries
License: LGPL-2.1-or-later

Url: http://musicbrainz.org/doc/%name
Source: http://ftp.musicbrainz.org/pub/musicbrainz/%name/%name-%version.tar.gz

%description
This C library %name creates MusicBrainz DiscIDs from audio CDs. It
reads the table of contents (TOC) of a CD and generates an identifier
which can be used to lookup the CD at MusicBrainz. Additionally, it
provides a submission URL for adding the DiscID to the database.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %EVR

%description devel-static
Static libs for building statically linked software that uses %name.


%prep
%setup

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS ChangeLog README

%files devel
%_includedir/%_name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%if_enabled static
%files -n %name-devel-static
%_libdir/%name.a
%endif


%changelog
* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3
- fixed License tag

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Thu Oct 23 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.
- Rebuilt for debuginfo.

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdiscid
  * postun_ldconfig for libdiscid
  * postclean-05-filetriggers for spec file

* Sun Mar 18 2007 Mikhail Yakshin <greycat@altlinux.org> 0.1.1-alt1
- Initial build for ALT Linux

