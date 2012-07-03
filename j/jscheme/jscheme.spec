BuildRequires: /proc
BuildRequires: jpackage-1.6-compat
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

Summary:                An Open Source implementation of the Java Transaction Service
Name:                   jscheme
Version:                7.2
Release:                alt1_1jpp6
Epoch:                  0
Group:                  Development/Java
License:                zlib/libpng
Url:                    http://jscheme.sourceforge.net/jscheme/main.html
BuildArch:              noarch
Source0:                http://downloads.sourceforge.net/project/jscheme/jscheme/7.2/jscheme-7.2.tgz

BuildRequires:          jpackage-utils >= 0:1.7.5
BuildRequires:          apache-commons-fileupload
BuildRequires:          bsf
BuildRequires:          classpathx-mail
BuildRequires:          hsqldb
BuildRequires:          jaf_1_0_2_api
BuildRequires:          jetty5
BuildRequires:          mysql-connector-java
BuildRequires:          servlet_2_4_api
BuildRequires:          tomcat5-jasper
Requires:          bsf
Requires:          servlet_2_4_api
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
JScheme is a dialect of Scheme with a very simple interface
to Java, called the Javadot notation . This notation provides
a transparent access to all Java classes, constructors,
methods, and fields on the classpath.
JScheme implements all of R4RS Scheme except that
continuations can only be used as escape procedures and
strings are not mutable. 

%package javadoc
Group:          Development/Documentation
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%package manual
Group:          Development/Documentation
Summary:        Documents for %{name}
BuildArch: noarch

%description manual
%{summary}.

%prep
%setup -q
# remove external jars
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
# ext/ia/ia_math.jar.no
# ext/ia/ia_solver.jar.no
# ext/jetty/jasper-compiler.jar.no
ln -sf $(build-classpath jasper5-compiler) ext/jetty/jasper-compiler.jar
# ext/jetty/jasper-runtime.jar.no
ln -sf $(build-classpath jasper5-runtime) ext/jetty/jasper-runtime.jar
# ext/jetty/javax.servlet.jar.no
ln -sf $(build-classpath servlet_2_4_api) ext/jetty/javax.servlet.jar
# ext/jetty/org.mortbay.jetty.jar.no
ln -sf $(build-classpath jetty5/jetty5) ext/jetty/org.mortbay.jetty.jar
# ext/jetty/org.mortbay.jmx.jar.no
ln -sf $(build-classpath jetty5/jetty5-jmx) ext/jetty/org.mortbay.jmx.jar
# ext/webapp/activation-1.0.2.jar.no
ln -sf $(build-classpath jaf_1_0_2_api) ext/webapp/activation-1.0.2.jar
# ext/webapp/commons-fileupload-1.0.jar.no
ln -sf $(build-classpath commons-fileupload) ext/webapp/commons-fileupload-1.0.jar
# ext/webapp/hsqldb-1.7.1.jar.no
ln -sf $(build-classpath hsqldb) ext/webapp/hsqldb-1.7.1.jar
# ext/webapp/mail-1.3.1.jar.no
ln -sf $(build-classpath classpathx-mail-1.3.1-monolithic) ext/webapp/mail-1.3.1.jar
# ext/webapp/multipartformreader.jar.no

# ext/webapp/mysql-connector-java-3.0.14-production-bin.jar.no
ln -sf $(build-classpath mysql-connector-java) ext/mysql-connector-java-3.0.14-production-bin.jar
# lib/bsf.jar.no
ln -sf $(build-classpath bsf) lib/bsf.jar
# lib/ia_math.jar.no

# lib/ia_solver.jar.no

# lib/servlet.jar.no
ln -sf $(build-classpath servlet_2_4_api) lib/servlet.jar

%build
bin/make.sh

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 lib/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -prf doc/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink
rm -rf doc/api

# manual
install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -prf doc/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%files
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Thu Jan 12 2012 Igor Vlasenko <viy@altlinux.ru> 0:7.2-alt1_1jpp6
- converted from JPackage by jppimport script

