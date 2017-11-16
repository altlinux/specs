# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/a2x /usr/bin/asciidoc
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           calcurse
Version:        4.2.2
Release:        alt1_4
Summary:        Text-based personal organizer

Group:          Office
License:        BSD
URL:            http://calcurse.org
Source0:        http://calcurse.org/files/%{name}-%{version}.tar.gz

BuildRequires:  gettext gettext-tools libncurses++-devel libncurses-devel libncursesw-devel libtic-devel libtinfo-devel
Source44: import.info

%description
Calcurse is a text-based calendar and scheduling application. It helps 
keep track of events, appointments, and everyday tasks.

A configurable notification system reminds the user of upcoming 
deadlines, and the curses based interface can be customized to suit user 
needs.

%prep
%setup -q

%build
%configure
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
install -p -m 0644 doc/calcurse.1 $RPM_BUILD_ROOT%{_mandir}/man1/
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS NEWS README doc/*.txt
%{_bindir}/calcurse*
%{_mandir}/man1/calcurse.1*


%changelog
* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1_4
- NMU: update to new version by fcimport
- requiest by oddity@

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.8-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Aug 27 2010 Ilya Mashkin <oddity@altlinux.ru> 2.8-alt1
- 2.8

* Sat Oct 17 2009 Ilya Mashkin <oddity@altlinux.ru> 2.7-alt1
- 2.7

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 2.5-alt1
- 2.5

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 2.3-alt1
- 2.1 -> 2.3

* Sun May 18 2008 Igor Zubkov <icesik@altlinux.org> 2.1-alt1
- 2.0 -> 2.1

* Tue Mar 04 2008 Igor Zubkov <icesik@altlinux.org> 2.0-alt1
- 1.9 -> 2.0

* Wed Oct 24 2007 Igor Zubkov <icesik@altlinux.org> 1.9-alt1
- 1.8 -> 1.9

* Wed May 23 2007 Igor Zubkov <icesik@altlinux.org> 1.8-alt1
- 1.7 -> 1.8

* Wed Feb 21 2007 Igor Zubkov <icesik@altlinux.org> 1.7-alt1
- 1.6 -> 1.7
- clean up build requires

* Mon Oct 23 2006 Igor Zubkov <icesik@altlinux.org> 1.6-alt1
- 1.5 -> 1.6

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 1.5-alt1
- 1.4 -> 1.5
- buildreq

* Fri May 19 2006 Igor Zubkov <icesik@altlinux.ru> 1.4-alt1
- 1.4

* Fri Mar 31 2006 Igor Zubkov <icesik@altlinux.ru> 1.3-alt1
- 1.3
- buildreq

* Fri Dec 16 2005 Igor Zubkov <icesik@altlinux.ru> 1.2-alt1
- 1.2

* Sun Oct 30 2005 Igor Zubkov <icesik@altlinux.ru> 1.1-alt1
- Initial build for Sisyphus
