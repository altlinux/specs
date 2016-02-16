Summary:	A text-mode maze game
Name:		lsnipes
Version:	0.9.4
Release:	alt2_15
License:	GPLv2+
Group:		Games/Other
Source:		http://www.ugcs.caltech.edu/~boultonj/snipes/%{name}-%{version}.tgz
URL:		http://www.ugcs.caltech.edu/~boultonj/snipes.html
Patch1:		lsnipes-adapt-CFLAGS-LIBS.patch
# Man page update about levels from Debian package
Patch2:		lsnipes-man-levels-doc.patch

BuildRequires:	ncurses-devel
Source44: import.info

%description
Linux Snipes is a reimplementation of an old text-mode DOS game. You
are in a maze with a number of enemies (the "snipes") and a few
"hives" which create more of the enemies. Your job is to kill the
snipes and their hives before they get the best of you.  26 "option
levels" let you change characteristics of the game such as whether or
not diagonal shots bounce off the walls.  10 levels of difficulty (only
partially implemented) let you build your skills gradually.

%prep
%setup -q
%patch1 -p1 -b .cflags
%patch2 -p1 -b .man-levels

# as-needed
sed -i -e 's,${LIBS} ${OBJS},${OBJS} ${LIBS},' Makefile

%build
%{__make} RPM_CFLAGS="%{optflags}"

%install
%{__install} -p -m 0755 -d	%{buildroot}%{_bindir}
%{__install} -p -m 0755 snipes	%{buildroot}%{_bindir}/snipes
%{__install} -p -m 0755 -d	%{buildroot}%{_mandir}/man6
%{__install} -p -m 0644 snipes.6 %{buildroot}%{_mandir}/man6/snipes.6

%files
%doc README TODO COPYING CHANGELOG
%{_bindir}/snipes
%{_mandir}/man6/snipes.6*

%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2_8
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_8
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt1_7
- initial release by fcimport

