%def_disable static
%def_disable gtk_doc

Name: raptor
Version: 1.4.21
Release: alt3

Summary: Raptor RDF Parser Toolkit for Redland
License: LGPLv2+ or ASL 2.0
Group: Development/Other
Url: http://librdf.org/raptor/

Source: http://download.librdf.org/source/%name-%version.tar.gz
Patch: raptor-alt-curl.patch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
Requires: lib%name = %version-%release

# Automatically added by buildreq on Tue Jan 04 2005
BuildRequires: flex gcc-c++ libcurl-devel libexpat-devel libssl-devel libstdc++-devel libxml2-devel zlib-devel gtk-doc

BuildPreReq: chrpath

%description
Raptor is the RDF Parser Toolkit for Redland that provides a set of
standalone RDF parsers, generating triples from RDF/XML or N-Triples.

%package -n lib%name
Summary: Dynamic libraries from %name
Group: System/Libraries

%description -n lib%name
Dynamic libraries from %name.

%package -n lib%name-devel
Summary: Header files and static libraries from %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Libraries and includes files for developing programs based on %name.

%package -n lib%name-devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
Documentation needed for developing programs based on %name.


%prep
%setup

%patch0 -p2

%build
export PATH=`pwd`:$PATH
%configure \
    %{subst_enable static} \
    %{?_enable_gtk_doc:--enable-gtk-doc}

# SMP-incompatible build
%make

%check
%make check

%install
%makeinstall

chrpath -d %buildroot%_bindir/rapper

%files
%_bindir/*
%exclude %_bindir/%name-config
%_man1dir/*
%exclude %_man1dir/%name-config*
%doc AUTHORS ChangeLog LICENSE.txt NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%_man1dir/%name-config*
%_man3dir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt3
- Fixed RPATH

* Tue Aug 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt2
- Fixed build

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt1.2
- Rebuilt for debuginfo

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.21-alt1.1
- Rebuilt for soname set-versions

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.4.21-alt1
- 1.4.21
- %%check section
- new lib%%name-devel-doc noarch subpackage

* Sun Dec 14 2008 Yuri N. Sedunov <aris@altlinux.org> 1.4.18-alt1
- new version
- fixed Url and License tags
- removed obsolete %%post{,un}_ldconfig
- don't rebuild documentation
- built all tests

* Tue Oct 23 2007 Eugene Ostapets <eostapets@altlinux.ru> 1.4.16-alt1
- new version

* Fri Mar 16 2007 Eugene Ostapets <eostapets@altlinux.ru> 1.4.14-alt1
- new version

* Mon Dec 04 2006 Eugene Ostapets <eostapets@altlinux.ru> 1.4.13-alt1
- new version

* Tue Jan 04 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.4.3-alt1
- 1.4.3

* Tue Jan 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt1
- new version.

* Sat Nov 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- new version.
- use libtool-1.4
- do not package .la files.

* Tue Feb 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.9.8-alt1
- Adopted for Sisyphus.

* Tue Feb 18 2003 Austin Acton <aacton@yorku.ca> 0.9.8-1mdk
- initial package
