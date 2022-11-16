Name:           siril
Version:        1.0.6
Release:        alt2
Summary:        Astronomical image processing software
Group: 		Graphics
Packager: Ilya Mashkin <oddity@altlinux.ru>
# Selected portions of the software derived from SLEEF
# are licensed under Boost license:
# - src/core/sleef.h
License:        GPLv3+ and Boost
URL:            https://siril.org
Source0:        https://free-astro.org/download/%{name}-%{version}.tar.bz2

Patch1:         siril-1.0.0-opencv_flann.patch

# Notes on dependencies:
# No ffms and heif support 

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg libavcodec-devel
# libffmpegthumbnailer-devel libopenmpt-devel
BuildRequires:  gcc-c++
BuildRequires:  libgif-devel libopencv-devel  libgomp-devel libopenmpt-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
#BuildRequires:  pkgconfig(rtprocess)
#BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(wcslib)

#Recommends:     gvfs

#Provides:       bundled(kplot) = 0.1.14

%description
Siril is an image processing tool specially tailored for noise reduction and
improving the signal/noise ratio of an image from multiple captures, as
required in astronomy. Siril can align automatically or manually, stack and
enhance pictures from various file formats, even images sequences (movies and
SER files)


%prep
#setup -c -n siril-%version
%setup
#patch1 -p1
%ifarch %e2k
sed -i -E "/^[[:space:]]*#pragma omp.*\\\\$/N;\
/^[[:space:]]*#pragma omp .*(num_threads| if)\(/{s/#/for(long &/;\
s/(#.*num_threads\()([^()]*)\)/_xxxn=\\2,\\1_xxxn)/;\
s/(#.*if *\()([^()]*(\([^()]*(\([^()]*\)[^()]*)*\)[^()]*)*)\)/_xxxi=\\2,\\1_xxxi)/;\
s/(#.*schedule\([^()]*, *)([^()]*)\)/_xxxs=\\2,\\1_xxxs)/;\
s/#/_xxxc=1;_xxxc;_xxxc=0)\n&/}" \
 src/{registration,filters,stacking,rt,algos,gui,compositing,pixelMath,core,io}/*.c
%endif

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%meson \
    -Drelocatable-bundle=no \
    -Dopenmp=true \
    -Denable-libcurl=yes

%meson_build


%install
%meson_install

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    platform-specific/linux/org.free_astro.siril.desktop

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.free_astro.siril.appdata.xml

%files -f %{name}.lang

%doc AUTHORS ChangeLog NEWS README.md LICENSE.md LICENSE_sleef.txt
%{_bindir}/%{name}*
%{_datadir}/applications/org.free_astro.siril.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.free_astro.siril.appdata.xml
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*


%changelog
* Thu Nov 17 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.6-alt2
- fix build on Elbrus (Ilya Kurdyukov)

* Wed Oct 19 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sat Sep 10 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Tue Sep 06 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Sat Jul 02 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue May 17 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Apr 07 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Tue Mar 15 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt2
- Update BR

* Mon Mar 14 2022 Ilya Mashkin <oddity@altlinux.ru> 1.0.0-alt1
- First build for Sisyphus from FC

* Sat Mar 12 2022 Mattia Verga <mattia.verga@protonmail.com> 1.0.0-1
- Update to 1.0.0 final (fixes fedora#2062218, fedora#1994996)

* Tue Mar 08 2022 Neal Gompa <ngompa@fedoraproject.org> - 1.0.0~rc2-2
- Rebuild for ffmpeg 5.0 ABI fix (#2061392)

* Tue Mar 01 2022 Mattia Verga <mattia.verga@protonmail.com> - 1.0.0~rc2-1
- Update to 1.0.0~rc2
- Enable ffmpeg support

* Sun Aug 29 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.99.10.1-1
- Update to 0.99.10.1
- License changed to GPLv3+ and Boost

* Mon Apr 05 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.99.8.1-2
- Use librtprocess from Fedora repo
- Use meson build system

* Sun Mar 07 2021 Mattia Verga <mattia.verga@protonmail.com> - 0.99.8.1-1
- Update to 0.99.8.1

* Tue Feb 02 2021 Christian Dersch <lupinix@mailbox.org> - 0.99.6-4
- Rebuilt for libcfitsio.so.7

* Thu Oct 22 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.99.6-2
- Add patch for opencv-4.5

* Tue Oct 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.99.6-1
- Update to 0.99.6

* Tue Sep 15 2020 Jeff Law <law@redhat.com> - 0.99.4-2
- Fix missing include for gcc-11

* Tue Aug 25 2020 Christian Dersch <lupinix@mailbox.org> - 0.99.4-1
- new version

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-7
- Rebuilt for OpenCV 4.3

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.12-6
- Rebuild for new LibRaw

* Wed Jan 29 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-4
- Add upstream patch to fix compilation

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-3
- Rebuild for OpenCV 4.2

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 0.9.12-2
- Rebuilt for opencv4

* Wed Nov 06 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.9.12-1
- new version

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.9.11-3
- Rebuilt for GSL 2.6.

* Sat Jun 08 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.9.11-1
- new version

* Thu Jan 24 2019 Christian Dersch - 0.9.10-1
- new version

* Tue Jul 24 2018 Adam Williamson <awilliam@redhat.com> - 0.9.9-6
- Rebuild for new libconfig

* Thu Jul 19 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-5
- Rebuilt for LibRaw soname bump

* Tue Jul 17 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.9-4
- BuildRequires: gcc-c++

* Tue Jul 03 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.9.9-2
- Fix #1588442 with siril-0.9.9-fix-build-glibc2.28.patch

* Fri Jun 15 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.9.9-1
- new version

* Sat May 26 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-4
- rebuilt for cfitsio 3.450

* Sun Mar 04 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-3
- new dependency: curl-devel/curl

* Fri Mar 02 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-2
- rebuild for opencv 3.4.1

* Fri Feb 23 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8.3-1
- new version

* Wed Jan 31 2018 Christian Dersch <lupinix@mailbox.org> - 0.9.8-1
- new version

* Mon Dec 25 2017 Christian Dersch <lupinix@fedoraproject.org> - 0.9.7-2
- rebuilt (opencv)

* Thu Sep 21 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.7-1
- new version

* Sat Aug 05 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.6-4
- Rebuild (gsl)

* Fri Jun 23 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.6-1
- new version

* Thu Mar 02 2017 Christian Dersch <lupinix@mailbox.org> - 0.9.5-4
- rebuilt for opencv-3.2.0

* Wed Dec 28 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.5-2
- Rebuild for new LibRaw.

* Tue Nov 29 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.5-1
- new version

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-3
- Rebuilt

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-2
- fix scriptlets, use update-desktop-database only for Fedora < 25

* Fri Oct 14 2016 Christian Dersch <lupinix@mailbox.org> - 0.9.4-1
- update to version 0.9.4
- complete rework of the package

* Wed May 28 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.8-17
- Fix format string security error
- Deal with the compile warnings
- Actually rebuild for the new cfitsio

* Fri Jan 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.8-16
- Rebuild for cfitsio 3.360

* Sat Mar 30 2013 Kevin Fenzi <kevin@scrye.com> - 0.8-14
- Rebuild for broken deps in rawhide

* Mon Aug 3 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8-9
- Fix build
- Fix out of string bound writes (#494536)

* Sat Apr 4 2009 Lubomir Rintel <lkundrak@v3.sk> - 0.8-7
- Fix crash on incorrectly loaded pictures (#494536)

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 0.8-5
- Include unowned directories

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-4
- Autorebuild for GCC 4.3

* Sat Nov 24 2007 Marek Mahut <mmahut@fedoraproject.org> - 0.8-3
- Initial build.

