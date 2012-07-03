Name: mmsrip
Version: 0.7.0
Release: alt1
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: MMSRIP is a client for the proprietary protocol MMS

License: %gpl2only
Group: Video
Url: http://nbenoit.tuxfamily.org/projects.php?rq=mmsrip
Source0: http://nbenoit.tuxfamily.org/projects/mmsrip/%name-%version.tar.gz

BuildRequires: rpm-build-licenses

%description
MMSRIP is a client for the proprietary protocol MMS://.
It actually saves to a file the content being streamed.

%prep

%setup -q

%configure

%build

%make_build

%install

%makeinstall

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_bindir/mmsrip
%_mandir/man?/*

%changelog
* Wed Jan 14 2009 Sergey Y. Afonin <asy@altlinux.ru> 0.7.0-alt1
- Initial build for AltLinux
