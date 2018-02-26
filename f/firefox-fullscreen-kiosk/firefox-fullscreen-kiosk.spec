%define cid 	\{4bb4e4c5-b6aa-4e34-9ead-c0f4a6e4e3fc\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		firefox-fullscreen-kiosk
Version:	1.0.1
Release:	alt11

Summary:	Mozilla Firefox fullscreen kiosk.

License:	GPL
Group:		Networking/WWW
URL:		http://git.altlinux.org/people/hsv/packages/firefox-fullscreen-kiosk.git

Packager:	Sergey Shilov <hsv@altlinux.ru>
Source0:	%name-%version.tar.bz2

BuildArch:	noarch

BuildRequires(pre):	rpm-build-firefox
Requires:	%firefox_name >= 2.0

%description 	
extension for run Mozilla Firefox browser in fullscreen kiosk mode. 

%prep
%setup -q

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

sed -r -i \
    -e 's,<em:maxVersion>3\.5\.\*</em:maxVersion>,<em:maxVersion>99\.\*</em:maxVersion>,g' \
    %buildroot/%ciddir/install.rdf

%files
%ciddir


%changelog
* Sun Feb 19 2012 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt11
- add firefox 9.0+ support  ( ALT #26853 )

* Wed Nov 16 2011 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt10
- Rebuild with Firefox 8.0

* Tue Oct 18 2011 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt9
- Rebuild with Firefox 7.0

* Wed Aug 24 2011 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt8
- Rebuild with Firefox 6.0

* Sun Jul 31 2011 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt7
- Enable rebuilt with firefox-5.X.

* Sun Apr 10 2011 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt6
- Enable rebuilt with firefox-4.X.

* Thu Jan 28 2010 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt5
- Rebuilt with firefox-3.6.

* Mon Oct 26 2009 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt4
- fix #22043.

* Fri Oct 23 2009 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt3
- fix ru_RU.KOI8-R lang in spec.

* Mon Jul 13 2009 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt2
- disale bookmarks toolbar
- hide main menubar
- enable close browser (for reset on restart by external tools)
- enable tabs management
- optimized run from IceWM
- removed custom environment

* Fri Jul 10 2009 Sergey Shilov <hsv@altlinux.org> 1.0.1-alt1
- Initial build for ALTLinux.
