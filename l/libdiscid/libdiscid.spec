Name: libdiscid
Version: 0.2.2
Release: alt1

Summary: Library for creating MusicBrainz DiscIDs from audio CDs
License: LGPLv2+
Group: System/Libraries
Url: http://musicbrainz.org/doc/libdiscid
Source: http://users.musicbrainz.org/~matt/%name-%version.tar.gz
%def_disable static

%description
libdiscid is a C library for creating MusicBrainz DiscIDs from audio
CDs. It reads a CD's table of contents (TOC) and generates an identifier
which can be used to lookup the CD at MusicBrainz. Additionally, it
provides a submission URL for adding the DiscID to the database.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name.

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
%doc AUTHORS README ChangeLog

%files devel
%_libdir/*.so
%_includedir/discid
%_pkgconfigdir/*

%if_enabled static
%files -n %name-devel-static
%_libdir/%name.a
%endif

%changelog
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

