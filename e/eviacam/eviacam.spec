%define _unpackaged_files_terminate_build 1

Name:     eviacam
Version:  2.1.4
Release:  alt2

Summary:  Mouse replacement software that moves the pointer as you move your head
Group: 	  System/Base
License:  GPLv3
Url:      http://viacam.org
# VCS:    https://github.com/cmauri/eviacam.git

Packager: Andrey Cherepanov <cas@altlinux.org>
Source:   %name-%version.tar
Patch1:   %name-alt-compat.patch
Patch2:   %name-upstream-opencv-4.2-compat.patch
Patch3:   %name-2.1.4-wx3.2-compat.patch

BuildRequires: libwxGTK3.2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libopencv-devel libXtst-devel libXext-devel gcc-c++ libv4l-devel

%description
Mouse replacement software that moves the pointer as you move your head.
It works on standard PCs equipped with a web camera. No additional hardware
is required. Based on the award winning Facial Mouse software.

%prep
%setup -q
%autopatch1 -p1

%build
touch config.rpath
%autoreconf
%configure
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
%_man1dir/*

%changelog
* Mon Oct 16 2023 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt2
- NMU: rebuild with wxGTK3.2

* Tue Apr 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.4-alt1
- Updated to upstream version 2.1.4.

* Tue Sep 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.3-alt3
- Rebuilt with wxGTK-3.0 and gtk+-3.

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 2.1.3-alt2
- Rebuilt with compat-libwxGTK3.0-gtk2-devel

* Tue Jun 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.3-alt1
- Updated to upstream version 2.1.3.

* Sun Sep 20 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version (ALT #31285)

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
