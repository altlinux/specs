# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: fbpager
Version: 0.1.4
Release: alt8

Summary: Workspaces pager for Fluxbox
Summary(ru_RU.CP1251): Пейджер рабочих столов для Fluxbox

License: MIT
Group: Graphical desktop/Other
Url: http://old.fluxbox.org/fbpager/
Packager: Afanasov Dmitry <ender@altlinux.ru>

Source0: http://fluxbox.org/download/%name-%version.tar.gz
Source1: %name.menu

Patch1: %name-0.1.4-alt-warnings-Wall_fix.patch

Requires: fluxbox >= 0.9.13-alt2
Provides: fluxter >= 0.1.0-alt1
Obsoletes: fluxter >= 0.1.0-alt1

BuildRequires: gcc-c++ libXt-devel libXrender-devel

%description
Workspaces pager. Was developeed specifically for use in conjunction
with Fluxbox window manager. It is highly configurable and moreover
supports transparency.

%description -l ru_RU.CP1251
Пейджер рабочих столов. Предназначен специально для использования в
менеджере окон Fluxbox. Поддерживает прозрачность и возможность гибкой
настройки "под себя".

%prep
%setup

#patch1 -p1

%build
%autoreconf
%configure
%make_build --silent --no-print-directory CXXFLAGS="%optflags -Wno-strict-aliasing"

%install
%make_install --silent --no-print-directory DESTDIR=%buildroot install

install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc ChangeLog COPYING README
%_bindir/%name
%_menudir/%name

%changelog
* Wed Apr 15 2009 Afanasov Dmitry <ender@altlinux.org> 0.1.4-alt8
- 8e0927e... from git://git.fluxbox.org/fbpager.git.
  + Added autogen.sh from fluxbox and regenerated autogen/autoconf files

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.4-alt7
- removed obsolete %%update_menus/%%clean_menus calls

* Tue Nov 25 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.4-alt6
- 40f09b8... from git://git.fluxbox.org/fbpager.git.
- remove unused patches (alt-fix-build, deb-src-gcc4_fix).
- disable Wall_fix patch.

* Thu Nov 06 2008 Afanasov Dmitry <ender@altlinux.org> 0.1.4-alt5
- fix gcc4.3 build (and some another errors)
- change packager and pickup package from orphaned

* Mon Jun 25 2007 Slava Semushin <php-coder@altlinux.ru> 0.1.4-alt4
- Changes in patches:
  + memory_leak_fix: don't mention about me
  + Wall_fix: use static_cast<> instead of C style casting
- Spec cleanup:
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/
  + Removed useless --with-x option for configure script
- Imported into git and built with gear

* Wed Oct 11 2006 Slava Semushin <php-coder@altlinux.ru> 0.1.4-alt3
- Fixed build:
  + Added patch from Debian for building with gcc4
    (debian #357774, gentoo #135504)
  + Updated Wall_fix patch (thnx to damir@)
  + Build with -Wno-strict-aliasing
- Spec cleanup:
  + Change my name in Packager tag
  + Dont use macros in Url tag
  + Added full url to Source tag
  + Formatted %%description and %%changelog
- Enable _unpackaged_files_terminate_build

* Mon Feb 13 2006 php-coder <php-coder@altlinux.ru> 0.1.4-alt2
- Using -Werror flag for compiler by default
- Plug memory leak
- Updated BuildRequires for Xorg7
- Running make with --no-print-directory and --silent options to make
  terminal output clean
- Removed INSTALL file from package
- Fixed orthographical errors in %%changelog (spotted by mike@)
- More strict names in %%files section
- Dont use macros for install command
- Removed Summary and %%description in koi8-r and utf8 charsets

* Thu Jun 02 2005 php-coder <php-coder@altlinux.ru> 0.1.4-alt1.1
- Use macros %%__install instead of %%__cp (#6950)
- Fixed tag Obsoletes (correctly release for fluxter)

* Wed May 18 2005 php-coder <php-coder@altlinux.ru> 0.1.4-alt1
- First build for Sisyphus
- Requires fluxbox 0.9.13-alt2
- Fbpager is available in Session/Tools submenu
- Updated BuildRequires
- Added Provides and Obsoletes for fluxter (suggestion from kas@)
- Added needs=fluxbox to menu-file
- Changed Packager's email
- Fixed %%description, so that is doesn't start with %%name macros
- Added %%description and Summary in English and in Russian in KOI8-R
  and UTF-8 charset
- %%setup is called with -q option to make terminal output clean
- longtitle in English

