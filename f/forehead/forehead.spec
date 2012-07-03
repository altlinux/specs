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


Name:           forehead
Version:        1.0
Release:        alt1_0.b4.3jpp6
Epoch:          1
Summary:        Forehead: Java ClassLoader Management Framework

Group:          Development/Java
License:        Open Source
URL:            http://forehead.sourceforge.net/
Source0:        forehead.tar.gz
Source1:        forehead_doc.tar.gz
Source2:        http://mirrors.dotsrc.org/maven2/forehead/forehead/1.0-beta-4/forehead-1.0-beta-4.pom

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-junit
BuildRequires:  junit >= 0:3.8.1
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info

%description
forehead is a very small framework to assist in controlling 
the run-time ClassLoader hierarchy of Java applications.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documentation for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n %{name}

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only test dist
rm -rf target/docs/*
(cd target/docs; gzip -dc %{SOURCE1} | tar -xf -)

%install
install -Dm 644 dist/%{name}-%{version}-beta-4.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
%add_to_maven_depmap %{name} %{name} %{version}-beta-4 JPP %{name}

install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp LICENSE.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
cp -pr target/docs/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%files
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%{_docdir}/%{name}-%{version}

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.b4.3jpp6
- new jpp relase

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.b4.2jpp5
- new jpp release

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.b4.1jpp5
- fixed repocop warnings

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1_0.b4.1jpp1.7
- converted from JPackage by jppimport script

* Sat Apr 30 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt0.1
- Rebuilt for ALTLinux Sisyphus
- spec cleanup

* Mon Aug 23 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.b4-4jpp
- Build with ant-1.6.2

* Fri Aug 06 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.b4-3jpp
- Void change

* Tue Jun 01 2004 Randy Watler <rwatler at finali.com> - 0:1.0.b4-2jpp
- Upgrade to Ant 1.6.X

* Tue Jan 20 2004 Ralph Apel <r.apel at r-apel.de> - 0:1.0.b4-1jpp
- First JPackage release
