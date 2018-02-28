Group: Games/Arcade
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install zip
# END SourceDeps(oneline)
%define fedora 27
%define mips mips mipsel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           mrrescue
Version:        1.02e
Release:        alt1_5
Summary:        Arcade-style fire fighting game

#See LICENSE file in source for details
#All code is zlib, excluding slam, AnAL and TSerial, which are MIT
#All assets are CC-BY-SA
License:        zlib and CC-BY-SA and MIT
URL:            http://tangramgames.dk/games/mrrescue
Source0:        https://github.com/SimonLarsen/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  ImageMagick-tools
BuildArch:      noarch
Requires:       love

# List the arches that love builds on below for f26+
%if 0%{?fedora} > 25
ExclusiveArch: %{arm} %{ix86} x86_64 %{mips} aarch64 ppc64
%endif
Source44: import.info

#From the website (see URL above)
%description
Mr. Rescue is an arcade styled 2d action game centered around evacuating
civilians from burning buildings. The game features fast paced fire
extinguishing action, intense boss battles, a catchy soundtrack and lots of
throwing people around in pseudo-randomly generated buildings.

%prep
%setup -q
%patch0 -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources, but should exclude appdata
zip -r %{name}.love . -x appdata
#Generate icon (modified splash.png)
convert data/splash.png -crop 256x205+0+0 -background none -gravity center -extent 256x256! %{name}.png

%install
#Install love file
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
#Install execution script
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
#Install manpage
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
#Install appdata.xml and verify
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 %{name}.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc --no-dereference LICENSE
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
* Wed Feb 28 2018 Igor Vlasenko <viy@altlinux.ru> 1.02e-alt1_5
- to Sisyphus by mike@ request

* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.02e-alt1_1
- update by mgaimport

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.02d-alt1_1
- converted for ALT Linux by srpmconvert tools

