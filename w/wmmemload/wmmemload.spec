# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wmmemload
Version: 0.1.6
Release: alt6

Summary: This dockapp displays memory and swap space usage
Summary(ru_RU.CP1251): Этот апплет отображает использование памяти и файла подкачки

License: GPL
Group: Graphical desktop/Window Maker
Url: http://markstaggs.net/wmmemload/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://markstaggs.net/wmmemload-download/%name-%version.tar.gz
Source1: %name.menu

Patch0: %name-0.1.6-alt-src-memory_leak_fix.patch
Patch1: %name-0.1.6-alt-warnings-fix.patch
Patch2: %name-0.1.6-alt-src-print_help_fix.patch
Patch3: %name-0.1.6-alt-man-options_fix.patch

# For %%autoreconf (-alt83) macros
BuildPreReq: rpm >= 4.0.4-alt83

BuildRequires: libXt-devel libXext-devel libXpm-devel

%description
Dockapp which displays memory and swap space usage in percent and uses
nice LCD-style.

%description -l ru_RU.CP1251
Апплет отображающий использование оперативной памяти и свопа в
процентах и выполненный в приятном LCD стиле.

%prep
%setup

# avoid autoreconf fails which appear after switch to using git/gear
# http://lists.altlinux.org/pipermail/devel/2007-October/064308.html
rm -rf autom4te.cache

# fix warnings from aclocal
sed -i 's|AC_DEFUN(DA_CHECK_LIB,|AC_DEFUN([DA_CHECK_LIB],|' acinclude.m4
sed -i 's|AC_DEFUN(DA_CHECK_HEADER,|AC_DEFUN([DA_CHECK_HEADER],|' acinclude.m4

# fix Makefile.am
sed -i 's|CPPFLAGS =|AM_CPPFLAGS =|' src/Makefile.am

%patch0
%patch1
%patch2
%patch3

%autoreconf

%build
%configure
%make_build --no-print-directory CFLAGS="%optflags -W -Werror"

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install
install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog THANKS
%_bindir/%name
%_man1dir/%name.1.*
%_menudir/%name

%changelog
* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 0.1.6-alt6
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Mon May 26 2008 Slava Semushin <php-coder@altlinux.ru> 0.1.6-alt5
- Fixed names of some short options in manual page
- Replace %%__autoreconf macros to %%autoreconf

* Fri Oct 05 2007 Slava Semushin <php-coder@altlinux.ru> 0.1.6-alt4
- Spec cleanup:
  + Change my name in Packager tag
  + Updated Url/Source tags
  + Formatted and corrected %%description
  + s/%%setup -q/%%setup/
  + Use builtin %%patch instead of external command
  + Removed useless --with-x option for configure script
- Imported into git and built with gear
  (thanks to Victor Forsyuk aka force@ for help)
- Enable _unpackaged_files_terminate_build

* Sat Jun 03 2006 php-coder <php-coder@altlinux.ru> 0.1.6-alt3
- Fixed build with gcc4.1
- Joined Wall_fix and W_fix patches to warning-fix patch
- Corrected output for --help option
- Use macros %%__autoreconf

* Fri Feb 03 2006 php-coder <php-coder@altlinux.ru> 0.1.6-alt2
- Using -W flag for compiler by default
- Plug memory leak
- Updated BuildRequires for Xorg7
- Give CFLAGS variable to make instead of using %%add_optflags
- Separate changes from sed to patch (Wall_fix)
- More strict names in %%files section
- Dont use macros for sed, install, aclocal, automake and autoconf
  commands
- Dont use --silent option for make in %%build section
- Removed Summary and %%description in koi8-r and utf8 charsets

* Mon Dec 12 2005 php-coder <php-coder@altlinux.ru> 0.1.6-alt1
- Initial build for ALT Linux Sisyphus
- Using -Werror flag for compiler by default

