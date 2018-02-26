# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:           alex4
Version:        1.0
Release:        alt2_12
Summary:        Alex the Allegator 4 - Platform game
Group:          Games/Other
License:        GPL+
URL:            http://allegator.sourceforge.net/
Source0:        http://dl.sf.net/sourceforge/allegator/alex4src_data.zip
Source1:        alex4.desktop
Source2:        alex4.png
Patch0:         alex4-unix.patch
Patch1:         alex4-allegro-4.2.patch
Patch2:         alex4-dot-files-endian-clean.patch
Patch3:         alex4-fsf-address.patch
BuildRequires:  liballegro-devel dumb-devel desktop-file-utils ImageMagick
Requires:       icon-theme-hicolor
Source44: import.info

%description
In the latest installment of the series Alex travels through the jungle in
search of his kidnapped girlfriend. Plenty of classic platforming in four
nice colors guaranteed!


%prep
%setup -q -n alex4src
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i 's/\r//' *.txt

# as-needed
sed -i -e 's,$(CC) $(LDFLAGS) -o $@ $^,$(CC) -o $@ $^ $(LDFLAGS),' src/Makefile


%build
pushd src
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"
popd


%install
pushd src
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
popd

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps


%files
%doc license.txt readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png


%changelog
* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2_12
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_12
- update to new release by fcimport

* Thu Jul 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_11
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_10
- initial release by fcimport

