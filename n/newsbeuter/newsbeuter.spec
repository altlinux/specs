Name: newsbeuter
Version: 2.9
Release: alt3

Summary: Newsbeuter is an open-source RSS/Atom feed reader for text terminals

License: MIT/X11
Group: Networking/News
Url: http://www.newsbeuter.org/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
# repacked https://newsbeuter.org/downloads/newsbeuter-%version.tar.gz
Source: %name-%version.tar
# https://sources.debian.net/src/newsbeuter/2.9-6/debian/patches/23-fix-RCE-on-bookmark.patch/
Patch1: newsbeuter-2.9-debian-cve-2017-12904.patch
Patch2: newsbeuter-2.9-debian-cve-2017-14500.patch

# Automatically added by buildreq on Tue Dec 22 2015
# optimized out: libjson-c libncurses-devel libstdc++-devel libtinfo-devel pkg-config
BuildRequires: gcc-c++ libcurl-devel libjson-c-devel libncursesw-devel libsqlite3-devel libssl-devel libstfl0-devel libxml2-devel

%description
Newsbeuter is an open-source RSS/Atom feed reader for text terminals.
Newsbeuter's great configurability and vast number of features make it a
perfect choice for people that need a slick and fast feed reader that
can be completely controlled via keyboard.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
export CXXFLAGS="%optflags"
%make_build prefix=%_prefix

%install
%make_install DESTDIR=%buildroot prefix=%_prefix install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_defaultdocdir/*


%changelog
* Tue Oct 03 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.9-alt3
- Fixes:
  + CVE-2017-12904
  + CVE-2017-14500

* Sun Mar 13 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.9-alt2
- fix locale path.

* Thu Dec 10 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.9-alt1
- Initial build.
