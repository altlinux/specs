# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libICE-devel libSM-devel
# END SourceDeps(oneline)
Name:		flaw
Version:	1.3.2a
Release:	alt1_1
Summary:	Free top-down wizard battle game
Group:		Games/Other
License:	GPLv3+
URL:		http://flaw.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:	libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL-devel
BuildRequires:	libSDL_gfx-devel desktop-file-utils fonts-ttf-gnu-freefont-sans gettext intltool
Requires:	fonts-ttf-gnu-freefont-sans
Source44: import.info

%description
FLAW is a free top-down wizard battle game.
It can be played by up to 5 players simultaneously. The goal of the game is to
survive as long as possible while more and more fireballs appear in the arena.
Game play is simple and self-explanatory. It's all about evading the fireballs
and knocking your opponents down. In addition there are collectible magic gems
that provide special abilities.

%prep
%setup -q

# Fix spurious executable permissions
chmod 644 src/*.cc
chmod 644 src/*.h

%build
%configure --docdir=%{_docdir}/%{name}-%{version} --enable-fontpath=%{_datadir}/fonts/ttf/gnu-free/
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%{_bindir}/flaw
%{_datadir}/flaw
%{_datadir}/pixmaps/flaw.png
%{_datadir}/applications/flaw.desktop
%exclude %{_docdir}/%{name}-%{version}/INSTALL
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Nov 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.2a-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt3_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt3_4
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_4
- update to new release by fcimport

* Fri Oct 14 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt2_3
- bugfix release, close 33627 from ALTLinux Testers Team

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_3
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.4-alt1_2
- converted from Fedora by srpmconvert script

