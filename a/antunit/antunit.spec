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


Name:           antunit
Version:        1.1
Release:        alt1_1jpp6
Epoch:          0
Summary:        Ant testing framework
Group:          Development/Java
License:        ASL 2.0
URL:            http://ant.apache.org/antlibs/antunit/
Source0:        antunit-1.1.tgz
# svn export http://svn.apache.org/repos/asf/ant/antlibs/antunit/tags/1.1 antunit-1.1
# tar czf antunit-1.1.tgz antunit-1.1/

BuildRequires: jpackage-utils >= 0:1.7.5
BuildRequires: ant17 >= 0:1.7
BuildRequires: ant17-trax
BuildArch:      noarch

Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Source44: import.info

%description
Ant testing framework.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%prep 
%setup -q 

%build
ant17 distribution
javadoc -d api $(find src/main -name "*.java")

%install

# jars
install -d -m 755 %{buildroot}%{_javadir}

install -m 644 build/lib/ant-%{name}-%{version}.jar \
           %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 build/lib/ant-%{name}-%{version}.pom \
        $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap org.apache.ant ant-antunit %{version} JPP %{name}

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr api/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

# manual
install -dm 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr docs/* %{buildroot}%{_docdir}/%{name}-%{version}

%files
%{_javadir}/%{name}*.jar
%doc %{_docdir}/%{name}-%{version}
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
* Tue Feb 15 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp6
- new version

