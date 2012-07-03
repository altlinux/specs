Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2010, JPackage Project
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
#def_with test
%bcond_with test

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           velocity
Version:        1.6.4
Release:        alt2_1jpp6
Epoch:          1
Summary:        Java-based template engine
License:        ASL 2.0
Group:          Development/Java
URL:            http://velocity.apache.org/
Source0:        http://www.apache.org/dist/velocity/engine/1.6.4/velocity-1.6.4.tar.gz
Source1:        http://www.apache.org/dist/velocity/engine/1.6.4/velocity-1.6.4.pom
Patch0:         velocity-build_xml.patch
Patch1:         velocity-link-offline.patch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires: excalibur-avalon-logkit
Requires: jakarta-commons-collections
Requires: jakarta-commons-lang >= 0:2.3
Requires: jakarta-commons-logging
Requires: jakarta-oro
Requires: jdom >= 0:1.0-1
Requires: jpackage-utils
Requires: log4j >= 0:1.1
%if %with test
Requires: servlet_2_3_api
%else
Requires: servlet_2_5_api
%endif
Requires: werken-xpath
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: antlr
BuildRequires: classworlds
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-collections
BuildRequires: jakarta-commons-lang >= 0:2.3
BuildRequires: jakarta-commons-logging
BuildRequires: jdom >= 0:1.0-1
BuildRequires: jpackage-utils >= 0:1.7.3
BuildRequires: log4j >= 0:1.1
BuildRequires: jakarta-oro
%if %with test
BuildRequires: hsqldb
BuildRequires: junit
%endif
%if %with test
BuildRequires: servlet_2_3_api
%else
BuildRequires: servlet_2_5_api
%endif
BuildRequires: werken-xpath
BuildRequires: excalibur-avalon-logkit-javadoc
BuildRequires: jakarta-oro-javadoc
BuildRequires: jakarta-commons-collections-javadoc
BuildRequires: jakarta-commons-lang-javadoc
BuildRequires: java-javadoc
BuildRequires: jdom-javadoc
BuildRequires: log4j-javadoc
BuildRequires: tomcat6-javadoc
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

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

%package manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description manual
Documentation for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q
# Remove all binary libs used in compiling the package.
# Note that velocity has some jar files containing macros under
# examples and test that should not be removed.

%if %with test
for j in $(find . -name "*.jar" | grep -v /test/); do
    rm $j
done
%else
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t %{__rm}
%endif

%patch0 -b .sav0
%patch1 -b .sav1

%if %with test
mkdir -p bin/test-lib
pushd bin/test-lib
ln -s $(build-classpath hsqldb)
ln -s $(build-classpath junit)
popd
%endif
mkdir -p bin/lib
pushd bin/lib
ln -s $(build-classpath ant)
ln -s $(build-classpath antlr)
ln -s $(build-classpath excalibur/avalon-logkit)
ln -s $(build-classpath commons-collections)
ln -s $(build-classpath commons-lang)
ln -s $(build-classpath commons-logging)
ln -s $(build-classpath jdom)
ln -s $(build-classpath log4j)
ln -s $(build-classpath oro)
%if %with test
ln -s $(build-classpath servlet_2_3_api)
%else
ln -s $(build-classpath servlet_2_5_api)
%endif
ln -s $(build-classpath werken-xpath)
ln -s $(build-classpath classworlds)
popd

perl -pi -e 's/\r$//g' LICENSE

%build
export CLASSPATH=$(%{_bindir}/build-classpath antlr commons-collections commons-lang commons-logging jdom werken-xpath)
%if %with test
CLASSPATH=${CLASSPATH}:$(pwd)/test/texen-classpath/test.jar
%endif
#export OPT_JAR_LIST=`%{__cat} %{_sysconfdir}/ant.d/junit`
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 \
  -Djavadocs.ref.jsdk=file://%{_javadocdir}/java \
  -buildfile build/build.xml \
  jar javadocs \
%if %with test
test
%else

%endif

%{__rm} -r docs/api

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 bin/velocity-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.velocity velocity %{version} JPP %{name}
%add_to_maven_depmap velocity velocity %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr bin/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# data
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -pr convert examples $RPM_BUILD_ROOT%{_datadir}/%{name}
%if %with test
cp -pr test $RPM_BUILD_ROOT%{_datadir}/%{name}
%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%doc LICENSE NOTICE README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%{_libdir}/gcj/%{name}/classloader.*
%endif

%files manual
%doc docs/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

