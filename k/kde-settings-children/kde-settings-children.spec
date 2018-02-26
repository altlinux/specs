Name: kde-settings-children
Version: 0.1
Release: alt7.qa1
BuildArch: noarch

Source:%name-%version.tar


Summary: KDE settings for Children version
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>

Requires: kdelibs >= 3.5.7-alt3 kde-styles-splash-children
PreReq(post,preun): alternatives >= 0.2

%description
KDE settings for Children version


%prep
%setup -q


%install
mkdir -p %buildroot/etc/kde/settings-children/share/config
install -m 0644 config/* %buildroot/etc/kde/settings-children/share/config

mkdir -p %buildroot/etc/kde/settings-children/share/apps/kdisplay/color-schemes
install -m 0644 apps/kdisplay/color-schemes/* %buildroot/etc/kde/settings-children/share/apps/kdisplay/color-schemes/


mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name <<__EOF__
/etc/kde/distribution	/etc/kde/settings-children 50
__EOF__


%files
%config %_altdir/%name
/etc/kde/settings-children/share/config/*
/etc/kde/settings-children/share/apps/kdisplay/color-schemes/*


%changelog
* Tue Feb 09 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.1-alt7.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-alternatives-0.3 for kde-settings-children
  * postclean-05-filetriggers for spec file

* Wed Jul 16 2008 Alexandra Panyukova <mex3@altlinux.ru> 0.1-alt7
- build for Children

* Thu Oct 18 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt6
- changed splash screen 

* Thu Aug 09 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt5
- Changed konquerror background 

* Tue Jul 24 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt4
- Added BrowserApplication key 

* Thu Jul 05 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt3
- color scheme really added 

* Wed Jun 27 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- color scheme added 

* Wed Jun 20 2007 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build 




