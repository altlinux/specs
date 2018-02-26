Name: comparepdf
Version: 1.0.1
Release: alt1
License: GPLv2
Summary: Compare two PDF files
Group: Publishing
Url: http://www.qtrac.eu/comparepdf.html
Source: %name-%version.tar.gz

# /*G*/ Can't be fount by findreq :(
BuildRequires:	libpoppler-cpp-devel

# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: fontconfig libpoppler3-qt4 libqt4-core libqt4-devel libqt4-gui libqt4-xml libstdc++-devel
BuildRequires: gcc-c++ libpoppler-qt4-devel phonon-devel

%description
The default comparison mode is text mode where the text of each
corresponding pair of pages is compared. As soon as a difference is
detected the program terminates with a message (unless -v0 is set) and
an indicative return code.

%prep
%setup

%build
qmake-qt4
%make

%install
install -D %name %buildroot%_bindir/%name
install -D %name.1 %buildroot%_man1dir/%name.1

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Thu Jan 12 2012 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Autobuild version bump to 1.0.1
- BuildRequires fix

* Tue Oct 11 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1
- Initial build from scratch

