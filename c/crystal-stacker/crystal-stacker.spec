# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           crystal-stacker
Version:        1.5
Release:        alt2_25
Summary:        Falling blocks, match 3 or more of the same color crystals
Group:          Games/Other
License:        Crystal Stacker
URL:            http://www.t3-i.com/cstacker.htm
Source0:        http://www.t3-i.com/games/crystal_stacker/downloads/crystal_stacker-1.5-src.zip
Source1:        %{name}.desktop
Source2:        %{name}-theme-editor.desktop
Patch0:         crystal-stacker-1.5-ImplicitDSOLinking.patch
BuildRequires:  liballegro-devel dumb-devel ImageMagick-tools desktop-file-utils
Source44: import.info

%description
If you've played Columns then you know what Crystal Stacker is all about. Match
3 or more of the same color crystals either horizontally, vertically, or dia-
gonally to destroy them. For every 45 crystals you destroy, the level increases
and the crystals fall faster. The higher the level, the more points you are   
awarded for destroying crystals.

%package theme-editor
Summary:        Themes editor for Crystal Stacker
Group:          Games/Other
Requires:       %{name} = %{version}

%description theme-editor
Create new Themes for Crystal Stacker

%prep
%setup -q -c
%patch0 -p1
sed -i 's/\r//' ce/*.txt cs/*.txt

%build
export CC="gcc -Wl,--no-as-needed"
pushd cs/source
%make_build -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char"
popd

pushd ce/source
%make_build -f Makefile.unix PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-char-subscripts"
popd

convert cs/cs.ico %{name}.png
convert ce/ce.ico %{name}-theme-editor.png

%install
pushd cs/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

pushd ce/source
make -f Makefile.unix install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png %{name}-theme-editor.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%doc cs/*.txt
%{_bindir}/crystal-stacker
%dir %{_datadir}/crystal-stacker
%{_datadir}/crystal-stacker/cs.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%files theme-editor
%doc ce/*.txt
%{_bindir}/crystal-stacker-theme-editor
%{_datadir}/crystal-stacker/ce.dat
%{_datadir}/applications/%{name}-theme-editor.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}-theme-editor.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_22
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_20
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_19
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_18
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_17
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_16
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_14
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_13
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_11
- update to new release by fcimport

* Mon May 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_10
- converted from Fedora by srpmconvert script

