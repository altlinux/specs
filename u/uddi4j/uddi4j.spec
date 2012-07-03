BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2005, JPackage Project
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

%define name            uddi4j
%define version         2.0.4
%define release         1jpp

# -----------------------------------------------------------------------------

Summary:        API to interact with a UDDI registry
Name:           %{name}
Version:        %{version}
Release:        alt2_1jpp1.7
Epoch:		0
Group:          Development/Java
License:        IBM Public License
URL:            http://oss.software.ibm.com/developerworks/opensource/uddi4j/
BuildArch:      noarch
Source0:        ftp://www-126.ibm.com/pub/uddi4j/uddi4j-src-2_0_4.tar.bz2
Requires: axis
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: %{_bindir}/perl
BuildRequires: ant
BuildRequires: axis

%description
UDDI4J is a Java class library that provides an API to interact 
with a UDDI (Universal Description, Discovery and Integration) 
registry. The UDDI Project is a comprehensive, open industry 
initiative enabling businesses to (I) discover each other, and 
(II) define how they interact over the internet and share 
information in a global registry architecture. UDDI is the 
building block which will enable businesses to quickly, easily 
and dynamically find and transact with one another via their 
preferred applications.

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}

%build
export LANG=en_US.ISO8859-1
[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
export JAVA_HOME

export CLASSPATH=$(build-classpath \
axis/axis \
axis/jaxrpc \
axis/saaj \
javamail/mailapi \
)
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.compiler=modern -Djavac.executable=`which javac` compile
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.compiler=modern -Djavac.executable=`which javac` javadocs

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}

for jar in %{name}.jar ; do
   vjar=$(echo $jar | sed s+.jar+-%{version}.jar+g)
   install -m 644 build/lib/$jar $RPM_BUILD_ROOT%{_javadir}/$vjar
   pushd $RPM_BUILD_ROOT%{_javadir}
      ln -fs $vjar $jar
   popd
done

# javadoc
install -d -m 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%doc LICENSE.html
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt2_1jpp1.7
- fixed build with java 7

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.0.4-alt1_1jpp1.7
- converted from JPackage by jppimport script

