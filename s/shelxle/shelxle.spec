Name: shelxle
Version: 1.0.818
Release: alt1

Summary: A Qt GUI for SHELX
License: LGPLv2
Group: Sciences/Chemistry

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
subst 's/Qt;Science;Chemistry;Physics;Education/Science;Chemistry;/' %name.desktop

%build
qmake-qt4
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
mv %buildroot%_pixmapsdir/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/
rm -rf %buildroot%_pixmapsdir

%files
%doc COPYING
%_bindir/%name
#_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Sun Jan 15 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.818-alt1
- new version

* Sat Jul 02 2016 Denis G. Samsonenko <ogion@altlinux.org> 1.0.771-alt1
- new version

* Sun Apr 10 2016 Denis G. Samsonenko <ogion@altlinux.org> 1.0.764-alt1
- new version

* Sun Feb 14 2016 Denis G. Samsonenko <ogion@altlinux.org> 1.0.758-alt1
- new version

* Sun Oct 25 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.745-alt1
- new version

* Sun Sep 13 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.740-alt1
- new version

* Fri Aug 14 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.737-alt1
- new version

* Sat Jun 13 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.723-alt1
- new version
- move %name.png to %_iconsdir/hicolor/64x64/apps/

* Fri May 29 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.720-alt1
- new version

* Thu Feb 12 2015 Denis G. Samsonenko <ogion@altlinux.org> 1.0.709-alt1
- new version

* Mon Nov 03 2014 Denis G. Samsonenko <ogion@altlinux.org> 1.0.680-alt1
- new version

* Tue Jul 22 2014 Denis G. Samsonenko <ogion@altlinux.org> 1.0.664-alt1
- new version

* Tue Feb 18 2014 Denis G. Samsonenko <ogion@altlinux.org> 1.0.661-alt1
- new version

* Thu Nov 21 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.651-alt1
- new version

* Fri Sep 06 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.647-alt1
- new version

* Thu Aug 08 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.645-alt1
- new version

* Wed Jul 17 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.639-alt1
- new version

* Sat Jun 01 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.629-alt1
- new version

* Thu Apr 11 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.618-alt1
- new version

* Wed Mar 06 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.615-alt1
- new version

* Mon Feb 04 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.612-alt1
- new version

* Sun Jan 13 2013 Denis G. Samsonenko <ogion@altlinux.org> 1.0.609-alt1
- new version

* Thu Nov 29 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.606-alt1
- new version

* Wed Nov 14 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.602-alt1
- new version

* Sun Oct 21 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.594-alt1
- new version

* Tue Oct 16 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.590-alt1
- new version

* Sat Oct 13 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.588-alt1
- new version

* Fri Jul 20 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.576-alt1
- new version

* Mon Jul 09 2012 Denis G. Samsonenko <ogion@altlinux.org> 1.0.564-alt1
- new version

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
