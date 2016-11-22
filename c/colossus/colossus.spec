# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: /usr/bin/desktop-file-install
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           colossus
%global         rev        5331
%global         revdate    20130917
Version:        0.14.0
%global         branch    %{nil}
Release:        alt1_5jpp8
Summary:        Allows people to play Titan against each other or AIs

Group:          Games/Other
License:        GPLv2
URL:            http://colossus.sourceforge.net/

# The svn repo includes some prebuilt jar files that need to be removed
# The colossus-gen-tarball.sh can be used to fetch either the latest
# revision or a specified revision from the repo, strip the jar files
# and some artwork and then build a tar.gz archive.
# colossus-rev.xsl is used to extract the current revision of HEAD
# when grabbing the latest revision, using svn info.
# The repo is at:
# https://colossus.svn.sourceforge.net/svnroot/colossus/trunk/Colossus
Source0:        colossus-%{branch}-%{revdate}-%{rev}.tar.gz
Source1:        colossus-gen-tarball.sh
Source2:        colossus-rev.xsl

BuildArch:      noarch


# Note the intention is to eventually require only java 1.5 for both building
# and installing. But bug 510243 in gjdoc currently blocks this.
BuildRequires: javapackages-tools rpm-build-java
BuildRequires:  ant
BuildRequires:  jdom
BuildRequires:  desktop-file-utils
BuildRequires:  zip
Requires: javapackages-tools rpm-build-java
Requires:       jdom
Requires(post):  coreutils
Requires(postun):  coreutils
Source44: import.info

%description
Colossus allows people to play Titan
(http://www.boardgamegeek.com/boardgame/103) and several Titan variants, hot
seat or via a network. Several different AIs are provided that can play instead
of humans.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}
Requires: javapackages-tools rpm-build-java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{branch}-%{revdate}-%{rev}

%build

# Tell colossus' build process where to look for needed jar files
echo "libs.dir=%{_javadir}" > local_build.properties

# Tell colossus some build info that the game will display
mkdir -p build/ant/classes/META-INF
cat <<EOF > build/ant/classes/META-INF/build.properties
release.version=%{version}
svn.revision.max-with-flags=%{rev}
build.timestamp=%{revdate}
username=rpmbuild
EOF

ant jar

# The supplied build.xml adds a classpath to the manifest that needs to
# be removed.

# First remove the existing manifest file
zip -d Colossus.jar META-INF/MANIFEST.MF

# Then put one back without a class path
cat <<EOF > fixup.xml
<?xml version="1.0"?>
<!-- Replace manifest with one without a classpath -->
<project name="Colossus" default="fixup" basedir=".">
  <target name="fixup"
  description="Remove classpath from manifest">
    <jar jarfile="Colossus.jar" update="true">
      <manifest>
        <attribute name="Main-Class"
        value="net.sf.colossus.appmain.Start" /> 
      </manifest>
    </jar>
  </target>
</project>
EOF

ant -f fixup.xml

ant -lib %{_javadir}/jdom.jar javadoc

# Allow for simple command to run colossus
echo -e "#!/bin/sh\njava -cp %{_javadir}/jdom.jar:%{_javadir}/colossus.jar net.sf.colossus.appmain.Start" > %{name}

# Make a .desktop file
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Colossus
GenericName=Strategy Game
Comment=Multiplayer turned based fantasy game with AIs available
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%install
install -D -m 755 Colossus.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 core/src/main/resource/icons/ColossusIcon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rpv build/ant/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
chmod -R og=u-w $RPM_BUILD_ROOT%{_javadocdir}

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/colossus/feature-requests/225/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">colossus.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fantasy board game with strategic and tactical battle elements</summary>
  <description>
    <p>
      Colossus is a clone of Avalon Hill's "Titan" Board game.
    </p>
    <p>
      It is a fantasy board game where you lead an army of mythological creatures
      against other players.
    </p>
  </description>
  <url type="homepage">http://colossus.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://colossus.sourceforge.net/pics/screenshots/Colossi.jpg</screenshot>
  </screenshots>
</application>
EOF

%post
touch --no-create %{_datadir}/pixmaps || :


%postun
touch --no-create %{_datadir}/pixmaps || :


%files
%{_javadir}/*
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_5jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_4jpp8
- new version

* Sun Nov 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_4jpp7
- update to new release by jppimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_2jpp7
- update to new release by jppimport

* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.14.0-alt1_1jpp7
- update

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.13.2-alt1_5jpp7
- update to new release by jppimport

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.13.2-alt1_4jpp7
- fc update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.2-alt1_2jpp7
- update to new release by jppimport

* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.2-alt1_1jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_0.1.svn5033jpp6
- update to new release by jppimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1_1jpp6
- import by jppimport

