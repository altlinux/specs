Group: Games/Other
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#remove once using %%configure again
%global debug_package %{nil}
%define apricotsdir %{_datadir}/apricots
Name: apricots
Version:  0.2.7
Release:  alt1_2
Summary: 2D air combat game

License: GPLv2
URL: https://github.com/moggers87/apricots
Source0: %{url}/archive/v%{version}/apricots-%{version}.tar.gz
Source1: apricots.png
#Icon created from screenshot on website
Source2: apricots.desktop

BuildRequires: gcc gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libalut-devel
BuildRequires: desktop-file-utils
BuildRequires: libopenal-devel
BuildRequires: autoconf automake
ExcludeArch: ppc64le aarch64
Source44: import.info

%description
It's a game where you fly a little plane around the screen and
shoot things and drop bombs on enemy targets, and it's meant to be quick 
and fun.

%prep
%setup -q
# e2k support (deprecated in 0.2.7)
#cp -at admin -- \
#       /usr/share/gnu-config/config.sub /usr/share/gnu-config/config.guess


%build
./bootstrap
#Use %%configure once --as-needed is fixed, and fix debug at top of spec.
./configure --prefix=%{_prefix}
%make_build


%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 apricots/apricots %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/apricots
install -m 644 apricots/*.wav %{buildroot}%{_datadir}/apricots
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 apricots/apricots.cfg %{buildroot}%{_sysconfdir}
ln -s ../../..%{_sysconfdir}/apricots.cfg %{buildroot}%{_datadir}/apricots/apricots.cfg
install -m 644 apricots/*.psf %{buildroot}%{_datadir}/apricots
install -m 644 apricots/*.shapes %{buildroot}%{_datadir}/apricots

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps


%files
%doc --no-dereference COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/apricots
%{_datadir}/apricots
%{_datadir}/applications/apricots.desktop
%{_datadir}/icons/hicolor/24x24/apps/apricots.png
%config(noreplace) %{_sysconfdir}/apricots.cfg


%changelog
* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 0.2.7-alt1_2
- new version

* Sat Dec 07 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt4_27
- restored e2k patch

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt3_27
- update to new release by fcimport

* Sat Jun 29 2019 Michael Shigorin <mike@altlinux.org> 0.2.6-alt3_25
- fix build on new arches

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_25
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_23
- update to new release by fcimport

* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_20
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_17
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_16
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_15
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_11
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_9
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Fri Jan 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_7
- update to new release by fcimport

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.6-alt1_6
- converted from Fedora by srpmconvert script

