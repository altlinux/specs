# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pkg-config gcc-c++
# END SourceDeps(oneline)
Name:           grhino
Version:        0.16.0
Release:        alt3_11
Summary:        Reversi game for GNOME, supporting the Go/Game Text Protocol

Group:          Games/Other
License:        GPLv2+
URL:            http://rhino.sourceforge.net/
Source0:        http://dl.sourceforge.net/rhino/grhino-%{version}.tar.gz
Patch0:         grhino-0.16.0-gcc43.patch
Patch1:         grhino-0.16.0-types.patch
Patch2:         grhino-0.16.0-emptyelse.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libgnomeui-devel
BuildRequires:  scrollkeeper
#Requires:       
Requires(post):         scrollkeeper
Requires(postun):       scrollkeeper
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
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .types
%patch2 -p1 -b .emptyelse


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# desktop file
desktop-file-install  \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications \
        --remove-key=Version\
        desktop/%{name}.desktop

# Icon
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog COPYING NEWS README TODO
%{_bindir}/grhino
%{_bindir}/gtp-rhino
%{_datadir}/applications/*.desktop
%{_datadir}/gnome/help/grhino/
%{_datadir}/pixmaps/grhino.png
%{_datadir}/grhino-%{version}/
%{_datadir}/omf/grhino/


%changelog
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

