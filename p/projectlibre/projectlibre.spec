Name:    projectlibre
Version: 1.6.2
Release: alt1

Summary: ProjectLibre - The open source replacement of Microsoft Project

License: CPAL
Group:   Office
Url:     https://sourceforge.net/projects/projectlibre/
# VCS:   git://git.code.sf.net/p/projectlibre/code

Source:  %name-%version.tar
Source1: %name.watch

Packager: Danil Mikhailov <danil@altlinux.org>

#PreReq:
Requires: java

BuildArch: noarch
BuildPreReq: rpm-build-compat
BuildRequires: ant

%define projectlibredir %_libexecdir/%name

%description
ProjectLibre is an open source alternative to Microsoft Project.  It is
also the new updated version of OpenProj. We were the developers of
OpenProj A compliment to Apache OpenOffice and LibreOffice.  We have a
community site as well at http://www.projectlibre.org It has been
downloaded over 500,000 times in 200 countries and was just won
InfoWorld "Best of Open Source" award. ProjectLibre is compatible
with Microsoft Project 2003, 2007 and 2010 files. You can simply open
them on Linux, Mac OS or Windows. ProjectLibre has been rewritten and
added key features:

* Compatibility with Microsoft Project 2010
* User Interface improvement
* Printing (does not allow printing)
* Bug fixes

%prep
%setup
# Replace hard-coded library path by default JRE path
subst 's|/Library/Java/JavaVirtualMachines/jdk1.7.0_45.jdk/Contents/Home/jre/lib/rt.jar|%_libexecdir/jvm/jre/lib/rt.jar|' openproj_contrib/openproj_*.conf

%build
cd openproj_build/
ant

%install
install -Dm0755 openproj_build/resources/%name %buildroot/%_bindir/%name
# Fix path to projectlibre dir
subst 's|^OPENPROJ_HOME0=.*|OPENPROJ_HOME0="%projectlibredir"|' %buildroot/%_bindir/%name

install -Dm0644 openproj_build/resources/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm0644 openproj_build/resources/%name.png %buildroot%_pixmapsdir/%name.png

mkdir -p %buildroot/%projectlibredir/
cp -a openproj_build/dist/* %buildroot/%projectlibredir/

%check
#check that port listening

%files
%attr(755,root,root) %_bindir/projectlibre
%attr(755,root,root) %dir %projectlibredir/
%_desktopdir/*
%_pixmapsdir/*
%projectlibredir/*

%changelog
* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.2-alt1
- New version
- Build from upstream Git repository

* Thu Feb 19 2015 Andrey Cherepanov <cas@altlinux.org> 1.5.9-alt4
- Fix path to jar file in startup script

* Fri Nov 07 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt3
- set BuildArch: noarch

* Wed Oct 29 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt2
- Some cleaup

* Wed Oct 15 2014 Danil Mikhailov <danil@altlinux.org> 1.5.9-alt1
- Added right pixmap, and run script
- Change to right version
