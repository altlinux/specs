Name:           libaosd
Version:        0.2.7
Release:        alt3
License:        GPL v2 or later
Summary:        An Advanced On-Screen Display Library
Group:          Graphical desktop/Other
Packager:	Mykola Grechukh <gns@altlinux.org>
Url:            http://atheme.org/projects/libaosd.shtml
Source:         libaosd_%version.orig.tar.bz2
BuildRequires:  libfreetype-devel libgtk+2-devel glib2-devel

%description
Libaosd is an advanced on screen display library. It supports
many modern features like anti-aliased text and composited
rendering via XComposite, as well as support for rendering
Cairo and Pango layouts.

%package        devel
License:        GPL v2 or later
Summary:        An Advanced On-Screen Display Library
Group:          Development/C
Requires:       libaosd-text = %version-%release

%description    devel
Libaosd is an advanced on screen display library. It supports
many modern features like anti-aliased text and composited
rendering via XComposite, as well as support for rendering
Cairo and Pango layouts.

This package contains the development headers.

%package -n     aosd_cat
License:        GPL v2 or later
Summary:        On-Screen Display Tool
Group:          Graphical desktop/Other
Requires:       libaosd-text = %version-%release

%description -n aosd_cat
Aosd_cat is an advanced on-screen display tool based on
libaosd. It can be used for OSD-style notifications in
shell scripts.

%package -n     libaosd-text
License:        GPL v2 or later
Summary:        An Advanced On-Screen Display Library
Group:          Graphical desktop/Other
Requires:       %name = %version-%release

%description -n libaosd-text
libaosd is an advanced on screen display library. It supports many modern
features like anti-aliased text and composited rendering via XComposite, as
well as support for rendering Cairo and Pango layouts.

This package contains the text layout library.

%prep
%setup -q
/bin/cp aclocal.m4 acinclude.m4

%build
%autoreconf
%configure \
	--disable-static

%install
%makeinstall

%files 
%doc LICENSE
%_libdir/libaosd.so.*

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*

%files -n aosd_cat
%_bindir/aosd_cat
%_mandir/man1/aosd_cat.1.*

%files -n libaosd-text
%_libdir/libaosd-text.so.*

%changelog
* Fri Sep 23 2011 Alexey Tourbin <at@altlinux.ru> 0.2.7-alt3
- rebuilt for debuginfo
- enabled strict dependencies between subpackages

* Wed Jan 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.2.7-alt2
- updated build dependencies
- spec cleanup

* Mon Oct 04 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.7-alt1
- new version (closes: #24218)

* Tue Oct 06 2009 Nick S. Grechukh <gns@altlinux.org> 0.2.5-alt2
- Initial build for ALT Linux
