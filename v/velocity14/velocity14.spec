Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define oname velocity


Name:           velocity14
Version:        1.4
Release:	alt3_8jpp5
Epoch:          0
Summary:        Java-based template engine
License:        Apache Software License
Source0:        http://jakarta.apache.org/builds/jakarta-velocity/release/v1.4/velocity-1.4.tar.gz
Source1:        http://repo1.maven.org/maven2/velocity/velocity/1.4/velocity-1.4.pom
Patch0:		velocity14-AnakiaJDOMFactory-jdom-DefaultJDOMFactory.patch
Patch1:		velocity14-AnakiaTask-jdom-XMLOutputter.patch
Patch2:		velocity14-servletapi5.patch
Patch3:		velocity14-build.patch
URL:            http://jakarta.apache.org/velocity/
Group:          Development/Java
BuildRequires: jpackage-utils >= 0:1.7.4
BuildRequires: ant >= 0:1.6.5
BuildRequires: antlr
BuildRequires: junit
BuildRequires: bcel
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-oro
BuildRequires: jdom >= 0:1.0-1
BuildRequires: log4j >= 0:1.1
# Use servletapi5 instead of servletapi3
BuildRequires: servletapi5
BuildRequires: werken-xpath

Requires: bcel
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: jakarta-oro
Requires: jdom >= 0:1.0-1
Requires: log4j >= 0:1.1
# Use servletapi5 instead of servletapi3
Requires: servletapi5
Requires: werken-xpath
Provides:       %{oname} = %{epoch}:%{version}-%{release}
%if ! %{gcj_support}
BuildArch:      noarch
%endif

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

Requires(post): jpackage-utils >= 0:1.7.4
Requires(postun): jpackage-utils >= 0:1.7.4


%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires(post): %{__rm}
Requires(postun): %{__rm}
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif

%description    demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{oname}-%{version}
# Remove all binary libs used in compiling the package.
# Note that velocity has some jar files containing macros under
# examples and test that should not be removed.
# find build -name '*.jar' -exec rm -f \{\} \;
for j in $(find . -name "*.jar" | grep -v /test/ | grep -v /examples/); do
    mv $j $j.no
done

%patch0 -b .sav0
%patch1 -b .sav1
#Apply patch to remove explicit dependency on servletapi3
%patch2 -p1
#Introduce source="1.4" for java5+ compile
%patch3 -b .sav3

%build
# Use servletapi5 instead of servletapi3 in CLASSPATH
export CLASSPATH=$(build-classpath \
antlr \
jakarta-commons-collections \
servletapi5 \
excalibur/avalon-logkit \
junit \
oro \
log4j \
jdom \
bcel \
werken-xpath)
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -buildfile build/build.xml \
  -Djunit.jar=%{_javadir}/junit.jar \
  -Dbuild.sysclasspath=first \
  jar javadocs test

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 bin/%{oname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
%add_to_maven_depmap org.apache.velocity velocity %{version} JPP %{name}
%add_to_maven_depmap velocity velocity %{version} JPP %{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
rm -rf docs/api

# data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr convert examples test $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%doc LICENSE NOTICE README.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%{_libdir}/gcj/%{name}/velocity-1.4.jar.*
%{_libdir}/gcj/%{name}/classloader.*
%endif

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%files demo
%{_datadir}/%{name}

#FIXME: Generated by spec-convert-gcj-* script. These cant be natively compiled
#since they only contain *.vm files. Check if these are ignored in subsequent versions
#of spec-convert-gcj-* script.
#%if %{gcj_support}
#%attr(-,root,root) %{_libdir}/gcj/%{name}/template.jar.*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/test1.jar.*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/test2.jar.*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/test1.jar.*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/test2.jar.*
#%attr(-,root,root) %{_libdir}/gcj/%{name}/test.jar.*
#%endif

%changelog
* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_8jpp5
- added velocity:velocity depmap

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_8jpp5
- new jpp release

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_7jpp5
- rebuild with velocity14.jar

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_7jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_6jpp1.7
- compatibility package

