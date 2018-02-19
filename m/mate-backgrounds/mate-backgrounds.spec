Group: Graphics
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		mate-backgrounds
Version:	1.20.0
Release:	alt1_1
Summary:	MATE Desktop backgrounds
License:	GPLv2+
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.20/%{name}-%{version}.tar.xz

BuildArch:	noarch
BuildRequires:	mate-common
Source44: import.info

%description
Backgrounds for MATE Desktop

%prep
%setup -q


%build
%configure

%make_build V=1


%install
%{makeinstall_std}

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/mate-background-properties
%{_datadir}/backgrounds/mate


%changelog
* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_2
- new fc release

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new version

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new version

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_2
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- new fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1.1
- Build for Sisyphus

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Tue Oct 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- adapted alt patches

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

