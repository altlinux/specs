%define bordersversion 0.0.2

Name: photoprint
Version: 0.4.1
Release: alt3

Summary: Photo Print - Prints photos in various layouts and with color management
License: GPLv2+
Group: Publishing

Url: http://blackfiveimaging.co.uk/index.php?article=02Software/01PhotoPrint
# In fact version is 0.4.1b, as 0.4.1 turn out to contain major bug (but I prefer to package as just 0.4.1)
Source: http://www.blackfiveimaging.co.uk/photoprint/photoprint-%{version}b.tar.gz
Source1: http://www.blackfiveservices.co.uk/PhotoPrint/Downloads/photoprint-borders-%{bordersversion}.tar.gz
#Source2: http://www.blackfiveservices.co.uk/PhotoPrint/Downloads/ProfilingKit.tar.bz2
Source10: fotoprint16.png
Source11: fotoprint32.png

Patch0: photoprint-fix-autoconf.patch
Patch1: photoprint-0.4.1b-glib.patch
Patch2: photoprint-0.4.2_pre2-cups-automagic.patch
Patch3: photoprint-0.4.2_pre2-underlinking.patch
Patch4: photoprint-0.4.2_pre2-tests.patch

# Automatically added by buildreq on Tue Mar 09 2010
BuildRequires: gcc-c++ libcups-devel libgutenprint-devel libjpeg-devel liblcms-devel libnetpbm-devel libtiff-devel

%description
Photo Print is a utility for printing images via Gutenprint.

It supports different printing layouts, as one picture per page, several
pictures (scaled to equal size) per page, a poster of one picture put together
of several sheets, or several pictures combined to one round picture for a CD
back. Image frames and color management are also supported.

Photo Print can be used as GUI tool and also as command line tool in batch
mode.

%prep

%setup -n photoprint-%{version}b -a 1
#setup -n photoprint-%version -T -D -a 1
#%setup -q -T -D -a 2 -n %{name}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
gettextize -f
%autoreconf
%configure
# Do not do any compiler optimizations, they break the program. (?? recheck!)
%make_build CFLAGS="" CXXFLAGS="-I%_includedir/lcms"
make -C po ru.gmo

%install
%makeinstall_std
install -pD -m644 photoprint.1 %buildroot%_man1dir/photoprint.1
install -pD -m644 %_sourcedir/fotoprint16.png %buildroot%_miconsdir/fotoprint.png
install -pD -m644 %_sourcedir/fotoprint32.png %buildroot%_niconsdir/fotoprint.png

# install borders (TODO: move to separate noarch package)
install -d %buildroot%_datadir/photoprint/borders
pushd photoprint-borders*
%configure
%makeinstall_std
popd

%find_lang --with-gnome %name

%files -f %name.lang
%doc README NEWS
%_bindir/*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_man1dir/*
%_desktopdir/*
%_datadir/photoprint

%changelog
* Sat Jun 16 2012 Michael Shigorin <mike@altlinux.org> 0.4.1-alt3
- NMU:
- rebuilt against gutenprint 5.2.8
- fixed FTBFS with recent binutils
  + applied gentoo patches and a debian patch
  + autoreconf

* Fri Apr 06 2012 Victor Forsiuk <force@altlinux.org> 0.4.1-alt2
- Fix glib include compile problem.

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 0.4.1-alt1
- 0.4.1

* Tue Jun 30 2009 Victor Forsyuk <force@altlinux.org> 0.4.0-alt1
- 0.4.0
- Fix FTBFS due to missing stdio header includes.

* Mon Jan 05 2009 Victor Forsyuk <force@altlinux.org> 0.4.0-alt0.pre4
- 0.4.0-pre4

* Wed Oct 08 2008 Victor Forsyuk <force@altlinux.org> 0.3.9-alt1
- 0.3.9

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 0.3.8b-alt1
- 0.3.8b

* Fri Apr 11 2008 Victor Forsyuk <force@altlinux.org> 0.3.7-alt1
- 0.3.7
- Desktop file mime entry fix.

* Fri Dec 28 2007 Victor Forsyuk <force@altlinux.org> 0.3.6-alt1
- Initial build.
