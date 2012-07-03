%define _unpackaged_files_terminate_build 1
%def_disable backport
%def_with qt
%define truename gle-graphics
Name: gle
Version: 4.2.2
Release: alt2
Summary: GLE - Graphics language that produces ps/eps/pdf/png/jpg ouput
Summary(ru_RU.CP1251): GLE - язык создания изображений. Вывод в ps/eps/pdf/png/jpg
Copyright: GPL
Group: Graphics
Packager: Igor Vlasenko <viy@altlinux.org>
URL: http://glx.sourceforge.net/
Source: http://dl.sourceforge.net/glx/%{truename}-%{version}f-src.tar.gz
Source2:gle.el
Source3:http://dl.sourceforge.net/glx/gle-graphics-extrafonts-1.0.tar.gz
Source7:http://glx.sourceforge.net/download/bbox_gle.sh
Source8:http://glx.sourceforge.net/download/makeani.pl
# moved to gle-doc
#Source4:http://dl.sourceforge.net/glx/gle-manual-%version.pdf
#Source5:http://dl.sourceforge.net/glx/GLEusersguide.pdf

Patch: gle-graphics-4.2.2f-alt-autoconf.patch

# Automatically added by buildreq on Thu Sep 21 2006
BuildRequires: gcc-c++ libjpeg-devel libncurses-devel libtiff-devel libpng-devel libcairo-devel
#BuildRequires: xorg-x11-devel xorg-x11-libs gcc-c++  libstdc++-devel libtiff-devel unzip zlib-devel libjpeg-devel libncurses-devel

BuildRequires: /proc
# tmp hack
BuildRequires: dos2unix

#BuildNotRequires: fontconfig qt4-settings 
BuildRequires: imake libXt-devel xorg-cf-files
%if_with qt
BuildRequires: libqt4-devel
%endif

%description
GLE is a graphics language that produces postscript, EPS, PDF, PNG, or JPG ouput from a simple script file. The GLE scripting language is full featured with variables, subroutines, logic control, looping, and graphing tools. It is great for plotting and charting data.

GLE can create very complex output with text and graphics (including graphs and charts) from a simple plain text file.

GLE is a full featured programing language that includes variables, subroutines, logic control, looping, a graphing tool, and more to produce high quality postscript output. It has a full range of facilities for producing publication-quality graphs, diagrams, posters and slides. GLE provides LaTeX quality fonts together with a flexible graphics module which allows the user to specify any feature of a graph (down to the line width of the subticks, for example). Complex pictures can be drawn with user-defined subroutines and simple looping structures. Essentially, GLE is a programming language and if you are used to writing software, using LaTeX, or any other non-WYSIWYG tools, then you will enjoy using GLE.

%if_with qt
%package qt
Summary: QT GUI tool for GLE Graphics language
Requires: %name = %version-%release
Requires: ghostscript-lib
Group: Graphics

%description qt
GLE is a graphics language that produces postscript, EPS, PDF, PNG, or JPG ouput from a simple script file. The GLE scripting language is full featured with variables, subroutines, logic control, looping, and graphing tools. It is great for plotting and charting data.

GLE can create very complex output with text and graphics (including graphs and charts) from a simple plain text file.

This package contains QGLE - A Graphical Interface to GLE.
%endif

%prep

%setup -q -n %{truename}-%{version} -a3
%patch

%build
%autoreconf -fisv
%configure --with-manip \
	--with-x \
	--with-qt=%{_libdir}/qt4 \
	--with-rpath=no \
	--with-jpeg=yes --with-png=yes --with-tiff=yes --with-z=yes \
	--with-extrafonts

#  --with-scripts          install scripts instead of executables (yes/no)
#  --with-libgle           build libgle (yes/no/static/both)
#  --with-extrafonts       include additional fonts (or yes/no)

#%make_build # parallel build fails
make

%install
#make -f Makefile.gcc GLE_RPM_ROOT=$RPM_BUILD_ROOT install
%make_install install DESTDIR=%buildroot

install -m 755 %{SOURCE7} $RPM_BUILD_ROOT/%_bindir/bbox_gle
# hack: to report upstream
dos2unix $RPM_BUILD_ROOT/%_bindir/bbox_gle
cp %{SOURCE8} .

mkdir -p $RPM_BUILD_ROOT/%_emacslispdir
mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d
cp contrib/editors/highlighting/gle-emacs.el $RPM_BUILD_ROOT/%_emacslispdir/
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/emacs/site-start.d/

%if_with qt
mkdir -p $RPM_BUILD_ROOT/%_desktopdir
install -m644 platform/autopackage/gle.desktop $RPM_BUILD_ROOT/%_desktopdir/
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
install -m644 platform/autopackage/gle.png $RPM_BUILD_ROOT/%_liconsdir/
%endif

%files
%doc README.txt contrib/editors/highlighting/gle.nedit
%doc makeani.pl
%_bindir/gle
%_bindir/manip
%_bindir/bbox_gle
%dir %_datadir/gle-graphics/%{version}
%_datadir/gle-graphics/%{version}/*
%_emacslispdir/*
/etc/emacs/site-start.d/*
%_libdir/libgle-graphics*.so
# devel subpackage? who requires?
%exclude %_pkgconfigdir/gle-graphics.pc
%_man1dir/gle.1.gz

%if_with qt
%files qt
%_bindir/qgle
%_liconsdir/gle.png
%_desktopdir/gle.desktop
%endif

%changelog 
* Fri Feb 12 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt2
- fixed inittex.ini genaeraion
- added lbcairo-devel

* Thu Feb 11 2010 Igor Vlasenko <viy@altlinux.org> 4.2.2-alt0.M51.2
- backport

* Thu Feb 11 2010 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1
- new version

* Fri May 08 2009 Igor Vlasenko <viy@altlinux.ru> 4.2.0-alt1
- new version

* Wed Nov 19 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2.beta.1
- NMU (by repocop): the following fixes applied:
 * update_menus for gle-qt
 * desktop-mime-entry for gle-qt

* Wed Sep 17 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt2.beta
- fixed bbox_gle script

* Sun Aug 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1.beta
- new version

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt3.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for gle-qt

* Thu Feb 07 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt3
- removed -rpath

* Wed Jan 09 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt2
- added .desktop file; added requires on ghostscript-lib

* Tue Jan 08 2008 Igor Vlasenko <viy@altlinux.ru> 4.1.1-alt1
- new version

* Mon Oct 23 2006 Igor Vlasenko <viy@altlinux.ru> 4.0.12-alt3
- built def_without qt due to compilation problems in fresh Sisyphus

* Fri Sep 22 2006 Igor Vlasenko <viy@altlinux.ru> 4.0.12-alt2
- fixed spec for x86_64

* Mon Sep 18 2006 Igor Vlasenko <viy@altlinux.ru> 4.0.12-alt1
- new version
- fixed Group to Graphics

* Mon May 15 2006 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt3
- C++ fixes for gcc 4

* Mon Dec 26 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt2
- added /usr/lib/gle (thanks to Vitaliy Lipatov)
- split gle and gle-doc. 
  gle-doc is updated less frequent and asynchronically with gle,
  so this split will considerably reduce gle traffic.

* Fri Dec 23 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1
- new version

* Mon Nov 21 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.10-alt2
- gle-manual updated

* Wed Nov 16 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.10-alt1
- new version

* Tue Sep 27 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.9-alt2
- utils moved from _datadir to _libdir

* Fri Aug 26 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.9-alt1
- new version

* Tue Jun 23 2005 Igor Vlasenko <viy@altlinux.ru> 4.0.8-alt0.1
- first build for Sisyphus
