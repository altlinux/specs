# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# camel-case name at the request of the upstream maintainers.
Name: MegaMek
Version: 0.30.11
Release: alt2_8jpp7
Summary: A portable, network-enabled BattleTech engine

Group: Games/Other
License: GPLv2+
URL: http://prdownloads.sourceforge.net/megamek/MegaMek-v0.30.11.zip
Source0: MegaMek-v0.30.11.zip
# converted from data/images/misc/megamek-icon.gif
Source1: MegaMek-icon.png
Patch0: MegaMek-directories.patch

BuildRequires: desktop-file-utils
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
Provides: megamek = %{version}-%{release}
Source44: import.info

%description
MegaMek is a community effort to implement the Classic BattleTech
rules in an operating-system-agnostic, network-enabled manner.

%prep
%setup -q -c -n MegaMek
%patch0 -p0
# remove included binaries and rebuild everything from source
rm -f MegaMek.exe MegaMek.jar
rm -f lib/TinyXML.jar lib/retroweaver-rt.jar
pushd src
  jar xf ../lib/Ostermiller.jar
  # remove hard-to-build sources that are not required
  rm -f com/Ostermiller/util/*CSV*
  rm -f com/Ostermiller/util/*CGI*
  rm -f com/Ostermiller/util/*Properties*
  rm -r com/Ostermiller/util/*Browser*
  rm -rf META-INF
  jar xf ../lib/PngEncoder.jar
  rm -rf META-INF
  rm -f LICENSE.txt PngEncoderB.html PngEncoder.html
  jar xf ../lib/TabPanel.jar
  rm -rf META-INF gov doc
  rm -f LICENSE README
  mv src/gov .
  rmdir src
  unzip -qq ../lib/tinyXML07-src.zip
  mv sources/*.java .
  mv sources/gd .
  rm -rf classes javadoc
  rmdir sources
  rm -f DevelopmentDiary-TinyXML.txt readme.txt gpl.txt
  jar xf ../lib/collections.jar
  rm -rf META-INF
  rm -f ../lib/collections.jar
  find -name \*.class | xargs rm -f
  rm -f ../lib/Ostermiller.jar ../lib/PngEncoder.jar
  rm -f ../lib/TabPanel.jar ../lib/tinyXML07-src.zip
  find -name .svn | xargs rm -rf
  cp ../l10n/megamek/client/*.properties megamek/client
  cp ../l10n/megamek/client/bot/*.properties megamek/client/bot
  cp ../l10n/megamek/common/*.properties megamek/common
  cp ../l10n/megamek/common/options/*.properties megamek/common/options
popd
find data docs mmconf -name .svn -print0 | xargs -0 rm -rf
find data docs mmconf -type f -print0 | xargs -0 chmod 644
find data docs mmconf -type d -print0 | xargs -0 chmod 755
rm -f mmconf/MegaMek.bat
mv docs/stats.pl .

%build
pushd src
  javac `find -name '*.java'`
  jar cf MegaMek.jar com gd gnu gov keypoint megamek *.class *.java
popd

cat > MegaMek.sh << EOF
#!/bin/sh

cd %{_datadir}/MegaMek
exec java -classpath %{_javadir}/MegaMek.jar megamek.MegaMek
EOF

cat > MegaMek.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=MegaMek
GenericName=A BattleTech engine
Comment=Play MegaMek
Exec=MegaMek
Icon=MegaMek-icon.png
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%install

install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 src/MegaMek.jar \
  $RPM_BUILD_ROOT%{_javadir}/MegaMek.jar

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/MegaMek
cp -r data docs mmconf $RPM_BUILD_ROOT%{_datadir}/MegaMek
install -pm 644 readme.txt \
  $RPM_BUILD_ROOT%{_datadir}/MegaMek/readme.txt

install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 MegaMek.sh \
  $RPM_BUILD_ROOT%{_bindir}/MegaMek
install -pm 755 stats.pl \
  $RPM_BUILD_ROOT%{_bindir}/MegaMek-stats

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor fedora \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora \
  MegaMek.desktop

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -pm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/pixmaps/MegaMek-icon.png

%{_bindir}/aot-compile-rpm

%files
%doc HACKING license.txt readme-German.txt readme.txt
%{_javadir}/MegaMek.jar
%{_datadir}/MegaMek
%{_bindir}/MegaMek
%{_bindir}/MegaMek-stats
%{_datadir}/applications/fedora-MegaMek.desktop
%{_datadir}/pixmaps/MegaMek-icon.png

%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/MegaMek.jar.*

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.30.11-alt2_8jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.30.11-alt2_7jpp6
- update to new release by jppimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.30.11-alt1_7jpp6
- import by jppimport

