Group: Development/Tools
%define _libexecdir %_prefix/libexec
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mate-common
Summary:        mate common build files
Version:        1.20.0
Release:        alt1_1
License:        GPLv3+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.20/mate-common-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  automake autoconf
Requires:       automake 
Requires:       autoconf 
Requires:       gettext 
Requires:       intltool 
Requires:       libtool 
Requires:       gtk-doc 
Requires:       itstool 
Requires:       yelp-tools
Source44: import.info

%description
binaries for building all MATE desktop sub components

%prep
%setup -q


%build
%configure

%make_build V=1


%install
%{makeinstall_std}


%files
%{_bindir}/mate-*
%{_datadir}/aclocal/mate-*.m4
%{_datadir}/mate-common
%{_mandir}/man1/*

%changelog
* Mon Feb 19 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_1
- new fc release

* Wed Sep 06 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.18.0-alt1_2
- new fc release

* Thu Oct 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.16.0-alt1_1
- converted for ALT Linux by srpmconvert tools

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_1
- new fc release

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.0-alt1_2
- new fc release

* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Sat Sep 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_2
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Wed Mar 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- new fc release

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_1
- new fc release

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- converted by srpmconvert script

