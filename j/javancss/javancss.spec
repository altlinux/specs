BuildRequires: /proc
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


Name:           javancss
Version:        32.53
Release:        alt1_2jpp6
Epoch:          0
Summary:        Source Measurement Suite
License:        LGPLv3
URL:            http://www.kclee.de/clemens/java/javancss/
Group:          Development/Java
# svn export http://svn.codehaus.org/javancss/tags/javancss-32.53/ && tar cjf javancss-32.53.tar.bz2 javancss-32.53
# Exported revision 199.
# http://www.kclee.de/clemens/java/javancss/javancss-32.53.zip
Source0:        javancss-32.53.tar.bz2
Patch0:         javancss-build_xml.patch
Patch1:         javancss-pom.patch
Patch2:         javancss-ant.patch
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       ant
Requires:       ccl
Requires:       jpackage-utils
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  ccl-util
BuildRequires:  javacc
BuildRequires:  jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Ever wondered how many lines of code or how many classes there are 
in the Sun JDK? Curious about the size of your own projects - or do 
you want to keep track of your work-progress. 
That's what JavaNCSS is for.

JavaNCSS is a simple command line utility which measures two 
standard source code metrics for the Java programming language. 
The metrics are collected globally, for each class and/or for 
each function. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q
%patch0 -p0 -b .sav0
%patch1 -p0 -b .sav1
%patch2 -p0 -b .sav2

#rm src/main/java/javancss/JavancssFrame.java

%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t rm

pushd lib
ln -s $(%{_bindir}/build-classpath ccl-util) ccl.jar
ln -s $(%{_bindir}/build-classpath javacc) javacc.jar
popd

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 all

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -p lib/javancss.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s ${jar} `echo $jar | sed "s|-%{version}||g"`; done)

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p pom.xml %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom

# depmaps
%add_to_maven_depmap org.codehaus.javancss javancss %{version} JPP %{name}
%add_to_maven_depmap javancss javancss %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp -p COPYING %{buildroot}%{_docdir}/%{name}-%{version}
cp -p README.TXT %{buildroot}%{_docdir}/%{name}-%{version}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}/doc
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}/doc

# data
mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}
cp -p javancss.dtd %{buildroot}%{_datadir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_datadir}/%{name}

# bin
mkdir -p %{buildroot}%{_bindir}
cp -p bin/javancss %{buildroot}%{_bindir}

%files
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/README.TXT
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}-%{version}/%{name}.dtd
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/doc
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:32.53-alt1_2jpp6
- new jpp relase

* Fri Mar 18 2011 Igor Vlasenko <viy@altlinux.ru> 0:30.51-alt3_1jpp5
- fixed build with new javacc5

* Tue Mar 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:30.51-alt2_1jpp5
- removed unmet pom dependencies (breaks mono-maven2-plugins)

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:30.51-alt1_1jpp5
- new jpp release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:27.48-alt3_2jpp5
- fixed docdir ownership

* Sat Oct 18 2008 Igor Vlasenko <viy@altlinux.ru> 0:27.48-alt2_2jpp5
- fixed build with java 5

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:27.48-alt1_2jpp1.7
- converted from JPackage by jppimport script

