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


Name:           nanoxml
Version:        2.2.3
Release:        alt2_6jpp6
Epoch:          0
Summary:        NanoXML is a small XML parser for Java
License:        zlib License
Group:          Development/Java
URL:            http://nanoxml.cyberelf.be/
Source0:        http://nanoxml.cyberelf.be/downloads/NanoXML-2.2.3.tar.gz
Source1:        http://repo1.maven.org/maven2/be/cyberelf/nanoxml/nanoxml/2.2.3/nanoxml-2.2.3.pom
Source2:        http://repo1.maven.org/maven2/be/cyberelf/nanoxml/lite/2.2.3/lite-2.2.3.pom
Source3:        java-1.5.0-package-list
Patch0:         %{name}-build.patch
BuildRequires:  jpackage-utils >= 0:1.7.5
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5

BuildArch:      noarch
Source44: import.info

%description
The intent of NanoXML is to be a small parser which is easy to use.
Although many features were added to NanoXML, it is very small.
The full parser with builder fits in a JAR file of about 32K.

%package        lite
Summary:        Lite version of %{name}
Group:          Development/Java

%description    lite
Lite version of %{name}.

%package        manual
Summary:        Manual for %{name}
Group:          Development/Java
BuildArch: noarch

%description    manual
Documentation for %{name}.

%package        manual-lite
Summary:        Manual for the lite version of %{name}
Group:          Development/Java

%description    manual-lite
Documentation for the lite version of %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.


%prep
%setup -q -n NanoXML-%{version}
%patch0 -b .sav0
cp %{SOURCE3} package-list
find . -name "*.jar" | xargs -r rm -f

%build
sh ./build.sh

%install

# jars
install -dm 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 Output/%{name}-lite.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-lite-%{version}.jar
install -pm 644 Output/%{name}-sax.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-sax-%{version}.jar
install -pm 644 Output/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap be.cyberelf.nanoxml %{name} %{version} JPP %{name}
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-lite.pom
%add_to_maven_depmap be.cyberelf.nanoxml lite %{version} JPP %{name}-lite

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr Documentation/JavaDoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink


%files
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-sax-%{version}.jar
%{_javadir}/%{name}-sax.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*


%files lite
%{_javadir}/%{name}-lite-%{version}.jar
%{_javadir}/%{name}-lite.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*

%files manual
%doc Documentation/NanoXML-Java/*

%files manual-lite
%doc Documentation/NanoXML-Lite/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_6jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_5jpp5
- new jpp release

* Wed Nov 12 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt2_4jpp1.7
- force build with java4

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.2.3-alt1_4jpp1.7
- converted from JPackage by jppimport script

