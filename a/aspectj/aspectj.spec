%def_with modified_bcel_rebuild
# BEGIN SourceDeps(oneline):
BuildRequires: python-devel unzip
# END SourceDeps(oneline)
BuildRequires: ant-apache-regexp ant-apache-xalan2
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2012, JPackage Project
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
Version:        1.6.12
Release:        alt3_1jpp6
Epoch:          0
Summary:        AspectJ aspect-oriented language extension to Java
License:        EPL
URL:            http://eclipse.org/aspectj/
Group:          Development/Java
# git clone http://git.eclipse.org/gitroot/aspectj/org.aspectj.git && git archive --prefix="aspectj-1.6.0/" --format=tar V1_6_0 | bzip2 > ../../SOURCES/aspectj-1.6.0.tar.bz2
Source0:        aspectj-%{version}.tar.bz2
Source1:        aspectj-build-build.xml
Source2:        aspectj-jdtcore4aspectj-build.xml
Source3:        http://archive.apache.org/dist/jakarta/bcel/source/bcel-5.1-src.zip
Source4:        aspectj-1.5.3-build-bcel.xml
Source5:        aspectj-1.5.3-script-aj
Source6:        aspectj-1.5.3-script-aj5
Source7:        aspectj-1.5.3-script-ajbrowser
Source8:        aspectj-1.5.3-script-ajc
Source9:        aspectj-1.5.3-script-ajdoc
Source10:       http://repo1.maven.org/maven2/org/aspectj/aspectjlib/%{version}/aspectjlib-%{version}.pom
Source11:       http://repo1.maven.org/maven2/org/aspectj/aspectjrt/%{version}/aspectjrt-%{version}.pom
Source12:       http://repo1.maven.org/maven2/org/aspectj/aspectjtools/%{version}/aspectjtools-%{version}.pom
Source13:       http://repo1.maven.org/maven2/org/aspectj/aspectjweaver/%{version}/aspectjweaver-%{version}.pom

%if_with modified_bcel_rebuild
Source99: patch.txt
%endif

# fedora aspectjweaver
Patch0:     aspectjweaver-build-fixes.patch

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  junit
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-nodeps
BuildRequires:  ant-junit
BuildRequires:  eclipse-platform
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  saxon6
Requires:  apache-commons-beanutils
Requires:  apache-commons-collections
Requires:  apache-commons-digester
Requires:  apache-commons-logging
Requires:  saxon6
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

Requires: aspectjweaver = %{?epoch:%epoch:}%version-%release

BuildArch:      noarch
Source44: import.info

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

%package -n aspectjweaver
Group:      Development/Java
Summary:    Java byte-code weaving library

%description -n aspectjweaver
The AspectJ Weaver supports byte-code weaving for aspect-oriented
programming (AOP) in java.


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
%setup -q 

####################################
for j in $(find . -name "*.jar" -a ! -name "aspectj*"); do
    mv $j $j.no
done
( cd lib/commons
  %{jar} xf $(find-jar commons-beanutils)
  %{jar} xf $(find-jar commons-collections)
  %{jar} xf $(find-jar commons-digester)
  %{jar} xf $(find-jar commons-logging)
  %{jar} cf commons.jar org
)
ln -s $(build-classpath junit) lib/junit/junit.jar
ln -s $(build-classpath ant) lib/ant/lib/ant.jar
ln -s $(build-classpath saxon6) lib/saxon/saxon.jar
mv lib/ext/jrockit/jrockit.jar.no lib/ext/jrockit/jrockit.jar
####################################

cp -p %{SOURCE1} build/build-build.xml
cp -p %{SOURCE2} org.eclipse.jdt.core/build.xml
cp -p %{SOURCE3} bcel-builder
cp -p %{SOURCE4} bcel-builder/build-bcel.xml

pushd org.eclipse.jdt.core
  mkdir src
  pushd src
  unzip -qq -o ../jdtcore-for-aspectj-src.zip
  popd
popd

#sed -i -e 's,classpathref=,classpath refid=,g'  build/build-properties.xml
sed -i -e 's,<antcall,<antcall inheritRefs="true",g'  build/build-properties.xml

%if_with modified_bcel_rebuild
# bcel-builder fixes
sed -i -e 's,source="1\.4",source="1.5",' bcel-builder/build-bcel.xml
sed -i -e 's,"diff\.exe","diff",' bcel-builder/build.xml
cp -a %{SOURCE99} bcel-builder/patch.txt
%else
pushd lib/bcel/
mv bcel-verifier.jar.no bcel-verifier.jar
mv bcel.jar.no bcel.jar
popd
%endif

%patch0 -p1
#grep -rl aj.org.objectweb.asm .


%build
#export JAVA_HOME=%{java_home}
export ANT_OPTS="-Xmx1024M"
# CLASSPATH needed for rebuilds from sources
export CLASSPATH=$(build-classpath \
ant \
ant-launcher \
commons-logging \
objectweb-asm/asm \
)

# now for eclipse 3.6.X
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.osgi_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.text_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.update.configurator_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.runtime_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.resources_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.common_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.contenttype_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.preferences_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.registry_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.jobs_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.filesystem_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.app_*.jar)
CLASSPATH=${CLASSPATH}:$(ls %{_libdir}/eclipse/plugins/org.eclipse.core.runtime_*.jar)

%if_with modified_bcel_rebuild
pushd bcel-builder
%{ant} -v -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build-bcel.xml
cp bin/bcel.jar .
cp ../lib/bcel/bcel-verifier.jar.no bcel-verifier.jar
mv ../lib/bcel/bcel-verifier-src.zip .
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  extractAndPatchAndJar
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  push
popd
%endif

# rebuild jdtcore-for-aspectj.jar from sources
pushd org.eclipse.jdt.core
export ASPECTJ_HOME=$RPM_BUILD_DIR/aspectj-%{version}/lib/aspectj
"%{java}" -classpath "$ASPECTJ_HOME/lib/aspectjtools.jar:$ASPECTJ_HOME/lib/aspectjrt.jar:$JAVA_HOME/lib/tools.jar:$CLASSPATH" -Xmx1024M org.aspectj.tools.ajc.Main -sourceroots src -d build-classes
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar
popd

# rebuild the build-module from sources
pushd build
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -f build-build.xml
popd

touch build/local.properties
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first

pushd org.aspectj.lib
%{ant} -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dbuild.sysclasspath=first -f build-aspectjlib.xml 
popd

%install
# jars, poms, depmap frags
install -d -m 0755 %{buildroot}%{_javadir}
install -d -m 0755 %{buildroot}%{_mavenpomdir}

install -m 0644 org.aspectj.lib/jars/aspectjlib.out.jar \
        %{buildroot}%{_javadir}/%{name}lib-%{version}.jar
install -m 0644 %{SOURCE10} %{buildroot}%{_mavenpomdir}/JPP-aspectjlib.pom
%add_to_maven_depmap org.aspectj aspectjlib %{version} JPP %{name}lib
install -m 0644 aj-build/dist/tools/lib/aspectjrt.jar \
        %{buildroot}%{_javadir}/%{name}rt-%{version}.jar
install -m 0644 %{SOURCE11} %{buildroot}%{_mavenpomdir}/JPP-aspectjrt.pom
%add_to_maven_depmap org.aspectj aspectjrt %{version} JPP %{name}rt
install -m 0644 aj-build/dist/tools/lib/aspectjtools.jar \
        %{buildroot}%{_javadir}/%{name}tools-%{version}.jar
install -m 0644 %{SOURCE12} %{buildroot}%{_mavenpomdir}/JPP-aspectjtools.pom
%add_to_maven_depmap org.aspectj aspectjtools %{version} JPP %{name}tools
install -m 0644 aj-build/dist/tools/lib/aspectjweaver.jar \
        %{buildroot}%{_javadir}/%{name}weaver-%{version}.jar
install -m 0644 %{SOURCE13} %{buildroot}%{_mavenpomdir}/JPP-aspectjweaver.pom
%add_to_maven_depmap_at aspectjweaver org.aspectj aspectjweaver %{version} JPP %{name}weaver
install -m 0644 aj-build/dist/aspectj-DEVELOPMENT.jar \
        %{buildroot}%{_javadir}/%{name}installer-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# plugins
install -d -m 0755 %{buildroot}%{_datadir}/eclipse/plugins
install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
cp -pr aj-build/dist/ide/eclipse/org.aspectj.ajde/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
pushd %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
rm aspectjtools.jar
ln -sf ../../aspectjtools.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
cp -pr aj-build/dist/ide/eclipse/org.aspectj.ajde.doc/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.doc %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde.doc

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
cp -pr aj-build/dist/ide/eclipse/org.aspectj.ajde.source/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.ajde.source
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.ajde.source %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.ajde.source

install -d -m 0755 %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
cp -pr aj-build/dist/ide/eclipse/org.aspectj.aspectjrt/* %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
pushd %{buildroot}%{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt
rm aspectjrt.jar
ln -sf ../../aspectjrt.jar .
popd
ln -sf %{_javadir}/aspectj-eclipse/org.aspectj.aspectjrt %{buildroot}%{_datadir}/eclipse/plugins/org.aspectj.aspecjrt

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr aj-build/dist/docs/doc/runtime-api \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr aj-build/dist/docs/doc/weaver-api \
        %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

rm -rf aj-build/dist/docs/doc/runtime-api
rm -rf aj-build/dist/docs/doc/weaver-api

# manual
install -d -m 0755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr aj-build/dist/docs/* \
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
%{_mavenpomdir}/JPP-aspectjlib.pom
%{_mavenpomdir}/JPP-aspectjrt.pom
%{_mavenpomdir}/JPP-aspectjtools.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}
%config(noreplace,missingok) /etc/java/aspectj.conf

%files -n aspectjweaver
%{_javadir}/%{name}weaver-%{version}.jar
%{_javadir}/%{name}weaver.jar
%{_mavendepmapfragdir}/%{name}weaver
%{_mavenpomdir}/JPP-aspectjweaver.pom


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
* Thu Oct 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt3_1jpp6
- merged aspectjweaver back

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.12-alt1_1jpp6
- new version

* Sat Oct 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.11-alt1_1jpp6
- new version

* Fri Oct 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.5-alt1_1jpp6
- new version

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6.0-alt1_1jpp6
- new version

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.5.4-alt3_1jpp6
- build with saxon6

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

