# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wmbday
Version: 0.3.1
Release: alt5

Summary: This dockapp will remind you of birthdays
Summary(ru_RU.CP1251): Этот апплет будет напоминать вам о днях рождения

License: GPL-2
Group: Graphical desktop/Other
Url: http://buzzinhornetz.ath.cx/code/wmbday/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://buzzinhornetz.ath.cx/code/wmbday/files/%name-%version.tar.gz
Source1: %name.menu

Patch0: %name-0.3.1-alt-warnings-x86_64.patch
Patch1: %name-0.3.1-alt-autotools-support.patch
Patch2: %name-0.3.1-alt-man-kill_x11_path.patch
Patch3: %name-0.3.1-alt-doc-update_my_email.patch

BuildRequires: libXext-devel libXpm-devel

Requires: xmessage

%description
wmbday is a Window Maker dockapp for Linux und FreeBSD that will
remind you of birthdays. It can show up to four names of persons whose
birthday is next. On a particular birthday it will notify you by
highlighting the concerning person. The data is loaded either from a
simple text file or from a vCard file.

%description -l ru_RU.CP1251
wmbday это апплет для Window Maker под Linux и FreeBSD, который будет
напоминать вам о днях рождения. Он отображает четыре имени для людей,
чьи дни рождения будут следующими. В день рождения человека из списка
апплет подсветит имя именинника. Данные могут загружаться из простого
текстового файла или же из vCard файла.

%prep
%setup

# fix modifier for size_t type
%patch0

# add autotools support
%patch1 -p1

# change path to rgb.txt in man page
%patch2

# update my email in ChangeLog
%patch3

rm -f BSDmakefile configure Makefile
chmod -x *.[ch] wmbday.1 wmbday_text.xpm

mv build/wmbday-0.3.1.ebuild build/wmbday.ebuild
mv *.[ch] *.xpm src/
mv data.sample* data/
mv wmbday.1 doc/

autoheader &&
aclocal &&
automake --foreign --add-missing &&
autoconf

%build
export ac_cv_path_XM_PATH=/usr/bin/xmessage
%configure
%make_build CFLAGS="%optflags -Werror -U_FORTIFY_SOURCE" --silent --no-print-directory

%install
%make_install DESTDIR=%buildroot install --silent --no-print-directory
install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog data/data.sample.simple data/data.sample.vcard
%_bindir/%name
%_man1dir/%name.1.*
%_menudir/%name

%changelog
* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 0.3.1-alt5
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Fri Aug 10 2007 Slava Semushin <php-coder@altlinux.ru> 0.3.1-alt4
- Fixed path to rgb.txt in man-page
- Added autotools support
- Update my email address in ChangeLog file
- Removed xmessage from BuildRequires (use ac_cv_path_XM_PATH trick)
- Imported into git and built with gear
- Running make with --no-print-directory and --silent options to make
  terminal output clean

* Sun Nov 26 2006 Slava Semushin <php-coder@altlinux.ru> 0.3.1-alt3
- Fixed build by using -U_FORTIFY_SOURCE
- Spec cleanup:
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/

* Sat Aug 12 2006 Slava Semushin <php-coder@altlinux.ru> 0.3.1-alt2
- Fixed build on x86_64: use %%zu instead of %%d for size_t type

* Wed Jul 26 2006 Slava Semushin <php-coder@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus
- Using -Werror flag for compiler by default

