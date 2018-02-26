Name: tkabber-plugins
Version: 0.11.1
Release: alt4

Summary: Set of plugins for Tkabber.
License: GPL
Group: Networking/Instant messaging
Url: http://www.jabber.ru/projects/tkabber/

BuildArch: noarch
BuildRequires: tcl
Source: %name-%version-%release.tar

%description
%name contains some addons for open-source jabber client - Tkabber.

%prep
%setup
sed -i '/^#!\/usr\/bin\/wishx/d' whiteboard/svgrender.tcl
for d in attline checkers ctcomp jidlink presencecmd receipts socials unixkeys; do
mv $d/README README.$d
done

%install
mkdir -p %buildroot%_datadir/%name
find . -mindepth 2 -type f -not -name ChangeLog | cpio -pmd %buildroot%_datadir/%name

%files
%doc README* ChangeLog
%_datadir/%name

%changelog
* Mon Dec 27 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt4
- updated to svn rev.1973

* Fri Aug 21 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt3
- updated to svn rev.1833

* Thu Jan 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt2
- updated to svn rev.1626

* Fri Oct 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.1-alt1
- 0.11.1 released

* Sun Jun  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt1
- 0.11.0 released

* Fri May 23 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11.0-alt0.1
- updated to svn rev.1444

* Thu Jan 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt0.3
- updated to svn rev.1341

* Thu Nov  1 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt0.2
- updated to svn rev.1291, near 0.10.1beta2 release

* Fri Oct 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt2
- updated to svn rev.1274

* Mon Apr 16 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt1
- 0.10.0 released

* Mon Mar  5 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt0.2
- 0.10.0 beta2 released

* Sat Feb 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.0-alt0.1
- 0.10.0 beta1 released

* Sun Nov 12 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt2
- updated to svn rev.778

* Sun Jul  2 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9-alt1
- 0.9.9 released

* Thu May 19 2005 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.7-alt1
- Added new plugins:  ejabberd, mute, osd, reversi, spy

* Mon Oct 21 2002 Sergey Kalinin  <banzaj@altlinux.ru> 0.9.1-alt1
- Initial release
