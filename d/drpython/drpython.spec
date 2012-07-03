Name: drpython
Version: 3.11.0
Release: alt1.1.qa2.1
Epoch: 1

Summary: Python editor and development environment
Summary(ru_RU.KOI8-R): Среда разработки и редактор для языка Python

Url: http://drpython.sourceforge.net/
License: GPL
Group: Development/Python

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Source1: %name.desktop

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildPreReq: python-devel
BuildRequires: ImageMagick, rpm-build-compat >= 1.2
Requires: python-module-wx >= 2.6
Requires: webclient
BuildRequires: desktop-file-utils

%description
DrPython is a highly customizable, simple, and clean editing environment for
developing Python programs. It is intended primarily for use in schools, and
is a tribute to DrScheme.

%description -l ru_RU.KOI8-R
DrPython -- это хорошо настраиваемая простая среда для разработки программ
на Python, первоначально предназначенная для использования в школах.
Сделан он по подобию DrScheme.

%prep
%setup -q -n %name
chmod 644 %name.py

# Fix default paths to docs
sed -i "s/mozilla/url_handler.sh/" drPreferences.py
sed -i "s|http://www.python.org/doc/current/|%_docdir/python-doc-2.4.2/index.html|" drPreferences.py
sed -i "s|http://www.wxwidgets.org/docs.htm|%_docdir/wxGTK2-doc-2.6.2|" drPreferences.py

# Change Windows line endings to Unix line endings
for file in $(find *.txt *.TXT -type f); do
  sed -i 's/\r//' $file
done

# Remove Windows related files and patch the setup.py file so it doesn't rely on the file
rm -rf tools/
rm -f setup.cfg

%build
%python_build

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/%name/documentation
cp *.py* %buildroot%_datadir/%name
cp -r examples bitmaps %buildroot%_datadir/%name
cp -r documentation/* %buildroot%_datadir/%name/documentation/

echo '#!/bin/bash' > %buildroot%_bindir/%name
#echo 'cd %_datadir/%name' >> %buildroot%_bindir/%name
echo 'python %_datadir/%name/drpython.py' >> %buildroot%_bindir/%name
chmod 755 %buildroot%_bindir/%name

install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

#icons
mkdir -p %buildroot%_liconsdir
convert -size 16x16 documentation/%name.png %buildroot%_liconsdir/%name.png
mkdir -p %buildroot%_niconsdir
convert -size 32x32 documentation/%name.png %buildroot%_niconsdir/%name.png
mkdir -p %buildroot%_miconsdir
convert -size 48x48 documentation/%name.png %buildroot%_miconsdir/%name.png

rm -rf %buildroot%_datadir/drpython/bitmaps/24/.xvpics
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=IDE \
	%buildroot%_desktopdir/drpython.desktop

%files
%doc examples/ *.txt
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_niconsdir/%name.png
%_miconsdir/%name.png

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:3.11.0-alt1.1.qa2.1
- Rebuild with Python-2.7

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.11.0-alt1.1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for drpython

* Sun Dec 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:3.11.0-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for drpython
  * postclean-05-filetriggers for spec file

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.11.0-alt1.1
- Rebuilt with python 2.6

* Mon Jul 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1:3.11.0-alt1
- new version (3.11.0)
- set Epoch to 1
- replace Debian menu with desktop file
- sync spec with Fedora's spec

* Mon Feb 18 2008 Vitaly Lipatov <lav@altlinux.ru> 165-alt2
- rebuild with python 2.5

* Fri Oct 12 2007 Vitaly Lipatov <lav@altlinux.ru> 165-alt1
- new version 165 (with rpmrb script)

* Sun Feb 25 2007 Vitaly Lipatov <lav@altlinux.ru> 164-alt1
- new version

* Tue Nov 01 2005 Vitaly Lipatov <lav@altlinux.ru> 161-alt1
- new version

* Tue Aug 02 2005 Vitaly Lipatov <lav@altlinux.ru> 3.10.13-alt1
- new version

* Fri Mar 25 2005 Vitaly Lipatov <lav@altlinux.ru> 3.10.12-alt1.1
- rebuild with python 2.4 and wxPython 2.5.4

* Tue Mar 01 2005 Vitaly Lipatov <lav@altlinux.ru> 3.10.12-alt1
- new version

* Sat Feb 12 2005 Vitaly Lipatov <lav@altlinux.ru> 3.10.1-alt1
- new version

* Thu Feb 10 2005 Vitaly Lipatov <lav@altlinux.ru> 3.9.10-alt1
- new version (fixed bug #5644)

* Mon Jan 24 2005 Vitaly Lipatov <lav@altlinux.ru> 3.9.2-alt1
- new version

* Mon Jan 17 2005 Vitaly Lipatov <lav@altlinux.ru> 3.8.5-alt1
- new version

* Mon Jan 10 2005 Vitaly Lipatov <lav@altlinux.ru> 3.8.4-alt1
- new version

* Wed Jan 05 2005 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version

* Thu Dec 23 2004 Vitaly Lipatov <lav@altlinux.ru> 3.7.9-alt1
- new version

* Mon Dec 06 2004 Vitaly Lipatov <lav@altlinux.ru> 3.7.3-alt1
- new version

* Fri Dec 03 2004 Vitaly Lipatov <lav@altlinux.ru> 3.6.12-alt2
- fix spec and menu entry
- add require for new python-module-wx

* Tue Nov 30 2004 Vitaly Lipatov <lav@altlinux.ru> 3.6.12-alt1
- first build for ALT Linux Sisyphus

* Tue Nov 09 2004 Jerome Soyer <saispo@mandrake.org> 3.6.10-1mdk
- 3.6.10

* Sat Nov 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.6.9-1mdk
- 3.6.9
- install documentation in the right path

* Fri Oct 29 2004 Jerome Soyer <saispo@mandrake.org> 3.6.6-1mdk
- 3.6.6

* Wed Oct 27 2004 Jerome Soyer <saispo@mandrake.org> 3.6.5-1mdk
- 3.6.5

* Tue Oct 26 2004 Jerome Soyer <saispo@mandrake.org> 3.6.4-1mdk
- 3.6.4

* Sat Oct 23 2004 Jerome Soyer <saispo@mandrake.org> 3.6.3-1mdk
- 3.6.3

* Fri Oct 22 2004 Jerome Soyer <saispo@mandrake.org> 3.6.2-1mdk
- 3.6.2

* Thu Oct 21 2004 Jerome Soyer <saispo@mandrake.org> 3.6.1-1mdk
- 3.6.1

* Tue Oct 19 2004 Jerome Soyer <saispo@mandrake.org> 3.6.0-1mdk
- 3.6.0

* Mon Oct 11 2004 Jerome Soyer <saispo@mandrake.org> 3.5.9-1mdk
- 3.5.9

* Sat Oct 09 2004 Jerome Soyer <saispo@mandrake.org> 3.5.8-1mdk
- 3.5.8

* Wed Oct 06 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.6-1mdk
- 3.5.6

* Thu Sep 30 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.3-1mdk
- 3.5.3

* Thu Sep 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.5.0-1mdk
- 3.5.0

* Mon Sep 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.7-1mdk
- 3.4.7

* Wed Sep 08 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.5-1mdk
- 3.4.5

* Wed Sep 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.3-1mdk
- 3.4.3

* Thu Aug 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.4.0-1mdk
- 3.4.0

* Fri Aug 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.7-1mdk
- 3.3.7

* Fri Aug 13 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.3-1mdk
- 3.3.3

* Mon Aug 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.3.2-1mdk
- 3.3.2

* Mon Aug 2 2004 Austin Acton <austin@mandrake.org> 3.3.0-1mdk
- 3.3.0

* Thu Jul 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.2.0-1mdk
- 3.2.0

* Fri Jun 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.7-1mdk
- 3.0.7

* Tue Jun 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.6-1mdk
- 3.0.6

* Sat Jun 19 2004 Austin Acton <austin@mandrake.org> 3.0.4-1mdk
- 3.0.4

* Mon Jun 14 2004 Austin Acton <austin@mandrake.org> 3.0.1-1mdk
- 3.0.1
- new menu

* Fri Apr 2 2004 Austin Acton <austin@mandrake.org> 2.3.5-1mdk
- 2.3.5

* Sun Feb 22 2004 Austin Acton <austin@mandrake.org> 2.2.7-1mdk
- 2.2.7

* Fri Feb 21 2004 Austin Acton <austin@mandrake.org> 2.2.6-1mdk
- 2.2.6

* Sun Feb 15 2004 Austin Acton <austin@mandrake.org> 2.2.3-1mdk
- 2.2.3

* Mon Feb 9 2004 Austin Acton <austin@mandrake.org> 2.2.1-1mdk
- 2.2.1

* Sun Feb 8 2004 Austin Acton <austin@mandrake.org> 2.1.4-2mdk
- oops, make it run (James Sparenberg)
- put in /usr/share

* Wed Jan 28 2004 Austin Acton <austin@mandrake.org> 2.1.4-1mdk
- 2.1.4

* Sat Jan 24 2004 Austin Acton <austin@mandrake.org> 2.1.0-1mdk
- 2.1.0

* Sat Jan 17 2004 Austin Acton <austin@mandrake.org> 2.0.3-1mdk
- 2.0.3

* Wed Jan 14 2004 Franck Villaume <fvill@freesurf.fr> 2.0.2-2mdk
- BuildRequires : ImageMagick

* Thu Jan 8 2004 Austin Acton <austin@linux.ca> 2.0.2-1mdk
- initial package
