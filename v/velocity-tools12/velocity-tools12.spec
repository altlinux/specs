Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-compat
BuildRequires: struts-taglib struts-tiles
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

%define oname		velocity-tools

Name:           velocity-tools12
Version:        1.2
Release:        alt3_2jpp5
Epoch:          0
Summary:        Java-based template engine
License:        Apache Software License
URL:            http://jakarta.apache.org/velocity/tools/
Group:          Development/Java
#Vendor:         JPackage Project
#Distribution:   JPackage
Source:         http://www.apache.org/dist/jakarta/velocity-tools/source/velocity-tools-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/velocity-tools/velocity-tools/1.2/velocity-tools-1.2.pom
Source2:        http://repo1.maven.org/maven2/velocity-tools/velocity-tools-generic/1.2/velocity-tools-generic-1.2.pom
Source3:        http://repo1.maven.org/maven2/velocity-tools/velocity-tools-view/1.2/velocity-tools-view-1.2.pom
Patch0:		velocity-tools-1.2-docs.patch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant
BuildRequires: jakarta-commons-beanutils >= 0:1.7.0
BuildRequires: jakarta-commons-collections >= 0:3.1
BuildRequires: jakarta-commons-digester >= 0:1.7
BuildRequires: jakarta-commons-lang >= 0:2.1
BuildRequires: jakarta-commons-logging >= 0:1.0.4
BuildRequires: jakarta-commons-validator >= 0:1.1.4
BuildRequires: dom4j
BuildRequires: jaxen >= 0:1.1
BuildRequires: servletapi4
BuildRequires: struts >= 0:1.2.7
# FIXME
#BuildRequires:	struts-sslext >= 0:1.2
BuildRequires: velocity >= 0:1.4
BuildRequires: velocity-dvsl
BuildRequires: oro >= 0:2.0.8
Requires: jpackage-utils >= 0:1.7.5
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: jakarta-commons-validator
Requires: dom4j
Requires: jaxen >= 0:1.1
Requires: servletapi4
Requires: struts >= 0:1.2.4
Requires: velocity
Requires: velocity-dvsl
Requires: oro
BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
VelocityTools is a collection of Velocity subprojects with a common
goal of creating tools and infrastructure for building both web and
non-web applications using the Velocity template engine.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
Javadoc for %{name}.

#%package        demo
#Summary:        Demo for %{name}
#Group:          Development/Libraries/Java
#Requires:       %{name} = %{epoch}:%{version}-%{release}

#%description    demo
#Demonstrations and samples for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -c -n %{oname}-%{version}
# Remove all binary libs used in compiling the package.
# Note that velocity has some jar files containing macros under
# examples and test that should not be removed.
#FIXME Use struts-sslext package
find lib -name "*.jar" -and -not -name sslext-1.2.jar -print | xargs rm -f

%patch0 -p1

%build
export JAVA_HOME=%{_jvmdir}/java-1.5.0
cat > build.properties <<EOBP

commons-beanutils.jar=$(build-classpath commons-beanutils)
commons-collections.jar=$(build-classpath commons-collections)
commons-digester.jar=$(build-classpath commons-digester)
commons-lang.jar=$(build-classpath commons-lang)
commons-logging.jar=$(build-classpath commons-logging)
commons-validator.jar=$(build-classpath commons-validator)
dom4j.jar=$(build-classpath dom4j)
jaxen.jar=$(build-classpath jaxen)
saxpath.jar=$(build-classpath jaxen)
servlet.jar=$(build-classpath servletapi4)
struts.jar=$(build-classpath struts)
#FIXME Use struts-sslext package
sslext.jar=lib/sslext-1.2.jar
velocity.jar=$(build-classpath velocity)
velocity-dvsl.jar=$(build-classpath velocity-dvsl)
oro.jar=$(build-classpath oro)
EOBP

export CLASSPATH=$(build-classpath  struts-taglib struts-tiles)
ant -Dbuild.sysclasspath=first jar.struts jar.view jar.generic javadoc docs

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 dist/%{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{oname} %{oname} %{version} JPP %{name}
install -m 644 dist/%{oname}-generic-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-generic-%{version}.jar
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-generic.pom
%add_to_maven_depmap %{oname} %{oname}-generic %{version} JPP %{name}-generic
install -m 644 dist/%{oname}-view-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-view-%{version}.jar
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-view.pom
%add_to_maven_depmap %{oname} %{oname}-view %{version} JPP %{name}-view
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf docs/javadoc

# data
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -pr convert examples test $RPM_BUILD_ROOT%{_datadir}/%{name}

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc LICENSE README.txt WHY_THREE_JARS.txt VLS_README.txt STATUS
%{_javadir}/*.jar
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

#%files demo
#%defattr(0644,root,root,0755)
#%{_datadir}/%{name}

# -----------------------------------------------------------------------------

%changelog
* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt3_2jpp5
- explicit selection of java5 compiler

* Thu May 14 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt2_2jpp5
- build with new struts

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp5
- jpackage 5.0

