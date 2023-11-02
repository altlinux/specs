Name: shelxle
Version: 1.0.1566
Release: alt2

Summary: A Qt GUI for SHELX
License: LGPLv2
Group: Sciences/Chemistry

Url: http://www.shelxle.org/
Source: %name-%version.tar.bz2

ExcludeArch: armh

BuildRequires: gcc-c++ libgomp-devel qt6-base-devel libGLU-devel

Requires: qt6-svg

%description
ShelXle is a graphical user interface for the SHELX structure
solution and refinement program.
J. Appl. Cryst. (2011). 44, 1281-1284.

%prep
%setup
#patch0 -p1
subst 's/Qt;Science;Chemistry;Physics;Education/Science;Chemistry;/' %name.desktop

%build
%qmake_qt6 "CONFIG+=debug"
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_iconsdir/hicolor/64x64/apps
mv %buildroot%_pixmapsdir/%name.png %buildroot%_iconsdir/hicolor/64x64/apps/
rm -rf %buildroot%_pixmapsdir
cp kissfft/COPYING COPYING_kissfft

%files
%doc COPYING COPYING_kissfft
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Thu Nov 02 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1566-alt2
- build with Qt6

* Wed Nov 01 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1566-alt1
- new version

* Tue Oct 24 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1561-alt1
- new version

* Sun Sep 17 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1556-alt1
- new version

* Sun Aug 20 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1554-alt1
- new version

* Thu Jul 27 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1549-alt1
- new version

* Tue Jul 11 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1541-alt1
- new version

* Wed Jun 28 2023 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1434-alt1
- new version

* Fri Sep 30 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1432-alt1
- new version

* Sat Sep 03 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1418-alt1
- new version

* Mon Aug 15 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1416-alt1
- new version

* Thu Jul 14 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1410-alt1
- new version

* Wed May 11 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1385-alt1
- new version
- flickering cursor issues fixed
- fixing context menu

* Thu Apr 07 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1378-alt1
- new version

* Fri Feb 25 2022 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1365-alt1
- new version

* Wed Dec 15 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1352-alt1
- new version
- fix Voronoi polyhedra drawing

* Tue Dec 14 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1348-alt1
- new version

* Mon Nov 22 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1346-alt1
- new version

* Sat Oct 16 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1330-alt1
- new version

* Fri Oct 08 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1326-alt1
- new version
- fix wght refine

* Mon Sep 27 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1324-alt1
- new version
- fix DSR gui fragment rotation without left mouse button pressed

* Thu Sep 23 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1322-alt1
- new version
- fix problem with visibility of some icons

* Wed Sep 15 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1318-alt1
- new version

* Sun Sep 05 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1309-alt1
- new version

* Wed Jul 14 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1285-alt1
- new version

* Fri Apr 30 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1246-alt1
- new version

* Tue Mar 30 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1235-alt1
- new version

* Tue Mar 02 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1229-alt1
- new version

* Tue Feb 16 2021 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1226-alt1
- new version

* Thu Oct 08 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1165-alt1
- new version

* Mon Sep 07 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1143-alt1
- new version

* Tue Aug 18 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1140-alt1
- new version

* Sun Jul 12 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1124-alt1
- new version

* Mon Jun 22 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1117-alt1
- new version
- exclude armh

* Fri Jun 12 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1113-alt1
- new version

* Thu Feb 20 2020 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1070-alt1
- new version

* Mon Dec 16 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1024-alt1
- new version

* Mon Nov 18 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.1008-alt1
- new version

* Tue Oct 22 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.997-alt2
- fixed build flags and debuginfo

* Mon Oct 21 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.997-alt1
- new version
- build with Qt5

* Fri Apr 12 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.955-alt1
- new version

* Sun Jan 20 2019 Denis G. Samsonenko <ogion@altlinux.org> 1.0.949-alt1
- new version

* Sun Nov 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.940-alt1
- new version

* Sat Sep 15 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.937-alt1
- new version

* Thu Aug 16 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.929-alt1
- new version

* Wed May 30 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.918-alt1
- new version

* Sat Mar 10 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.901-alt1
- new version

* Sun Feb 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.891-alt1
- new version

* Thu Jan 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 1.0.882-alt1
- new version

* Sat Aug 26 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.861-alt1
- new version

* Sat Jul 08 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.859-alt1
- new version

* Sun May 07 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.844-alt1
- new version

* Sun Apr 09 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.839-alt1
- new version

* Mon Mar 27 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.836-alt1
- new version

* Thu Feb 16 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.833-alt1
- new version

* Sat Jan 28 2017 Denis G. Samsonenko <ogion@altlinux.org> 1.0.825-alt1
- new version

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
