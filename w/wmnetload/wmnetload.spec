# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: wmnetload
Version: 1.3
Release: alt6

Summary: dockapp which monitor network interfaces
Summary(ru_RU.UTF-8): апплет, который следит за сетевыми интерфейсами

License: GPLv2
Group: Graphical desktop/Window Maker
Url: http://freshmeat.net/projects/wmnetload/
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: %name-%version.tar.bz2
Source1: %name.menu
Source2: %name.1

Patch0: wmnetload-alt-warnings-fix.patch
Patch1: wmnetload-alt-configure-rpath_fix.patch
Patch2: wmnetload-alt-autotools-warnings_fix.patch

BuildRequires: libdockapp-devel libICE-devel libXext-devel

%description
wmnetload is a network interface monitor dockapp for Window Maker. It
is designed to fit well with dockapps like wmcpuload and wmmemmon. It
tracks whether the interface is functioning and displays current
network interface throughput, along with an auto-scaling graph of
recent network activity (the graph separates upstream and downstream
traffic load cleanly without resorting to colors).

%description -l ru_RU.UTF-8
wmnetload это апплет для Window Maker, который следит за сетевыми
интерфейсами. Он имеет такой же дизайн как wmcpuload и wmmemmon. Он
отслеживает работает ли интерфейс, и показывает поток, проходящий
через него, вместе с автомасштабируемым графиком недавней сетевой
активности (график разделяет входящий и исходящий трафик очень четко,
не прибегая к использованию цветов).

%prep
%setup
%patch0 -p1
%patch1 -p2
%patch2 -p2

%autoreconf

%build
%configure
%make_build CFLAGS="%optflags -Werror" --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory
install -pD -m 644 %SOURCE1 %buildroot%_menudir/%name
install -pD -m 644 %SOURCE2 %buildroot%_man1dir/%name.1

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name
%_man1dir/%name.1.*
%_menudir/%name

%changelog
* Tue Jan 04 2011 Slava Semushin <php-coder@altlinux.ru> 1.3-alt6
- Imported manual page from Debian (deb #608580)
- Spec cleanup

* Sat Nov 29 2008 Slava Semushin <php-coder@altlinux.ru> 1.3-alt5
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
- More proper License tag
- Spec cleanup:
  + Replaced %%__autoreconf macros to %%autoreconf
  + Removed useless --with-x option for configure script
  + Use builtin %%patch instead of external command
  + s/%%setup -q/%%setup/

* Fri Oct 06 2006 Slava Semushin <php-coder@altlinux.ru> 1.3-alt4
- Updated BuildRequires for Xorg7
- Changed my name in Packager tag
- Added url to Source tag
- Enable _unpackaged_files_terminate_build
- Give CFLAGS variable to make instead of using %%add_optflags
- Dont use macros for patch, install and sed commands
- More strict names in %%files section
- Use macros %%__autoreconf
- Formatted %%description
- Removed Summary and %%description in koi8-r and utf8 charsets
- Fixed orthographical errors in %%changelog (thnx to mike@)

* Fri Dec 09 2005 php-coder <php-coder@altlinux.ru> 1.3-alt3
- Running make with --no-print-directory and --silent options to make
  terminal output clean
- Added patch which fixes warnings from compiler (thnx Yuriy Kashirin
  <kashirin@emict.com> for help)
- Using -Werror flag for compiler by default

* Thu Nov 17 2005 php-coder <php-coder@altlinux.ru> 1.3-alt2
- Removed all pragma directives (grep + xargs + sed)

* Fri Oct 21 2005 php-coder <php-coder@altlinux.ru> 1.3-alt1
- Initial build for ALT Linux

