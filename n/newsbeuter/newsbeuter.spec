Name: newsbeuter
Version: 2.9
Release: alt2

Summary: Newsbeuter is an open-source RSS/Atom feed reader for text terminals

License: MIT/X11
Group: Networking/News
Url: http://www.newsbeuter.org/

Packager: Vladimir D. Seleznev <vseleznv@altlinux.org>
Source: %name-%version.tar.gz

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

%build
export CXXFLAGS="%optflags"
%make_build DESTDIR=%buildroot prefix=%_prefix

%install
%make_install DESTDIR=%buildroot prefix=%_prefix install
%find_lang %name

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_defaultdocdir/*


%changelog
* Sun Mar 13 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.9-alt2
- fix locale path.

* Thu Dec 10 2015 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.9-alt1
- Initial build.
