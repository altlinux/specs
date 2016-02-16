# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
Name:		gnujump
Version:	1.0.8
Release:	alt1_7
Summary:	A jumping game which is a clone of xjump

Group:		Games/Other
License:	GPLv3+
URL:		http://gnu.org/software/%{name}
Source0:	http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch1:		%{name}-Makefile.in.patch

BuildRequires:	libSDL-devel >= 1.2, libSDL_mixer-devel, libSDL_image-devel
BuildRequires:	desktop-file-utils
Source44: import.info

%description
GNUjump is a clone of the simple yet addictive game Xjump, adding new features
like multiplaying, unlimited FPS, smooth floor falling, themable graphics,
sounds,replays, etc.

The goal in this game is to jump to the next floor trying not to fall down. As
you go upper in the Falling Tower the floors will fall faster. Try to survive 
longer get upper than anyone. It might seem too simple but once you've tried 
you'll realize how addictive this is. 

%prep
%setup -q
%patch1 -p0 -b .orig

%build
%configure
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%find_lang gnujump

%files -f gnujump.lang
%doc AUTHORS ABOUT-NLS COPYING README 
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_2
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_2
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_1
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt3_6
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_6
- update to new release by fcimport

* Wed Mar 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_5
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1_5
- converted from Fedora by srpmconvert script

