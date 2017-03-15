Name: cherrytree
Version: 0.38.0
Release: alt1

Summary: Hierarchical note taking application
Summary(ru_RU.UTF-8):  Записная книжка иерархической структуры для заметок

Group: Office
License: GPLv2+
Url: http://www.giuspen.com/cherrytree/

Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: http://www.giuspen.com/software/%name-%version.tar
Patch: categories.patch

BuildArch: noarch

BuildRequires: python-dev
BuildRequires: desktop-file-utils
BuildRequires: gettext

#Requires: python-module-pygtk
#Requires: python-module-pygobject
#Requires: python-module-pygtksourceview
#Requires: python-module-enchant

Requires: %_bindir/7z
Requires: python-module-enchant

%description
CherryTree is a hierarchical note taking application, featuring rich text and
syntax highlighting, storing all the data (including images) in a single XML
file with extension ".ctd".

%description -l ru_RU.UTF-8
Иерархическое хранилище заметок с подсветкой синтаксиса и возможностью
экспорта в различные форматы.

%prep
%setup
%patch -p0
# remove shebang to make rpmlint happy
#sed '/\/usr\/bin\/env/d' modules/main.py > modules/main.py.new && \
#  touch -r modules/main.py modules/main.py.new && \
#  mv modules/main.py.new modules/main.py

%build
%python_build

%install
#python_install
# --skip-build makes it crazy
%__python setup.py install -O2 --root %buildroot

#install -D cherrytree %buildroot%_bindir/%name
rm -rf %buildroot%python_sitelibdir_noarch/

%find_lang %name

%files -f %name.lang
%doc changelog.txt license.txt
%_bindir/%name
%_datadir/%name/
%_datadir/appdata/%name.appdata.xml
%_datadir/application-registry/%name.applications
%_desktopdir/%name.desktop
%_datadir/mime-info/*
%_iconsdir/hicolor/scalable/apps/%%name.svg
%_datadir/mime/packages/%name.xml
%_man1dir/*.1*
#_datadir/locale/*


%changelog
* Wed Mar 15 2017 Konstantin Artyushkin <akv@altlinux.org> 0.38.0-alt1
- new version

* Mon Oct 10 2016 Konstantin Artyushkin <akv@altlinux.org> 0.37.5-alt1
- new version

* Fri Mar 25 2016 Konstantin Artyushkin <akv@altlinux.org> 0.36.3-alt3
- fix spellcheck requares

* Wed Jan 13 2016 Konstantin Artyushkin <akv@altlinux.org> 0.36.3-alt2
- new version 0.36.3

* Fri Aug 14 2015 Konstantin Artyushkin <akv@altlinux.org> 0.35.9-alt2
- -- initial new version 0.35.9 

* Fri Aug 01 2014 Konstantin Artyushkin <akv@altlinux.org> 0.33.4-alt4
- 0.33.4-alt3 categories.patch
- new build 0.33.4-alt4 (with rpmlog script)
- plus categories.patch
- plus categories.patch

* Thu Jul 31 2014 Konstantin Artyushkin <akv@altlinux.org> 0.33.4-alt3
- + datadir/appadata/name.appdata.xml

* Wed Jul 23 2014 Konstantin Artyushkin <akv@altlinux.org> 0.33.4-alt2
+ Update to 0.33.4-alt2 

* Tue Apr 15 2014 Konstantin Artyushkin <akv@altlinux.org> 0.32.0-alt3
+ 0.32.0-alt3 tag 

* Mon Apr 07 2014 akv <akv@altlinux.org> 0.32.0-alt2.M70P.1
- change packager 

* Sun Feb 23 2014 bla-bla <bla-bla@altlinux.org> 0.32.0-alt1.M70P.2
- fixes

* Sun Feb 23 2014 bla-bla <bla-bla@altlinux.org> 0.32.0-alt1.M70P.1
- 32.0 version

* Fri Sep 6 2013 Robin Lee <cheeselee@altlinux.org> - 0.30.5-alt1.M70P1
- Update to 0.30.5

* Wed Jan 25 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.2-1
- Update to 0.25.2

* Sun Jan 22 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25.1-1
- Update to 0.25.1

* Mon Jan 16 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.25-1
- Update to 0.25

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 31 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.24-1
- Update to 0.24

* Thu Nov  3 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.23.1-1
- Update to 0.23.1
- Add manuall python(abi) requirement

* Thu Jun 23 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.22.1-1
- Update to 0.22.1

* Sun Apr 25 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.21-1
- Update to 0.21

* Tue Mar 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.20.1-1
- Update to 0.20.1

* Tue Mar 08 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.20.1-1
- Update to 0.20

* Sat Jan 22 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-2
- Omit %%{_datadir}/application-registry/ and %%{_datadir}/mime-info/

* Fri Jan 21 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-2
- Remove useless egg and manually add python(abi) requirement

* Mon Jan 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.3-1
- Update to 0.19.3

* Sat Jan 15 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.2-1
- Update to 0.19.2
- Drop cherrytree.glade.h again
- Make sure cherrytree.desktop is not executable

* Tue Jan 11 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19.1-1
- Update to 0.19.1
- Use setup.py instead of manual installation
- BR python2-devel instead of python-devel

* Tue Jan 04 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19-2
- Drop cherrytree.glade.h

* Mon Jan 03 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.19-1
- Update to 0.19

* Wed Dec 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.18.1-1
- Update to 0.18.1

* Mon Dec 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.17.1-1
- Inital package
