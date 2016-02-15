# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/emacs /usr/bin/emacsclient /usr/bin/gconftool-2 /usr/bin/glib-gettextize /usr/bin/gvim /usr/bin/ldd /usr/bin/valgrind glib2-devel pkgconfig(gconf-2.0) pkgconfig(glib-2.0) pkgconfig(gtk+-2.0) pkgconfig(libglade-2.0) pkgconfig(libgnomeui-2.0)
# END SourceDeps(oneline)
Name:       alleyoop
Version:    0.9.8
Release:    alt1_6
License:    GPLv2+
Group:      Development/Tools
Summary:    Graphical front-end to the Valgrind memory checker for x86
URL:        http://alleyoop.sourceforge.net/
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:    alleyoop.desktop

BuildRequires: valgrind >= 3.1.0
BuildRequires: libgnomeui-devel, gettext, intltool
BuildRequires: desktop-file-utils
BuildRequires: binutils-devel

Requires: valgrind >= 3.1.0
Requires: GConf2, scrollkeeper

# valgrind available only on these
ExclusiveArch: %{ix86} x86_64 ppc ppc64 ppc64le s390x %{arm} aarch64
Source44: import.info

%description
Alleyoop is a graphical front-end to the increasingly popular Valgrind
memory checker for x86 GNU/ Linux using the Gtk+ widget set and other
GNOME libraries for the X Windows System.

Features include a right-click context menu to intelligently suppress
errors or launch an editor on the source file/jumping to the exact
line of the error condition. A searchbar at the top of the viewer can
be used to limit the viewable errors to those that match the regex
criteria entered. Also included is a fully functional Suppressions
editor.

%prep
%setup -q

%build
%configure --disable-install-schemas
make %{?_smp_mflags}

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall_std
%find_lang %{name}

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null


%postun
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null


%files -f %{name}.lang
%doc COPYING README NEWS AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.8-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt3_9
- update to new release by fcimport

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt3_8
- fixed build

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2_8
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2_7
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2_6
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt2_5
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_5
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_4
- update to new release by fcimport

* Sat Jul 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.7-alt1_3
- initial release by fcimport

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.5-alt1
- initial build
