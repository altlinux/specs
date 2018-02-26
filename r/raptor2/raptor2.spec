
Name: raptor2
Version: 2.0.7
Release: alt1

Group: Development/Other
Summary: RDF Parser Toolkit for Redland
Url: http://librdf.org/raptor/
License: GPLv2+ or LGPLv2+ or ASL 2.0

# /usr/bin/rapper
Conflicts: raptor

Source: http://download.librdf.org/source/raptor2-%version.tar.gz
# FC
Patch50: raptor2-2.0.3-raptor2_doc.patch

# Automatically added by buildreq on Thu Sep 01 2011 (-bi)
# optimized out: elfutils libxml2-devel pkg-config
#BuildRequires: flex glibc-devel-static gtk-doc libcurl-devel libexpat-devel libxslt-devel libyajl-devel
BuildRequires: flex glibc-devel gtk-doc libcurl-devel libexpat-devel libxslt-devel libyajl-devel libxml2-devel

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package -n libraptor2
Summary: %name core library
Group: System/Libraries
%description -n libraptor2
%name core library.

%package devel
Group: Development/Other
Summary: Development files for %name
%description devel
%summary.

%prep
%setup

#%patch50 -p1 -b .raptor2_doc

# hack to nuke rpaths
%if "%_libdir" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%_lib %_libdir|' configure
%endif


%build
%configure \
    --disable-static \
    --enable-release
%make_build


%install
%make DESTDIR=%buildroot install


%files
%_bindir/rapper
%_man1dir/rapper*

%files -n libraptor2
%doc AUTHORS ChangeLog NEWS README
%doc COPYING* LICENSE*.txt
%_libdir/libraptor2.so.*

%files devel
%doc UPGRADING.html
%doc %_datadir/gtk-doc/html/raptor2/
%_includedir/raptor2/
%_libdir/libraptor2.so
%_libdir/pkgconfig/raptor2.pc
%_man3dir/libraptor2*


%changelog
* Thu May 24 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.7-alt1
- new version

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.4-alt0.M60P.1
- built for M60P

* Thu Sep 01 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.4-alt1
- initial build
