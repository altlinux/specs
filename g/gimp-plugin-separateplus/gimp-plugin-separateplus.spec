%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-plugin-separateplus
Version: 0.5.8
Release: alt1
Epoch: 1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Improved version of the CMYK Separation plug-in for The GIMP
License: GPLv2+
Group: Graphics

Url: http://cue.yellowmagic.info/softwares/separate.html
Source: http://osdn.dl.sourceforge.jp/separate-plus/47873/separate+-%version.zip

# Automatically added by buildreq on Wed Dec 23 2009
BuildRequires: libgimp-devel libjpeg-devel liblcms-devel libtiff-devel unzip

Requires: gimp

%description
One thing preventing The GIMP from being useful in a pre-press environment is
the lack of support for the CMYK colour-space. This plug-in goes some small
way towards rectifying the situation, using a trick with layers to fake CMYK
support.

%prep
%setup -n separate+-%version

%build
%make_build

%install
install -d %buildroot%gimpplugindir/plug-ins/
install -d %buildroot%gimpdatadir/scripts/
install -p -m644 sample-scripts/* %buildroot%gimpdatadir/scripts/

%make_install install \
	INSTALLDIR=%buildroot%gimpplugindir/plug-ins/ \
	LOCALEDIR=%buildroot%_datadir/locale

%find_lang gimp20-separate

%files -f gimp20-separate.lang
%gimpplugindir/plug-ins/*
%gimpdatadir/scripts/*
%doc README*

%changelog
* Thu Nov 25 2010 Victor Forsiuk <force@altlinux.org> 1:0.5.8-alt1
- 0.5.8

* Wed May 26 2010 Victor Forsiuk <force@altlinux.org> 1:0.5.7-alt1
- 0.5.7

* Tue Mar 09 2010 Victor Forsiuk <force@altlinux.org> 1:0.5.6-alt1
- 0.5.6

* Wed Dec 23 2009 Victor Forsyuk <force@altlinux.org> 1:0.5.5-alt1
- 0.5.5

* Fri Nov 13 2009 Victor Forsyuk <force@altlinux.org> 1:0.5.4-alt1
- 0.5.4

* Fri Nov 21 2008 Victor Forsyuk <force@altlinux.org> 1:0.5.3-alt3
- Update russian .po (fix ALT#17714).

* Tue Oct 07 2008 Victor Forsyuk <force@altlinux.org> 1:0.5.3-alt2
- Fix build with rpm that unzip sources without lowercasing filenames.

* Wed Sep 24 2008 Victor Forsyuk <force@altlinux.org> 1:0.5.3-alt1
- 0.5.3
- Package icc_colorspace.

* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 1:0.5.2-alt1
- 0.5.2

* Wed Jul 30 2008 Victor Forsyuk <force@altlinux.org> 1:0.5.1-alt1
- 0.5.1

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 20070727-alt2
- Build for gimp >= 2.3.

* Wed Sep 05 2007 Victor Forsyuk <force@altlinux.org> 20070727-alt1
- Update to 20070727 date version.

* Mon Jul 16 2007 Victor Forsyuk <force@altlinux.org> 20070709-alt1
- Initial build.
