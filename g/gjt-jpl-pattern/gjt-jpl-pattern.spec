# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
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


Name:           gjt-jpl-pattern
Version:        0.2
Release:        alt1_5jpp6
Epoch:          0
Summary:        Support for using design patterns.
License:        GPL
Group:          Development/Java
URL:            http://www.gjt.org/pkgdoc/org/gjt/lindfors/pattern/index.html
Source0:        gjt-jpl-pattern-source.zip
# download http://www.gjt.org/servlets/JCVSlet/zip/gjt/org/gjt/lindfors/pattern/pattern.zip
Source1:        gjt-jpl-pattern-build.xml
Source2:        http://repository.jboss.com/maven2/jpl-pattern/jpl-pattern/1.0/jpl-pattern-1.0.pom
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
Requires:       jpackage-utils >= 0:1.7.3
BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildArch:      noarch
Source44: import.info

%description
This package consists mainly of interfaces used to recognize 
well known design patterns in a software system. Most 
interfaces are only useful for 'tagging' classes as being a 
part of certain design patterns, and there isn't any 
implementing code present here. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
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
%setup -q -c -n %{name}-%{version}
mkdir -p pattern/build
cp -p %{SOURCE1} pattern/build/build.xml
mkdir -p pattern/classes

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f pattern/build/build.xml lib javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 pattern/build/jpl-pattern-0_2.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `/bin/echo ${jar} | sed "s|-%{version}||g"`; done)

install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap jpl-pattern jpl-pattern %{version} JPP %{name}

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr pattern/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr pattern/doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_docdir}/%{name}-%{version}/LICENSE
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
%{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_5jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_4jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_3jpp5
- fixed repocop warnings

* Tue Jun 05 2007 Igor Vlasenko <viy@altlinux.ru> 0:0.2-alt1_3jpp1.7
- converted from JPackage by jppimport script

