Name: shelxle
Version: 1.0.554
Release: alt1

Summary: A Qt GUI for SHELX
License: LGPLv2
Group: Sciences/Chemistry

#Patch0: shelxle-1.0.519-alt-build-fix.patch

Url: http://ewald.ac.chemie.uni-goettingen.de/shelx/
Source: %name-%version.tar.bz2

# Automatically added by buildreq on Fri Dec 09 2011
# optimized out: fontconfig libGL-devel libGLU-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-webkit libqt4-xml libstdc++-devel
#BuildRequires: gcc-c++ libfftw3-devel libgomp-devel phonon-devel
BuildRequires: gcc-c++ libfftw3-devel libgomp-devel libqt4-devel

%description
ShelXle is a graphical user interface for the SHELX structure
solution and refinement program.
J. Appl. Cryst. (2011). 44, 1281-1284.

%prep
%setup
#patch0 -p1
subst 's/Qt;Science;Chemistry;Physics;Education/Education;Science;Chemistry;/' %name.desktop

%build
qmake-qt4
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc LICENSE
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Fri May 25 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.554-alt1
- new version

* Wed May 16 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.551-alt1
- new version
- patch0 removed
- changelog fixed

* Tue Apr 03 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.548-alt1
- new version

* Wed Mar 21 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.544-alt1
- new version

* Wed Feb 29 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.540-alt1
- new version

* Tue Jan 24 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.519-alt1
- new version
- fix building for Sisyphus (patch0)

* Sat Dec 24 2011 Denis G. Samsonenko <ogion@altlinux.org> 1.0.513-alt1
- new version

* Sat Dec 24 2011 Denis G. Samsonenko <ogion@altlinux.org> 1.0.509-alt1
- new version

* Fri Dec 09 2011 Denis G. Samsonenko <ogion@altlinux.org> 1.0.500-alt1
- initial build for ALT Linux Sisyphus
