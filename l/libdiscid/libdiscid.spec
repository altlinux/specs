%def_disable static

Name: libdiscid
Version: 0.6.2
Release: alt1

Summary: A Library for creating MusicBrainz DiscIDs
Group: System/Libraries
License: LGPLv2+

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
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

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
%_libdir/*.so.*
%doc AUTHORS ChangeLog README

%files devel
%_includedir/discid/
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files -n %name-devel-static
%_libdir/%name.a
%endif


%changelog
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

