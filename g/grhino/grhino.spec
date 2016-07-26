Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++
# END SourceDeps(oneline)
Name:           grhino
Version:        0.16.1
Release:        alt1_1
Summary:        Reversi game for GNOME, supporting the Go/Game Text Protocol

License:        GPLv2+
URL:            http://rhino.sourceforge.net/
Source0:        http://downloads.sourceforge.net/rhino/grhino-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires: gettext gettext-tools gettext-tools-python
BuildRequires:  libgnomeui-devel
BuildRequires:  librarian
#Requires:       
Requires(post):         librarian
Requires(postun):       librarian
Source44: import.info

%description
GRhino, or Rhino its former name, is a Reversi game on Linux and other
UNIX-like systems as long as GNOME 2 libraries are installed. It is currently
under development and a new version is available occasionally.

What distinguish GRhino from most other Reversi games is that GRhino will be
targeted for experienced Reversi players. Strong AI is the main focus with some
additional good, useful features (like an endgame solver) is planned. The
ultimate target strength of the AI is that it should be able to beat the best
human player at the highest difficulty level. Beating Logistello (the strongest
program available) is not in the plan :) 

GRhino supports the Go/Game Text Protocol (GTP), allowing it to be used as
an engine for a GTP-compliant controller like Quarry.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# desktop file
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --remove-key=Version\
        desktop/%{name}.desktop

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING
%doc ChangeLog NEWS README TODO
%{_bindir}/grhino
%{_bindir}/gtp-rhino
%{_datadir}/applications/*.desktop
%{_datadir}/gnome/help/grhino/
%{_datadir}/pixmaps/grhino.png
%{_datadir}/grhino-%{version}/
%{_datadir}/omf/grhino/


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.1-alt1_1
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_20
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_15
- update to new release by fcimport

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_14
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_13
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_12
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_11
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt3_10
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt2_10
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt2_9
- update to new release by fcimport

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.16.0-alt2_8.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * obsolete-call-in-post-scrollkeeper-update for grhino
  * postclean-05-filetriggers for the spec file

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt2_8
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.16.0-alt1_8
- converted from Fedora by srpmconvert script

