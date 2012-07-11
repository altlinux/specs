Name: gromit
Version: 20041213
Release: alt1.1

Summary: Paint annotations on top of the X screen
License: GPLv2
Group: System/X11
Url: http://www.home.unix-ag.org/simon/gromit/

Source0: http://www.home.unix-ag.org/simon/gromit/%name-%version.tar.bz2
Patch0: gromit-20041213-alt-DSO.patch

BuildRequires: libgtk+2-devel

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

It is useful for recording presentations with xvidcap.

%prep
%setup -q
%patch0 -p2

%build
%make

%install
install -m 755 -D %name %buildroot%_bindir/%name

%files
%doc AUTHORS ChangeLog README
%_bindir/%name

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20041213-alt1.1
- Fixed build

* Thu Apr 23 2009 Alexey Shabalin <shaba@altlinux.ru> 20041213-alt1
- initial package for ALTLinux
