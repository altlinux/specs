%define ver_build 20091031

Name: autopano-sift-C
Version: 2.5.1
Release: alt2
Epoch: 1

Group: Graphics
Summary: autopano-sift-C is a port of autopano-SIFT to pure C
License: GPLv2
Source0: %name-%version.tar.gz
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

# Automatically added by buildreq on Wed Jul 27 2005
BuildRequires: libpano13-devel libxml2-devel libjpeg-devel libpng-devel libtiff-devel zlib-devel cmake gcc-c++
Provides: autopano-sift
Obsoletes: autopano-sift

%description
autopano-sift-C is a port of autopano-SIFT to pure C.
Panorama images are wide-angle images that amaze people:
you often feel being inside the scene when watching a good
panorama image. Creating such images is easy and everybody
with a digital camera and a bit of patience can do it.
Autopano-sift-C is there to make the creation of panorama images more fun.

%prep
%setup -q

%build
cmake -Wno-dev -D CMAKE_INSTALL_PREFIX:PATH=%buildroot/usr .
make

%install
mkdir -p %buildroot%_bindir
%makeinstall

%files
%doc README README.1ST
%_bindir/*
%_man1dir/*
%_man7dir/*

%changelog
* Wed May 23 2012 Sergei Epiphanov <serpiph@altlinux.ru> 1:2.5.1-alt2
- Rebuild due to fix libs

* Mon Feb 08 2010 Sergei Epiphanov <serpiph@altlinux.ru> 1:2.5.1-alt1
- Revert to version 2.5.1 (r4054) due to bugs in keypoints (closes #22567)

* Mon Nov 09 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.5.2-alt2.20091031
- Rebuild with new libpano13 version

* Sat Oct 31 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.5.2-alt1.20091031
- New version from trunk

* Tue Jun 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.5.0-alt3.20080723
- NMU: conflict to autopano-sift replaced by obsoleting to be installable 
  via plain RPM (closes #20299)

* Wed Feb 25 2009 Sergei Epiphanov <serpiph@altlinux.ru> 2.5.0-alt2.20080723
- Set conflicts with autopano-sift

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.5.0-alt1.20080723
- Remove conflict with autopano-sift

* Thu Jul 24 2008 Sergei Epiphanov <serpiph@altlinux.ru> 2.5.0-alt0.20080723
- New version

* Wed Sep 05 2007 Sergei Epiphanov <serpiph@altlinux.ru> 2.4-alt0.20070905
- Initial build for Sisyphus
