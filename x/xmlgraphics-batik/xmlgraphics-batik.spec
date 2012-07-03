AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
# Copyright (c) 2000-2011, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Name:           xmlgraphics-batik
Version:        1.7
Release:        alt7_14jpp6
Epoch:          0
Summary:        Scalable Vector Graphics for Java
License:        ASL 2.0
URL:            http://xml.apache.org/batik/
Group:          Graphics
Source0:        batik-src-%{version}.zip
Source1:        %{name}.squiggle.script
Source2:        %{name}.svgpp.script
Source3:        %{name}.ttf2svg.script
Source4:        %{name}.rasterizer.script
Source5:        %{name}.slideshow.script
Source6:        %{name}-squiggle.desktop
Source7:        %{name}.rasterizer.policy
Patch0:         %{name}-manifests.patch
Patch1:         %{name}-policy.patch
Patch2:         %{name}-rasterizer-ext-pom-template.patch
Patch3:         %{name}-squiggle-ext-pom-template.patch
Patch4:         %{name}-no-svn.patch
Patch5:         %{name}-javadoc-maxmemory.patch
Obsoletes:      batik < %{epoch}:%{version}-%{release}
Provides:       batik = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       rhino
Requires:       xalan-j2
Requires:       xml-commons-jaxp-1.3-apis >= 0:1.3.04-7
BuildRequires:  ant
BuildRequires:  java-javadoc
BuildRequires:  rhino
BuildRequires:  rhino-javadoc
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-jaxp-1.3-apis >= 0:1.3.04-7
BuildArch:      noarch
Source44: import.info
Source45: batik-anim.jar-OSGi-MANIFEST.MF
Source46: batik-awt-util.jar-OSGi-MANIFEST.MF
Source47: batik-bridge.jar-OSGi-MANIFEST.MF
Source48: batik-codec.jar-OSGi-MANIFEST.MF
Source49: batik-css.jar-OSGi-MANIFEST.MF
Source50: batik-dom.jar-OSGi-MANIFEST.MF
Source51: batik-ext.jar-OSGi-MANIFEST.MF
Source52: batik-extension.jar-OSGi-MANIFEST.MF
Source53: batik-gui-util.jar-OSGi-MANIFEST.MF
Source54: batik-gvt.jar-OSGi-MANIFEST.MF
Source55: batik-parser.jar-OSGi-MANIFEST.MF
Source56: batik-script.jar-OSGi-MANIFEST.MF
Source57: batik-svg-dom.jar-OSGi-MANIFEST.MF
Source58: batik-svggen.jar-OSGi-MANIFEST.MF
Source59: batik-swing.jar-OSGi-MANIFEST.MF
Source60: batik-transcoder.jar-OSGi-MANIFEST.MF
Source61: batik-util.jar-OSGi-MANIFEST.MF
Source62: batik-xml.jar-OSGi-MANIFEST.MF
#19119
Conflicts: batik < 0:%version
Conflicts: batik-rasterizer < 0:%version
Conflicts: batik-slideshow < 0:%version
Conflicts: batik-svgpp < 0:%version
Conflicts: batik-ttf2svg < 0:%version

%description
Batik is a Java(tm) technology based toolkit for applications that want
to use images in the Scalable Vector Graphics (SVG) format for various
purposes, such as viewing, generation or manipulation.

%package squiggle
Summary:        Batik SVG browser
Group:          Graphics
Obsoletes:      batik-squiggle < %{epoch}:%{version}-%{release}
Provides:       batik-squiggle = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils

%description squiggle
The Squiggle SVG Browser lets you view SVG file, zoom, pan and rotate
in the content and select text items in the image and much more.

%package svgpp
Summary:        Batik SVG pretty printer
Group:          Graphics
Obsoletes:      batik-svgpp < %{epoch}:%{version}-%{release}
Provides:       batik-svgpp = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
#19119
Conflicts: batik < 0:%version
Conflicts: batik-rasterizer < 0:%version
Conflicts: batik-slideshow < 0:%version
Conflicts: batik-svgpp < 0:%version
Conflicts: batik-ttf2svg < 0:%version

%description svgpp
The SVG Pretty Printer lets developers "pretty-up" their SVG files and
get their tabulations and other cosmetic parameters in order. It can
also be used to modify the DOCTYPE declaration on SVG files.

%package ttf2svg
Summary:        Batik SVG font converter
Group:          Graphics
Obsoletes:      batik-ttf2svg < %{epoch}:%{version}-%{release}
Provides:       batik-ttf2svg = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
#19119
Conflicts: batik < 0:%version
Conflicts: batik-rasterizer < 0:%version
Conflicts: batik-slideshow < 0:%version
Conflicts: batik-svgpp < 0:%version
Conflicts: batik-ttf2svg < 0:%version

%description ttf2svg
The SVG Font Converter lets developers convert character ranges from
the True Type Font format to the SVG Font format to embed in SVG
documents. This allows SVG document to be fully self-contained be
rendered exactly the same on all systems.

%package rasterizer
Summary:        Batik SVG rasterizer
Group:          Graphics
Obsoletes:      batik-rasterizer < %{epoch}:%{version}-%{release}
Provides:       batik-rasterizer = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
#19119
Conflicts: batik < 0:%version
Conflicts: batik-rasterizer < 0:%version
Conflicts: batik-slideshow < 0:%version
Conflicts: batik-svgpp < 0:%version
Conflicts: batik-ttf2svg < 0:%version

%description rasterizer
The SVG Rasterizer is a utility that can convert SVG files to a raster
format. The tool can convert individual files or sets of files, making
it easy to convert entire directories of SVG files. The supported
formats are JPEG, PNG, and TIFF, however the design allows new formats
to be added easily.

%package slideshow
Summary:        Batik SVG slideshow
Group:          Graphics
Obsoletes:      batik-slideshow < %{epoch}:%{version}-%{release}
Provides:       batik-slideshow = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
#19119
Conflicts: batik < 0:%version
Conflicts: batik-rasterizer < 0:%version
Conflicts: batik-slideshow < 0:%version
Conflicts: batik-svgpp < 0:%version
Conflicts: batik-ttf2svg < 0:%version

%description slideshow
Batik SVG slideshow.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Graphics
Obsoletes:      batik-javadoc < %{epoch}:%{version}-%{release}
Provides:       batik-javadoc = %{epoch}:%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Graphics
Obsoletes:      batik-demo < %{epoch}:%{version}-%{release}
Provides:       batik-demo = %{epoch}:%{version}-%{release}
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n batik-%{version}
%patch0 -p1 -b .sav0
%patch1 -p1 -b .sav1
%patch2 -p0 -b .sav2
%patch3 -p0 -b .sav3
%patch4 -p0 -b .sav4
%patch5 -p0 -b .sav5

%{_bindir}/find -type f -name "*.class" | %{_bindir}/xargs -t %{__rm}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}

%{_bindir}/find -type f -name "*.sh" | %{_bindir}/xargs -t %{__chmod} 0755

rm resources/org/apache/batik/ext/awt/image/codec/properties
rm test-resources/org/apache/batik/apps/rasterizer/readOnly.png

%{__mkdir_p} batik-%{version}/lib
ln -s $(build-classpath rhino) batik-%{version}/lib/js.jar

%build

export ANT_OPTS="-Xmx512m"
# due to javadoc x86_64 out of memory
subst 's,maxmemory="128m",maxmemory="512m",' build.xml
export CLASSPATH=`%{_bindir}/build-classpath xalan-j2 xml-commons-jaxp-1.3-apis-ext js`
export OPT_JAR_LIST=:
export ANT_OPTS="-Xms1g"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Drhino.javadoc=file:%{_javadocdir}/rhino -Dbuild.sysclasspath=first all-jar jars javadoc maven-artifacts

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}

for dir in batik-%{version} batik-%{version}/lib batik-%{version}/extensions; do
  pushd ${dir}
    for jar in batik*.jar; do
      basename=`/bin/basename ${jar} .jar`
      %{__cp} -p ${basename}.jar %{buildroot}%{_javadir}/%{name}/${basename}-%{version}.jar
    done
  popd
done

for pkg in squiggle squiggle-ext svgpp ttf2svg rasterizer rasterizer-ext slideshow; do
  ln -s %{name}/batik-${pkg}-%{version}.jar %{buildroot}%{_javadir}/batik-${pkg}-%{version}.jar
done

mv %{buildroot}%{_javadir}/%{name}/batik-all-%{version}.jar %{buildroot}%{_javadir}/batik-all-%{version}.jar
#ln -s %{name}/batik-all-%{version}.jar %{buildroot}%{_javadir}/batik-all-%{version}.jar

for dir in %{buildroot}%{_javadir} %{buildroot}%{_javadir}/%{name}; do
  pushd ${dir}
    for jar in *-%{version}*.jar; do
      ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; 
    done
  popd
done

# pom
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p batik-%{version}/maven/batik-anim/%{version}/batik-anim-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-anim.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-anim %{version} JPP/%{name} batik-anim
%{__cp} -p batik-%{version}/maven/batik-awt-util/%{version}/batik-awt-util-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-awt-util.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-awt-util %{version} JPP/%{name} batik-awt-util
%{__cp} -p batik-%{version}/maven/batik-bridge/%{version}/batik-bridge-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-bridge.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-bridge %{version} JPP/%{name} batik-bridge
%{__cp} -p batik-%{version}/maven/batik-codec/%{version}/batik-codec-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-codec.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-codec %{version} JPP/%{name} batik-codec
%{__cp} -p batik-%{version}/maven/batik-css/%{version}/batik-css-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-css.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-css %{version} JPP/%{name} batik-css
%{__cp} -p batik-%{version}/maven/batik-dom/%{version}/batik-dom-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-dom.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-dom %{version} JPP/%{name} batik-dom
%{__cp} -p batik-%{version}/maven/batik-ext/%{version}/batik-ext-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-ext.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-ext %{version} JPP/%{name} batik-ext
%{__cp} -p batik-%{version}/maven/batik-extension/%{version}/batik-extension-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-extension.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-extension %{version} JPP/%{name} batik-extension
%{__cp} -p batik-%{version}/maven/batik-gui-util/%{version}/batik-gui-util-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-gui-util.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-gui-util %{version} JPP/%{name} batik-gui-util
%{__cp} -p batik-%{version}/maven/batik-gvt/%{version}/batik-gvt-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-gvt.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-gvt %{version} JPP/%{name} batik-gvt
%if 0
%{__cp} -p batik-%{version}/maven/batik-js/%{version}/batik-js-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-js.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-js %{version} JPP/%{name} batik-js
%else
%add_to_maven_depmap org.apache.xmlgraphics batik-js %{version} JPP rhino
%endif
%{__cp} -p batik-%{version}/maven/batik-parser/%{version}/batik-parser-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-parser.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-parser %{version} JPP/%{name} batik-parser
%{__cp} -p batik-%{version}/maven/batik-rasterizer/%{version}/batik-rasterizer-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-rasterizer.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-rasterizer %{version} JPP/%{name} batik-rasterizer
%{__cp} -p batik-%{version}/maven/batik-rasterizer-ext/%{version}/batik-rasterizer-ext-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-rasterizer-ext.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-rasterizer-ext %{version} JPP/%{name} batik-rasterizer-ext
%{__cp} -p batik-%{version}/maven/batik-script/%{version}/batik-script-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-script.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-script %{version} JPP/%{name} batik-script
%{__cp} -p batik-%{version}/maven/batik-slideshow/%{version}/batik-slideshow-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-slideshow.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-slideshow %{version} JPP/%{name} batik-slideshow
%{__cp} -p batik-%{version}/maven/batik-squiggle/%{version}/batik-squiggle-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-squiggle.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-squiggle %{version} JPP/%{name} batik-squiggle
%{__cp} -p batik-%{version}/maven/batik-squiggle-ext/%{version}/batik-squiggle-ext-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-squiggle-ext.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-squiggle-ext %{version} JPP/%{name} batik-squiggle-ext
%{__cp} -p batik-%{version}/maven/batik-svg-dom/%{version}/batik-svg-dom-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-svg-dom.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-svg-dom %{version} JPP/%{name} batik-svg-dom
%{__cp} -p batik-%{version}/maven/batik-svggen/%{version}/batik-svggen-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-svggen.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-svggen %{version} JPP/%{name} batik-svggen
%{__cp} -p batik-%{version}/maven/batik-svgpp/%{version}/batik-svgpp-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-svgpp.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-svgpp %{version} JPP/%{name} batik-svgpp
%{__cp} -p batik-%{version}/maven/batik-swing/%{version}/batik-swing-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-swing.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-swing %{version} JPP/%{name} batik-swing
%{__cp} -p batik-%{version}/maven/batik-transcoder/%{version}/batik-transcoder-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-transcoder.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-transcoder %{version} JPP/%{name} batik-transcoder
%{__cp} -p batik-%{version}/maven/batik-ttf2svg/%{version}/batik-ttf2svg-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-ttf2svg.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-ttf2svg %{version} JPP/%{name} batik-ttf2svg
%{__cp} -p batik-%{version}/maven/batik-util/%{version}/batik-util-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-util.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-util %{version} JPP/%{name} batik-util
%{__cp} -p batik-%{version}/maven/batik-xml/%{version}/batik-xml-%{version}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-batik-xml.pom
%add_to_maven_depmap org.apache.xmlgraphics batik-xml %{version} JPP/%{name} batik-xml

# scripts
mkdir -p %{buildroot}%{_bindir}
cp -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}-squiggle
cp -p %{SOURCE2} %{buildroot}%{_bindir}/%{name}-svgpp
cp -p %{SOURCE3} %{buildroot}%{_bindir}/%{name}-ttf2svg
cp -p %{SOURCE4} %{buildroot}%{_bindir}/%{name}-rasterizer
cp -p %{SOURCE5} %{buildroot}%{_bindir}/%{name}-slideshow

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr batik-%{version}/docs/javadoc/* \
  %{buildroot}%{_javadocdir}/%{name}-%{version} || :
# FIXME: (dwalluck): This breaks bi --short-circuit
rm -rf %{name}-%{version}/docs/javadoc
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/batik-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
ln -s %{name} %{buildroot}%{_javadocdir}/batik

# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr contrib resources samples test-resources test-sources \
  %{buildroot}%{_datadir}/%{name}
ln -s %{name} %{buildroot}%{_datadir}/batik

# policy
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp -p %{SOURCE7} %{buildroot}%{_sysconfdir}/%{name}/rasterizer.policy

# inject OSGi manifest batik-anim.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-anim.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-awt-util.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE46} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-awt-util.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-bridge.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE47} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-bridge.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-codec.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE48} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-codec.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-css.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE49} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-css.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-dom.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE50} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-dom.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-ext.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE51} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-ext.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-extension.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE52} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-extension.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-gui-util.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE53} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-gui-util.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-gvt.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE54} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-gvt.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-parser.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE55} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-parser.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-script.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE56} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-script.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-svg-dom.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE57} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-svg-dom.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-svggen.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE58} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-svggen.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-swing.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE59} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-swing.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-transcoder.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE60} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-transcoder.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-util.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE61} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-util.jar META-INF/MANIFEST.MF

# inject OSGi manifest batik-xml.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE62} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/xmlgraphics-batik/batik-xml.jar META-INF/MANIFEST.MF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}-rasterizer.conf`
touch $RPM_BUILD_ROOT/etc/%{name}-rasterizer.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}-slideshow.conf`
touch $RPM_BUILD_ROOT/etc/%{name}-slideshow.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}-squiggle.conf`
touch $RPM_BUILD_ROOT/etc/%{name}-squiggle.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}-svgpp.conf`
touch $RPM_BUILD_ROOT/etc/%{name}-svgpp.conf

mkdir -p $RPM_BUILD_ROOT`dirname /etc/%{name}-ttf2svg.conf`
touch $RPM_BUILD_ROOT/etc/%{name}-ttf2svg.conf
pushd $RPM_BUILD_ROOT%_javadir/xmlgraphics-batik
  ln -s batik-anim.jar anim.jar
  ln -s batik-awt-util.jar awt-util.jar
  ln -s batik-bridge.jar bridge.jar
  ln -s batik-codec.jar codec.jar
  ln -s batik-css.jar css.jar
  ln -s batik-dom.jar dom.jar
  ln -s batik-ext.jar ext.jar
  ln -s batik-extension.jar extension.jar
  ln -s batik-gui-util.jar gui-util.jar
  ln -s batik-gvt.jar gvt.jar
  ln -s batik-parser.jar parser.jar
  ln -s batik-script.jar script.jar
  ln -s batik-svg-dom.jar svg-dom.jar
  ln -s batik-svggen.jar svggen.jar
  ln -s batik-swing.jar swing.jar
  ln -s batik-transcoder.jar transcoder.jar
  ln -s batik-util.jar util.jar
  ln -s batik-xml.jar xml.jar
  ln -s batik-rasterizer.jar rasterizer.jar
  ln -s batik-rasterizer-ext.jar rasterizer-ext.jar
popd

pushd $RPM_BUILD_ROOT%_javadir
  ln -s xmlgraphics-batik batik
popd

# due to #19119
#1: xmlgraphics-batik         error: unpacking of archive failed on file
#/usr/share/java/batik: cpio: rename failed - Is a directory
#E: Some errors occurred while running transaction
%pre
[ -d /usr/share/java/batik ] && rm -rf /usr/share/java/batik ||:
# end inject OSGi manifest batik-xml.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-util.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-transcoder.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-swing.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-svggen.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-svg-dom.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-script.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-parser.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-gvt.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-gui-util.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-extension.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-ext.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-dom.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-css.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-codec.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-bridge.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-awt-util.jar-OSGi-MANIFEST.MF
# end inject OSGi manifest batik-anim.jar-OSGi-MANIFEST.MF

%files
%doc CHANGES KEYS LICENSE MAINTAIN NOTICE README
%dir %{_javadir}*/%{name}
%exclude %dir %{_javadocdir}/%{name}
%{_javadir}*/batik-all-%{version}.jar
%{_javadir}*/batik-all.jar
%{_javadir}*/%{name}/batik-%{version}.jar
%{_javadir}*/%{name}/batik.jar
%{_javadir}*/%{name}/batik-anim-%{version}.jar
%{_javadir}*/%{name}/batik-anim.jar
%{_javadir}*/%{name}/batik-awt-util-%{version}.jar
%{_javadir}*/%{name}/batik-awt-util.jar
%{_javadir}*/%{name}/batik-bridge-%{version}.jar
%{_javadir}*/%{name}/batik-bridge.jar
%{_javadir}*/%{name}/batik-codec-%{version}.jar
%{_javadir}*/%{name}/batik-codec.jar
%{_javadir}*/%{name}/batik-css-%{version}.jar
%{_javadir}*/%{name}/batik-css.jar
%{_javadir}*/%{name}/batik-dom-%{version}.jar
%{_javadir}*/%{name}/batik-dom.jar
%{_javadir}*/%{name}/batik-ext-%{version}.jar
%{_javadir}*/%{name}/batik-ext.jar
%{_javadir}*/%{name}/batik-extension-%{version}.jar
%{_javadir}*/%{name}/batik-extension.jar
%{_javadir}*/%{name}/batik-gui-util-%{version}.jar
%{_javadir}*/%{name}/batik-gui-util.jar
%{_javadir}*/%{name}/batik-gvt-%{version}.jar
%{_javadir}*/%{name}/batik-gvt.jar
%{_javadir}*/%{name}/batik-parser-%{version}.jar
%{_javadir}*/%{name}/batik-parser.jar
%{_javadir}*/%{name}/batik-script-%{version}.jar
%{_javadir}*/%{name}/batik-script.jar
%{_javadir}*/%{name}/batik-svg-dom-%{version}.jar
%{_javadir}*/%{name}/batik-svg-dom.jar
%{_javadir}*/%{name}/batik-svggen-%{version}.jar
%{_javadir}*/%{name}/batik-svggen.jar
%{_javadir}*/%{name}/batik-swing-%{version}.jar
%{_javadir}*/%{name}/batik-swing.jar
%{_javadir}*/%{name}/batik-transcoder-%{version}.jar
%{_javadir}*/%{name}/batik-transcoder.jar
%{_javadir}*/%{name}/batik-util-%{version}.jar
%{_javadir}*/%{name}/batik-util.jar
%{_javadir}*/%{name}/batik-xml-%{version}.jar
%{_javadir}*/%{name}/batik-xml.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-anim.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-awt-util.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-bridge.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-codec.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-css.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-dom.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-ext.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-extension.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-gui-util.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-gvt.pom
%if 0
%{_datadir}/maven2/poms/JPP.%{name}-batik-js.pom
%endif
%{_datadir}/maven2/poms/JPP.%{name}-batik-parser.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-script.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-svg-dom.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-svggen.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-swing.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-transcoder.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-util.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-xml.pom
%{_mavendepmapfragdir}/%{name}
%dir %{_sysconfdir}/%{name}
%_javadir/xmlgraphics-batik/anim.jar
%_javadir/xmlgraphics-batik/awt-util.jar
%_javadir/xmlgraphics-batik/bridge.jar
%_javadir/xmlgraphics-batik/codec.jar
%_javadir/xmlgraphics-batik/css.jar
%_javadir/xmlgraphics-batik/dom.jar
%_javadir/xmlgraphics-batik/ext.jar
%_javadir/xmlgraphics-batik/extension.jar
%_javadir/xmlgraphics-batik/gui-util.jar
%_javadir/xmlgraphics-batik/gvt.jar
%_javadir/xmlgraphics-batik/parser.jar
%_javadir/xmlgraphics-batik/script.jar
%_javadir/xmlgraphics-batik/svg-dom.jar
%_javadir/xmlgraphics-batik/svggen.jar
%_javadir/xmlgraphics-batik/swing.jar
%_javadir/xmlgraphics-batik/transcoder.jar
%_javadir/xmlgraphics-batik/util.jar
%_javadir/xmlgraphics-batik/xml.jar
%_javadir/batik

%files squiggle
%{_javadir}*/%{name}/batik-squiggle-%{version}.jar
%{_javadir}*/%{name}/batik-squiggle.jar
%{_javadir}*/%{name}/batik-squiggle-ext-%{version}.jar
%{_javadir}*/%{name}/batik-squiggle-ext.jar
%{_javadir}*/batik-squiggle-%{version}.jar
%{_javadir}*/batik-squiggle.jar
%{_javadir}*/batik-squiggle-ext-%{version}.jar
%{_javadir}*/batik-squiggle-ext.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-squiggle.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-squiggle-ext.pom
%attr(0755,root,root) %{_bindir}/%{name}-squiggle
%config(noreplace,missingok) /etc/%{name}-squiggle.conf

%files svgpp
%{_javadir}*/%{name}/batik-svgpp-%{version}.jar
%{_javadir}*/%{name}/batik-svgpp.jar
%{_javadir}*/batik-svgpp-%{version}.jar
%{_javadir}*/batik-svgpp.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-svgpp.pom
%attr(0755,root,root) %{_bindir}/%{name}-svgpp
%config(noreplace,missingok) /etc/%{name}-svgpp.conf

%files ttf2svg
%{_javadir}*/%{name}/batik-ttf2svg-%{version}.jar
%{_javadir}*/%{name}/batik-ttf2svg.jar
%{_javadir}*/batik-ttf2svg-%{version}.jar
%{_javadir}*/batik-ttf2svg.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-ttf2svg.pom
%attr(0755,root,root) %{_bindir}/%{name}-ttf2svg
%config(noreplace,missingok) /etc/%{name}-ttf2svg.conf

%files rasterizer
%{_javadir}*/%{name}/batik-rasterizer-%{version}.jar
%{_javadir}*/%{name}/batik-rasterizer.jar
%{_javadir}*/%{name}/batik-rasterizer-ext-%{version}.jar
%{_javadir}*/%{name}/batik-rasterizer-ext.jar
%{_javadir}*/batik-rasterizer-%{version}.jar
%{_javadir}*/batik-rasterizer.jar
%{_javadir}*/batik-rasterizer-ext-%{version}.jar
%{_javadir}*/batik-rasterizer-ext.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-rasterizer.pom
%{_datadir}/maven2/poms/JPP.%{name}-batik-rasterizer-ext.pom
%attr(0755,root,root) %{_bindir}/%{name}-rasterizer
%config(noreplace) %{_sysconfdir}/%{name}/rasterizer.policy
%config(noreplace,missingok) /etc/%{name}-rasterizer.conf
%_javadir/xmlgraphics-batik/rasterizer.jar
%_javadir/xmlgraphics-batik/rasterizer-ext.jar

%files slideshow
%{_javadir}*/%{name}/batik-slideshow-%{version}.jar
%{_javadir}*/%{name}/batik-slideshow.jar
%{_javadir}*/batik-slideshow-%{version}.jar
%{_javadir}*/batik-slideshow.jar
%{_datadir}/maven2/poms/JPP.%{name}-batik-slideshow.pom
%attr(0755,root,root) %{_bindir}/%{name}-slideshow
%config(noreplace,missingok) /etc/%{name}-slideshow.conf

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%{_javadocdir}/batik-%{version}
%{_javadocdir}/batik

%files demo
%{_datadir}/%{name}
%{_datadir}/batik

%changelog
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

