BuildRequires: javapackages-local
Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
BuildRequires: subversion
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name xmlbeans
%define version 2.6.0
# Copyright (c) 2000-2005, JPackage Project
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

#def_with bootstrap
%bcond_with bootstrap
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:           xmlbeans
Version:        2.6.0
Release:        alt2_13jpp8
Summary:        XML-Java binding tool
URL:            http://xmlbeans.apache.org/
Source0:        http://www.apache.org/dist/xmlbeans/source/%{name}-%{version}-src.tgz
# Pom file is not available from maven repository for the
# currently released version
Source1:        %{version}/%{name}-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}-xpath/%{version}/%{name}-xpath-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/apache/%{name}/%{name}-xmlpublic/%{version}/%{name}-xmlpublic-%{version}.pom
Patch0:         xmlbeans-2.6.0-nodownload.patch
Patch1:         0001-Update-to-newer-saxon-API.patch
Patch2:         xmlbeans-2.6.0-iso-8859-1-encoding.patch
Patch3:         xmlbeans-2.6.0-jsr-bundle.patch
Patch4:         xmlbeans-scripts-classpath.patch
# error: cannot access TypeStoreUser
Patch5:         xmlbeans-2.6.0-java8.patch

License:        ASL 2.0

%if %without bootstrap
BuildRequires:  xmlbeans
%endif
BuildRequires:  java-devel
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  ant >= 0:1.6 ant-junit ant-contrib junit
BuildRequires:  xml-commons-resolver >= 0:1.1
BuildRequires:  bea-stax-api
BuildRequires:  saxon >= 8
Requires:       jpackage-utils >= 0:1.6

BuildArch:      noarch
Source44: import.info

%description
XMLBeans is a tool that allows you to access the full power 
of XML in a Java friendly way. It is an XML-Java binding tool. 
The idea is that you can take advantage the richness and 
features of XML and XML Schema and have these features mapped 
as naturally as possible to the equivalent Java language and 
typing constructs. XMLBeans uses XML Schema to compile Java 
interfaces and classes that you can then use to access and 
modify XML instance data. Using XMLBeans is similar to using 
any other Java interface/class, you will see things like 
getFoo or setFoo just as you would expect when working with 
Java. While a major use of XMLBeans is to access your XML 
instance data with strongly typed Java classes there are also 
API's that allow you access to the full XML infoset (XMLBeans 
keeps full XML Infoset fidelity) as well as to allow you to 
reflect into the XML schema itself through an XML Schema 
Object model.


%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.


%package manual
Group: Development/Java
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.


%package scripts
Group: Development/Java
Summary:        Scripts for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description scripts
%{summary}.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .nodownload
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

%build
# Piccolo and jam are rebuilt from source and bundled with xbean
# ant clean.jars leaves some dangling jars around, do not use it
find . \( -name '*.jar' -o -name '*.zip' \) \
        -not -name 'piccolo*.jar' -not -name 'jam*.jar' \
        %{?with_bootstrap:-not -name 'oldxbean.jar' } \
        -print -delete

# Replace bundled libraries
mkdir -p build/lib
ln -sf $(build-classpath xml-commons-resolver) build/lib/resolver.jar
ln -sf $(build-classpath xmlbeans/xbean) external/lib/oldxbean.jar
ln -sf $(build-classpath bea-stax-api) external/lib/jsr173_1.0_api.jar
ln -sf $(build-classpath saxon/saxon) external/lib/saxon9.jar
ln -sf $(build-classpath saxon/saxon) external/lib/saxon9-dom.jar

# Fix CRLF
sed 's/\r//' -i LICENSE.txt NOTICE.txt README.txt docs/stylesheet.css docs/xmlbeans.css docs/guide/tools.html

# Build
ant -Djavac.source=1.6 -Djavac.target=1.6 default docs

%install
# jar
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 build/lib/xmlpublic.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xmlpublic.jar
install -p -m 0644 build/lib/xbean_xpath.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean_xpath.jar
install -p -m 0644 build/lib/xbean.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/xbean.jar

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xbean.pom
%add_maven_depmap JPP.%{name}-xbean.pom %{name}/xbean.jar
install -pm 644 %{SOURCE2} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xbean_xpath.pom
%add_maven_depmap JPP.%{name}-xbean_xpath.pom %{name}/xbean_xpath.jar
install -pm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-xmlpublic.pom
%add_maven_depmap JPP.%{name}-xmlpublic.pom %{name}/xmlpublic.jar

# bin
install -d -m 0755 $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/dumpxsb   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/inst2xsd  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/scomp     $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sdownload $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/sfactor   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/svalidate $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/validate  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xpretty   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsd2inst  $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xsdtree   $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 bin/xstc      $RPM_BUILD_ROOT%{_bindir}


# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr build/docs/reference/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
rm -rf build/docs/reference

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -pr build/docs/* README.txt $RPM_BUILD_ROOT%{_docdir}/%{name}

%files -f .mfiles
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/README.txt
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

%files manual
%{_docdir}/%{name}

%files scripts
%attr(0755,root,root) %{_bindir}/*


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt2_13jpp8
- added BR: javapackages-local for javapackages 5

* Tue Oct 17 2017 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_13jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_12jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_11jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_10jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_3jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.6.0-alt1_2jpp7
- fc update

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.4.0-alt1_3jpp6
- new version

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt3_2jpp5
- new jpp release

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt3_1jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt2_1jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.3.0-alt1_1jpp5
- converted from JPackage by jppimport script

* Fri Jul 20 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.0-alt1_4jpp1.7
- converted from JPackage by jppimport script

