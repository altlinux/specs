%define origname LabCurves
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: labcurves
Version: 20100709
Release: alt4.1

Summary: L*a*b curves for GIMP
License: %gpl3only
Group: Graphics

Url: http://www.mm-log.com/lab-curves-gimp
Packager: Yuriy Al. Shirokov <yushi@altlinux.org>

#Original source in 7z format: http://sourceforge.net/projects/mmfilters/files/LabCurves/2010-07-09/LabCurves-src-20100709.7z
Source: %origname.tar
Patch0: labcurves-alt-bindir.patch

%package -n gimp-plugin-labcurves
Summary: GIMP plugin for curves in L*a*b
Group: Graphics
Requires: gimp
Requires: %name = %version-%release

BuildPreReq: rpm-build-licenses
# Automatically added by buildreq on Sat Nov 06 2010
BuildRequires: gcc-c++ libGraphicsMagick-c++-devel libexiv2-devel libgimp-devel libgomp-devel liblcms2-devel libqt4-devel


%description
LabCurves is a small program, which allows to use se curves on the
L*a*b* color channels of the given image. The internal computation is
done with 16 bit, while input and output are 8 bit. Together with a
small wrapper script it can be seemlessly used from GIMP.

%description -n gimp-plugin-labcurves
LabCurves is a small program, which allows to use se curves on the
L*a*b* color channels of the given image. The internal computation is
done with 16 bit, while input and output are 8 bit. Together with a
small wrapper script it can be seemlessly used from GIMP.

This package contains GIMP wrapper script for LabCurves.

%prep
%setup -n %origname
%patch0 -p0

%build
qmake-qt4 -after \"QMAKE_CC=/usr/bin/gcc QMAKE_CXX=/usr/bin/g++\"
%make

%install
install -D -m755 LabCurves %buildroot/%_bindir/LabCurves
install -D -m755 mm\ extern\ LabCurves.py %buildroot/%gimpplugindir/plug-ins/mm_extern_LabCurves.py

%files
%_bindir/*

%files -n gimp-plugin-labcurves
%gimpplugindir/plug-ins/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20100709-alt4.1
- Rebuild with Python-2.7

* Tue Nov 09 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 20100709-alt4
- no need for ccache patch now

* Sun Nov 07 2010 Yuiry Al. Shirokov <yushi@altlinux.org> 20100709-alt3
- ccache removed from QMake file

* Sun Nov 07 2010 Yuiry Al. Shirokov <yushi@altlinux.org> 20100709-alt2
- spec cleanup

* Sun Sep 19 2010 Yuriy Al. Shirokov <yushi@altlinux.org> 20100709-alt1
- initial build for ALT Linux Sisyphus
