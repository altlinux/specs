Name: scim
Version: 1.4.17
Release: alt1
Summary: Smart Common Input Method platform
Packager: Andrey Cherepanov <cas@altlinux.org>
License: LGPLv2+
Group: System/Configuration/Other
Url: https://github.com/scim-im/scim
Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
# VCS:   https://github.com/scim-im/scim
Source1: xinput-scim
Source2: scim-icons-0.7.tar.gz
Source3: scim-system-config
Source4: scim-system-global

BuildRequires: gtk2-devel, libXt-devel, libgtk+3-devel
# for autoreconf
BuildRequires: autoconf automake gettext libtool intltool
# for system ltdl
BuildRequires: libltdl-devel gcc-c++ libqt4-devel
# for autogen.sh
BuildRequires: gnome-common
Requires: %name-libs = %version-%release
Requires: imsettings, im-chooser
Obsoletes: iiimf-gtk <= 1:12.2, iiimf-gnome-im-switcher <= 1:12.2, iiimf-server <= 1:12.2, iiimf-x <= 1:12.2
Obsoletes: iiimf-libs-devel <= 1:12.2
Obsoletes: iiimf-docs <= 1:12.2
Obsoletes: iiimf-libs <= 1:12.2, iiimf-csconv <= 1:12.2
Obsoletes: scim-lang-assamese
Obsoletes: scim-lang-bengali
Obsoletes: scim-lang-chinese
Obsoletes: scim-lang-dhivehi
Obsoletes: scim-lang-farsi
Obsoletes: scim-lang-gujarati
Obsoletes: scim-lang-hindi
Obsoletes: scim-lang-japanese
Obsoletes: scim-lang-kannada
Obsoletes: scim-lang-korean
Obsoletes: scim-lang-latin
Obsoletes: scim-lang-malayalam
Obsoletes: scim-lang-marathi
Obsoletes: scim-lang-nepali
Obsoletes: scim-lang-oriya
Obsoletes: scim-lang-punjabi
Obsoletes: scim-lang-sinhalese
Obsoletes: scim-lang-tamil
Obsoletes: scim-lang-telugu
Obsoletes: scim-lang-thai
Obsoletes: scim-lang-tibetan
Obsoletes: scim-python
Obsoletes: scim-python-chinese
Obsoletes: scim-python-english
Obsoletes: scim-python-pinyin
Obsoletes: scim-python-xingma
Obsoletes: scim-python-xingma-cangjie
Obsoletes: scim-python-xingma-erbi
Obsoletes: scim-python-xingma-wubi
Obsoletes: scim-python-xingma-zhengma
Patch1: scim-add-restart.patch
Patch7: scim_panel_gtk-emacs-cc-style.patch

%description
SCIM is a user friendly and full featured input method user interface and
also a development platform to make life easier for Input Method developers.

%package devel
Summary: Smart Common Input Method platform
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: gtk2-devel
Requires: pkgconfig
Obsoletes: iiimf-libs-devel <= 1:12.2

%description devel
The scim-devel package includes the header files for the scim package.
Install scim-devel if you want to develop programs which will use scim.

%package gtk
Summary: Smart Common Input Method Gtk IM module
Group: System/Libraries
# for %_libdir/gtk-2.0/immodules
Requires: gtk2 >= 2.11.6-7.fc8
# for update-gtk-immodules
Requires(post): gtk2 >= 2.9.1-2
Requires(postun): gtk2 >= 2.9.1-2

%description gtk
This package provides a GTK input method module for SCIM.

%package libs
Summary: Smart Common Input Method libraries
Group: System/Libraries
Obsoletes: iiimf-libs <= 1:12.2, iiimf-csconv <= 1:12.2

%description libs
This package provides the libraries for SCIM.

%package rawcode
Summary: SCIM Unicode Input Method Engine
Group: System/Libraries
Requires: %name = %version-%release

%description rawcode
This package provides an Input Method Engine for inputting unicode characters
but their unicode codepoints.

%package qt4
Summary: SCIM im module for qt4
Group: System/Libraries
Requires: %name = %version
BuildRequires: libqt4-devel

%description qt4
This package contains SCIM im module for qt4

%define scim_api 1.4.0

%define _xinputconf %_sysconfdir/X11/xinit/xinput.d/scim.conf

%prep
%setup -a2

cp -p scim-icons/icons/*.png data/icons
cp -p scim-icons/pixmaps/*.png data/pixmaps

# use our system config & global file
mv configs/config{,.orig}
cp -p %SOURCE3 configs/config
mv configs/global{,.orig}
cp -p %SOURCE4 configs/global

%patch7 -p1 -b .7-emacs-ccmode~

# patch17 touches configure.ac and Makefile.am
./bootstrap

%build
%configure --disable-static --enable-ld-version-script --with-gtk-version=2 --enable-qt4-immodule
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%__install -p"

# remove .la files
find $RPM_BUILD_ROOT -name '*.la' | xargs rm

# remove scim-setup.desktop file since it is confusing with im-chooser
rm $RPM_BUILD_ROOT/%_datadir/applications/scim-setup.desktop
# remove capplet
rm $RPM_BUILD_ROOT/%_datadir/control-center-2.0/capplets/scim-setup.desktop

# don't need this
rm -f docs/html/FreeSans.ttf

# install xinput config file
mkdir -pm 755 $RPM_BUILD_ROOT/%_sysconfdir/X11/xinit/xinput.d
install -pm 644 %SOURCE1 $RPM_BUILD_ROOT/%_xinputconf

%find_lang %name

%post gtk
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules ||:

%postun gtk
[ "$1" = 0 ] || \
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules ||:


%post libs
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules ||:

%postun libs
[ "$1" = 0 ] || \
%_bindir/gtk-query-immodules-2.0 > %_sysconfdir/gtk-2.0/gtk.immodules ||:




%files -f %name.lang
%doc AUTHORS COPYING README ChangeLog TODO
%dir %_sysconfdir/scim
%config(noreplace) %_sysconfdir/scim/*
%_bindir/*
%dir %_libdir/scim-1.0
%_libdir/scim-1.0/scim-helper-launcher
%_libdir/scim-1.0/scim-helper-manager
%_libdir/scim-1.0/scim-launcher
%_libdir/scim-1.0/scim-panel-gtk
%dir %_libdir/scim-1.0/%scim_api
%_libdir/scim-1.0/%scim_api/Filter
%_libdir/scim-1.0/%scim_api/FrontEnd
%_libdir/scim-1.0/%scim_api/Helper
%dir %_libdir/scim-1.0/%scim_api/IMEngine
%_libdir/scim-1.0/%scim_api/SetupUI
%_datadir/scim
%_datadir/pixmaps/*
%config(noreplace) %_xinputconf

%files devel
%doc docs/developers
%_includedir/scim-1.0
%_libdir/libscim*.so
%_libdir/pkgconfig/*.pc

%files gtk
%_libdir/gtk-2.0/*/immodules/im-scim.so
%_libdir/gtk-3.0/*/immodules/im-scim.so

%files libs
%_libdir/libscim-*.so.*
%dir %_libdir/scim-1.0
%dir %_libdir/scim-1.0/%scim_api
%_libdir/scim-1.0/%scim_api/Config
%dir %_libdir/scim-1.0/%scim_api/IMEngine
%_libdir/scim-1.0/%scim_api/IMEngine/socket.so

%files rawcode
%_libdir/scim-1.0/%scim_api/IMEngine/rawcode.so

%files qt4
%_libdir/qt4/plugins/

%changelog
* Thu Jun 02 2016 Andrey Cherepanov <cas@altlinux.org> 1.4.17-alt1
- New version

* Thu Nov 12 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.4.15-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Fri Feb 20 2015 Ilya Mashkin <oddity@altlinux.ru> 1.4.15-alt1
- 1.4.15
- fix postun sections

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.4.14-alt3
- add post/postun sections

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.4.14-alt2
- add scim-qt4 package

* Tue Aug 26 2014 Ilya Mashkin <oddity@altlinux.ru> 1.4.14-alt1
- 1.4.14
- sync spec with FC

* Mon Feb 07 2011 Ilya Mashkin <oddity@altlinux.ru> 1.4.9-alt2
- rebuild for set-versions

* Wed Aug 05 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.9-alt1
- 1.4.9
- remove old ldconfig calls
- spec cleanup

* Thu Sep 27 2007 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.7-alt1
- Up to version 1.4.7.

* Tue Jun 06 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt3
- fix spec.

* Tue May 16 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt2
- fix spec.

* Wed May 10 2006 Dmitri Kuzishchin <dim@altlinux.ru> 1.4.4-alt1
- first ALT release of SCIM.

