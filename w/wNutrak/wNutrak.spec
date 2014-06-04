# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: wNutrak
Version: 0.18
Release: %branch_release alt1.1

Summary: Converts Garmin nuvi 2/7xx tracks into gpx format (GUI version)
License: %gpl3plus
Group: File tools

URL: http://www.anpo.republika.pl/
Packager: Aleksey Avdeev <solo@altlinux.ru>

# Source URL: http://www.anpo.republika.pl/files/wnutrak018.zip
Source: %name-%version.tar
Source10: %name.desktop

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: libX11-devel
BuildPreReq: libfltk-devel
BuildPreReq: gcc-c++
BuildPreReq: libuuid-devel
BuildPreReq: icoutils
BuildPreReq: ImageMagick-tools

%description
Program wNutrak will convert tracks created by Garmnin nuvi 2xx and 7xx
into gpx format. GUI version.

%package -n nutrak
Summary: Converts Garmin nuvi 2/7xx tracks into gpx format (command line version)
Group: File tools

%description -n nutrak
Program nutrak will convert tracks created by Garmnin nuvi 2xx and 7xx
into gpx format. Command line version.

%prep
%setup -c -n %name

%build
%make_build -C source

%install
install -pD -m 755 source/nutrak %buildroot%_bindir/nutrak
install -pD -m 755 source/wNutrak %buildroot%_bindir/%name

# incons install
install -d %buildroot%_niconsdir
install -d %buildroot%_liconsdir

icotool -x -i 1 -o %buildroot%_niconsdir/%name.png source/wNutrak.ico
convert source/wNutrak.ico -geometry 48x48 %buildroot%_liconsdir/%name.png

# .desktop install
install -pD %SOURCE10 %buildroot%_desktopdir/%name.desktop

%files
%doc wNutrak.txt source/copying.txt
%_bindir/wNutrak
%_niconsdir/%name.png
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%files -n nutrak
%doc command_line/nutrak.txt source/copying.txt
%_bindir/nutrak

%changelog
* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1.1
- Rebuilt with updated libfltk

* Tue Aug 07 2012 Aleksey Avdeev <solo@altlinux.ru> 0.18-alt1
- Initial build for ALT Linux Sisyphus
- Create nutrak subpackage

* Fri Feb 05 2010 Manuel F Martinez <manpaz@bashlinux.com> - 0.17-1
- Fixed warnings on build time

* Mon Jan 17 2010 Greg Swift <gregswift@gmail.com> - 0.16-1
- Initial build
