# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           fbg
Version:        0.9.1
Release:        alt3_9
Summary:        Falling Block Game
Group:          Games/Other
License:        GPLv2+
URL:            http://fbg.sourceforge.net/
# Upstream has done a new release at our request (changing the license from
# GPLv2 to GPLv2+) but has not gotten around to providing a tarbal, thus we use
# one generated from cvs like this:
# cvs -z3 -d:pserver:anonymous@fbg.cvs.sourceforge.net:/cvsroot/fbg co -P -r rel-0-9-1 fbg
# rm -r `find fbg -name CVS`
# mv fbg fbg-0.9.1
# tar cvfz fbg-0.9.1.tar.gz fbg-0.9.1
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         fbg-fixes.patch
Patch1:         fbg-0.9-wx28.patch
BuildRequires:  libSDL-devel libphysfs-devel libmikmod-devel wxGTK-devel libtool
BuildRequires:  desktop-file-utils ImageMagick
Requires:       icon-theme-hicolor
Source44: import.info

%description
Move and rotate variously shaped falling blocks to make them form a complete
row. Once a complete row has formed it will disappear. If you make incomplete
rows the screen will fill up and when it reaches the top the game is over.


%prep
%setup -q
%patch0 -p1 -z .fix
%patch1 -p1 -z .wx28
./autogen.sh


%build
%configure
make %{?_smp_mflags}
convert startfbg/icon.xpm %{name}.png


%install
make install DESTDIR=$RPM_BUILD_ROOT
# rm make install installed docs as we install them with %doc
rm $RPM_BUILD_ROOT/usr/doc/fbg/COPYING $RPM_BUILD_ROOT/usr/doc/fbg/README

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_mandir}/man6/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_9
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt3_8
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_8
- update to new release by fcimport

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_7
- update to new release by fcimport

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt2_6.1
- Rebuilt with libphysfs 2.0.2 and for debuginfo
- Added libICE-devel into BuildPreReq

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2_6
- converted from Fedora by srpmconvert script

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1_6
- converted from Fedora by srpmconvert script

