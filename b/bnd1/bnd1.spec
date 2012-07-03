BuildRequires: /proc
BuildRequires: jpackage-1.6.0-compat
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
#

%define gcj_support 0


Name:           bnd1
Version:        1.43.0
Release:        alt2_1jpp6
Epoch:          0
Summary:        BND OSGi bundle tools
Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.aqute.biz/Code/Bnd
Source0:        bnd-1.43.0.tar.bz2
# git clone git://github.com/bnd/bnd.git && cd bnd && git archive HEAD > ../bnd-1.43.0.tar && bzip2 ../bnd-1.43.0.tar
Source1:        bndlib-1.43.0.pom
Source2:        bnd-1.43.0.pom
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  org.osgi.core
BuildRequires:  org.osgi.compendium
BuildRequires:  eclipse-jdt
BuildRequires:  eclipse-swt
BuildRequires:  eclipse-pde
BuildRequires:  eclipse-rcp
BuildRequires:  eclipse-platform

%if %{gcj_support}
BuildRequires:  java-gcj-compat-devel
%endif
Source44: import.info

%description
Bnd is the swiss army knife of OSGi bundles. It is used in 
many different incarnations to reduce the effort to create 
bundles from projects or jars using a myriad of tools like 
ant, maven, bndtools, sigil, eclipse, etc. 

#%package        javadoc
#Summary:        Javadoc for %{name}
#Group:          Development/Documentation
#
#%description    javadoc
#%{summary}.

%prep
%setup -q -c
for j in $(find . -name "*.jar"); do 
    mv $j $j.no
done
mv cnf/repo/biz.aQute.bnd/biz.aQute.bnd-latest.jar.no cnf/repo/biz.aQute.bnd/biz.aQute.bnd-latest.jar
ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.junit_3.8.2*/junit.jar) cnf/repo/com.springsource.junit/com.springsource.junit-3.8.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.core.runtime_3.*.jar) cnf/repo/org.eclipse.core.runtime/org.eclipse.core.runtime-3.3.100.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.core.resources_3.*.jar) cnf/repo/org.eclipse.core.resources/org.eclipse.core.resources-3.3.1.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.core.commands_3.*.jar) cnf/repo/org.eclipse.core.commands/org.eclipse.core.commands-3.3.0.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.debug.core_3.*.jar) cnf/repo/org.eclipse.debug.core/org.eclipse.debug.core-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.debug.ui_3.*.jar) cnf/repo/org.eclipse.debug.ui/org.eclipse.debug.ui-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.eclipse.jdt.debug.ui_3.*.jar) cnf/repo/org.eclipse.jdt.debug.ui/org.eclipse.jdt.debug.ui-3.2.102.jar
ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.eclipse.jdt.launching_3.*.jar) cnf/repo/org.eclipse.jdt.launching/org.eclipse.jdt.launching-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.eclipse.jdt.core_3.*.jar) cnf/repo/org.eclipse.jdt.core/org.eclipse.jdt.core-3.3.3.jar
mv cnf/repo/junit.osgi/junit.osgi-3.8.2.jar.no cnf/repo/junit.osgi/junit.osgi-3.8.2.jar
mv cnf/repo/org.eclipse.jdt.junit/org.eclipse.jdt.junit-3.3.2.jar.no cnf/repo/org.eclipse.jdt.junit/org.eclipse.jdt.junit-3.3.2.jar
#ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.eclipse.jdt.junit_3.*.jar) cnf/repo/org.eclipse.jdt.junit/org.eclipse.jdt.junit-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/dropins/jdt/plugins/org.eclipse.jdt.ui_3.*.jar) cnf/repo/org.eclipse.jdt.ui/org.eclipse.jdt.ui-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.jface.text_3.*.jar) cnf/repo/org.eclipse.jface.text/org.eclipse.jface.text-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.jface_3.*.jar) cnf/repo/org.eclipse.jface/org.eclipse.jface-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.text_3.*.jar) cnf/repo/org.eclipse.text/org.eclipse.text-3.3.0.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.ui_3.*.jar) cnf/repo/org.eclipse.ui/org.eclipse.ui-3.3.1.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.ui.editors_3.*.jar) cnf/repo/org.eclipse.ui.editors/org.eclipse.ui.editors-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.ui.workbench.texteditor_3.*.jar) cnf/repo/org.eclipse.ui.workbench.texteditor/org.eclipse.ui.workbench.texteditor-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.ui.workbench_3.*.jar) cnf/repo/org.eclipse.ui.ide/org.eclipse.ui.ide-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.ui.ide_3.*.jar) cnf/repo/org.eclipse.ui.workbench/org.eclipse.ui.workbench-3.3.2.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.equinox.registry_3.*.jar) cnf/repo/org.eclipse.equinox.registry/org.eclipse.equinox.registry-3.3.1.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.equinox.common_3.*.jar) cnf/repo/org.eclipse.equinox.common/org.eclipse.equinox.common-3.3.0.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.core.jobs_3.*.jar) cnf/repo/org.eclipse.core.jobs/org.eclipse.core.jobs-3.3.1.jar
ln -s $(build-classpath ant) cnf/repo/org.apache.tools.ant/org.apache.tools.ant-1.7.1.jar
ln -s $(ls /usr/lib*/eclipse/plugins/org.eclipse.osgi_3.*.jar) cnf/repo/org.eclipse.osgi/org.eclipse.osgi-3.5.1.jar
ln -s $(build-classpath org.osgi.compendium) cnf/repo/osgi.cmpn/osgi.cmpn-4.0.0.jar
ln -s $(build-classpath org.osgi.compendium) cnf/repo/osgi.cmpn/osgi.cmpn-4.0.1.jar
ln -s $(build-classpath org.osgi.compendium) cnf/repo/osgi.cmpn/osgi.cmpn-4.1.0.jar
ln -s $(build-classpath org.osgi.compendium) cnf/repo/osgi.cmpn/osgi.cmpn-4.2.0.jar
ln -s $(build-classpath org.osgi.compendium) cnf/repo/osgi.cmpn/osgi.cmpn-4.2.1.jar
ln -s $(build-classpath org.osgi.core) cnf/repo/osgi.core/osgi.core-4.2.1.jar

mv cnf/repo/ee.minimum/ee.minimum-1.0.0.jar.no cnf/repo/ee.minimum/ee.minimum-1.0.0.jar
mv cnf/repo/ee.minimum/ee.minimum-1.1.0.jar.no cnf/repo/ee.minimum/ee.minimum-1.1.0.jar
mv cnf/repo/ee.minimum/ee.minimum-1.1.1.jar.no cnf/repo/ee.minimum/ee.minimum-1.1.1.jar
mv cnf/repo/ee.minimum/ee.minimum-1.1.3.jar.no cnf/repo/ee.minimum/ee.minimum-1.1.3.jar
mv cnf/repo/ee.minimum/ee.minimum-1.2.0.jar.no cnf/repo/ee.minimum/ee.minimum-1.2.0.jar
mv cnf/repo/ee.minimum/ee.minimum-1.2.1.jar.no cnf/repo/ee.minimum/ee.minimum-1.2.1.jar

ln -s $(ls /usr/lib*/eclipse/swt-gtk-3.*.jar) cnf/repo/org.eclipse.swt.carbon.macosx/org.eclipse.swt.carbon.macosx-3.3.3.jar
#mv cnf/repo/org.eclipse.swt/org.eclipse.swt-3.3.2.jar.no cnf/repo/org.eclipse.swt/org.eclipse.swt-3.3.2.jar
#ln -s $(build-classpath maven2/empty-dep) cnf/repo/org.eclipse.swt.carbon.macosx/org.eclipse.swt.carbon.macosx-3.3.3.jar


%build
export ANT_OPTS="-Xmx128m -XX:MaxPermSize=128m"
ant

%install

install -d 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 biz.aQute.bndlib/tmp/biz.aQute.bndlib.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bndlib-%{version}.jar
install -m 644 biz.aQute.bnd/tmp/biz.aQute.bnd.annotation.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/annotation-%{version}.jar
install -m 644 biz.aQute.bnd/tmp/biz.aQute.bnd.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/bnd-%{version}.jar
install -m 644 biz.aQute.junit/tmp/biz.aQute.junit.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/junit-%{version}.jar
install -m 644 biz.aQute.launcher/tmp/biz.aQute.launcher.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/launcher-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)


# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bndlib.pom
%add_to_maven_depmap biz.aQute bndlib %{version} JPP/%{name} bndlib

install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-bnd.pom
%add_to_maven_depmap biz.aQute bnd %{version} JPP/%{name} bnd

##
#install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#cp -pr dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
#ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

#%files javadoc
#%defattr(0644,root,root,0755)
#%doc %{_javadocdir}/%{name}-%{version}
#%doc %{_javadocdir}/%{name}


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.43.0-alt2_1jpp6
- built with java 6

* Thu Feb 09 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.43.0-alt1_1jpp6
- new version

