# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wmdiskmon
Version: 0.0.2
Release: alt3

Summary: This dockapp monitors your disks usage
Summary(ru_RU.CP1251): Ётот апплет следит за использованием вашего жесткого диска

License: GPL
Group: Graphical desktop/Window Maker
Url: http://tnemeth.free.fr/projets/dockapps.html
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: http://tnemeth.free.fr/projets/programmes/%name-%version.tar.gz
Source1: %name.menu

Patch0: %name-alt-warnings-Wall_fix.patch
Patch1: %name-alt-warnings-W_fix.patch
Patch2: %name-alt-src-print_help_fix.patch
Patch3: %name-alt-src-memory_leak_fix.patch
Patch4: %name-alt-src-shorter_paths.patch

BuildRequires: libXt-devel libXext-devel libXpm-devel

%description
Dockapp which displays disk usage in percent and uses nice LCD-style.
May show load for a number of disks.

%description -l ru_RU.CP1251
јпплет отображающий использование жесткого диска в процентах и
выполненный в при€тном LCD стиле. ћожет показывать загруженность сразу
нескольких дисков.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure --with-x
%make_build --no-print-directory CFLAGS="%optflags -W -Werror -U_FORTIFY_SOURCE"

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install
install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc AUTHORS ChangeLog THANKS TODO
%_bindir/%name
%_man1dir/%name.1.*
%_menudir/%name

%changelog
* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 0.0.2-alt3
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)

* Fri Oct 26 2007 Slava Semushin <php-coder@altlinux.ru> 0.0.2-alt2
- Added shorter_paths patch which make paths more shortest:
  + skips /dev directory in device path
  + skips /mnt or /media directory in mount point path
- Imported into git and built with gear

* Thu Mar 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.0.2-alt1.1
- NMU based on spec from Slava Semushin <php-coder@>

* Tue Mar 06 2007 Slava Semushin <php-coder@altlinux.ru> 0.0.2-alt1
- Updated to 0.0.2
- Adapted print_help_fix patch

* Sun Nov 26 2006 Slava Semushin <php-coder@altlinux.ru> 0.0.1-alt3
- Fixed build by using -U_FORTIFY_SOURCE
- Spec cleanup:
  + Change my name in Packager tag
  + Formatted %%description
  + Dont mention about Fluxbox and another WMs in %%description
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/
- Enable _unpackaged_files_terminate_build

* Tue Jan 31 2006 php-coder <php-coder@altlinux.ru> 0.0.1-alt2
- Using -W flag for compiler by default
- Plug memory leak
- Corrected output for --help option
- Updated BuildRequires for Xorg7
- Give CFLAGS variable to make instead of using %%add_optflags
- More strict names in %%files section
- Dont use macros for patch and install commands
- Dont use --silent option for make in %%build section
- Removed Summary and %%description in koi8-r and utf8 charsets

* Sun Dec 11 2005 php-coder <php-coder@altlinux.ru> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
- Using -Werror flag for compiler by default

