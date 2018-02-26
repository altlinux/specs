AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:           objectweb-asm
Version:        3.3.1
Release:        alt4_4jpp6
Epoch:          0
Summary:        Code manipulation tool to implement adaptable systems
License:        BSD
URL:            http://asm.objectweb.org/
Group:          Development/Java
Source0:        http://download.forge.objectweb.org/asm/asm-%{version}.tar.gz
Source1:        asm-%{version}.pom
#based on Source1:        http://repo1.maven.org/maven2/asm/asm/3.3.1/asm-3.3.1.pom
Source2:        asm-analysis-%{version}.pom
#based on Source2:        http://repo1.maven.org/maven2/asm/asm-analysis/3.3.1/asm-analysis-3.3.1.pom
Source3:        asm-commons-%{version}.pom
#based on Source3:        http://repo1.maven.org/maven2/asm/asm-commons/3.3.1/asm-commons-3.3.1.pom
Source4:        asm-tree-%{version}.pom
#based on Source4:        http://repo1.maven.org/maven2/asm/asm-tree/3.3.1/asm-tree-3.3.1.pom
Source5:        asm-util-%{version}.pom
#based on Source5:        http://repo1.maven.org/maven2/asm/asm-util/3.3.1/asm-util-3.3.1.pom
Source6:        asm-xml-%{version}.pom
#based on Source6:        http://repo1.maven.org/maven2/asm/asm-xml/3.3.1/asm-xml-3.3.1.pom
Source7:        asm-all-%{version}.pom
#based on Source7:        http://repo1.maven.org/maven2/asm/asm-all/3.3.1/asm-all-3.3.1.pom
Source8:        asm-parent-%{version}.pom
#based on Source8:        http://repo1.maven.org/maven2/asm/asm-parent/3.3.1/asm-parent-3.3.1.pom
Source9:        asm-MANIFEST.MF
Source10:        asm-debug-all-%{version}.pom
#based on Source10:        http://repo1.maven.org/maven2/asm/asm-debug-all/3.3.1/asm-debug-all-3.3.1.pom
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       jpackage-utils
# Needed by asm-xml.jar
Requires:       xml-commons-jaxp-1.3-apis
BuildRequires:  ant >= 0:1.7
BuildRequires:  jpackage-utils
BuildRequires:  objectweb-anttask
BuildRequires:  xml-commons-jaxp-1.3-apis
BuildRequires:  zip
BuildArch:      noarch
Source44: import.info
Source45: asm-all.jar-OSGi-MANIFEST.MF

%description
ASM is a code manipulation tool to implement adaptable systems.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n asm-%{version}
perl -pi -e 's/\r$//g' LICENSE.txt README.txt

mkdir META-INF
cp -p %{SOURCE9} META-INF/MANIFEST.MF

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) jar jdoc

%install

# jars
mkdir -p %{buildroot}%{_javadir}/%{name}

for jar in output/dist/lib/*.jar; do
    cp -p ${jar} %{buildroot}%{_javadir}/%{name}/`basename ${jar}`
done

touch META-INF/MANIFEST.MF
zip -q -u output/dist/lib/all/asm-all-%{version}.jar META-INF/MANIFEST.MF

cp -p output/dist/lib/all/asm-all-%{version}.jar %{buildroot}%{_javadir}/%{name}/
cp -p output/dist/lib/all/asm-debug-all-%{version}.jar %{buildroot}%{_javadir}/%{name}/

(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do ln -s ${jar} ${jar/-%{version}/}; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm.pom
%add_to_maven_depmap org.objectweb.asm asm %{version} JPP/%{name} asm
%add_to_maven_depmap asm asm %{version} JPP/%{name} asm
cp -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-analysis.pom
%add_to_maven_depmap org.objectweb.asm asm-analysis %{version} JPP/%{name} asm-analysis
%add_to_maven_depmap asm asm-analysis %{version} JPP/%{name} asm-analysis
cp -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-commons.pom
%add_to_maven_depmap org.objectweb.asm asm-commons %{version} JPP/%{name} asm-commons
%add_to_maven_depmap asm asm-commons %{version} JPP/%{name} asm-commons
cp -p %{SOURCE10} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-debug-all.pom
%add_to_maven_depmap org.objectweb.asm asm-debug-all %{version} JPP/%{name} asm-debug-all
%add_to_maven_depmap asm asm-debug-all %{version} JPP/%{name} asm-debug-all
cp -p %{SOURCE4} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-tree.pom
%add_to_maven_depmap org.objectweb.asm asm-tree %{version} JPP/%{name} asm-tree
%add_to_maven_depmap asm asm-tree %{version} JPP/%{name} asm-tree
cp -p %{SOURCE5} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-util.pom
%add_to_maven_depmap org.objectweb.asm asm-util %{version} JPP/%{name} asm-util
%add_to_maven_depmap asm asm-util %{version} JPP/%{name} asm-util
cp -p %{SOURCE6} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-xml.pom
%add_to_maven_depmap org.objectweb.asm asm-xml %{version} JPP/%{name} asm-xml
%add_to_maven_depmap asm asm-xml %{version} JPP/%{name} asm-xml
cp -p %{SOURCE7} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-all.pom
%add_to_maven_depmap org.objectweb.asm asm-all %{version} JPP/%{name} asm-all
%add_to_maven_depmap asm asm-all %{version} JPP/%{name} asm-all
cp -p %{SOURCE8} %{buildroot}%{_datadir}/maven2/poms/JPP.objectweb-asm-asm-parent.pom
%add_to_maven_depmap org.objectweb.asm asm-parent %{version} JPP/%{name} asm-parent
%add_to_maven_depmap asm asm-parent %{version} JPP/%{name} asm-parent

# javadoc
install -p -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# inject OSGi manifest asm-all.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/objectweb-asm/asm-all.jar META-INF/MANIFEST.MF

# poms use asm group now - incompatible with oweb-asm 3.2 and confilcts with asm2 :( 
# seems like we need to patch asm2 to have asm2 group.
sed -i -e 's,<groupId>asm</groupId>,<groupId>org.objectweb.asm</groupId>,g' %buildroot/usr/share/maven2/poms/JPP.objectweb-asm-asm*
# end inject OSGi manifest asm-all.jar-OSGi-MANIFEST.MF

%files
%doc LICENSE.txt README.txt
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/asm-%{version}.jar
%{_javadir}/%{name}/asm-all-%{version}.jar
%{_javadir}/%{name}/asm-all.jar
%{_javadir}/%{name}/asm-analysis-%{version}.jar
%{_javadir}/%{name}/asm-analysis.jar
%{_javadir}/%{name}/asm-commons-%{version}.jar
%{_javadir}/%{name}/asm-commons.jar
%{_javadir}/%{name}/asm-debug-all-%{version}.jar
%{_javadir}/%{name}/asm-debug-all.jar
%{_javadir}/%{name}/asm-tree-%{version}.jar
%{_javadir}/%{name}/asm-tree.jar
%{_javadir}/%{name}/asm-util-%{version}.jar
%{_javadir}/%{name}/asm-util.jar
%{_javadir}/%{name}/asm-xml-%{version}.jar
%{_javadir}/%{name}/asm-xml.jar
%{_javadir}/%{name}/asm.jar
%{_datadir}/maven2/poms/JPP.%{name}-asm-all.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-analysis.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-commons.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-debug-all.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-tree.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-util.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm-xml.pom
%{_datadir}/maven2/poms/JPP.%{name}-asm.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt4_4jpp6
- added pom groupid asm

* Sun Oct 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt3_4jpp6
- fixed poms

* Fri Sep 16 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt2_4jpp6
- removed asm2 pom provides

* Tue Sep 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3.1-alt1_4jpp6
- new version

* Sat Feb 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_2jpp6
- added osgi manifest

* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_2jpp6
- new version

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt2_5jpp5
- added OSGi manifest

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_3jpp5
- converted from JPackage by jppimport script

* Mon Jan 28 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_2jpp1.7
- converted from JPackage by jppimport script

