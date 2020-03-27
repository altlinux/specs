# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: scrot
Version: 0.8
Release: alt3

Summary: Screen-shot capture using Imlib 2
License: MIT-feh
Group: Graphical desktop/Other
Url: https://github.com/resurrecting-open-source-projects/scrot
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Source: %name-%version.tar
Patch0: scrot-alt-warnings-fix.patch
Patch1: scrot-alt-makefile-fix.patch
Patch2: scrot-alt-deb-man-typos_fix.patch
Patch3: scrot-upstream-fix-gcc8-Wstringop-truncation.patch

BuildRequires: libgiblib-devel libX11-devel imlib2-devel libfreetype-devel
BuildRequires: libXext-devel

%description
A nice and straightforward screen capture utility implementing the
dynamic loaders of imlib2.

%prep
%setup
%patch0 -p2

# remove own getopt version
rm -fv -- src/getopt*
%patch1 -p2

%patch2 -p2
rm -f configure.in

%patch3 -p1

%build
%autoreconf
%configure
%make_build CFLAGS="%optflags -Werror" --silent --no-print-directory

%install
%makeinstall_std --silent --no-print-directory

%files
%_bindir/%name
%_man1dir/%name.1.*
%_defaultdocdir/%name-%version/

%changelog
* Fri Mar 27 2020 Dmitriy Khanzhin <jinn@altlinux.org> 0.8-alt3
- built by new scheme
- fixed FTBFS (backported from upstream)
- updated License tag (identified by nomossa)
- changed Url
- changed packager

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8-alt2.qa1
- NMU: rebuilt for debuginfo.

* Sat Apr 11 2009 Slava Semushin <php-coder@altlinux.ru> 0.8-alt2
- Fixed typos in --help output and manual page (deb #233835)

* Sat Mar 21 2009 Slava Semushin <php-coder@altlinux.ru> 0.8-alt1
- Initial build for ALT Linux Sisyphus

* Thu Oct 26 2000 Tom Gilbert <tom@linuxbrit.co.uk>
- created spec file

