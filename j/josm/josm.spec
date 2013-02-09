# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
#
# spec file for package josm

%global svn_revision 5608


Name:           josm
Version:        0
Release:        alt1_0.38.5608svnjpp7
Summary:        An editor for  OpenStreetMap (OSM)
Group:          Networking/WWW
License:        GPLv2+
URL:            http://josm.openstreetmap.de/
Source0:        %{name}-%{version}.%{svn_revision}svn.tar.gz
Source1:        %{name}
Source2:        %{name}.desktop
Source3:        %{name}-generate-tarball.sh
Source4:        %{name}.1
#Source built using the following commands : ./josm-generate-tarball.sh 3751

#patch to remove metadata-extractor and signpost-core of final jar
Patch1:         %{name}-%{version}-add_classpath.patch

#remove call to "svn info" and fix in build.xml revision and commit date 
Patch2:         %{name}-%{version}-remove_svn_call.patch 



BuildArch:      noarch
BuildRequires:  jpackage-utils
BuildRequires:  desktop-file-utils
BuildRequires:  ant
BuildRequires:  gettext
BuildRequires:  javacc
BuildRequires:  signpost-core >= 1.2.1.1
BuildRequires:  metadata-extractor >= 2.3.1
BuildRequires:  svgsalamander
BuildRequires:  apache-commons-codec
BuildRequires:  gnu-getopt
BuildRequires:  gdata-java
Requires:       jpackage-utils
Requires:       icon-theme-hicolor
Requires:       metadata-extractor >= 2.3.1
Requires:       ant
Requires:       signpost-core >= 1.2.1.1
Requires:       svgsalamander
Requires:       gnu-getopt
Requires:       gdata-java
Source44: import.info

%description
JOSM is an editor for OpenStreetMap (OSM) written in Java 
Currently it supports loading stand alone GPX track data from the OSM database,
loading and editing existing nodes, ways, metadata tags and relations. 

OpenStreetMap is a project aimed squarely at creating and providing
free geographic data such as street maps to anyone who wants them. 
The project was started because most maps you think of as free actually
have legal or technical restrictions on their use, holding back people
from using them in creative, productive or unexpected ways.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.

%prep
%setup -q
%patch1 -p0
%patch2 -p0

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

# removing signpost source files and include signpost-core in buildrequires and requires
rm -rf ./src/oauth
# removing metadata-extractor and svgSalamander sources files and include metadata-extractor and svgSalamander dependencies
rm -rf ./src/com
# removing gnu-getopt from sources and include it as dependencie
rm -rf ./src/gnu

ln -s $(build-classpath metadata-extractor) lib/metadata-extractor.jar
ln -s $(build-classpath signpost-core) lib/signpost-core.jar
ln -s $(build-classpath svgsalamander) lib/svgsalamander.jar
ln -s $(build-classpath javacc) tools/javacc.jar
ln -s $(build-classpath commons-codec) lib/apache-commons-codec.jar
ln -s $(build-classpath ant) lib/ant.jar
ln -s $(build-classpath gnu-getopt) lib/gnu-getopt.jar
ln -s $(build-classpath gdata/gdata-core) lib/gdata-core.jar

iconv -f iso8859-15 -t utf-8 CONTRIBUTION > CONTRIBUTION.conv && mv -f CONTRIBUTION.conv CONTRIBUTION

%build
ant javadoc
ant


%install
mkdir -p %{buildroot}%{_javadir}

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp javadoc  \
%{buildroot}%{_javadocdir}/%{name}

install -p -m 644 dist/%{name}-custom.jar %{buildroot}%{_javadir}/%{name}.jar

install -Dp -m 755 %SOURCE1 %{buildroot}%{_bindir}/%{name}

install -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 images/logo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

install -Dp -m 644 %SOURCE4 %{buildroot}%{_mandir}/man1/%{name}.1

desktop-file-install --dir=%{buildroot}%{_datadir}/applications/ %SOURCE2



%files
%doc README LICENSE CONTRIBUTION gpl-2.0.txt gpl-3.0.txt 
%{_mandir}/man1/%{name}.1*
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png


%files javadoc
%{_javadocdir}/%{name}



%changelog
* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.38.5608svnjpp7
- fc update

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.33.5485svnjpp7
- new fc release

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0-alt1_0.31.5210svnjpp7
- new version

