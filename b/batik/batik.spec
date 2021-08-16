Epoch: 0
Group: Graphics
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global classpath batik:xml-commons-apis:xml-commons-apis-ext:xmlgraphics-commons

Name:           batik
Version:        1.14
Release:        alt1_3jpp8
Summary:        Scalable Vector Graphics for Java
License:        ASL 2.0 and W3C
URL:            https://xmlgraphics.apache.org/batik/
Source0:        http://archive.apache.org/dist/xmlgraphics/batik/source/batik-src-%{version}.zip
Source1:        %{name}-security.policy

Patch1:         0001-Fix-imageio-codec-lookup.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.xmlgraphics:xmlgraphics-commons)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)
BuildRequires:  mvn(xml-apis:xml-apis-ext)
Source44: import.info
#19119
Provides: xmlgraphics-batik = 0:%version-%release
Obsoletes: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description
Batik is a Java(tm) technology based toolkit for applications that want
to use images in the Scalable Vector Graphics (SVG) format for various
purposes, such as viewing, generation or manipulation.

%package util
Group: Graphics
Summary:        Batik utility library

%description util
Util component of the Apache Batik SVG manipulation and rendering library.

%package css
Group: Graphics
Summary:        Batik CSS engine
#32067
Conflicts: batik < 0:1.8-alt1_1

%description css
CSS component of the Apache Batik SVG manipulation and rendering library.

%package        squiggle
Group: Graphics
Summary:        Batik SVG browser
# Explicit requires for javapackages-tools since squiggle-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
# Requires AWT, so can't rely on java-headless alone
Requires:       java
#19119
Provides: xmlgraphics-batik-squiggle = 0:%version-%release
Obsoletes: xmlgraphics-batik-squiggle < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    squiggle
The Squiggle SVG Browser lets you view SVG file, zoom, pan and rotate
in the content and select text items in the image and much more.

%package        svgpp
Group: Graphics
Summary:        Batik SVG pretty printer
# Explicit requires for javapackages-tools since svgpp-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
#19119
Provides: xmlgraphics-batik-svgpp = 0:%version-%release
Obsoletes: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    svgpp
The SVG Pretty Printer lets developers "pretty-up" their SVG files and
get their tabulations and other cosmetic parameters in order. It can
also be used to modify the DOCTYPE declaration on SVG files.

%package        ttf2svg
Group: Graphics
Summary:        Batik SVG font converter
# Explicit requires for javapackages-tools since ttf2svg-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
#19119
Provides: xmlgraphics-batik-ttf2svg = 0:%version-%release
Obsoletes: xmlgraphics-batik-ttf2svg < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    ttf2svg
The SVG Font Converter lets developers convert character ranges from
the True Type Font format to the SVG Font format to embed in SVG
documents. This allows SVG document to be fully self-contained be
rendered exactly the same on all systems.

%package        rasterizer
Group: Graphics
Summary:        Batik SVG rasterizer
# Explicit requires for javapackages-tools since rasterizer-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
#19119
Provides: xmlgraphics-batik-rasterizer = 0:%version-%release
Obsoletes: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    rasterizer
The SVG Rasterizer is a utility that can convert SVG files to a raster
format. The tool can convert individual files or sets of files, making
it easy to convert entire directories of SVG files. The supported
formats are JPEG, PNG, and TIFF, however the design allows new formats
to be added easily.

%package        slideshow
Group: Graphics
Summary:        Batik SVG slideshow
# Explicit requires for javapackages-tools since slideshow-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
# Requires AWT, so can't rely on java-headless alone
Requires:       java
#19119
Provides: xmlgraphics-batik-slideshow = 0:%version-%release
Obsoletes: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik < 0:%version
Conflicts: xmlgraphics-batik-rasterizer < 0:%version
Conflicts: xmlgraphics-batik-slideshow < 0:%version
Conflicts: xmlgraphics-batik-svgpp < 0:%version
Conflicts: xmlgraphics-batik-ttf2svg < 0:%version

%description    slideshow
Batik SVG slideshow.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Group: Development/Java
Summary:        Samples for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.


%prep
%setup -q -n %{name}-%{version}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%patch1 -p1

cp -p %{SOURCE1} batik-svgrasterizer/src/main/resources/org/apache/batik/apps/rasterizer/resources/rasterizer.policy
cp -p %{SOURCE1} batik-svgbrowser/src/main/resources/org/apache/batik/apps/svgbrowser/resources/svgbrowser.policy

# It's an uberjar, it shouldn't have requires
%pom_xpath_inject pom:dependency '<optional>true</optional>' batik-all

# Generate OSGi metadata
for pom in `find -mindepth 2 -name pom.xml -not -path ./batik-all/pom.xml`; do
    %pom_add_plugin org.apache.felix:maven-bundle-plugin $pom "
        <extensions>true</extensions>
        <configuration>
            <instructions>
                <Bundle-SymbolicName>org.apache.batik.$(sed 's:./batik-::;s:/pom.xml::' <<< $pom)</Bundle-SymbolicName>
            </instructions>
        </configuration>
    "
    %pom_xpath_inject pom:project '<packaging>bundle</packaging>' $pom
done

# The "old-test" module cannot be built due to missing deps in Fedora
%pom_disable_module batik-test-old

# Remove optional deps on rhino and jython
%pom_remove_dep :rhino batik-{bridge,script}
%pom_remove_dep :jython batik-script
rm -rf batik-script/src/main/java/org/apache/batik/script/{jpython,rhino}
rm batik-bridge/src/main/java/org/apache/batik/bridge/BatikWrapFactory.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/SVG12RhinoInterpreter.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/RhinoInterpreter.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/RhinoInterpreterFactory.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/EventTargetWrapper.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/GlobalWrapper.java
rm batik-bridge/src/main/java/org/apache/batik/bridge/WindowWrapper.java

%mvn_package :batik-squiggle squiggle
%mvn_package :batik-squiggle-ext squiggle
%mvn_package :batik-svgpp svgpp
%mvn_package :batik-ttf2svg ttf2svg
%mvn_package :batik-rasterizer rasterizer
%mvn_package :batik-rasterizer-ext rasterizer
%mvn_package :batik-slideshow slideshow
%mvn_package :batik-css css
%mvn_package :batik-constants util
%mvn_package :batik-shared-resources util
%mvn_package :batik-i18n util
%mvn_package :batik-util util
%mvn_package ':batik-test*' __noinstall

%mvn_file :batik-all batik-all

#no jacl rpm and it breaks javadoc
rm batik-script/src/main/java/org/apache/batik/script/jacl/JaclInterpreter.java

%build

export ANT_OPTS="-Xmx512m"
# due to javadoc x86_64 out of memory
subst 's,maxmemory="128m",maxmemory="512m",' build.xml
%mvn_build

%install
%mvn_install

%jpackage_script org.apache.batik.apps.svgbrowser.Main '' '' %{classpath}:rhino squiggle true
%jpackage_script org.apache.batik.apps.svgpp.Main '' '' %{classpath} svgpp true
%jpackage_script org.apache.batik.apps.ttf2svg.Main '' '' %{classpath} ttf2svg true
%jpackage_script org.apache.batik.apps.rasterizer.Main '' '' %{classpath}:rhino rasterizer true
%jpackage_script org.apache.batik.apps.slideshow.Main '' '' %{classpath} slideshow true

# Demo
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -pr samples $RPM_BUILD_ROOT%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT`dirname /etc/rasterizer.conf`
touch $RPM_BUILD_ROOT/etc/rasterizer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/slideshow.conf`
touch $RPM_BUILD_ROOT/etc/slideshow.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/squiggle.conf`
touch $RPM_BUILD_ROOT/etc/squiggle.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/svgpp.conf`
touch $RPM_BUILD_ROOT/etc/svgpp.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/ttf2svg.conf`
touch $RPM_BUILD_ROOT/etc/ttf2svg.conf


%files -f .mfiles
%doc --no-dereference LICENSE NOTICE
%doc CHANGES MAINTAIN README

%files css -f .mfiles-css
%files util -f .mfiles-util

%files squiggle -f .mfiles-squiggle
%{_bindir}/squiggle
%config(noreplace,missingok) /etc/squiggle.conf

%files svgpp -f .mfiles-svgpp
%{_bindir}/svgpp
%config(noreplace,missingok) /etc/svgpp.conf

%files ttf2svg -f .mfiles-ttf2svg
%{_bindir}/ttf2svg
%config(noreplace,missingok) /etc/ttf2svg.conf

%files rasterizer -f .mfiles-rasterizer
%{_bindir}/rasterizer
%config(noreplace,missingok) /etc/rasterizer.conf

%files slideshow -f .mfiles-slideshow
%{_bindir}/slideshow
%config(noreplace,missingok) /etc/slideshow.conf

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%files demo
%{_datadir}/%{name}


%changelog
* Mon Aug 16 2021 Igor Vlasenko <viy@altlinux.org> 0:1.14-alt1_3jpp8
- update

* Sat Jun 12 2021 Igor Vlasenko <viy@altlinux.org> 0:1.14-alt1_1jpp8
- new version

* Tue Jun 01 2021 Igor Vlasenko <viy@altlinux.org> 0:1.13-alt1_1jpp8
- new version

* Sat Dec 12 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt2_3jpp8
- use zerg@'s hack for armh

* Sun Oct 11 2020 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_3jpp8
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_4jpp8
- new version

* Mon Feb 04 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_2jpp8
- java update

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_1jpp8
- java update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_6jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.9-alt1_5jpp8
- new jpp release

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt3_6jpp8
-dropped deprecated upgrade hack (closes: #32819)

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_6jpp8
- new fc release

* Thu May 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt2_2jpp8
- added conflicts (closes: #32067)

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_2jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.10.svn1230816jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.7.svn1230816jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.5.svn1230816jpp7
- fc update

* Thu Aug 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_0.4.svn1230816jpp7
- new version

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt7_14jpp6
- added compat symlinks

* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_14jpp6
- updated OSGi manifest

* Sat Dec 04 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_7jpp6
- added OSGi provides

* Tue Mar 31 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt6_5jpp5
- proper fix of #19119. Thanks to mithraen@ for report.

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt5_5jpp5
- fixed #19119

* Sat Feb 21 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4_5jpp5
- added batik dir symlink

* Thu Sep 11 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_5jpp5
- fixed unmets

* Wed Sep 10 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_5jpp5
- converted from JPackage by jppimport script

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_5jpp5
- converted from JPackage by jppimport script

