%define _unpackaged_files_terminate_build 1

Name: xzoom
Epoch: 1
Version: 20200501
Release: alt1
License: distributable
Group: Accessibility
Summary: X zoomer

Source: %name-%version.tar

Url: https://github.com/cpantel/xzoom
VCS: https://github.com/cpantel/xzoom

BuildRequires: imake 
BuildRequires: libXext-devel
BuildRequires: libXt-devel
BuildRequires: xorg-cf-files

%description
Xzoom displays in its window a magnified area of the X11 display.
The user can interactively change the zoomed area, the window size,
magnification (optionally different magnification for X and Y axes)
or rotate or mirror the image.

%prep
%setup

%build
xmkmf
make

%install
mkdir $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
mkdir -p $RPM_BUILD_ROOT%_man1dir
install -m 755 -s xzoom $RPM_BUILD_ROOT%_bindir
install -m 644 xzoom.man $RPM_BUILD_ROOT%_man1dir/xzoom.1

%files
%_bindir/*
%doc %_man1dir/*
%doc README xzoom.lsm

%changelog
* Fri Feb 07 2025 Artem Semenov <savoptik@altlinux.org> 1:20200501-alt1
- Build from new sources (Closes: #52614)

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 0.3-alt3
- BuildRequires recalculated

* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt2
- libXext-devel added

* Mon Aug 27 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build for ALT

* Mon Nov 11 2002 - ro@suse.de
- changed neededforbuild <xf86 xdevel> to <x-devel-packages>
* Mon Dec 03 2001 - egmont@suselinux.hu
- Initial release.
