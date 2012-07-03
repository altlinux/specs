Name:		lxlogo
Version:	10
Release:	alt2
License:	GPL
Summary:	An interactive LOGO programming environment for K-12 educational use or just for fun.
URL:		http://lxlogo.sourceforge.net/
Source:		http://dl.sourceforge.net/sourceforge/%name/%name%version.tar.gz
Group:		Education
Patch:		lxlogo10-static_int.patch
Packager:	Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Fri Mar 06 2009
BuildRequires: libX11-devel
Requires: xedit

%description
LXlogo is a variant of the LOGO language. Logo is interesting because it gives students immediate graphical results with just a few commands or lines of code, and allows students to gradually become familiar with geometric concepts, and how to write programs and think procedurally. As students move beyond the beginning stages, they can move on to create fun animations and user interfaces.

Most students today are very familiar with how to play video games and use applications, but have never experienced the thrill of having complete control over the computer like they can when they progam in a language like LXlogo.

%prep
%setup -n %name%version
%patch -p0

%build
make -C src %name getgui renderd

%install
mkdir -p %buildroot%_bindir
install -s bin/* %buildroot%_bindir/

%files
%doc examples README
%_bindir/*

%changelog
* Sat Mar 07 2009 Fr. Br. George <george@altlinux.ru> 10-alt2
- Fix dependency and typo

* Fri Mar 06 2009 Fr. Br. George <george@altlinux.ru> 10-alt1
- Initial build from scratch

