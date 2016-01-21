%define gimpplugindir %(gimptool-2.0 --gimpplugindir)
# /usr/bin/hg identify | cut -c -12
%define rev 66a8c1082d88
%def_with gimp

Name: photivo
Version: 0
Release: alt13.%{rev}

Summary: Photivo photo processor
Group: Graphics
License: GPLv3+
Url: http://%name.org

# mercurial repository
# /usr/bin/hg clone https://photivo.googlecode.com/hg/ photivo && cd photivo && /usr/bin/hg archive -t tar photivo.tar

Source: %name.tar
Patch: %name.patch

Requires: %name-data = %version-%release

BuildRequires: gcc-c++ libgomp-devel

BuildRequires: ccache libqt4-devel libltdl-devel
BuildRequires: libexiv2-devel liblensfun-devel libfftw3-devel liblqr-devel
BuildRequires: libGraphicsMagick-c++-devel libjpeg-devel libtiff-devel libpng-devel
BuildRequires: bzlib-devel liblcms-devel liblcms2-devel liblzma-devel
%{?_with_gimp:BuildRequires: libgimp-devel}

%description
Photivo is a free and open source photo processor. It handles RAW files
as well as bitmap files in a non-destructive 16 bit processing pipe with
gimp workflow integration and batch mode.

Photivo tries to provide the best algorithms available; even if this
implies some redundancy. So, to my knowledge, it offers the most
flexible and powerful denoise, sharpen and local contrast (fake HDR)
algorithms in the open source world. (If not, let's port them )
Although, to get the desired results, there may be a quite steep
learning curve.

Photivo is just a developer, no manager and no Gimp. It is intended to
be used in a workflow together with digiKam/F-Spot/Shotwell and Gimp. It
needs a quite strong computer and is not aimed at beginners.

%package data
Summary: Data for the Photivo photo processor
Group: Graphics
BuildArch: noarch

%description data
Photivo is a free and open source photo processor. It handles RAW files
as well as bitmap files in a non-destructive 16 bit processing pipe with
gimp workflow integration and batch mode.

This package provides the data files needed for the Photivo to work.


%package -n gimp-plugin-%name
Summary: Photivo plugin for Gimp
Group: Graphics
Requires: %name = %version-%release

%description -n gimp-plugin-%name
Photivo is a free and open source photo processor. It handles RAW files
as well as bitmap files in a non-destructive 16 bit processing pipe with
gimp workflow integration and batch mode.

This package provides Photivo plugin for Gimp.

%prep
%setup -n %name
%patch -p1

# quick hack for new liblensfun-0.2.6
find -type f -print0| xargs -r0 subst 's@#include <lensfun.h>@#include <lensfun/lensfun.h>@
	s@#include "lensfun.h"@#include <lensfun/lensfun.h>@' --

%build
qmake-qt4 PREFIX=%_prefix %{?_with_gimp:CONFIG+=WithGimp}
%make_build

%install
%make INSTALL_ROOT=%buildroot install
# install gimp plugin
%{?_with_gimp:install -pD -m755 ptGimp %buildroot%gimpplugindir/ptGimp}

# install utilities
#install -pD -m755 ptClear %buildroot%_bindir/PtClear
chmod 755 %buildroot%_bindir/ptClear
ln -s ptClear %buildroot%_bindir/%name-clear
#install -pD -m755 ptCreateAdobeProfiles %buildroot%_bindir/ptCreateAdobeProfiles
#ln -s ptCreateAdobeProfiles  %buildroot%_bindir/%name-CreateAdobeProfiles
#install -pD -m755 ptCreateCurves %buildroot%_bindir/ptCreateCurves
#ln -s ptCreateCurves  %buildroot%_bindir/%name-CreateCurves

# fix permissions under %_datadir/%name
find %buildroot%_datadir/%name -type f -print0|xargs -r0 chmod 644 --

%files
%_bindir/*
%doc README

%files data
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/pixmaps/photivo-appicon.png

%if_with gimp
%files -n gimp-plugin-%name
%gimpplugindir/ptGimp
%endif

%changelog
* Thu Jan 21 2016 Yuri N. Sedunov <aris@altlinux.org> 0-alt13.66a8c1082d88
- rebuilt against liblensfun.so.1

* Mon Jun 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0-alt12.66a8c1082d88
- rebuilt against libexiv2.so.14

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0-alt11.66a8c1082d88.1
- Rebuilt for gcc5 C++11 ABI.

* Thu May 21 2015 Yuri N. Sedunov <aris@altlinux.org> 0-alt11.66a8c1082d88
- update to current snapshot
- built with gcc4.9

* Tue Dec 03 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt10.f1a2a2889c33
- update to current snapshot
- built against libexiv2.so.13

* Tue Oct 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt9.99e7c7510b70
- update to current snapshot

* Fri Apr 12 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt8.6256ff175312
- built current snapshot

* Thu Jan 24 2013 Yuri N. Sedunov <aris@altlinux.org> 0-alt7.50b234e492b
- rebuilt against libexiv2.so.12

* Wed Nov 21 2012 Yuri N. Sedunov <aris@altlinux.org> 0-alt6.50b234e492b
- built current snapshot

* Mon Feb 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0-alt5.0c5babd64674
- built current snapshot

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt4.571a226abd23
- built current snapshot

* Sat Jul 02 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt3.bac78754fba4
- built current snapshot

* Sun May 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt2.60f1eb32cced
- built current snapshot

* Fri Apr 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt1.a02c90cbbe57.2
- built current snapshot

* Thu Mar 17 2011 Yuri N. Sedunov <aris@altlinux.org> 0-alt1
- first build for Sisyphus

