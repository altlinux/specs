# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize gcc-c++ pkgconfig(gthread-2.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name arpage
%define version 0.3.3
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		arpage
Version:	0.3.3
Release:	alt3_24
Summary:	A JACK MIDI arpeggiator

Group:		Sound
License:	GPLv3
URL:		http://arpage.sourceforge.net
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-gcc46.patch
Patch1:		%{name}-gcc47.patch

BuildRequires:	libjack-devel
BuildRequires:	libgtkmm2-devel
BuildRequires:	intltool libxml++2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
Source44: import.info

%description

A GTK application that runs up to 4 arpeggiators on incoming MIDI
data, synchronized to JACK.

%prep

%setup -q

#fix compilation with gcc 4.6
%patch0 -p1 -b .%{name}-gcc46.patch
#fix compilation with gcc 4.7
%patch1 -p1 -b .%{name}.gcc47.patch

# fix bad permissions in debuginfo
chmod 644 %{_builddir}/%{name}-%{version}/src/main.cc

%build
%add_optflags -std=c++11

# Fix for aarch64 build
#automake --add-missing
autoreconf -i

%configure
%make_build


%install
make install DESTDIR=%{buildroot} arpagedocdir=%{_docdir}/%{name}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
install -m 644 %{_builddir}/%{name}-%{version}/src/arpage.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/


%files
%doc COPYING ChangeLog AUTHORS README INSTALL NEWS
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/ui/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
* Sat Feb 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_23
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_21
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_20
- update to new release by fcimport

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt3_19
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_19
- update to new release by fcimport

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3.3-alt2_17.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_16
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_11
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_10
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_9
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt2_8
- rebuild to get rid of #27020

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_8
- update to new release by fcimport

* Sat Dec 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_7
- update to new release by fcimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.3-alt1_6
- initial release by fcimport

