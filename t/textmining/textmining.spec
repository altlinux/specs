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


Summary:        Textmining Extractors
Name:           textmining
Version:        1.0
Release:        alt1_1jpp6
Epoch:          0
License:        Apache License 2.0
URL:            http://code.google.com/p/text-mining/
Group:          Development/Java
Source0:        %{name}-%{version}.tgz
# svn export http://text-mining.googlecode.com/svn/trunk/ textmining-1.0
# tar czf textmining-1.0.tgz textmining-1.0/

Source1:        tm-extractors-1.0.pom
Patch0:         %{name}-%{version}-build.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  jakarta-poi >= 0:3.2
BuildRequires:  junit4
BuildRequires:  xmlunit
Requires:  jakarta-poi >= 0:3.2

BuildArch:      noarch

Requires(post):   jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Text mining is the process of analyzing text and 
automatically extracting useful information from it. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%package demo
Summary:        Samples for %{name}
Group:          Development/Documentation
Requires:       %{name} = 0:%{version}

%description demo
%{summary}.

%prep
%setup -q 
%patch0 -b .sav0
# remove all binary libs
#find . -name "*.jar" -exec rm -f {} \;
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath poi) lib
ln -sf $(build-classpath junit4) lib
ln -sf $(build-classpath xmlunit) lib
mv test/text/winword2/fastsaved.doc test/text/winword2/fastSaved.doc
mv test/text/winword6/fastsaved.doc test/text/winword6/fastSaved.doc
mv test/text/winword97/fastsaved.doc test/text/winword97/fastSaved.doc

%build
ant run-tests create-jar 

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 0755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.textmining tm-extractors %{version} JPP %{name}

install -m 644 build/bin/tm-extractors-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}


# docs
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 ReleaseNotes.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 644 etc/lgpl-2_1.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_docdir}/%{name}-%{version}/*.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Fri Jan 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp6
- converted from JPackage by jppimport script

* Wed May 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt5_2jpp5
- explicit selection of java5 compiler

* Wed May 20 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt4_2jpp5
- fixed build

* Sat Jan 10 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt3_2jpp5
- robot now always fixes docdir ownership

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt2_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:0.4-alt1_2jpp5
- converted from JPackage by jppimport script

