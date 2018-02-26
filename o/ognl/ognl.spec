# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
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

Summary:        Object-Graph Navigation Language
Name:           ognl
Version:        2.7.3
Release:        alt1_1jpp6
Epoch:          0
License:        BSD -style
URL:            http://www.ognl.org/
Group:          Development/Java
Source0:        http://www.ognl.org/2.6.9/%{name}-2.6.9-dist.zip
Source1:        http://www.ognl.org/2.6.9/%{name}-2.6.9-doc.zip
Source2:        ognl-2.7.3-osbuild.xml
Source3:        ognl-copyright.html
Source4:        http://repo1.maven.org/maven2/ognl/ognl/2.7.3/ognl-2.7.3.pom
Source5:        http://repo1.maven.org/maven2/ognl/ognl/2.7.3/ognl-2.7.3-sources.jar
Patch0:         ognl-build-properties.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-trax
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps
BuildRequires:  ant-contrib
BuildRequires:  junit
BuildRequires:  javacc
BuildRequires:  javassist
%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info
Requires: javassist

%description
OGNL stands for Object-Graph Navigation Language; it is an 
expression language for getting and setting properties of 
Java objects. You use the same expression for both getting 
and setting the value of a property. 
The ognl.Ognl class contains convenience methods for evaluating 
OGNL expressions. You can do this in two stages, parsing an 
expression into an internal form and then using that internal 
form to either set or get the value of a property; or you can 
do it in a single stage, and get or set a property using the 
String form of the expression directly. 
Many people have asked exactly what OGNL is good for. Several 
of the uses to which OGNL has been applied are: 
* A binding language between GUI elements (textfield, combobox, 
  etc.) to model objects. Transformations are made easier by 
  OGNL's TypeConverter mechanism to convert values from one 
  type to another (String to numeric types, for example). 
* A data source language to map between table columns and a 
  TableModel. 
* A binding language between web components and the underlying 
  model objects (WebOGNL, Tapestry and WebWork). 
* A more expressive replacement for the property-getting 
  language used by the Jakarta Commons BeanUtils package 
  (which only allows simple property navigation and 
  rudimentary indexed properties). 
Most of what you can do in Java is possible in OGNL, plus other 
extras such as list projection and selection and lambda expressions.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Manual for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q -c -n %{name}-%{version}
unzip -qq %{SOURCE1}
# remove all binary libs
for j in $(find . -name "*.jar"); do
      mv $j $j.no
done
cp %{SOURCE2} osbuild.xml
%patch0 -b .sav0
cd src/java
rm -rf *
jar xf %{SOURCE5}


%build
build-jar-repository -s -p lib  \
ant-contrib \
javacc \
junit \
javassist \

export OPT_JAR_LIST="ant-contrib ant/ant-nodeps ant/ant-junit junit ant/ant-trax javacc"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadocs 
#ant jar javadocs junit.report

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

install -m 0644 build/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
install -d -m 0755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/pdf
cp -pr docs/html/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/html
cp -pr docs/pdf/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/pdf
cp -pr docs/index.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/copyright.html

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
%doc %{_docdir}/%{name}-%{version}/copyright.html
%{_javadir}/*.jar
%{_datadir}/maven2
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}/index.html
%doc %{_docdir}/%{name}-%{version}/html
%doc %{_docdir}/%{name}-%{version}/pdf
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Fri Jan 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.3-alt1_1jpp6
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt2_3jpp5
- fixed repocop warnings

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_3jpp5
- build w/java5

* Wed Mar 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_3jpp1.7
- updated to new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_2jpp1.7
- converted from JPackage by jppimport script

