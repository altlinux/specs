# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-gettextize pkgconfig(gdk-pixbuf-2.0) pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
Group: Graphical desktop/Other
%define _libexecdir %_prefix/libexec
Name:           mate-themes
Version:        1.5.0
Release:        alt1_1
Summary:        MATE Desktop themes
License:        GPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

BuildRequires:  icon-naming-utils
BuildRequires:  mate-common
BuildRequires:  mate-doc-utils
BuildRequires:  mate-icon-theme-devel
BuildRequires:  pkgconfig(gtk-engines-2)

Requires:       mate-icon-theme
Requires:       libgtk-engines-default
Requires:       libgtk-engine-murrine

BuildARch:      noarch
Source44: import.info

%description
MATE Desktop themes


%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure --enable-all-themes   \
           --enable-test-themes  \
           --enable-icon-mapping \
           --enable-test-themes
make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install
find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'
%find_lang %{name}


%post
for icon_theme in \
  Fog PrintLarge Quid Reverse Shiny Simply TraditionalOk \
  ContrastHighLargePrint ContrastHighLargePrintInverse \
  ContrastLow ContrastHigh ContrastHighInverse Aldabra ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
for icon_theme in \
  Fog PrintLarge Quid Reverse Shiny Simply TraditionalOk \
  ContrastHighLargePrint ContrastHighLargePrintInverse \
  ContrastLow ContrastHigh ContrastHighInverse Aldabra ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done
fi

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/icons/ContrastHigh-SVG
%{_datadir}/themes/TraditionalOkClassic
%{_datadir}/themes/ContrastLowLargePrint
%{_datadir}/themes/Fog
%{_datadir}/themes/PrintLarge
%{_datadir}/themes/Quid
%{_datadir}/themes/Reverse
%{_datadir}/themes/Shiny
%{_datadir}/themes/Simply
%{_datadir}/themes/TraditionalOk
%{_datadir}/themes/ContrastHighLargePrint
%{_datadir}/themes/ContrastHighLargePrintInverse
%{_datadir}/themes/ContrastLow
%{_datadir}/themes/ContrastHigh
%{_datadir}/themes/ContrastHighInverse
%{_datadir}/themes/Aldabra
%{_datadir}/icons/ContrastHigh
%{_datadir}/icons/ContrastHighInverse
%{_datadir}/icons/ContrastHighLargePrint
%{_datadir}/icons/Fog
%{_datadir}/icons/MateLargePrint
%{_datadir}/icons/Quid
%{_datadir}/themes/AlaDelta
%{_datadir}/themes/Atantla
%{_datadir}/icons/mate/cursors
%{_datadir}/icons/ContrastHighLargePrintInverse
%{_datadir}/themes/TraditionalOkTest

%changelog
* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

