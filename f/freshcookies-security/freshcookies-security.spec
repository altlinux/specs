Packager: Igor Vlasenko <viy@altlinux.ru>
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

%define gcj_support 0


Name:           freshcookies-security
Version:        0.60
Release:        alt1_1jpp6
Epoch:          0
Summary:        Security helper
License:        Apache Software License 2.0
Group:          Development/Java
URL:            http://www.freshcookies.org/freshcookies-security
Source0:        http://freshcookies.org/freshcookies-security/freshcookies-security-0.60-src.tar.gz

%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif


%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires: jpackage-utils >= 0:1.7.5

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
This package contains serveral useful utilities for managing
common security operations, such as SSL certificate extraction,
JAR certificate extraction, and policy file manipulation.
SSLHelper is a command-line based utility that examines the
SSL certificates and certificate chains for a given host and
port. If the SSL certificate chain is untrusted, the utility
offers the user the option of placing the certificates in the
JSSE certificate store. It also outputs all of the certificates
it finds (including the server's) as DER-encoded files in the
current directory. These files can then be double-clicked and
imported straight into the Windows certificate store, or
appended (using Keychain) to the Mac OS X trust anchors!
Incredibly handy for troubleshooting certificate trust issues
with (for instance) self-signed JNLP applications.

JarHelper is a command-line utility that extracts certificates
used to sign a specified JAR file and, if any are found, saves
them to disk. If the certificate chain is untrusted, the utility
offers the user the option of placing the certificates in the
java certificate trust store. 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -c
mkdir -p target/site/apidocs/
mkdir -p target/classes/

%build
%{java_home}/bin/javac -d target/classes $(find src -name "*.java")
%{java_home}/bin/javadoc -d target/site/apidocs -sourcepath src org.freshcookies.security.cert org.freshcookies.security.policy

pushd target/classes
%{java_home}/bin/jar cf ../%{name}-%{version}.jar *
popd

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -pm 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
* Tue Oct 19 2010 Igor Vlasenko <viy@altlinux.ru> 0:0.60-alt1_1jpp6
- new version

