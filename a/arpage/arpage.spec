# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gthread-2.0) pkgconfig(libxml++-2.6)
# END SourceDeps(oneline)
Name:		arpage
Version:	0.3.3
Release:	alt2_9
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
BuildRequires:	intltool libxml++-devel
BuildRequires:	desktop-file-utils
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


%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} arpagedocdir=%{_defaultdocdir}/%{name}-%{version}

desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE1}

mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps
install -m 644 %{_builddir}/%{name}-%{version}/src/arpage.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/



%files
%doc COPYING ChangeLog AUTHORS README
%{_bindir}/%{name}
%{_bindir}/zonage
%{_datadir}/%{name}/ui/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

%changelog
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

