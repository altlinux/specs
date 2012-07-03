Name: xtruss
Version: 9490
Release: alt1
Summary: Trace X protocol exchanges, in the manner of strace
License: MIT/X11
Group: System/X11
Source: %name-r%version.tar.gz
Url: http://www.chiark.greenend.org.uk/~sgtatham/xtruss/

# Automatically added by buildreq on Mon Aug 23 2010
BuildRequires: halibut

%description
XTruss is a utility which logs everything that passes between
the X server and one or more X client programs. In this it is
similar to xmon(1), but intended to combine xmon's basic
functionality with an interface much more similar to strace(1).

%prep
%setup -n %name-r%version

%build
%configure
%make_build
rm %name.1
halibut --man=%name.1 %name.but

%install
%makeinstall

%files
%doc README
%_bindir/*
%_man1dir/*

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 9490-alt1
- Autobuild version bump to 9490

* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 8615-alt2
- Homepage URL added

* Mon Aug 23 2010 Fr. Br. George <george@altlinux.ru> 8615-alt1
- Initial build for ALT

