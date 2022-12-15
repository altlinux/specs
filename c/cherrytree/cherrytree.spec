Name: cherrytree
Version: 0.99.53
Release: alt1

Summary: Hierarchical note taking application
Summary(ru_RU.UTF-8): Записная книжка иерархической структуры для заметок

Group: Office
License: GPLv2+
Url: http://www.giuspen.com/cherrytree/

Packager: Konstantin Artyushkin <akv@altlinux.org>

# Source-url: https://www.giuspen.com/software/cherrytree_%version.tar.xz
Source: %name-%version.tar
Patch: categories.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libgtkmm3-devel
BuildRequires: libxml++2-devel
BuildRequires: libgtksourceviewmm3-devel
BuildRequires: libsqlite3-devel
BuildRequires: libgspell-devel
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel
BuildRequires: gnome-icon-theme
BuildRequires: libuchardet-devel
BuildRequires: libcurl-devel
BuildRequires: libfribidi-devel
BuildRequires: libvte3-devel

Requires: %_bindir/7z

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
%ifarch %e2k
# workaround for EDG frontend
sed -i "s|g_autofree gchar\*|g_autofree_edg_ex(gchar,Glib::ustring) |" src/ct/ct_{misc_utils,storage_xml}.cc
sed -i "s|g_autofree gchar\*|g_autofree_edg_ex(gchar,std::string) |" src/ct/ct_*.cc
sed -i "s|pConverted+|(gchar*)&|" src/ct/ct_misc_utils.cc
sed -i "s|save_to_buffer(|&(gchar*\&)|" src/ct/ct_{imports,image,parser_html}.cc
sed -i "s|filename(pOutStr|filename((gchar*)pOutStr|" src/ct/ct_filesystem.cc
%endif

%build
%cmake  -DBUILD_TESTING=OFF -DCT_VERSION=%version
%cmake_build

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%doc changelog.txt license.txt
%_bindir/%name
#_datadir/metainfo/com.giuspen.%name.metainfo.xml
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/mime-info/*
%_iconsdir/hicolor/scalable/apps/%%name.svg
%_datadir/mime-info/%name.*
%_man1dir/*.1*


%changelog
* Thu Dec 15 2022 Vitaly Lipatov <lav@altlinux.ru> 0.99.53-alt1
- NMU: new version 0.99.53 (with rpmrb script)
- NMU: add BR: libfribidi-devel, libvte3-devel

* Tue Jan 18 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.99.40-alt1.1
- g_autofree workaround for the E2K compiler

* Fri Aug 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.99.40-alt1
- NMU: new version 0.99.40 (with rpmrb script)

* Fri Mar 12 2021 Konstantin Artyushkin <akv@altlinux.org> 0.99.31-alt1
- New Version

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.38.5-alt1.qa1
- NMU: applied repocop patch

* Wed Sep 12 2018 Konstantin Artyushkin <akv@altlinux.org> 0.38.5-alt1
- new version

* Wed Sep 20 2017 Konstantin Artyushkin <akv@altlinux.org> 0.38.2-alt1
- new version

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
