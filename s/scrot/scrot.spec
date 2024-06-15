# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: scrot
Version: 1.11.1
Release: alt1

Summary: Screen-shot capture using Imlib 2
License: MIT-feh
Group: Graphical desktop/Other
Url: https://github.com/resurrecting-open-source-projects/scrot
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

Source: %name-%version.tar

BuildRequires: autoconf-archive imlib2-devel libXcomposite-devel libXext-devel libXinerama-devel

%description
A nice and straightforward screen capture utility implementing the
dynamic loaders of imlib2.

%prep
%setup

%build
%autoreconf
%configure \
	--docdir=%_defaultdocdir/%name-%version
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.*
%_defaultdocdir/%name-%version/

%changelog
* Sat Jun 15 2024 Dmitriy Khanzhin <jinn@altlinux.org> 1.11.1-alt1
- 1.11.1

* Fri Jan 12 2024 Dmitriy Khanzhin <jinn@altlinux.org> 1.10-alt1
- 1.10-58-ge46d19f (by git describe --tags)
- Updated BuildRequires

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

