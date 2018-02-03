# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install libGL-devel libGLU-devel libSDL-devel
# END SourceDeps(oneline)
%define fedora 27
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define prever pre2

Name:           atomorun
Version:        1.1
Release:        alt5_0.25.%{prever}
Summary:        Jump & Run game where you have to flee an exploding nuclear bomb
Group:          Games/Other
License:        GPL+
URL:            http://atomorun.whosme.de/index.php
# the file seems to be gone from upstreams server so no URL
Source0:        %{name}-%{version}_%{prever}.tar.gz
Source1:        atomorun.desktop
Patch0:         atomorun-1.1-missing-protos.patch
BuildRequires:  libSDL_mixer-devel libSDL_image-devel libtiff-devel libtiffxx-devel libvorbis-devel
BuildRequires:  libalsa-devel desktop-file-utils
Requires:       icon-theme-hicolor
Source44: import.info

%description
Atomorun is a OpenGL Jump&Run game where you have to flee an exploding
nuclear bomb.


%prep
%setup -q -n %{name}-%{version}_%{prever}
%patch0 -p1


%build
%configure
%make_build


%install
%makeinstall_std
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/pixmaps/atomorun_winicon.ico
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora            \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 pixmaps/%{name}_icon.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.25.pre2
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.24.pre2
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.22.pre2
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.21.pre2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.20.pre2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.19.pre2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.18.pre2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.17.pre2
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.16.pre2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.15.pre2
- update to new release by fcimport

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.14.pre2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.13.pre2
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt5_0.12.pre2
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_0.12.pre2
- update to new release by fcimport

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt4_0.11.pre2
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_0.11.pre2
- rebuild with new rpm desktop cleaner

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_0.11.pre2
- spec sleanup

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_0.11.pre2
- converted from Fedora by srpmconvert script

