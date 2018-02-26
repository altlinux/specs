BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
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

Summary:        Dependency manager
Name:           ivy
Version:        1.3.1
Release:        alt3_4jpp6
Epoch:          0
License:        BSD
URL:            http://www.jayasoft.org/ivy
Group:          Development/Java
#Vendor:         JPackage Project
#Distribution:   JPackage
Source0:        ivy-1.3.1-src-withdep.zip
Source1:        ivy-buildlist.tar.gz
Source2:        ivy-1.3.1.pom
Patch0:		ivy-build_properties.patch
Patch1:		ivy-build_xml.patch
Patch2:		ivy-XmlIvyConfigurationParser.patch

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant >= 0:1.6.5
BuildRequires: ant-junit
BuildRequires: oro
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-httpclient >= 1:3.0
BuildRequires: jakarta-commons-logging
BuildRequires: jakarta-commons-cli
Requires: oro
Requires: jakarta-commons-codec
Requires: jakarta-commons-httpclient >= 1:3.0
Requires: jakarta-commons-logging
Requires: jakarta-commons-cli

BuildArch:      noarch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Ivy is a free java based dependency manager, with powerful features such 
as transitive dependencies, ant integration, maven repository compatibility,
continuous integration, html reports and many more.

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
%setup -q -n %{name}-%{version}
for j in $(find lib -name "*.jar"); do
    mv $j $j.no
done
pushd lib
rm -f *.jar
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath oro) .
ln -sf $(build-classpath commons-codec) .
ln -sf $(build-classpath commons-httpclient) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath commons-cli) .
popd
pushd test
gzip -dc %{SOURCE1} | tar xf -
popd

%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
rm -r test/java/fr/jayasoft/ivy/xml/XmlModuleDescriptorWriterTest.java

%build
#export JAVA_HOME=%{_jvmdir}/java-1.6.0
export OPT_JAR_LIST="ant/ant-junit junit"
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  test javadocs

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p build/artifact/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_datadir}/%{name}-%{version}

# poms
mkdir -p $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-ivy.pom
%add_to_maven_depmap fr.jayasoft %{name} %{version} JPP %{name}
%add_to_maven_depmap jayasoft %{name} %{version} JPP %{name}

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf doc/build/api
cp -pr doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%doc %{_datadir}/%{name}-%{version}
%{_javadir}/*
%{_datadir}/maven2/poms
%{_mavendepmapfragdir}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/*

%changelog
* Fri Sep 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt3_4jpp6
- new jpp release

* Sun May 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt3_3jpp5
- explicitly selected java5 as default

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_3jpp5
- converted from JPackage by jppimport script

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt2_1jpp1.7
- require new commons-cli

* Mon Oct 29 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

