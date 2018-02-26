BuildRequires: ant-apache-regexp ant-apache-xalan2
BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
BuildRequires: python-devel
# Copyright (c) 2000-2008, JPackage Project
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
#


Name:           aspectj
Version:        1.5.4
Release:        alt2_1jpp6
Epoch:          0
Summary:        AspectJ aspect-oriented language extension to Java
License:        EPL
URL:            http://eclipse.org/aspectj/
Group:          Development/Java
# cvs -d:pserver:anonymous@dev.eclipse.org:/cvsroot/tools/ export -r V1_5_4 org.aspectj && tar cjf aspectj-1.5.4.tar.bz2 org.aspectj
Source0:        aspectj-1.5.4.tar.bz2
Source1:        aspectj-build-build.xml
Source2:        aspectj-jdtcore4aspectj-build.xml
Source3:        http://archive.apache.org/dist/jakarta/bcel/source/bcel-5.1-src.zip
Source4:        aspectj-1.5.3-build-bcel.xml
Source5:        aspectj-1.5.3-script-aj
Source6:        aspectj-1.5.3-script-aj5
Source7:        aspectj-1.5.3-script-ajbrowser
Source8:        aspectj-1.5.3-script-ajc
Source9:        aspectj-1.5.3-script-ajdoc
Source10:       aspectjlib-1.5.4.pom
Source11:       http://mirrors.ibiblio.org/pub/mirrors/maven2/org/aspectj/aspectjrt/1.5.4/aspectjrt-1.5.4.pom
Source12:       http://mirrors.ibiblio.org/pub/mirrors/maven2/org/aspectj/aspectjtools/1.5.4/aspectjtools-1.5.4.pom
Source13:       http://mirrors.ibiblio.org/pub/mirrors/maven2/org/aspectj/aspectjweaver/1.5.4/aspectjweaver-1.5.4.pom


Patch0:         aspectj-1.5.3-bcel-builder-build_xml.patch
Patch1:         aspectj-1.5.3-PluginModel.patch
Patch2:         aspectj-1.5.3-PluginFragmentModel.patch
Patch3:         aspectj-1.5.3-PluginModelObject.patch
Patch4:         aspectj-1.5.3-PluginRegistryModel.patch
Patch5:         aspectj-1.5.3-PluginPrerequisiteModel.patch
Patch6:         aspectj-1.5.3-LibraryModel.patch
Patch7:         aspectj-1.5.3-ResourceTree.patch
Patch8:         aspectj-1.5.3-ProjectPreferences.patch
Patch9:         aspectj-1.5.3-Resource.patch
Patch10:        aspectj-1.5.3-File.patch
Patch11:        aspectj-1.5.3-Project.patch
Patch12:        aspectj-1.5.3-SaveManager.patch
Patch13:        aspectj-1.5.3-CharsetManager.patch
Patch14:        aspectj-1.5.3-Workspace.patch
Patch15:        aspectj-1.5.3-BlobStore.patch
Patch16:        aspectj-1.5.3-HistoryStore2.patch
Patch17:        aspectj-1.5.4-JavaCore.patch
Patch18:        aspectj-1.5.3-Factory.patch
Patch19:        aspectj-1.5.4-CompilationUnitResolver.patch
Patch20:        aspectj-1.5.4-CompilationUnitProblemFinder.patch

#Patch1:         aspectj-docs-build_xml.patch
BuildRequires:  jpackage-utils >= 0:1.7.3
#BuildRequires:  java-devel >= 0:1.4.2
#BuildRequires:  java-devel <  0:1.5.0
#BuildRequires:  java-devel >= 0:1.5.0
#BuildRequires:  java-devel <  0:1.6.0
BuildRequires:  junit
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
#BuildRequires:  java-devel >= 0:1.4.2
BuildRequires:  eclipse-platform
BuildRequires:  jakarta-commons-beanutils
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-digester
BuildRequires:  jakarta-commons-logging
BuildRequires:  regexp
BuildRequires:  saxon
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:  jakarta-commons-beanutils
Requires:  jakarta-commons-collections
Requires:  jakarta-commons-digester
Requires:  jakarta-commons-logging
Requires:  regexp
Requires:  saxon
Requires:  xalan-j2
Requires:  xerces-j2
Requires:  xml-commons-apis
Requires(post):    jpackage-utils >= 0:1.7.2
Requires(postun):  jpackage-utils >= 0:1.7.2

BuildArch:      noarch
Source44: import.info
Patch33: aspectj-ant_0_8_fix.diff

%description
AspectJ is a seamless aspect-oriented language 
extension to Java(tm). It can be used to cleanly 
modularize the crosscutting structure of concerns 
such as exception handling, multi-object protocols, 
synchronization, performance optimizations, and 
resource sharing. When implemented in a 
non-aspect-oriented fashion, the code for these concerns 
typically becomes spread out across entire programs. 
AspectJ controls such code-tangling and makes the 
underlying concerns more apparent, making programs 
easier to develop and maintain. The project goal 
is to support the AspectJ compiler and core tools. 

%package eclipse-plugins
Summary:        Eclipse Plugins for %{name}
Group:          Development/Java
Requires:       %{name} = 0:%{version}
Requires:       eclipse-platform

%description eclipse-plugins
%{summary}.

%package installer
Summary:        Installer for %{name}
Group:          Development/Java

%description installer
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Docs for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -n org.%{name}

%if 0
# save local jdiff sources
#export JAVA_HOME=%{java_home}
export ANT_OPTS="-Xmx512M"
( cd modules/lib/jdiff
  unzip -qq jdiff.jar
  rm jdiff.jar
  rm -r jdiff
  %{javac}  -target 1.5 -source 1.5 -d . -sourcepath src `find src -name "*.java"`
  %{jar} cf jdiff.jar.new jdiff
)
mv modules/lib/jdiff/jdiff.jar.new modules/lib/jdiff/jdiff.jar

( cd modules/lib/commons
  %{jar} xf $(find-jar commons-beanutils)
  %{jar} xf $(find-jar commons-collections)
  %{jar} xf $(find-jar commons-digester)
  %{jar} xf $(find-jar commons-logging)
  %{jar} cf commons.jar org
)
%endif

# FIXME: need to remove bundled jars
%{_bindir}/find -type f -name "*.jar" -a ! -name "aspectj*.jar" | %{_bindir}/xargs -t %{__rm}

cp -p %{SOURCE1} modules/build/build-build.xml
cp -p %{SOURCE3} modules/bcel-builder
cp -p %{SOURCE4} modules/bcel-builder/build-bcel.xml
#def##cp -p %{SOURCE3} modules/org.eclipse.jdt.core/jdtcore-for-aspectj-src.zip
#rap#touch modules/build/local.properties
#rap#rm modules/loadtime/src/org/aspectj/weaver/loadtime/JRockitAgent.java
cp -p %{SOURCE2} modules/org.eclipse.jdt.core/build.xml

ln -sf $(build-classpath ant) modules/lib/ant/lib/ant.jar
ln -sf $(build-classpath ant-launcher) modules/lib/ant/lib/ant-launcher.jar
ln -sf $(build-classpath ant/ant-junit) modules/lib/ant/lib/ant-junit.jar
ln -sf $(build-classpath ant/ant-nodeps) modules/lib/ant/lib/ant-nodeps.jar
ln -sf $(build-classpath xerces-j2) modules/lib/ant/lib/xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) modules/lib/ant/lib/xml-apis.jar

ln -sf $(build-classpath asm2/asm2) modules/lib/asm/asm-2.2.1.jar
ln -sf $(build-classpath junit) modules/lib/junit/junit.jar
ln -sf $(build-classpath regexp) modules/lib/regexp/jakarta-regexp-1.2.jar
ln -sf $(build-classpath saxon) modules/lib/saxon/saxon.jar

pushd modules/org.eclipse.jdt.core
  mkdir src
  pushd src
  unzip -qq -o ../jdtcore-for-aspectj-src.zip
  popd
popd
%patch0 -b .sav0
%if 0
%patch1 -b .sav1
%patch2 -b .sav2
%patch3 -b .sav3
%patch4 -b .sav4
%patch5 -b .sav5
%patch6 -b .sav6
%patch7 -b .sav7
%patch8 -b .sav8
%patch9 -b .sav9
%patch10 -b .sav10
%patch11 -b .sav11
%patch12 -b .sav12
%patch13 -b .sav13
%patch14 -b .sav14
%patch15 -b .sav15
%patch16 -b .sav16
%patch18 -b .sav18
%endif
%patch17 -b .sav17
%patch19 -b .sav19
%patch20 -b .sav20

rm modules/loadtime/src/org/aspectj/weaver/loadtime/JRockitAgent.java

mv modules/build/build-properties.xml modules/build/build-properties.xml.orig
sed -e 's|"DEVELOPMENT"|"%{version}"|' modules/build/build-properties.xml.orig \
     > modules/build/build-properties.xml

# Avoid use of eclipse's OperationCanceledException
for j in $(find . -name "*.java" -exec grep -l "org\.eclipse\.core\.runtime\.OperationCanceledException" {} \;); do
    sed -i -e '/import org\.eclipse\.core\.runtime\.OperationCanceledException/d' $j
    sed -i -e 's/org\.eclipse\.core\.runtime\.OperationCanceledException/org\.eclipse\.core\.runtime\.OperationCanceledException/' $j
    sed -i -e 's/OperationCanceledException/RuntimeException/g' $j
done
%patch33 -p2

%build
#export JAVA_HOME=%{java_home}
export ANT_OPTS="-Xmx1024M"
# CLASSPATH needed for rebuilds from sources
#rap#export OPT_JAR_LIST="ant/ant-junit junit ant/ant-nodeps"
export CLASSPATH=$(build-classpath \
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  \
ant-launcher \
commons-logging \
)

# now for eclipse 3.2.X
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.osgi_*.jar)
#CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.osgi.util_*.jar)
#CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.jface.text_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.text_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.update.configurator_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.runtime_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.resources_*.jar)
#rap#CLASSPATH=${CLASSPATH}:%{java_home}-bea/jre/lib/managementserver.jar
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.common_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.contenttype_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.preferences_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.registry_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.jobs_*.jar)

# rebuild jdtcore-for-aspectj.jar from sources
pushd modules/org.eclipse.jdt.core
export ASPECTJ_HOME=$RPM_BUILD_DIR/org.aspectj/modules/lib/aspectj
"%{java}" -classpath "$ASPECTJ_HOME/lib/aspectjtools.jar:$ASPECTJ_HOME/lib/aspectjrt.jar:$JAVA_HOME/lib/tools.jar:$CLASSPATH" -Xmx1024M org.aspectj.tools.ajc.Main -sourceroots src -d build-classes
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar
popd

#cp modules/org.eclipse.jdt.core/jdtcore-for-aspectj.jar.no modules/org.eclipse.jdt.core/jdtcore-for-aspectj.jar 

pushd modules/bcel-builder
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f build-bcel.xml
cp bin/bcel.jar .
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  extractAndPatchAndJar
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  push
popd

# rebuild the build-module from sources
pushd modules/build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f build-build.xml
# do the product build
touch local.properties
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first
# do the release build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f release/build.xml \
       -Dversion=%{version} -Dskip.cvs=true \
       -Daspectj.modules.dir=$(pwd)/.. \
       -Djava13.home=%{java_home} \
       -Djava14.home=%{java_home} \
       -Djava15.home=%{java_home} \
       -Drun.14.only=false \
       -Dmin.vm=14 \
       -Dmax.vm=15 \
       install \
    | tee build-log-release-aspectj-%{version}.txt
# do the test build
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f release/build.xml \
       -Dversion=%{version} -Dskip.cvs=true \
       -Daspectj.modules.dir=$(pwd)/.. \
       -Djava13.home=%{java_home} \
       -Djava14.home=%{java_home} \
       -Djava15.home=%{java_home} \
       -Dskip.build=true \
       -Drun.14.only=false \
       -Dmin.vm=14 \
       -Dmax.vm=15 \
       product-tests \
    | tee test-log-release-aspectj-%{version}.txt
popd


%install
# jars, poms, depmap frags
install -d -m 0755 %{buildroot}%{_javadir}
install -d -m 0755 %{buildroot}%{_datadir}/maven2/poms
install -m 0644 modules/aj-build/dist/tools/lib/aspectjlib.jar \
        %{buildroot}%{_javadir}/%{name}lib-%{version}.jar
install -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP-aspectjlib.pom
%add_to_maven_depmap org.aspectj aspectjlib %{version} JPP %{name}lib
install -m 0644 modules/aj-build/dist/tools/lib/aspectjrt.jar \
        %{buildroot}%{_javadir}/%{name}rt-%{version}.jar
install -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/maven2/poms/JPP-aspectjrt.pom
%add_to_maven_depmap org.aspectj aspectjrt %{version} JPP %{name}rt
install -m 0644 modules/aj-build/dist/tools/lib/aspectjtools.jar \
        %{buildroot}%{_javadir}/%{name}tools-%{version}.jar
install -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/maven2/poms/JPP-aspectjtools.pom
%add_to_maven_depmap org.aspectj aspectjtools %{version} JPP %{name}tools
install -m 0644 modules/aj-build/dist/tools/lib/aspectjweaver.jar \
        %{buildroot}%{_javadir}/%{name}weaver-%{version}.jar
install -m 0644 %{SOURCE13} %{buildroot}%{_datadir}/maven2/poms/JPP-aspectjweaver.pom
%add_to_maven_depmap org.aspectj aspectjweaver %{version} JPP %{name}weaver
install -m 0644 modules/aj-build/dist/aspectj-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}installer-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# plugins
install -d -m 0755 %{buildroot}%{_datadir}/eclipse/plugins
install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
pushd %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
rm aspectjtools.jar
ln -sf ../../aspectjtools.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde.doc/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde.doc

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.ajde.source/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.source %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde.source

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
cp -pr modules/aj-build/dist/ide/eclipse/org.aspectj.aspectjrt/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
pushd %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.aspecjrt

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/doc/runtime-api \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/doc/weaver-api \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

rm -rf modules/aj-build/dist/docs/doc/runtime-api
rm -rf modules/aj-build/dist/docs/doc/weaver-api

# manual
install -d -m 0755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr modules/aj-build/dist/docs/* \
        %{buildroot}%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}/runtime-api \
        %{buildroot}%{_docdir}/%{name}-%{version}
ln -s %{_javadocdir}/%{name}/weaver-api \
        %{buildroot}%{_docdir}/%{name}-%{version}

# scripts
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/aj
install -m 0755 %{SOURCE6} %{buildroot}%{_bindir}/aj5
install -m 0755 %{SOURCE7} %{buildroot}%{_bindir}/ajbrowser
install -m 0755 %{SOURCE8} %{buildroot}%{_bindir}/ajc
install -m 0755 %{SOURCE9} %{buildroot}%{_bindir}/ajdoc

# home
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/bin
ln -s %{_bindir}/aj %{buildroot}%{_datadir}/%{name}/bin/aj
ln -s %{_bindir}/aj5 %{buildroot}%{_datadir}/%{name}/bin/aj5
ln -s %{_bindir}/ajbrowser %{buildroot}%{_datadir}/%{name}/bin/ajbrowser
ln -s %{_bindir}/ajc %{buildroot}%{_datadir}/%{name}/bin/ajc
ln -s %{_bindir}/ajdoc %{buildroot}%{_datadir}/%{name}/bin/ajdoc
ln -s %{_docdir}/%{name}-%{version} %{buildroot}%{_datadir}/%{name}/doc
install -d -m 0755 %{buildroot}%{_datadir}/%{name}/lib
ln -s %{_javadir}/%{name}lib.jar \
      %{buildroot}%{_datadir}/%{name}/lib/%{name}lib.jar
ln -s %{_javadir}/%{name}rt.jar \
      %{buildroot}%{_datadir}/%{name}/lib/%{name}rt.jar
ln -s %{_javadir}/%{name}tools.jar \
      %{buildroot}%{_datadir}/%{name}/lib/%{name}tools.jar
ln -s %{_javadir}/%{name}weaver.jar \
      %{buildroot}%{_datadir}/%{name}/lib/%{name}weaver.jar
chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/aspectj.conf`
touch $RPM_BUILD_ROOT/etc/java/aspectj.conf

%files
%doc %{_docdir}/%{name}-%{version}/*.html
%attr(0755,root,root) %{_bindir}/aj
%attr(0755,root,root) %{_bindir}/aj5
%attr(0755,root,root) %{_bindir}/ajbrowser
%attr(0755,root,root) %{_bindir}/ajc
%attr(0755,root,root) %{_bindir}/ajdoc
%{_datadir}/%{name}
%{_javadir}/%{name}lib-%{version}.jar
%{_javadir}/%{name}lib.jar
%{_javadir}/%{name}rt-%{version}.jar
%{_javadir}/%{name}rt.jar
%{_javadir}/%{name}tools-%{version}.jar
%{_javadir}/%{name}tools.jar
%{_javadir}/%{name}weaver-%{version}.jar
%{_javadir}/%{name}weaver.jar
%{_datadir}/maven2/poms/JPP-aspectjlib.pom
%{_datadir}/maven2/poms/JPP-aspectjrt.pom
%{_datadir}/maven2/poms/JPP-aspectjtools.pom
%{_datadir}/maven2/poms/JPP-aspectjweaver.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%config(noreplace,missingok) /etc/java/aspectj.conf

%files eclipse-plugins
%{_javadir}/aspectj-eclipse
%{_datadir}/eclipse/plugins/org.aspectj.ajde
%{_datadir}/eclipse/plugins/org.aspectj.ajde.doc
%{_datadir}/eclipse/plugins/org.aspectj.ajde.source
%{_datadir}/eclipse/plugins/org.aspectj.aspecjrt

%files installer
%{_javadir}/%{name}installer-%{version}.jar
%{_javadir}/%{name}installer.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt2_1jpp6
- fixed build

* Wed Jan 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt1_1jpp6
- new version

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt3_2jpp5
- fixed build with eclipse 3.5

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt2_2jpp5
- rebuild with eclipse 3.4

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.5.3-alt1_2jpp5
- new version

