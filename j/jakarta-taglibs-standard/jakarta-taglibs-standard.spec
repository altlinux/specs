Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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

%global base_name       standard
%global short_name      taglibs-%{base_name}

Name:           jakarta-taglibs-standard
Version:        1.1.2
Release:        alt5_11jpp7
Epoch:          0
Summary:        An open-source implementation of the JSP Standard Tag Library
License:        ASL 2.0
URL:            http://jakarta.apache.org/taglibs/
Source0:        http://archive.apache.org/dist/jakarta/taglibs/standard/source/jakarta-taglibs-standard-%{version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/jstl/jstl/%{version}/jstl-%{version}.pom
Source2:        http://repo1.maven.org/maven2/taglibs/standard/%{version}/standard-%{version}.pom

Patch0:         jakarta-taglibs-standard-1.1.1-build.patch
Patch1:         fix-1.6.0-build.patch
Patch2:         %{name}-jdbc-4.1.patch
# remove relocation use -a parameter with %%add_maven_depmap
# prevent maven/system overflow
Patch3:         jakarta-taglibs-standard-1.1.2-jstl-pom.patch
Patch4:         jakarta-taglibs-standard-1.1.2-standard-pom.patch

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.5.30
BuildRequires:  ant
BuildRequires:  tomcat6-servlet-2.5-api
BuildRequires:  tomcat6-jsp-2.1-api
BuildRequires:  java-javadoc
BuildRequires:  xalan-j2 >= 2.6.0
#Requires:       tomcat-servlet-3.0-api
#Requires:       tomcat-jsp-2.3-api
#Requires:       xalan-j2 >= 2.6.0


Provides:       javax.servlet.jsp.jstl
Source44: import.info

%description
This package contains Jakarta Taglibs's open-source implementation of the
JSP Standard Tag Library (JSTL), version 1.1. JSTL is a standard under the
Java Community Process.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.


%prep
%setup -q -n %{name}-%{version}-src
%patch0 -b .orig
%patch1
%patch2
#
rm -fr standard/src/org/apache/taglibs/standard/lang/jstl/test/PageContextImpl.java
rm -fr standard/src/org/apache/taglibs/standard/lang/jstl/test/EvaluationTest.java
cat > build.properties <<EOBP
build.dir=build
dist.dir=dist
servlet24.jar=$(build-classpath tomcat6-servlet-api)
jsp20.jar=$(build-classpath tomcat6-jsp-api)
jaxp-api.jar=$(build-classpath xalan-j2)
EOBP

cp -p %{SOURCE1} jstl-1.1.2.pom
%patch3 -p0
cp -p %{SOURCE2} standard-1.1.2.pom
%patch4 -p0


%build
ant \
  -Dfinal.name=%{short_name} \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -f standard/build.xml \
  dist


%install
# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p standard/dist/standard/lib/jstl.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-taglibs-core.jar
cp -p standard/dist/standard/lib/standard.jar $RPM_BUILD_ROOT%{_javadir}/jakarta-taglibs-standard.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in jakarta-*; do ln -sf ${jar} `echo $jar| sed "s|jakarta-||g"`; done)

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 jstl-1.1.2.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-jakarta-taglibs-core.pom
touch .mfiles
echo '%_javadir/*' >> .mfiles
#add_maven_depmap JPP-jakarta-taglibs-core.pom jakarta-taglibs-core.jar -a "javax.servlet:jstl,org.eclipse.jetty.orbit:javax.servlet.jsp.jstl"
install -pm 644 standard-1.1.2.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
#add_maven_depmap JPP-%{name}.pom %{name}.jar -a "org.eclipse.jetty.orbit:org.apache.taglibs.standard.glassfish"

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr standard/dist/standard/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# J2EE API dir
install -d -m 755 %{buildroot}%{_javadir}/javax.servlet.jsp.jstl/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.servlet.jsp.jstl/
ln -sf ../jakarta-taglibs-core.jar %{buildroot}%{_javadir}/javax.servlet.jsp.jstl/

%files -f .mfiles
%doc LICENSE NOTICE
%doc standard/README_src.txt standard/README_bin.txt standard/dist/doc/doc/standard-doc/*.html
%{_javadir}/taglibs-core.jar
%{_javadir}/taglibs-standard.jar
%{_javadir}/javax.servlet.jsp.jstl/

%files javadoc
%doc LICENSE NOTICE
%doc %{_javadocdir}/%{name}


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt5_11jpp7
- fixed build

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt4_11jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt4_9jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt4_6jpp7
- update

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt3_8jpp6
- built with java 6 due to abstract getParentLogger

* Wed Feb 23 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_8jpp6
- renamed to apache-taglibs-standard

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt2_7jpp5
- selected java5 compiler explicitly

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.1.2-alt1_7jpp5
- fixed build with java 5

* Mon Jul 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt4_8jpp1.7
- converted from JPackage by jppimport script

* Fri May 04 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt4
- rebuild on x86_64 

* Mon Apr 30 2007 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt3
- added JPackage compat stuff

* Wed Mar 22 2006 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt2
- Fixed build with j2se1.5

* Wed Mar 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.1.1-alt1
- Initial build for ALT Linux Sisyphus

