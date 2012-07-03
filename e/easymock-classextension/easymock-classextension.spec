BuildRequires: /proc
BuildRequires: jpackage-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
%define version 1.2.1
%define name easymock-classextension
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

#def_with repolib
%bcond_with repolib

%define repodir %{_javadir}/repository.jboss.com/easymock/easymock-classextension/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src


Name:           easymock-classextension
Version:        1.2.1
Release:        alt1_2jpp6
Epoch:          0
Summary:        EasyMock class extension
Group:          Development/Java
License:        MIT
URL:            http://www.easymock.org/
Source0:        http://downloads.sourceforge.net/sourceforge/easymock/easymockclassextension1.2.1.zip
# XXX: based on 1.2
Source1:        http://repo1.maven.org/maven2/easymock/easymockclassextension/1.2.1/easymockclassextension-1.2.1.pom
Obsoletes:      easymockclassextension < %{epoch}:%{version}-%{release}
Provides:       easymockclassextension = %{epoch}:%{version}-%{release}
Requires(post): jpackage-utils
Requires(postun): jpackage-utils
Requires:       cglib
Requires:       easymock
Requires:       jpackage-utils
BuildRequires:  cglib
BuildRequires:  easymock
BuildRequires:  jpackage-utils
BuildRequires:  objenesis
BuildRequires:  unzip
%if %with repolib
BuildRequires:  maven2-plugin-deploy
%endif
BuildArch:      noarch
Source44: import.info

%description
This extension allows generating Mock Objects for classes. 
It has been contributed by Joel Shellman, Henri Tremblay 
and Chad Woolley. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %with repolib
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
%setup -q -n easymockclassextension%{version}
%{_bindir}/find -type f -name "*.jar" | %{_bindir}/xargs -t rm
mkdir -p build/classes
mkdir src
pushd src
%{__unzip} -qq ../src.zip
popd

%build
export CLASSPATH=$(%{_bindir}/build-classpath cglib easymock objenesis)
%{javac}  -target 1.5 -source 1.5 -sourcepath src -d build/classes `%{_bindir}/find src -type f -name "*.java"`
pushd build/classes
%{jar} cf ../easymock-classextension.jar org
popd
%{javadoc} -d build/javadoc -sourcepath src org.easymock.classextension

%install

# jar
mkdir -p %{buildroot}%{_javadir}
cp -p build/easymock-classextension.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
cp -p src.zip %{buildroot}%{_javadir}/%{name}-%{version}-sources.jar
ln -s %{name}-%{version}-sources.jar %{buildroot}%{_javadir}/%{name}-sources.jar

# pom
mkdir -p %{buildroot}%{_datadir}/maven2/poms
cp -p %{SOURCE1} %{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap easymock easymockclassextension %{version} JPP %{name}
%add_to_maven_depmap easymock easymock-classextension %{version} JPP %{name}

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %with repolib
# repolib
%{_bindir}/mvn-jpp deploy:deploy-file -DgroupId=easymock -DartifactId=easymock-classextension -Dversion=%{version} -Dpackaging=jar -Dfile=%{buildroot}%{_javadir}/%{name}-%{version}.jar \
    -DpomFile=%{buildroot}%{_datadir}/maven2/poms/JPP-%{name}.pom -Durl=file:%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew -DrepositoryId=oss-releases
%{_bindir}/mvn-jpp deploy:deploy-file -DgroupId=easymock -DartifactId=easymock-classextension -Dversion=%{version} -Dpackaging=jar -Dfile=src.zip \
    -Dclassifier=sources -Durl=file:%{buildroot}%{_javadir}/repository.jboss.com/maven2-brew -DrepositoryId=oss-releases
%endif

%files
%doc Documentation.html License.html news.txt
%{_javadir}*/%{name}-%{version}.jar
%{_javadir}*/%{name}.jar
%{_javadir}*/%{name}-%{version}-sources.jar
%{_javadir}*/%{name}-sources.jar
%{_datadir}/maven2/poms/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%dir %{_javadir}*
%exclude %dir %{_javadocdir}
%{_javadir}*/repository.jboss.com
%endif

%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.2.1-alt1_2jpp6
- new jpp relase

* Sat Jan 08 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp6
- jpp 6 release

* Sun Feb 21 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_3jpp5
- new jpackage release

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2-alt1_2jpp1.7
- converted from JPackage by jppimport script

