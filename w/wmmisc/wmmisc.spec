Name: wmmisc
Version: 1.1
Release: alt1

Summary: Display various info in WindowMaker Dock
License: GPL
Group: Graphical desktop/Window Maker

URL: http://www.dockapps.org/file.php/id/160
Source0: http://www.dockapps.org/download.php/id/660/wmmisc-%version.tar.bz2

# Automatically added by buildreq on Fri Oct 20 2006
BuildRequires: libXext-devel libXpm-devel

%description
Display various info in WindowMaker Dock.

%prep
%setup -q

%build
%make_build CFLAGS="%optflags"

%install
%__install -pD -m755 src/wmmisc %buildroot%_bindir/wmmisc

%files
%_bindir/*

%changelog
* Fri Oct 20 2006 Victor Forsyuk <force@altlinux.org> 1.1-alt1
- 1.1
- Updated build requirements.

* Wed Apr 06 2005 Victor Forsyuk <force@altlinux.ru> 0.9-alt1
- New version (now in plain C).

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Apr 28 2003 Ott Alex <ott@altlinux.ru> 0.5-alt1
- Initial build

