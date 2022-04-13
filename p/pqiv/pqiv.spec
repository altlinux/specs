Name: pqiv
Version: 2.12
Release: alt1

Summary: Minimalist Image Viewer
License: GPLv3+
Group: Graphics

Url: https://github.com/phillipberndt/pqiv
Source: %name-%version.tar.gz
#Patch: %name-alt.patch

BuildRequires: libgtk+2-devel libgtk+3-devel glib2-devel libcairo-devel libgio-devel
BuildRequires: libavformat-devel libavcodec-devel libswscale-devel libavutil-devel
BuildRequires: libpoppler-devel libpoppler-glib-devel
BuildRequires: libspectre-devel
BuildRequires: libImageMagick-devel

%description
Originally, PQIV was written as a drop-in replacement for QIV.

This is common package, install gtk2/gtk3 subpackages (or both).

%package gtk2
Summary: %name build with gtk2
Group: Graphics
Requires: %name = %version
%description gtk2
%name build with gtk2

%package gtk3
Summary: %name build with gtk3
Group: Graphics
Requires: %name = %version
%description gtk3
%name build with gtk3

%package gdkpixbuf
Summary: gdkpixbuf backend for %name
Group: Graphics
Requires: %name = %version
%description gdkpixbuf
Backend for %name

%package libav
Summary: libav backend for %name
Group: Graphics
Requires: %name = %version
%description libav
Backend for %name

%package poppler
Summary: poppler backend for %name
Group: Graphics
Requires: %name = %version
%description poppler
Backend for %name

%package spectre
Summary: spectre backend for %name
Group: Graphics
Requires: %name = %version
%description spectre
Backend for %name

%package wand
Summary: wand backend for %name
Group: Graphics
Requires: %name = %version
%description wand
Backend for %name

%prep
#setup -q -n %name-%version
%setup -q
#patch -p1
%if "%_lib" == "lib64"
sed -i 's|^LIBDIR=\$(PREFIX)/lib$|LIBDIR=%_libdir|' GNUmakefile
%endif

%build
for ver in 3 2;do
	./configure \
		--gtk-version=$ver \
		--prefix=%prefix \
		--destdir=%buildroot \
		--backends=gdkpixbuf,libav,poppler,spectre,wand \
		--backends-build=shared

	%make_build
	mv %name %{name}-gtk$ver
done
mv %{name}-gtk2 %name

%install
%makeinstall_std
mv %buildroot%_bindir/%name %buildroot%_bindir/%{name}-gtk2
install -p -m 755 %{name}-gtk3 %buildroot%_bindir/%{name}-gtk3

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name-gtk2
%_bindir/%name	%_bindir/%{name}-gtk2	10
_EOF_

cat <<'_EOF'_ > %buildroot%_altdir/%name-gtk3
%_bindir/%name	%_bindir/%{name}-gtk3	20
_EOF_

%files
%_man1dir/%name.1.*
%dir %_libdir/%name
%_datadir/applications/pqiv.desktop
%doc README.markdown

%files gtk2
%_altdir/%name-gtk2
%_bindir/%{name}-gtk2

%files gtk3
%_altdir/%name-gtk3
%_bindir/%{name}-gtk3

%files gdkpixbuf
%_libdir/%name/%name-backend-gdkpixbuf.so

%files libav
%_libdir/%name/%name-backend-libav.so

%files poppler
%_libdir/%name/%name-backend-poppler.so

%files spectre
%_libdir/%name/%name-backend-spectre.so

%files wand
%_libdir/%name/%name-backend-wand.so

%changelog
* Wed Apr 13 2022 Ilya Mashkin <oddity@altlinux.ru> 2.12-alt1
- 2.12
- Add desktop file
- Update license tag

* Wed Jun 26 2019 Michael Shigorin <mike@altlinux.org> 2.8.5-alt5
- Fixed build on 64-bit arches
- Minor spec cleanup

* Thu Aug 09 2018 Anton Farygin <rider@altlinux.ru> 2.8.5-alt4
- Rebuilt for ffmpeg-4.0.

* Wed May 30 2018 Anton Farygin <rider@altlinux.ru> 2.8.5-alt3
- Rebuilt for ImageMagick.

* Mon Aug 21 2017 Anton Farygin <rider@altlinux.ru> 2.8.5-alt2
- Rebuilt for ImageMagick.

* Mon Jun  5 2017 Terechkov Evgenii <evg@altlinux.org> 2.8.5-alt1
- 2.8.5
- Build with ffmpeg

* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt3
- Subpackages for gtk2/gtk3

* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt2
- Build backends: libav, poppler, spectre, wand
- Split to subpackages (one for backend)

* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt1
- Initial build for ALT Linux Sisyphus
- 2.4-40-gae7d440
