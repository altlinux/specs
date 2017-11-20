# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/desktop-file-validate glib2-devel pkgconfig(gtk+-3.0)
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%if 0%{!?_with_xfce:1} && 0%{!?_without_xfce:1}
%if 0%{?rhel}
%global _with_xfce 0
%else
%global _with_xfce 1
%endif
%endif

Name:		im-chooser
Version:	1.7.1
Release:	alt1_1
License:	GPLv2+ and LGPLv2+
URL:		http://pagure.io/im-chooser/
%{?_with_gtk2:BuildRequires:	gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel}
%{!?_with_gtk2:BuildRequires:	gtk3-demo libgail3-devel libgtk+3 libgtk+3-devel libgtk+3-gir-devel}
BuildRequires:	libSM-devel imsettings-devel >= 1.3.0
%if 0%{?_with_xfce}
BuildRequires:	libxfce4util-devel
%endif
BuildRequires:	desktop-file-utils intltool gettext gettext-tools

Source0:	http://releases.pagure.org/%{name}/%{name}-%{version}.tar.bz2

Summary:	Desktop Input Method configuration tool
Group:		System/Base
Obsoletes:	im-chooser-gnome3 < 1.4.2-2
Provides:	im-chooser-gnome3 = %{version}-%{release}
Requires:	%{name}-common = %{version}-%{release}
Source44: import.info

%description
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

%package	common
Summary:	Common files for im-chooser subpackages
Group:		System/Base
Requires:	imsettings >= 1.3.0
Obsoletes:	im-chooser < 1.5.0.1
## https://fedorahosted.org/fpc/ticket/174
Provides:	bundled(egglib)

%description	common
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the common libraries/files to be used in
im-chooser subpackages.

%if 0%{?_with_xfce}
%package	xfce
Summary:	XFCE settings panel for im-chooser
Group:		System/Base
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	im-chooser < 1.5.0.1

%description	xfce
im-chooser is a GUI configuration tool to choose the Input Method
to be used or disable Input Method usage on the desktop.

This package contains the XFCE settings panel for im-chooser.
%endif


%prep
%setup -q

%build
%configure
%make_build

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
	--vendor=fedora				\
%endif
	--add-category=X-GNOME-PersonalSettings			\
	--delete-original					\
	--dir=$RPM_BUILD_ROOT%{_datadir}/applications		\
	$RPM_BUILD_ROOT%{_datadir}/applications/im-chooser.desktop
%if 0%{?_with_xfce}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/xfce4-im-chooser.desktop
%endif
#%%{!?_with_gtk2:desktop-file-validate $RPM_BUILD_ROOT%%{_datadir}/applications/im-chooser-panel.desktop}

rm -rf $RPM_BUILD_ROOT%{_libdir}/libimchooseui.{so,la,a}
#%%{!?_with_gtk2:rm -rf $RPM_BUILD_ROOT%%{_libdir}/control-center-1/panels/libim-chooser.{a,la}}

# disable panel so far
rm -rf $RPM_BUILD_ROOT%{_libdir}/control-center-1/panels/libim-chooser.so
rm -rf $RPM_BUILD_ROOT%{_datadir}/applications/im-chooser-panel.desktop

%find_lang %{name}


%files
%{_bindir}/im-chooser
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-im-chooser.desktop
%else
%{_datadir}/applications/im-chooser.desktop
%endif
%{_mandir}/man1/im-chooser.1*

%files	common -f %{name}.lang
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/libimchooseui.so.*
%{_datadir}/icons/hicolor/*/apps/im-chooser.png
%dir %{_datadir}/imchooseui
%{_datadir}/imchooseui/imchoose.ui

%if 0%{?_with_xfce}
%files	xfce
%{_bindir}/xfce4-im-chooser
%{_datadir}/applications/xfce4-im-chooser.desktop
%endif

%changelog
* Mon Nov 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_1
- new version by request of oddity@

* Sat Mar 07 2015 Mikhail Efremov <sem@altlinux.org> 1.6.4-alt3
- Rebuild with libxfce4util-4.12.

* Tue Aug 26 2014 Ilya Mashkin <oddity@altlinux.ru> 1.6.4-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_3
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.4-alt1_1
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.3-alt1_1
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- initial fc import

