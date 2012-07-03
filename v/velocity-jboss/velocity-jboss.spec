Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2009, JPackage Project
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

%bcond_with gcj_support
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/apache-velocity/1.4jboss-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%if %with gcj_support
%define gcj_support 0
%else
%define gcj_support 0
%endif


Name:           velocity-jboss
Version:        1.4
Release:        alt2_5jpp6
Epoch:          0
Summary:        JBoss-patched version of velocity
License:        ASL 2.0
Group:          Development/Java
URL:            http://jakarta.apache.org/velocity/
Source0:        http://repository.jboss.com/apache-velocity/1.4jboss/src/velocity-src.tgz
Source1:        velocity-jboss-component-info.xml
Source2:        repolib-src-README.txt
Source3:        http://repository.jboss.com/maven2/apache-velocity/velocity/1.4jboss/velocity-1.4jboss.pom
Patch0:         velocity-AnakiaJDOMFactory-jdom-DefaultJDOMFactory.patch
Patch1:         velocity-AnakiaTask-jdom-XMLOutputter.patch
Patch2:         velocity-servletapi5.patch
Patch3:         velocity-1.4-java5-enumeration.patch
Patch4:         velocity-1.4-shebang.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires: jakarta-commons-collections
# Use servletapi5 instead of servletapi3
Requires: bcel
Requires: excalibur-avalon-logkit
Requires: jdom >= 0:1.0-1
Requires: log4j >= 0:1.1
Requires: oro
Requires: servlet_2_4_api
Requires: werken-xpath
BuildRequires: ant
BuildRequires: antlr
BuildRequires: bcel
BuildRequires: excalibur-avalon-logkit
BuildRequires: jakarta-commons-collections
BuildRequires: jdom >= 0:1.0-1
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: junit
BuildRequires: log4j >= 0:1.1
BuildRequires: oro
# Use servletapi5 instead of servletapi3
BuildRequires: servlet_2_4_api
BuildRequires: werken-xpath
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%else
BuildArch:      noarch
%endif
Source44: import.info

%description
This is a JBoss modified version of Velocity. This modification
allows ',' and ':' characters to be in a variable character set to work 
around the problem that velocity has no way to escape ${x:y} and ${x,y:z}
constructs that should just pass through the template engine unchanged.

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

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

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

%description    javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires: %{name} = %{epoch}:%{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n velocity-%{version}
# Remove all binary libs used in compiling the package.
# Note that velocity has some jar files containing macros under
# examples and test that should not be removed.
%{_bindir}/find build -name '*.jar' | %{_bindir}/xargs -t %{__rm}

%{_bindir}/find -name '*.sh' | %{_bindir}/xargs %{__chmod} 0755

%patch0 -p0
%patch1 -p0
# Apply patch to remove explicit dependency on servletapi3
%patch2 -p1
%patch3 -p0
%patch4 -p1
# -----------------------------------------------------------------------------

%{__perl} -pi -e 's/\r$//g' README.txt docs/api/stylesheet.css

%build
# Use servletapi5 instead of servletapi3 in CLASSPATH
export CLASSPATH=$(%{_bindir}/build-classpath antlr jakarta-commons-collections servlet_2_4_api excalibur/avalon-logkit junit oro log4j jdom bcel werken-xpath)
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -buildfile build/build.xml -Djunit.jar=$(%{_bindir}/build-classpath junit) -Dbuild.sysclasspath=first jar javadocs
# Note: test are not run due to the JBoss changes causing the tests to fail 

# -----------------------------------------------------------------------------

%install

# jars
%{__mkdir_p} %{buildroot}%{_javadir}
%{__cp} -p bin/velocity-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)

# poms
%{__mkdir_p} %{buildroot}%{_datadir}/maven2/poms
%{__cp} -p %{SOURCE3} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap apache-velocity velocity 1.4jboss JPP %{name}

# javadoc
%{__mkdir_p} %{buildroot}%{_javadocdir}/%{name}-%{version}
%{__ln_s} %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
%{__cp} -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}

# manual
%{__mkdir_p} %{buildroot}%{_docdir}/%{name}-%{version}
%{__cp} -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}
%{__rm} -r %{buildroot}%{_docdir}/%{name}-%{version}/api

# data
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__cp} -pr convert examples test %{buildroot}%{_datadir}/%{name}

# -----------------------------------------------------------------------------

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%if %with repolib
%{__mkdir_p} %{buildroot}%{repodir}
%{__mkdir_p} %{buildroot}%{repodirlib}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
tag=`/bin/echo %{name}-%{version}-%{release} | %{__sed} 's|\.|_|g'`
%{__sed} -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
%{__sed} -i "s/@VERSION@/%{version}jboss-brew/g" %{buildroot}%{repodir}/component-info.xml
%{__mkdir_p} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH0} %{buildroot}%{repodirsrc}
%{__cp} -p %{PATCH1} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE0} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE1} %{buildroot}%{repodirsrc}
%{__cp} -p %{SOURCE2} %{buildroot}%{repodirsrc}/README.txt
%{__cp} -p %{buildroot}%{_javadir}/%{name}.jar %{buildroot}%{repodirlib}/velocity.jar
%{__cp} -p %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom %{buildroot}%{repodirlib}/velocity.pom
%endif

%files
%doc LICENSE NOTICE README.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/velocity-1.4.jar.*
%{_libdir}/gcj/%{name}/classloader.*
%endif

%files manual
%doc %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

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

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- added pom

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_4jpp5
- converted from JPackage by jppimport script

