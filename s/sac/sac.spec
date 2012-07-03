AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# one of the sources is a zip file
BuildRequires: unzip
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


Name:           sac
Version:        1.3
Release:	alt2_7jpp6
Epoch:          0
Summary:        Java standard interface for CSS parser
License:        W3C
Group:          Development/Java
URL:            http://www.w3.org/Style/CSS/SAC/
Source0:        http://www.w3.org/2002/06/sacjava-1.3.zip
Source1:        sac-build.xml
Source2:        http://mirrors.dotsrc.org/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
Source3:        sac-MANIFEST.MF
Requires(post): jpackage-utils >= 0:1.7.3
Requires(postun): jpackage-utils >= 0:1.7.3
BuildRequires:  ant >= 0:1.6.5
BuildRequires:  jpackage-utils >= 0:1.7.3
BuildRequires:  zip
BuildArch:      noarch
Source44: import.info
Source45: sac.jar-OSGi-MANIFEST.MF

%description
SAC is a standard interface for CSS parser and supposed to work with CSS1,
CSS2, CSS3 (currently under development) and other CSS derived languages.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
cp -p %{SOURCE1} build.xml

# correct silly permissions
chmod -R go=u-w *

# remove all binary libs
find . -name "*.jar" | xargs -t rm

mkdir -p META-INF
cp -p %{SOURCE3} META-INF/MANIFEST.MF

%build
export OPT_JAR_LIST=:
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5  jar javadoc

touch META-INF/MANIFEST.MF
zip -u build/lib/sac.jar META-INF/MANIFEST.MF

%install

# jar
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms and depmap frags
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE2} %{buildroot}%{_datadir}/maven2/poms/JPP-sac.pom
%add_to_maven_depmap org.w3c.css sac %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# inject OSGi manifest sac.jar-OSGi-MANIFEST.MF
rm -rf META-INF
mkdir -p META-INF
cp %{SOURCE45} META-INF/MANIFEST.MF
# update even MANIFEST.MF already exists
# touch META-INF/MANIFEST.MF
zip -v %buildroot/usr/share/java/sac.jar META-INF/MANIFEST.MF
# end inject OSGi manifest sac.jar-OSGi-MANIFEST.MF

%files
%doc COPYRIGHT.html
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/JPP-sac.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Sat Sep 17 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt2_7jpp6
- updated OSGi manifest

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_7jpp6
- added osgi manifest

* Sat Dec 20 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_4jpp5
- first build

