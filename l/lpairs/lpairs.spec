Name:		lpairs
Summary:	Classical memory game with cards
Version:	1.0.4
Release:	alt3_13
License:	GPLv2+ and CC-BY-SA and Freely redistributable without restriction
Group: 		Games/Other
URL:		http://lgames.sourceforge.net/index.php?project=LPairs
#moved to .rpmmacros
#Packager:	Marcin Zajaczkowski <mszpak ATT wp DOTT pl>
Source0:	http://downloads.sourceforge.net/lgames/lpairs-%{version}.tar.gz
#there is a problem with data dir
#the Author said it would be hard for him to fix it at autoconf level
Patch0:		lpairs-1.0.3-datadir.diff
Patch1:		lpairs-1.0.4-desktop.diff
#SDL is required by soname dependency
#Requires:	SDL >= 1.0
BuildRequires:	desktop-file-utils
BuildRequires: 	libSDL-devel
BuildRequires:  gettext
Source44: import.info
#bison?

%description
LPairs is a classical memory game. This means you have to find pairs of
identical cards which will then be removed. Your time and tries needed
will be counted but there is no highscore chart or limit to this.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure inst_dir="%{_datadir}/%{name}"
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} inst_dir="%{_datadir}/%{name}" install
%find_lang %{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp lpairs.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
	lpairs.desktop

%files -f %{name}.lang
%{_bindir}/lpairs
%{_datadir}/%{name}
#there is no high scores for now
#%config(noreplace) %attr(664, games, games) %{_var}/lib/games/lpairs.hscr
%doc AUTHORS ChangeLog COPYING README
#TODO is in German also not in UTF-8
#doc TODO
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_13
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_12
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt3_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_9
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2_8
- converted from Fedora by srpmconvert script

* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_8
- converted from Fedora by srpmconvert script

