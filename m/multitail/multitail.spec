Summary: multitail lets you view one or multiple files like the original tail program.
Summary(ru_RU.KOI8-R): multitail позволяет просматривать один или несколько файлов
Name: multitail
Version: 7.0.0
Release: alt1
License: Apache-2.0
Group: Monitoring
Source: %name-%version.tar.gz
Patch1:		https://sources.debian.org/data/main/m/multitail/6.5.0-5/debian/patches/fix-format-strings.diff
Patch2:		https://github.com/folkertvanheusden/multitail/commit/608bad75a9acf51e2283768996721bd549149991.patch

URL: http://www.vanheusden.com/multitail/
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Fri May 18 2007
BuildRequires: libncurses-devel libtinfo-devel libncursesw-devel cmake

%description
multitail lets you view one or multiple files like the original tail program.
The difference is that it creates multiple windows on your console (with 
ncurses). It can also use colors while displaying the logfiles, for faster
recognition of which lines are important and which are not. It supports regular
expressions. It has interactive menus for editing given regular expressions and
deleting and adding windows.

%description -l ru_RU.KOI8-R
multitail позволяет просматривать один или несколько файлов подобно оригинальной 
программе tail. Различие заключается в том, что она создает множественные окна в консольном
окне (с использованием ncurses). Так же для отображения файлов журналов могут использоваться цвета
для визуального отделения важных и неважных строк в журнале. multitail поддерживает 
регулярные выражения. Програма имеет интерактивную систему меню для редактирования регулярных выражений
и работы с окнами.

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1
# Fix correct version
sed -i 's/6.4.3/7.0.0/' CMakeLists.txt
# Let rpm handle the config file
sed -i '/multitail.conf.new/d' CMakeLists.txt
# Install conversion-scripts manually
sed -i '/conversion-scripts/d' CMakeLists.txt
# Only build cmake version
rm GNUmakefile

%build
%cmake
%cmake_build

%install
%cmake_install

# Create necessary directories
mkdir -p %{buildroot}%{_sysconfdir}

install -D -m 644 $RPM_BUILD_DIR/%name-%version/%name.conf $RPM_BUILD_ROOT/%_sysconfdir/%name.conf.new
bzip2 -9 $RPM_BUILD_ROOT/%_man1dir/multitail.1
rm -f $RPM_BUILD_ROOT/%_datadir/doc/%name-VERSION=7.0.0/*
rmdir $RPM_BUILD_ROOT/%_datadir/doc/%name-VERSION=7.0.0/

%files
%_bindir/%name
%_man1dir/%name.1.*
%config(noreplace) %_sysconfdir/%name.conf.new
%doc INSTALL README.md LICENSE manual.html %name.conf

%changelog
* Wed Dec 07 2022 Ilya Mashkin <oddity@altlinux.ru> 7.0.0-alt1
- 7.0.0
- Change License from GPL2 to Apache2
- Build with cmake only

* Wed Jun 08 2022 Ilya Mashkin <oddity@altlinux.ru> 6.5.2-alt1
- 6.5.2

* Tue Feb 15 2022 Ilya Mashkin <oddity@altlinux.ru> 6.5.1-alt1
- 6.5.1 (A kind of fork with same name)

* Fri Jan 10 2020 Ilya Mashkin <oddity@altlinux.ru> 6.5.0-alt2
- Try to find/to not ignoring multitail.conf file (Closes: #37738) 

* Wed Jan 08 2020 Ilya Mashkin <oddity@altlinux.ru> 6.5.0-alt1
- 6.5.0

* Thu Dec 10 2015 Ilya Mashkin <oddity@altlinux.ru> 6.4.2-alt1
- 6.4.2

* Tue Feb 17 2015 Ilya Mashkin <oddity@altlinux.ru> 6.4.1-alt1
- 6.4.1

* Tue Feb 25 2014 Ilya Mashkin <oddity@altlinux.ru> 6.2.1-alt1
- 6.2.1

* Wed Dec 04 2013 Ilya Mashkin <oddity@altlinux.ru> 6.0-alt1
- 6.0

* Mon Jun 24 2013 Ilya Mashkin <oddity@altlinux.ru> 5.2.13-alt1
- 5.2.13

* Sun Jan 20 2013 Ilya Mashkin <oddity@altlinux.ru> 5.2.12-alt1
- 5.2.12

* Sun Dec 09 2012 Ilya Mashkin <oddity@altlinux.ru> 5.2.11-alt1
- 5.2.11
- fix url

* Mon Jan 02 2012 Ilya Mashkin <oddity@altlinux.ru> 5.2.9-alt1
- 5.2.9

* Sat Apr 16 2011 Ilya Mashkin <oddity@altlinux.ru> 5.2.8-alt1
- 5.2.8

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 5.2.7-alt2
- add noreplace to %_sysconfdir/%name.conf (Closes: #24956)

* Thu Jan 20 2011 Ilya Mashkin <oddity@altlinux.ru> 5.2.7-alt1
- 5.2.7

* Fri Feb 19 2010 Ilya Mashkin <oddity@altlinux.ru> 5.2.6-alt1
- 5.2.6

* Mon Feb 15 2010 Ilya Mashkin <oddity@altlinux.ru> 5.2.5-alt1
- 5.2.5

* Mon May 26 2008 Ilya Mashkin <oddity@altlinux.ru> 5.2.2-alt1
- 5.2.2

* Tue Feb 26 2008 Ilya Mashkin <oddity@altlinux.ru> 5.2.1-alt1
- 5.2.1

* Tue Aug 07 2007 Ilya Mashkin <oddity@altlinux.ru> 5.2.0-alt1
- new stable version 5.2.0

* Sun Jun 17 2007 Ilya Mashkin <oddity@altlinux.ru> 5.0.5-alt1
- new stable version 5.0.5

* Wed Jun 06 2007 Ilya Mashkin <oddity@altlinux.ru> 5.0.4-alt1
- new stable version 5.0.4

* Fri May 18 2007 Ilya Mashkin <oddity@altlinux.ru> 5.0.3-alt1
- new stable version 5.0.3

* Mon Jan 01 2007 Ilya Mashkin <oddity@altlinux.ru> 4.2.0-alt2
- fixed #8963, #5117

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 4.2.0-alt1
- new version

* Thu Apr 01 2004 Egor S. Orlov <oes@altlinux.ru> 3.0.6-alt1
- new version 

* Fri Oct 03 2003 Egor S. Orlov <oes@altlinux.ru> 3.0.0-alt1
- New version 

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 2.9.1-alt0.2
- Added URL
- Added russian translation for summary and description

* Mon Jul 14 2003 Egor S. Orlov <oes@altlinux.ru> 2.9.1-alt0.1
- Initial build for ALT
- Cleanup spec
- Added doc

* Tue Apr 22 2003 Udo van den Heuvel <udovdh@yahoo.com>
- initial RPM

