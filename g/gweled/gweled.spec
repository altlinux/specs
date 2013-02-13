# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
Name:           gweled
Version:        0.9.1
Release:        alt2_6

Summary:        Swapping gem game

Group:          Games/Other
License:        GPLv2+
URL:            http://launchpad.net/gweled
Source0:        http://launchpad.net/gweled/trunk/0.9/+download/gweled-%{version}.tar.gz
#Patch0:         %{name}-Makefile.patch
#Patch1:         %{name}-Sample_Free.patch
#Patch2:         %{name}-ppc.diff
#Patch3:         %{name}-mikmod-disable-disk-writers.diff
# patch4 and 5 taken from Ubuntu; https://bugs.launchpad.net/ubuntu/+source/gweled/+bug/90499
#Patch4:         %{name}-disable-music.diff
#Patch5:         %{name}-xdg_pref.diff

BuildRequires:  libgnomeui-devel >= 2.0.0
BuildRequires:  librsvg-devel >= 2.0.0
BuildRequires:  libcroco-devel >= 0.3.0
BuildRequires:  libmikmod-devel
BuildRequires:  desktop-file-utils
BuildRequires:	intltool
Source44: import.info

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make alignment of 3 or
more gems, both vertically or horizontally by swapping adjacent gems. The game
ends when there are no possible moves left.


%prep
%setup -q
#%patch0  -p0 -b .patch0
#%patch1  -p0 -b .patch1
# the next two were extracted from the debian package; I asked upstream to 
# apply them, but got no reply
# http://ftp.debian.org/debian/pool/main/g/gweled/gweled_0.7-2.diff.gz
#%patch2  -p0 -b .patch2
#%patch3  -p1 -b .patch3
#%patch4  -p1 -b .patch4
#%patch5  -p1 -b .patch5

%build
export LDFLAGS="${LDFLAGS} -lm -Wl,--export-dynamic "
%configure --localstatedir=/var/lib
#echo "Encoding=UTF-8" >> data/gweled.desktop
#mv gweled.desktop gweled.desktop.old
#iconv --from-code=ISO-8859-1 --to-code=UTF-8 <gweled.desktop.old > gweled.desktop
make %{?_smp_mflags}



%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --delete-original \
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications      \
  --add-category LogicGame                    \
  --remove-category Application                        \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
#mkdir $RPM_BUILD_ROOT%{_var}/lib/
#mv $RPM_BUILD_ROOT%{_var}/games/ $RPM_BUILD_ROOT%{_var}/lib/
# gweled.timed.scores not shipped in 0.7, but needed
#cp -p $RPM_BUILD_ROOT%{_var}/lib/games/gweled.easy.scores $RPM_BUILD_ROOT%{_var}/lib/games/gweled.timed.scores

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS
%attr(2711,root,games) %{_bindir}/%{name}
%config(noreplace) %attr(0664,games,games) %{_var}/lib/games/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%_iconsdir/*/*/*/*
%{_datadir}/%{name}/
%{_datadir}/sounds/%{name}/

%changelog
* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_6
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_5
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_4
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_4
- update to new release by fcimport

* Wed Nov 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_3
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_2
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.9-alt1_3
- converted from Fedora by srpmconvert script

