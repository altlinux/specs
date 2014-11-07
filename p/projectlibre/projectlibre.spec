Name: projectlibre
Version: 1.5.9
Release: alt3

Summary: ProjectLibre - The open source replacement of Microsoft Project

License: CPAL
Group: Office
Url: https://sourceforge.net/projects/projectlibre/

Source: %name-%version.tar
Source1: projectlibre.desktop
Source2: projectlibre.png
Source3: projectlibre

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: java

BuildArch: noarch
BuildPreReq: rpm-build-compat
BuildRequires: ant

%define projectlibredir /var/lib/projectlibre
#%define projectlibredir %_datadir/%name

%description
ProjectLibre is an open source alternative to Microsoft Project.
It is also the new updated version of OpenProj.
We were the developers of OpenProj A compliment to Apache OpenOffice and LibreOffice.
We have a community site as well at http://www.projectlibre.org 
It has been downloaded over 500,000 times in 200 countries and was just won 
InfoWorld "Best of Open Source" award. ProjectLibre is compatible with 
Microsoft Project 2003, 2007 and 2010 files. You can simply open them on Linux, 
Mac OS or Windows. ProjectLibre has been rewritten and added key features:

* Compatibility with Microsoft Project 2010
* User Interface improvement
* Printing (does not allow printing)
* Bug fixes

%prep
%setup

%build
cd openproj_build/
ant

%install
mkdir -p %buildroot/%projectlibredir/
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot%_pixmapsdir/
mkdir -p %buildroot%_desktopdir/

cp %SOURCE1 %buildroot%_desktopdir/
cp %SOURCE2 %buildroot/usr/share/pixmaps/
cp %SOURCE3 %buildroot/%_bindir/projectlibre

cp -a openproj_build/dist/* %buildroot/%projectlibredir/

%check
#check that port listening

%pre
%files
%attr(755,root,root) %dir %projectlibredir/
%_pixmapsdir/*
%_desktopdir/*
%projectlibredir/*
%attr(755,root,root) %_bindir/projectlibre

%changelog
* Fri Nov 07 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt3
- set BuildArch: noarch

* Wed Oct 29 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt2
- Some cleaup

* Wed Oct 15 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt1
- Added right pixmap, and run script
- Change to right version
