Name: graveman
%define fver 0.3.12-5
Version: 0.3.12.5
Release: alt3

Packager: Victor Forsyuk <force@altlinux.org>

Summary: A frontend for cdrtools, dvd+rw-tools and sox
License: GPLv2+
Group: Archiving/Cd burning

URL: http://graveman.tuxfamily.org
Source: %url/sources/%name-%fver.tar.bz2
Source1: graveman.desktop

# Automatically added by buildreq on Mon Jan 19 2009
BuildRequires: libflac-devel libglade-devel libid3tag-devel libjpeg-devel libmad-devel libmng-devel libvorbis-devel perl-XML-Parser

Requires: cdrecord, cdrdao, mkisofs, sox, dvd+rw-tools, flac

%description
Graveman! provides a graphical user interface for handling common CD/DVD
burning tasks. It can burn Audio CDs, Data CDs and DVDs, duplicate CDs,
and clean rewritable CD/DVD media.

%prep
%setup -n %name-%fver
install -pm644 %SOURCE1 desktop/graveman.desktop.in

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot
install -pD -m644 pixmaps/graveman32.png %buildroot%_niconsdir/graveman.png
install -pD -m644 pixmaps/graveman48.png %buildroot%_liconsdir/graveman.png

pushd %buildroot%_pixmapsdir
mv graveman48.png graveman.png
popd

# no, thanx :)
rm -rf %buildroot%_mandir/{fr,nl}/

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/graveman
%_desktopdir/*
%_pixmapsdir/*
%_niconsdir/*
%_liconsdir/*
%_man1dir/*

%changelog
* Mon Jan 19 2009 Victor Forsyuk <force@altlinux.org> 0.3.12.5-alt3
- Remove obsolete install time scripts.

* Fri Apr 11 2008 Victor Forsyuk <force@altlinux.org> 0.3.12.5-alt2
- Fix bugs spotted by repocop.

* Sat Apr 21 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.12.5-alt1.0
- Rebuilt due to libFLAC.so.7 -> libFLAC.so.8 soname change.

* Wed Jun 07 2006 Victor Forsyuk <force@altlinux.ru> 0.3.12.5-alt1
- 0.3.12-5

* Tue Nov 08 2005 Victor Forsyuk <force@altlinux.ru> 0.3.12.4-alt1
- Initial build.
