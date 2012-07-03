%define realversion 1.0a16

Name: avinfo
Version: 1.0
Release: alt2.a16

Summary: AVInfo is a utility for output information about AVI files
Summary(ru_RU.KOI8-R): AVInfo - программа для вывода информации об AVI файлах
Group: Video
License: GPL
URL: http://www.shounen.ru/soft/avinfo/

Source: %url/avinfo-%realversion.zip
Patch: avinfo-1.0-gcc3.4.patch
Patch1:  avinfo-1.0-config.h.patch
Patch2:  avinfo-1.0-gcc4.patch

# Automatically added by buildreq on Mon Feb 28 2005
BuildRequires: unzip

%description
AVInfo is a utility for displaying AVI header information. It returns the
length of a clip, FPS, resolution, codec, sound parametrs, and the number
and type of streams, including detailed information for each.

%description -l ru_RU.KOI8-R
AVInfo - программа для быстрого вывода на экран или в файл информации об
avi файлах. Полная, максимально возможная информативность, мощные средства
автоматизации обработки группы файлов, совместимость с другими приложениями.
Высокая настраиваемость внешнего вида и формы вывода сочетается с широчайшим
набором готовых шаблонов. Компактная, быстрая - она незаменима для повседневной
работы с видео файлами.
Программа не требует дополнительных настроек - просто запустите ее с именем
желаемого файла - и вы получите полную и достоверную информацию на экран.

%prep
%setup -q -c %name-%realversion
%patch -p1
%patch1 -p1
%patch2 -p1
find -type f -print0 | xargs -r0 sed -i 's,,,g 
s,,,g'

%build
mkdir -p doc
%define win_files readme.rus.txt whatsnew.rus
for f in %win_files; do
iconv -c -s -f windows-1251 -t koi8-r -o doc/$f $f || :
sed -i 's| Windows-1251 codepage, CRLF text||' doc/$f
done

pushd src
sed -i 's/-DMAKEFILE_WIN/-DCFG_PATH_STYLE_UNIX/g' Makefile
%make_build CXX="gcc %optflags"
popd

%install
install -pD src/%name %buildroot%_bindir/%name
install -pD -m644 src/avinfo.tpl %buildroot%_sysconfdir/%name/templates
install -pD -m644 src/avinfo.cfg %buildroot%_sysconfdir/%name/default.conf

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/templates
%config(noreplace) %_sysconfdir/%name/default.conf
%_bindir/*
%doc doc/* CHANGELOG

%changelog
* Thu May 27 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 1.0-alt2.a16
- fix build with gcc4

* Wed Sep 28 2005 Victor Forsyuk <force@altlinux.ru> 1.0-alt1.a16
- 1.0a16

* Mon Feb 28 2005 Victor Forsyuk <force@altlinux.ru> 1.0-alt1.a15
- 1.0a15

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.4-alt1
- 0.7.4

* Sat Aug 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Wed Jun 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Mar 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Fri Mar 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Fri Feb 14 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6-alt1
- 0.6

* Mon Feb 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt0.5
- new version.

* Thu Jan 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt0.5b
- First build for Sisyphus.
