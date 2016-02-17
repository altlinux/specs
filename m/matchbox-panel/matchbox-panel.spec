# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/msgfmt /usr/bin/msgmerge /usr/bin/xgettext pkgconfig(libmb) pkgconfig(libstartup-notification-1.0)
# END SourceDeps(oneline)
BuildRequires: desktop-file-utils
Summary: 	Panel for the Matchbox Desktop
Name: 		matchbox-panel
Version: 	0.9.3
Release: 	alt1_11
Url: 		http://matchbox-project.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%name/0.9/%name-%version.tar.bz2
Patch0:		matchbox-panel-0.9.3-linking.patch
Patch1:		matchbox-panel-0.9.3-automake-1.13.patch
BuildRequires:	libmatchbox-devel 
BuildRequires:	libapm-devel 
BuildRequires:	libstartup-notification-devel 
BuildRequires:	libwireless-devel
Source44: import.info
Patch33: matchbox-panel-0.9.3-alt-xvt.patch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains the panel from Matchbox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

#fix desktop files
sed -i -e 's,\(Icon=.*\)\.png,\1,g' applets/dotdesktop/*.desktop
%patch33 -p1

%build
autoreconf -vfi
%configure \
	--enable-nls \
	--enable-dnotify \
	--enable-startup-notification
%make

%install
%makeinstall_std

desktop-file-install \
	--vendor="" \
	--set-key="Type" \
	--set-value="Application" \
	--remove-category="MB" \
	--remove-category="Panel" \
	--dir=%{buildroot}%{_datadir}/applications/ \
		%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %name

%files -f %name.lang
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/pixmaps/*
%_datadir/applications/*





%changelog
* Thu Feb 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_11
- new release

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_10
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_9
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_8
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_7
- update by mgaimport

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_4
- mageia import

