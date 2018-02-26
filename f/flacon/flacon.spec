Name: flacon
Version: 0.6.1
Release: alt1

Summary: Audio File Encoder
Summary(ru_RU.UTF-8): Конвертер аудиофайлов
License: GPLv3+
Group: Sound

URL: http://kde-apps.org/content/show.php?content=113388
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: http://flacon.googlecode.com/files/%name-%version.tgz

Requires: shntool

BuildRequires: python-modules-compiler python-modules-encodings rpm-build-gir

%description
Extracts audio tracks from audio CD image to separate tracks.

%description -l ru_RU.UTF-8
Извлекает аудио треки из CD образа WAV, FLAC, APE в отдельные файлы.

%prep
%setup

%build
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_liconsdir/%name.png
%_niconsdir/%name.png
%_datadir/%name

%changelog
* Mon Feb 20 2012 Nazarov Denis <nenderus@altlinux.org> 0.6.1-alt1
- Version 0.6.1

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt0.M60T.1
- Build for branch t6

* Sat Dec 10 2011 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.7-alt1.1
- Rebuild with Python-2.7

* Fri May 27 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt0.M60T.1
- Build for branch t6

* Mon May 09 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.7-alt1
- Version 0.5.7

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M41.1
- Build for branch 4.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt0.M51.1
- Build for branch 5.1

* Sun Feb 13 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.6-alt1
- Version 0.5.6

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt0.M51.1
- Build for branch 5.1

* Fri Feb 11 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.5-alt1
- Version 0.5.5

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt0.M51.1
- Build for branch 5.1

* Sat Jan 29 2011 Nazarov Denis <nenderus@altlinux.org> 0.5.4-alt1
- Version 0.5.4

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt0.M51.1
- Build for branch 5.1

* Fri Nov 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.3-alt1
- Version 0.5.3

* Sun Oct 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt0.M51.1
- Build for branch 5.1

* Fri Oct 29 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.2-alt1
- Version 0.5.2

* Wed Oct 20 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt0.M41.1
- build for M41

* Tue Oct 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt0.M51.1
- Build for branch 5.1

* Mon Oct 18 2010 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt0.M51.1
- Build for branch 5.1

* Mon Oct 04 2010 Nazarov Denis <nenderus@altlinux.org> 0.5-alt1
- Version 0.5

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt0.M51.1
- Build for branch 5.1

* Thu Aug 19 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.7-alt1
- Version 0.4.7

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt0.M51.1
- Build for branch 5.1

* Sun Aug 08 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.5-alt1
- Version 0.4.5

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt0.M51.1
- Build for branch 5.1

* Sun Aug 01 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt0.M51.1
- Build for branch 5.1

* Sat Jul 24 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.3-alt1
- Version 0.4.3

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt0.M51.1
- Build for branch 5.1

* Sun Jun 13 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt0.M51.1
- Build for branch 5.1

* Mon May 31 2010 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt0.M51.1
- Build for branch 5.1

* Fri May 28 2010 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1
- Version 0.4

* Wed May 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.3
- Build for branch 5.1

* Fri Apr 30 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.2
- Fix desktop-file

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.2
- Build for branch 5.1

* Tue Apr 27 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2.1
- Cleanup spec-file

* Mon Apr 26 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1.M51.1
- First build for branch 5.1

* Mon Apr 12 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt2
- Fix requires, buildarch and icons

* Fri Apr 9 2010 Nazarov Denis <nenderus@altlinux.org> 0.3.1-alt1
- First build for ALT Linux 5.0 (p5)
