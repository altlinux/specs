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

# If you want repolib package to be built,
# issue the following: 'rpmbuild --with repolib'

%define _with_repolib 1

%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}

%define repodir %{_javadir}/repository.jboss.com/jfreechart/1.0.13-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

# If you want the demo to be built,
# give rpmbuild option '--with demo'

%define with_demo %{?_with_demo:1}%{!?_with_demo:0}
%define without_demo %{!?_with_demo:1}%{?_with_demo:0}


Name:			jfreechart
Version:		1.0.13
Release:	alt3_3jpp6
Epoch:			0
Summary:		Charts Generation library
License:		LGPLv2+
URL:			http://www.jfree.org/jfreechart/
#Source from http://www.jfree.org/jfreechart/download.html
Source0:		%{name}-%{version}.tar.gz
Source1:		%{name}-component-info.xml
Source2:                http://mirrors.ibiblio.org/pub/mirrors/maven2/jfree/jfreechart/1.0.13/jfreechart-1.0.13.pom

Patch0:			%{name}-%{version}-build_xml.patch
Group:			Development/Java
# Dependencies included in zip
Requires:		jcommon >= 0:1.0.12
BuildRequires:		ant
BuildRequires:		itext
BuildRequires:		jaxp
BuildRequires:		jcommon >= 0:1.0.12
BuildRequires:		jpackage-utils >= 0:1.7.3
BuildRequires:		junit
BuildRequires:		tomcat6-servlet-2.5-api
BuildArch:		noarch
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Source44: import.info

%description
Free Java class library for generating charts.

%if %{with_repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:		Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%if %{with_demo}
%package demo
Summary:        Demo for %{name}
Group:          Development/Java
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       jcommon
Requires:       servlet

%description demo
Demos for %{name}.
%endif

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Documentation
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%description javadoc -l fr
Javadoc pour %{name}.

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" | xargs %{__rm}

ln -sf $(build-classpath jcommon) lib
ln -sf $(build-classpath tomcat6-servlet-2.5-api) lib/servlet.jar
   
%if %{without_demo}
%patch0 -p1
%endif

%if %{with_repolib}
tag=`echo %{version}-brew`
sed -i "s/@VERSION@/$tag/g" %{SOURCE1}
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" %{SOURCE1}
%endif

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f ant/build.xml -Dgnujaxp.jar=%{_javadir}/jaxp.jar -Ditext.jar=%{_javadir}/itext.jar -Djunit.jar=%{_javadir}/junit.jar -Djcommon.jar=%{_javadir}/jcommon.jar -Dservlet.jar=%{_javadir}/tomcat6-servlet-2.5-api.jar -Dbuildstable=true -Dproject.outdir=. -Dbasedir=.

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
%if %{with_demo}
install -m 644 %{name}-%{version}-demo.jar $RPM_BUILD_ROOT%{_javadir}
%endif
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jfree %{name} %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %{with_repolib}
	install -d -m 755 $RPM_BUILD_ROOT%{repodir}
	install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
	install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{repodir}/component-info.xml
	install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
	install -m 755 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
	cp -p $RPM_BUILD_ROOT%{_javadir}/jfreechart.jar $RPM_BUILD_ROOT%{repodirlib}
%endif

%files
%doc 
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%if %{with_demo}
%files demo
%{_javadir}/%{name}-%{version}-demo.jar
%{_javadir}/%{name}-demo.jar
%endif

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %{with_repolib}
%files repolib
%{repodir}
%endif

%changelog
* Wed Jan 25 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt3_3jpp6
- fixed repolib dep on jcommon

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_3jpp6
- new jpp relase

* Wed Oct 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt2_2jpp6
- fixed jcommon version in repolib

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.13-alt1_2jpp6
- added pom

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt2_4jpp5
- new jpp release

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.0.9-alt1_2jpp5
- converted from JPackage by jppimport script

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.5-alt1_1jpp1.7
- updated to new jpackage release

* Tue Apr 26 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0.0-alt0.1pre2
- First build for ALTLinux
