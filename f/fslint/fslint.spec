Name: fslint
Version: 2.42
Release: alt1.1
Summary: FSlint - a utility to find and clean "lint" on a filesystem

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: File tools
License: GPL
Url: http://www.pixelbeat.org/fslint/
Source0: http://www.pixelbeat.org/fslint/%name-%version.tar.gz

BuildArch: noarch
BuildRequires: gettext >= 0.13, desktop-file-utils

Requires: python >= 2.0, cpio
Requires: python-module-pygtk, python-module-pygtk-libglade

%description
FSlint is a toolkit to find all redundant disk usage (duplicate files
for e.g.). It includes a GUI as well as a command line interface.

%package gnome
License: GPL
Group: File tools
Summary: It is a part of the program FSlint for which work it is necessary gnome
Requires: fslint
%description gnome
It is a part of the program FSlint for which work it is necessary gnome


%prep
%setup -q -n %name-%version
%__subst "s|fslint_icon.png|fslint_icon|g" %name.desktop
%__perl -pi -e 's|^liblocation=.*$|liblocation="%_datadir/%name" #RPM edit|' fslint-gui
%__perl -pi -e 's|^locale_base=.*$|locale_base=None #RPM edit|' fslint-gui

%build
# Not.

%install
install -Dpm 755 fslint-gui $RPM_BUILD_ROOT%_bindir/fslint-gui
install -dm 755 $RPM_BUILD_ROOT%_datadir/%name/%name/{fstool,supprt}
install -dm 755 $RPM_BUILD_ROOT%_datadir/%name/%name/supprt/rmlint
install -dm 755 $RPM_BUILD_ROOT%_mandir/man1
install -pm 644 fslint.glade fslint_icon.png \
  $RPM_BUILD_ROOT%_datadir/%name
install -dm 755 $RPM_BUILD_ROOT%_datadir/pixmaps
ln -s %_datadir/%name/fslint_icon.png $RPM_BUILD_ROOT%_datadir/pixmaps
install -pm 755 fslint/{find*,fslint,zipdir} \
  $RPM_BUILD_ROOT%_datadir/%name/fslint
install -pm 755 fslint/fstool/* \
  $RPM_BUILD_ROOT%_datadir/%name/fslint/fstool
install -pm 644 fslint/supprt/fslver \
  $RPM_BUILD_ROOT%_datadir/%name/fslint/supprt
install -pm 755 fslint/supprt/get* \
  $RPM_BUILD_ROOT%_datadir/%name/fslint/supprt
install -pm 755 fslint/supprt/rmlint/* \
  $RPM_BUILD_ROOT%_datadir/%name/fslint/supprt/rmlint

cp -a man/* \
  $RPM_BUILD_ROOT%_mandir/man1/

make -C po DESTDIR=$RPM_BUILD_ROOT LOCALEDIR=%_datadir/locale install

desktop-file-install \
  --vendor author \
  --dir $RPM_BUILD_ROOT%_datadir/applications \
  --mode 644 \
  %name.desktop

%find_lang %name

%files -f %name.lang
%doc doc/*
%_mandir/man1/fslint*
%_bindir/fslint*
%_datadir/%name
%_datadir/applications/*%name.desktop
%_datadir/pixmaps/fslint_icon.png
%exclude %_datadir/%name/fslint/supprt/rmlint/view_ws.sh

%files gnome
%_datadir/%name/fslint/supprt/rmlint/view_ws.sh


%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.42-alt1.1
- Rebuild with Python-2.7

* Wed Jan 12 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.42-alt1
- new version

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.40-alt1.1
- Rebuilt with python 2.6

* Tue Aug 11 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.40-alt1
- new version

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 2.28-alt2
- Remmove depricated update-menus

* Fri Oct 17 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 2.28-alt1
- new version

* Wed Jun 25 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 2.26-alt1
- new version

* Thu Mar 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 2.24-alt2
- Moving of a file view_ws.sh in a separate package fslint-gnome for
  an opportunity to not depend from gnome (#13438)

* Tue Nov 13 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 2.24-alt1
- new version

* Thu Jan 04 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.18-alt0
- initial build
