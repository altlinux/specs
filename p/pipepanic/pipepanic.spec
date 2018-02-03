# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name: pipepanic
Version: 0.1.3
Release: alt4_22
Summary: A pipe connecting game

Group: Games/Other
License: GPLv2+
URL: http://www.users.waitrose.com/~thunor/pipepanic/
Source0: http://www.users.waitrose.com/~thunor/pipepanic/dload/%{name}-%{version}-source.tar.gz
Source1: pipepanic.desktop
# Use standard Fedora CFLAGS to compile
Patch0: pipepanic-0.1.3-Makefile.patch
# Hans de Goede
# Set a window title and icon
Patch1: pipepanic-0.1.3-window-title.patch
# Miroslav Lichvar
# Fix wrong score with long pipes (BZ #847344)
Patch2: pipepanic-0.1.3-score.patch

BuildRequires: libSDL-devel
BuildRequires: desktop-file-utils
BuildRequires: ImageMagick-tools
Requires: icon-theme-hicolor
Source44: import.info


%description
Pipepanic is a pipe connecting game using libSDL. Connect as many 
different shaped pipes together as possible within the time given.


%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p0
%patch1 -p1
%patch2 -p1

# Fix file encoding
iconv --from=ISO-8859-1 --to=UTF-8 COPYING-ARTWORK > COPYING-ARTWORK.conv 
mv COPYING-ARTWORK.conv COPYING-ARTWORK

# Fix DATADIR
sed -i 's:/opt/QtPalmtop/share/pipepanic/:%{_datadir}/%{name}/:' main.h


%build
%make_build CFLAGS="$RPM_OPT_FLAGS"


%install

# Install binary
mkdir -p %{buildroot}%{_bindir}
install -m 755 pipepanic %{buildroot}%{_bindir}

# Install data files
mkdir -p %{buildroot}%{_datadir}/%{name}
install -m 644 *.bmp %{buildroot}%{_datadir}/%{name}/

# Install window icon (needed by patch1)
convert PipepanicIcon32.png bmp3:- | \
  convert - -fill '#FF00FF' -opaque black -colors 256 \
    -compress none bmp3:icon.bmp
install -m 644 icon.bmp %{buildroot}%{_datadir}/%{name}/

# Install icons
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m 644 PipepanicIcon16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -m 644 PipepanicIcon32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -m 644 PipepanicIcon48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -m 644 PipepanicIcon64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
           \
%endif
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}


%files
%{_bindir}/pipepanic
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%doc AUTHORS ChangeLog COPYING COPYING-ARTWORK README


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_19
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_14
- update to new release by fcimport

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_13
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_10
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt4_9
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_9
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt3_8
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2_8
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt1_8
- converted from Fedora by srpmconvert script

