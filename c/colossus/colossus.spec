BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           colossus
%global         rev        5134
%global         revdate    20120314
Version:        0.13.2
%global         branch     0.13.x
Release:        alt1_1jpp7
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
BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  jdom
BuildRequires:  desktop-file-utils
BuildRequires:  zip
Requires:       jpackage-utils
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
Requires:       colossus = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{branch}-%{revdate}-%{rev}
# With 0.13.x there is an extra direcory level
mv Colossus/* Colossus/.??* .

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

%post
touch --no-create %{_datadir}/pixmaps || :

%postun
touch --no-create %{_datadir}/pixmaps || :

%files
%{_javadir}/*
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jun 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.13.2-alt1_1jpp7
- update to new release by jppimport

* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.2-alt1_0.1.svn5033jpp6
- update to new release by jppimport

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.12.1-alt1_1jpp6
- import by jppimport

