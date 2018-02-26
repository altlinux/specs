BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%define gcj_support 0


Name:           aqute-bndlib
Version:        0.0.363
Release:        alt2_1jpp6
Epoch:          0
Summary:        BND Library
License:        ASL 2.0
Group:          Development/Java
URL:            http://www.aQute.biz/Code/Bnd
Source0:        http://www.aqute.biz/repo/biz/aQute/bnd/0.0.363/bnd-0.0.363.jar
Source1:        http://www.aqute.biz/repo/biz/aQute/bnd/0.0.363/bnd-0.0.363.pom
Source2:        aqute-service.tar.gz
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires: ant >= 0:1.6.5
BuildRequires: eclipse-jdt
BuildRequires: eclipse-platform
BuildRequires: eclipse-rcp
BuildRequires: jpackage-utils >= 0:1.7.3
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
The bnd tool helps you create and diagnose OSGi R4 bundles.
The key functions are: 
- Show the manifest and JAR contents of a bundle 
- Wrap a JAR so that it becomes a bundle 
- Create a Bundle from a specification and a class path 
- Verify the validity of the manifest entries 
The tool is capable of acting as: 
- Command line tool 
- File format 
- Directives 
- Use of macros 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
mkdir -p target/site/apidocs/
mkdir -p target/classes/
mkdir -p src/main/
mv OSGI-OPT/src src/main/java
pushd src/main/java
tar xfs %{SOURCE2}
popd
sed -i "s|import aQute.lib.filter.*;||g" src/main/java/aQute/bnd/make/ComponentDef.java
sed -i "s|import aQute.lib.filter.*;||g" src/main/java/aQute/bnd/make/ServiceComponent.java
sed -i "s|\r||g" LICENSE

%build
export LANG=en_US.utf8
export OPT_JAR_LIST=:
export CLASSPATH=$(build-classpath ant)
addclasspath()
{
for arg in "$@"; do
	if [ -e $arg ]; then
		CLASSPATH=${CLASSPATH}:$arg
	else
		echo $arg failed
		exit 1
	fi
done
}

addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.osgi_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.osgi.services_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.jface_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.jface.text_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.core.jobs_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.core.runtime_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.core.resources_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.debug.core_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.debug.ui_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.ui.console_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.ui.editors_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.ui.workbench_*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core_*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug.ui_*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit_*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit.*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.launching_*.jar)
addclasspath $(ls %{_libdir}/eclipse/dropins/jdt/plugins/org.eclipse.jdt.ui_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.common_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.equinox.registry_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.swt.*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.ui.workbench.texteditor_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.core.commands_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.text_*.jar)
addclasspath $(ls %{_libdir}/eclipse/plugins/org.eclipse.ui.ide_*.jar)
export CLASSPATH
%{javac}  -target 1.5 -source 1.5 -d target/classes -target 1.5 -source 1.5 $(find src/main/java -type f -name "*.java")
%{javadoc} -d target/site/apidocs -sourcepath src/main/java aQute.lib.header aQute.lib.osgi aQute.lib.qtokens aQute.lib.filter
cp -p LICENSE maven-dependencies.txt plugin.xml pom.xml target/classes
for f in $(find aQute/ -type f -not -name "*.class"); do
    cp -p $f target/classes/$f
done
pushd target/classes
%{jar} cmf ../../META-INF/MANIFEST.MF ../%{name}-%{version}.jar * 
popd

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap biz.aQute bndlib %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-aqute-bndlib.pom
%{_mavendepmapfragdir}/aqute-bndlib
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.db
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.so
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 11 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt2_1jpp6
- fixed build

* Mon Oct 11 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.0.363-alt1_1jpp6
- new version

* Mon Feb 23 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt4_2jpp5
- fixed build

* Sun Jan 04 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt3_2jpp5
- rebuild with eclipse 3.4

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt2_2jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.0.203-alt1_2jpp5
- converted from JPackage by jppimport script

