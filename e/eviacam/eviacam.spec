Summary: Mouse replacement software that moves the pointer as you move your head
Name: eviacam
Version: 1.7.0
Release: alt2
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: System/Base
License: GPLv3
Url: http://viacam.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: libwxGTK-devel libopencv-devel libXtst-devel libXext-devel libgtk+2-devel gcc-c++ libv4l-devel

%description
Mouse replacement software that moves the pointer as you move your head.
It works on standard PCs equipped with a web camera. No additional hardware
is required. Based on the award winning Facial Mouse software.

%prep
%setup -q
%patch -p1

%build
%autoreconf
#For temp fix https://bugzilla.altlinux.org/29231
%configure LIBS=" -lopencv_calib3d -lopencv_contrib -lopencv_core -lopencv_features2d -lopencv_flann -lopencv_highgui -lopencv_imgproc -lopencv_legacy -lopencv_ml -lopencv_objdetect -lopencv_photo -lopencv_stitching -lopencv_video -lopencv_videostab"
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog README THANKS TODO
%_bindir/*
%_datadir/%name
%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
* Fri Apr 18 2014 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt2
- Do not link with obsoleted library libopencv_ts

* Fri Jul 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.0-alt1
- New version

* Wed Sep 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.4-alt1
- New version

* Tue Jan 31 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.3-alt1
- New version

* Sat Aug 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.1
- Rebuilt with OpenCV 2.3.1

* Sun Apr 17 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5-alt1
- New version

* Fri Feb 04 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.2-alt1
- New version

* Tue Jan 04 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.4.1-alt1
- Build for ALT
