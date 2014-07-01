%global           upstream_version 4.0

Summary:          The card game Skat
Name:             xskat
# Upstream License requires to alter the version number
# for re-distribution
Version:          %{upstream_version}.0
Release:          alt2_11
# https://fedoraproject.org/wiki/Licensing/XSkat_License
License:          XSkat
Group:            Games/Other
Source0:          http://www.xskat.de/xskat-%{upstream_version}.tar.gz
Source1:          xskat.desktop
URL:              http://www.xskat.de/xskat.html
# xskat requires an 10x20 font
Requires:         fonts-bitmap-misc
BuildRequires: xorg-cf-files gccmakedep imake
BuildRequires:    libX11-devel
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick
Source44: import.info


%description
XSkat lets you play the card game Skat as defined by the official Skat Order.

Features:
    * Single- and multiplayer mode
    * Playing over LAN or IRC
    * Game lists and logs
    * Three types of scoring
    * English or German text
    * German or French suited cards
    * Selectable computer playing strength
    * Pre-definable card distributions
    * Variations: Ramsch, Bock, Kontra & Re, ... 

%prep
%setup -q -n %{name}-%{upstream_version}

# fix encoding
iconv -f iso8859-1 -t utf-8 CHANGES-de > CHANGES-de.conv && \
touch -r CHANGES-de CHANGES-de.conv && \
mv -f CHANGES-de.conv CHANGES-de

iconv -f iso8859-1 -t utf-8 README-de > README-de.conv && \
touch -r README-de README-de.conv && \
mv -f README-de.conv README-de

iconv -f iso8859-1 -t utf-8 README.IRC-de > README.IRC-de.conv && \
touch -r README.IRC-de README.IRC-de.conv && \
mv -f README.IRC-de.conv README.IRC-de

%build
%configure
make CDEBUGFLAGS="%{optflags}"

%install
make DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}/man6 MANSUFFIX=6 install install.man
install -d $RPM_BUILD_ROOT%{_mandir}/de/man6
mv $RPM_BUILD_ROOT%{_mandir}/man6/xskat-de.6 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man6/xskat.6*
chmod 644 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm
touch -r icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm

%files
%doc README* CHANGES*
%{_bindir}/xskat
%{_mandir}/man6/xskat.6*
%lang(de) %{_mandir}/de/man6/xskat.6*
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.xpm


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt2_7
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_7
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 4.0.0-alt1_6
- initial release by fcimport

