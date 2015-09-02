# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(x11)
# END SourceDeps(oneline)
Name:		ibus-unikey
Version:	0.6.1
Release:	alt1_9
Summary:	Vietnamese engine for IBus input platform

Group:		Graphical desktop/Other
License:	GPLv3
URL:		http://code.google.com/p/ibus-unikey/
Source0:	http://ibus-unikey.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:	gettext
BuildRequires:	libibus-devel
BuildRequires:	gtk2-devel
BuildRequires:  intltool
Source44: import.info

%description
A Vietnamese engine for IBus input platform that uses Unikey.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}


%files -f %{name}.lang
%doc README AUTHORS COPYING ChangeLog
%{_datadir}/%{name}/
%{_datadir}/ibus/component/unikey.xml
%{_libexecdir}/ibus-engine-unikey
%{_libexecdir}/ibus-setup-unikey


%changelog
* Wed Sep 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_9
- new version; moved to Sisyphus for gvy@

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_7
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_5
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_4
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.1-alt1_3
- initial fc import

