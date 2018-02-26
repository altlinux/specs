Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: struts-taglib
BuildRequires: /proc
BuildRequires: jpackage-1.5.0-core
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

%define gcj_support 0


Summary:        J2EE Unit Testing
Name:           mockrunner
Version:        0.3.8
Release:        alt6_1jpp5
Epoch:          0
License:        Apache Software License -style
URL:            http://mockrunner.sourceforge.net/
Group:          Development/Java
Source0:        http://download.sourceforge.net/sourceforge/mockrunner/mockrunner-0.3.8.zip
Source1:        mockrunner-0.3.8-build.xml
Source2:        mockrunner-0.3.8-excluded.properties
Source3:        mockrunner-0.3.8.pom
Source4:        mockrunner-ejb-0.3.8.pom
Source5:        mockrunner-jca-0.3.8.pom
Source6:        mockrunner-jdbc-0.3.8.pom
Source7:        mockrunner-jms-0.3.8.pom
Source8:        mockrunner-servlet-0.3.8.pom
Source9:        mockrunner-struts-0.3.8.pom
Source10:       mockrunner-tag-0.3.8.pom

BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant17 ant17-junit
BuildRequires: junit
BuildRequires: jboss4-j2ee
BuildRequires: nekohtml
BuildRequires: jaranalyzer


BuildRequires: cglib
BuildRequires: jakarta-commons-beanutils
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-digester
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-validator
BuildRequires: jdom
BuildRequires: jsp_2_0_api
BuildRequires: mockejb
BuildRequires: oro
BuildRequires: servlet_2_4_api
BuildRequires: servletapi4
BuildRequires: struts
BuildRequires: xerces-j2
BuildRequires: xml-commons-apis

Requires: cglib
Requires: jakarta-commons-beanutils
Requires: jakarta-commons-collections
Requires: jakarta-commons-digester
Requires: jakarta-commons-logging
Requires: jakarta-commons-validator
Requires: jdom
Requires: mockejb
Requires: oro
Requires: servlet
Requires: struts
Requires: xerces-j2
Requires: xml-commons-apis
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%if ! %{gcj_support}
BuildArch:      noarch
%endif


Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4

%description
Mockrunner is a lightweight framework for unit testing 
applications in the J2EE environment. It supports Struts 
actions and forms, servlets, filters and tag classes. 
Furthermore it includes a JDBC and a JMS test framework 
and can be used in conjunction with MockEJB to test EJB 
based applications. 
Mockrunner extends JUnit and simulates the necessary 
behaviour without calling the real infrastructure. It does 
not need a running application server or a database. 
Furthermore it does not call the webcontainer or the Struts 
ActionServlet. It is very fast and enables the user to 
manipulate all involved classes and mockobjects in all steps 
of the test. It can be used to write very sophisticated 
unit-tests for J2EE based applications without any overhead. 
Mockrunner does not support any type of in-container testing. 


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
# remove all binary libs
# find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
cp %{SOURCE1} build.xml
mkdir -p config/junit/runner
cp %{SOURCE2} config/junit/runner/excluded.properties
touch config/dependtemplate.txt

%build
cat /dev/null > .ant.properties
echo java1.5.home=/usr/lib/jvm/java-1.5.0 >> .ant.properties
echo build.j2ee1.3=false >> .ant.properties

pushd lib
ln -sf $(build-classpath bcel) bcel-5.1.jar
ln -sf $(build-classpath regexp) jakarta-regexp-1.3.jar
ln -sf $(build-classpath commons-digester)
ln -sf $(build-classpath oro) jakarta-oro-2.0.8.jar
ln -sf $(build-classpath junit)
ln -sf $(build-classpath nekohtml)
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath jboss4/jboss-j2ee) jboss-j2ee.jar
ln -sf $(build-classpath commons-beanutils)
ln -sf $(build-classpath struts)
ln -sf $(build-classpath struts-extras)
ln -sf $(build-classpath struts-taglib)
ln -sf $(build-classpath mockejb)
ln -sf $(build-classpath commons-collections)
ln -sf $(build-classpath commons-validator)
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
ln -sf $(build-classpath servletapi5) servlet-api.jar
ln -sf $(build-classpath commons-logging)
ln -sf $(build-classpath cglib) cglib-full-2.0-RC2.jar
ln -sf $(build-classpath jsp_2_0_api) jsp-api.jar
ln -sf $(build-classpath jdom)
ln -sf $(build-classpath jaranalyzer) jaranalyzer-1.1.jar
popd
ant17 -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 
%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}


install -m 0644 bin/%{name}-%{version}/lib/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-jca.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jca-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-servlet.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-servlet-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-tag.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-tag-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-jms.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jms-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-struts.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-struts-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-jdbc.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jdbc-%{version}.jar
install -m 0644 bin/%{name}-%{version}/lib/%{name}-ejb.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-ejb-%{version}.jar

#install -m 0644 bin/%{name}-%{version}/lib/j2ee1.3/%{name}-j2ee1.3.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-j2ee1.3-%{version}.jar
#install -m 0644 bin/%{name}-%{version}/lib/j2ee1.3/%{name}-servlet-j2ee1.3.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-servlet-j2ee1.3-%{version}.jar
#install -m 0644 bin/%{name}-%{version}/lib/j2ee1.3/%{name}-tag-j2ee1.3.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-tag-j2ee1.3-%{version}.jar
#install -m 0644 bin/%{name}-%{version}/lib/j2ee1.3/%{name}-struts-j2ee1.3.jar \
#  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-struts-j2ee1.3-%{version}.jar

(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom and depmap frags
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
%add_to_maven_depmap com.mockrunner %{name} %{version} JPP/%{name} %{name}
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}.pom
%add_to_maven_depmap com.mockrunner %{name}-ejb %{version} JPP/%{name} %{name}-ejb
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-ejb.pom
%add_to_maven_depmap com.mockrunner %{name}-jca %{version} JPP/%{name} %{name}-jca
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jca.pom
%add_to_maven_depmap com.mockrunner %{name}-jdbc %{version} JPP/%{name} %{name}-jdbc
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jdbc.pom
%add_to_maven_depmap com.mockrunner %{name}-jms %{version} JPP/%{name} %{name}-jms
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-jms.pom
%add_to_maven_depmap com.mockrunner %{name}-servlet %{version} JPP/%{name} %{name}-servlet
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-servlet.pom
%add_to_maven_depmap com.mockrunner %{name}-struts %{version} JPP/%{name} %{name}-struts
install -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-struts.pom
%add_to_maven_depmap com.mockrunner %{name}-tag %{version} JPP/%{name} %{name}-tag
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-%{name}-tag.pom


# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}


rm -rf doc/{build.txt,api,api_impl}

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p readme.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%{_docdir}/%{name}-%{version}/readme.txt
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/%{name}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-*%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Thu Mar 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt6_1jpp5
- build with ant17

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt5_1jpp5
- selected java5 compiler explicitly

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt4_1jpp5
- fixed build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.3.8-alt1_1jpp5
- converted from JPackage by jppimport script

