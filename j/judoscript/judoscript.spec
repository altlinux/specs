Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
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


Name:           judoscript
Version:        1.0
Release:        alt2_1jpp5
Epoch:          0
Summary:        Judo Scripting Language

Group:          Development/Java
License:        LGPL
URL:            http://www.judoscript.org/home.html
Source0:        http://www.judoscript.org/store/src.jar
Source1:        http://www.judoscript.org/store/generated.jar
Source2:        %{name}-%{version}.pom
Patch0:         judoscript-JavaSysFunLib.patch
Patch1:         judoscript-ExprWSDL.patch
Patch2:         judoscript-StmtSendMail.patch


BuildArch:      noarch
BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant
BuildRequires: axis
BuildRequires: bsf
BuildRequires: hibernate3
BuildRequires: jakarta-commons-compress10
BuildRequires: jakarta-commons-email
BuildRequires: jakarta-commons-fileupload
BuildRequires: jakarta-commons-lang
BuildRequires: jakarta-commons-logging
BuildRequires: jaf_1_0_2_api
BuildRequires: javamail_1_3_1_api
BuildRequires: jaxrpc_1_1_api
BuildRequires: log4j
BuildRequires: servlet_2_3_api
BuildRequires: wsdl4j
BuildRequires: xalan-j2

Requires: ant
Requires: bsf
Requires: jakarta-commons-compress10
Requires: jakarta-commons-email
Requires: jakarta-commons-fileupload
Requires: jakarta-commons-lang
Requires: jakarta-commons-logging
Requires: log4j

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5

%description
Judo is a practical, functional scripting language. It is 
designed to cover the use cases of not only algorithmic/
object-oriented/multi-threaded programming and Java 
scripting but also a number of major application domain 
tasks, such as scripting for JDBC, WSDL, ActiveX, OS, 
multiple file/data formats, etc. Despite its rich 
functionality, the base language is extremely simple, and 
domain support syntax is totally intuitive to domain 
experts, so that even though you have never programmed in 
Judo, you would have little trouble figuring out what the 
code does.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation

%description    javadoc
%{summary}.


%prep
%setup -T  -c
mkdir -p target/classes
mkdir -p target/site/apidocs
unzip -q %{SOURCE0}
unzip -q %{SOURCE1}
cp -pr src/com/* src/judo/com/
%patch0 -b .sav0
%patch1 -b .sav1
%patch2 -b .sav2
rm -rf src/judo/com/judoscript/ext
for j in $(find src/judo -name "*.java" -exec grep -l 'commons\.compress\.tar\.' {} \;); do
    sed -i -e 's/commons\.compress\.tar\./commons\.compress\.archivers\.tar\./' $j
done

%build
#export JAVA_HOME=%{_jvmdir}/java
export CLASSPATH=$(build-classpath \
ant \
axis/axis \
bsf \
commons-compress10 \
commons-email \
commons-fileupload \
commons-lang \
commons-logging \
hibernate3 \
log4j \
servlet_2_3_api \
wsdl4j \
xalan-j2 \
javamail_1_3_1_api \
jaf_1_0_2_api \
jaxrpc_1_1_api \
)

export BD=$(pwd)
#pushd src/judo/com/judoscript/parser
#$JAVA_HOME/bin/java -cp $(build-classpath javacc) javacc judo.jj
#popd
#patch -p0 < %{PATCH1}
pushd src/judo
$JAVA_HOME/bin/javac  -target 1.4 -source 1.4 -d ${BD}/target/classes $(find com -name "*.java")
$JAVA_HOME/bin/javadoc -d ${BD}/target/site/apidocs -sourcepath . \
com.judoscript \
com.judoscript.jmdl \
com.judoscript.jmdl.reader \
com.judoscript.studio \
com.judoscript.xml \
com.judoscript.user \
com.judoscript.user.httpserver \
com.judoscript.db \
com.judoscript.bio \
com.judoscript.hibernate \
com.judoscript.parser \
com.judoscript.parser.helper \
com.judoscript.jusp \
com.judoscript.jdk14 \
com.judoscript.gui \
com.judoscript.util \
com.judoscript.util.classfile \
com.judoscript.util.jdiff \

popd


pushd target/classes
$JAVA_HOME/bin/jar cf ../%{name}-%{version}.jar *
popd


%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/
%add_to_maven_depmap %{name} %{name} %{version} JPP %{name}
ln -sf %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar


# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%files
%{_javadir}/*.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}


%changelog
* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_1jpp5
- rebuild with compat commons-compress10

* Tue Mar 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_1jpp5
- new version

