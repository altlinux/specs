BuildRequires: /proc easymock2
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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

#def_with gcj_support
%bcond_with gcj_support
%bcond_with repolib

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif

%define namedversion %{version}


Name:           sisu-guice
Version:        2.9.2
Release:        alt2_2jpp6
Epoch:          0
Summary:        Sisu Guice
License:        ASL 2.0
URL:            http://sonatype.org
Group:          Development/Java
# git clone https://github.com/sonatype/sisu-guice.git && cd sisu-guice && git checkout sisu-guice-2.9.2 && rm -rf .git && cd .. && mv sisu-guice sisu-guice-2.9.2 && tar cjf sisu-guice-2.9.2.tar.bz2 sisu-guice-2.9.2
Source0:        sisu-guice-2.9.2.tar.bz2
Source1:        %{name}-jpp-depmap.xml
Patch0:         sisu-guice-pom.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: aopalliance
Requires: atinject
Requires: jpackage-utils
BuildRequires: aopalliance
BuildRequires: apache-commons-parent
BuildRequires: atinject
BuildRequires: cglib
BuildRequires: forge-parent >= 0:5
BuildRequires: google-guice >= 0:2.0
BuildRequires: jpa_3_0_api
BuildRequires: maven-plugin-bundle
BuildRequires: maven2-plugin-deploy
BuildRequires: maven-shared-filtering
BuildRequires: maven-surefire-provider-junit4
BuildRequires: servlet_2_5_api
BuildRequires: slf4j >= 0:1.6.1
# FIXME: should be spring3
BuildRequires: spring2-beans
BuildArch:      noarch
Source44: import.info

%description
Guice is a lightweight dependency injection framework for Java 5 and above.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%if 0
%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.
%endif

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q
%patch0 -p0 -b .sav0

%build
ln -s .m2 $(pwd)/maven2-brew
%{_bindir}/mvn-jpp \
        -e \
        -Dmaven2.jpp.depmap.file=%{SOURCE1} \
        -DaltDeploymentRepository=oss-releases::default::file://$(pwd)/maven2-brew \
        -Dmaven.test.skip=true \
        -Dguice.with.jarjar=false \
	install \
        javadoc:aggregate \
%if 0
        site
%endif

%install

pushd maven2-brew

mkdir -p %{buildroot}%{_javadir}/%{name}
#cp -p org/sonatype/sisu/inject/guice-assistedinject/%{namedversion}/guice-assistedinject-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-assistedinject/%{namedversion}/guice-assistedinject-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-grapher/%{namedversion}/guice-grapher-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-grapher/%{namedversion}/guice-grapher-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-jmx/%{namedversion}/guice-jmx-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-jmx/%{namedversion}/guice-jmx-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-jndi/%{namedversion}/guice-jndi-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-jndi/%{namedversion}/guice-jndi-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-multibindings/%{namedversion}/guice-multibindings-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-multibindings/%{namedversion}/guice-multibindings-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-persist/%{namedversion}/guice-persist-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-persist/%{namedversion}/guice-persist-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-servlet/%{namedversion}/guice-servlet-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-servlet/%{namedversion}/guice-servlet-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-spring/%{namedversion}/guice-spring-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-spring/%{namedversion}/guice-spring-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/inject/guice-throwingproviders/%{namedversion}/guice-throwingproviders-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/inject/guice-throwingproviders/%{namedversion}/guice-throwingproviders-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/sisu-guice/%{namedversion}/sisu-guice-%{namedversion}-no_aop.jar %{buildroot}%{_javadir}/%{name}/
#cp -p org/sonatype/sisu/sisu-guice/%{namedversion}/sisu-guice-%{namedversion}-tests.jar %{buildroot}%{_javadir}/%{name}/
cp -p org/sonatype/sisu/sisu-guice/%{namedversion}/sisu-guice-%{namedversion}.jar %{buildroot}%{_javadir}/%{name}/
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{namedversion}*; do ln -s ${jar} ${jar/-%{namedversion}/}; done)

mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p org/sonatype/sisu/inject/guice-assistedinject/%{namedversion}/guice-assistedinject-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-assistedinject.pom
cp -p org/sonatype/sisu/inject/guice-extensions/%{namedversion}/guice-extensions-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-extensions.pom
cp -p org/sonatype/sisu/inject/guice-grapher/%{namedversion}/guice-grapher-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-grapher.pom
cp -p org/sonatype/sisu/inject/guice-jmx/%{namedversion}/guice-jmx-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-jmx.pom
cp -p org/sonatype/sisu/inject/guice-jndi/%{namedversion}/guice-jndi-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-jndi.pom
cp -p org/sonatype/sisu/inject/guice-multibindings/%{namedversion}/guice-multibindings-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-multibindings.pom
cp -p org/sonatype/sisu/inject/guice-parent/%{namedversion}/guice-parent-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-parent.pom
cp -p org/sonatype/sisu/inject/guice-persist/%{namedversion}/guice-persist-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-persist.pom
cp -p org/sonatype/sisu/inject/guice-servlet/%{namedversion}/guice-servlet-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-servlet.pom
cp -p org/sonatype/sisu/inject/guice-spring/%{namedversion}/guice-spring-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-spring.pom
cp -p org/sonatype/sisu/inject/guice-throwingproviders/%{namedversion}/guice-throwingproviders-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-guice-throwingproviders.pom
cp -p org/sonatype/sisu/sisu-guice/%{namedversion}/sisu-guice-%{namedversion}.pom %{buildroot}%{_datadir}/maven2/poms/JPP.%{name}-sisu-guice.pom

popd

%add_to_maven_depmap org.sonatype.sisu.inject guice-assistedinject %{namedversion} JPP/%{name} guice-assistedinject
%add_to_maven_depmap org.sonatype.sisu.inject guice-extensions %{namedversion} JPP/%{name} guice-extensions
%add_to_maven_depmap org.sonatype.sisu.inject guice-grapher %{namedversion} JPP/%{name} guice-grapher
%add_to_maven_depmap org.sonatype.sisu.inject guice-jmx %{namedversion} JPP/%{name} guice-jmx
%add_to_maven_depmap org.sonatype.sisu.inject guice-jndi %{namedversion} JPP/%{name} guice-jndi
%add_to_maven_depmap org.sonatype.sisu.inject guice-multibindings %{namedversion} JPP/%{name} guice-multibindings
%add_to_maven_depmap org.sonatype.sisu.inject guice-parent %{namedversion} JPP/%{name} guice-parent
%add_to_maven_depmap org.sonatype.sisu.inject guice-persist %{namedversion} JPP/%{name} guice-persist
%add_to_maven_depmap org.sonatype.sisu.inject guice-servlet %{namedversion} JPP/%{name} guice-servlet
%add_to_maven_depmap org.sonatype.sisu.inject guice-spring %{namedversion} JPP/%{name} guice-spring
%add_to_maven_depmap org.sonatype.sisu.inject guice-throwingproviders %{namedversion} JPP/%{name} guice-throwingproviders
%add_to_maven_depmap org.sonatype.sisu sisu-guice %{namedversion} JPP/%{name} sisu-guice

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if 0
# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr target/target/site/* %{buildroot}%{_docdir}/%{name}-%{version}
rm -r %{buildroot}%{_docdir}/%{name}-%{version}/apidocs
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%{__cp} -pr maven2-brew/* %{buildroot}%{_javadir}/repository.jboss.com/maven2-brew
%endif

%files
%doc LICENSE PATCHES README
%dir %{_javadir}*/%{name}/
%exclude %dir %{_javadocdir}/%{name}/
#%{_javadir}*/%{name}/guice-assistedinject-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-assistedinject-tests.jar
%{_javadir}*/%{name}/guice-assistedinject-%{namedversion}.jar
%{_javadir}*/%{name}/guice-assistedinject.jar
#%{_javadir}*/%{name}/guice-grapher-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-grapher-tests.jar
%{_javadir}*/%{name}/guice-grapher-%{namedversion}.jar
%{_javadir}*/%{name}/guice-grapher.jar
#%{_javadir}*/%{name}/guice-jmx-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-jmx-tests.jar
%{_javadir}*/%{name}/guice-jmx-%{namedversion}.jar
%{_javadir}*/%{name}/guice-jmx.jar
#%{_javadir}*/%{name}/guice-jndi-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-jndi-tests.jar
%{_javadir}*/%{name}/guice-jndi-%{namedversion}.jar
%{_javadir}*/%{name}/guice-jndi.jar
#%{_javadir}*/%{name}/guice-multibindings-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-multibindings-tests.jar
%{_javadir}*/%{name}/guice-multibindings-%{namedversion}.jar
%{_javadir}*/%{name}/guice-multibindings.jar
#%{_javadir}*/%{name}/guice-persist-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-persist-tests.jar
%{_javadir}*/%{name}/guice-persist-%{namedversion}.jar
%{_javadir}*/%{name}/guice-persist.jar
#%{_javadir}*/%{name}/guice-servlet-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-servlet-tests.jar
%{_javadir}*/%{name}/guice-servlet-%{namedversion}.jar
%{_javadir}*/%{name}/guice-servlet.jar
#%{_javadir}*/%{name}/guice-spring-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-spring-tests.jar
%{_javadir}*/%{name}/guice-spring-%{namedversion}.jar
%{_javadir}*/%{name}/guice-spring.jar
#%{_javadir}*/%{name}/guice-throwingproviders-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/guice-throwingproviders-tests.jar
%{_javadir}*/%{name}/guice-throwingproviders-%{namedversion}.jar
%{_javadir}*/%{name}/guice-throwingproviders.jar
%{_javadir}*/%{name}/sisu-guice-%{namedversion}-no_aop.jar
%{_javadir}*/%{name}/sisu-guice-no_aop.jar
#%{_javadir}*/%{name}/sisu-guice-%{namedversion}-tests.jar
#%{_javadir}*/%{name}/sisu-guice-tests.jar
%{_javadir}*/%{name}/sisu-guice-%{namedversion}.jar
%{_javadir}*/%{name}/sisu-guice.jar
%{_datadir}/maven2/poms/JPP.%{name}-guice-assistedinject.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-extensions.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-grapher.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-jmx.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-jndi.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-multibindings.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-parent.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-persist.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-servlet.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-spring.pom
%{_datadir}/maven2/poms/JPP.%{name}-guice-throwingproviders.pom
%{_datadir}/maven2/poms/JPP.%{name}-sisu-guice.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if 0
%files manual
%doc %{_docdir}/%{name}-%{version}
%endif

%if %with repolib
%files repolib
%dir %{_javadir}*/
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.9.2-alt2_2jpp6
- fixed build with maven3

* Mon Mar 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.9.2-alt1_2jpp6
- new version

