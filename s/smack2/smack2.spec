BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2012, JPackage Project
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

%define oname   smack

Name:           smack2
Version:        2.2.1
Release:        alt2_2jpp6
Epoch:          0
Summary:        Open Source XMPP (Jabber) client library

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.igniterealtime.org/projects/smack/index.jsp
Source0:        smack-2.2.1.tgz
#svn export http://svn.igniterealtime.org/svn/repos/smack/tags/smack_2_2_1 smack-2.2.1
# tar czf smack-2.2.1.tgz smack-2.2.1/
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/jivesoftware/smack/2.2.1/smack-2.2.1.pom
Source2:        http://mirrors.ibiblio.org/pub/mirrors/maven2/jivesoftware/smackx/2.2.1/smackx-2.2.1.pom

%if %{gcj_support}
BuildRequires:    gnu-crypto
BuildRequires:          java-gcj-compat-devel
Requires(post):         java-gcj-compat
Requires(postun):       java-gcj-compat
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif

BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  ant-contrib >= 0:1.0
BuildRequires:  junit >= 0:3.8.1
BuildRequires:  jzlib
BuildRequires:  xpp3
Requires:  jzlib
Requires:  xpp3
Requires(post):    jpackage-utils >= 0:1.7.5
Requires(postun):  jpackage-utils >= 0:1.7.5
Source44: import.info


%description
Smack is an Open Source XMPP (Jabber) client library for instant 
messaging and presence. A pure Java library, it can be embedded 
into your applications to create anything from a full XMPP client 
to simple XMPP integrations such as sending notification messages.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    javadoc
%{summary}.

%package        manual
Summary:        Documents for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description    manual
%{summary}.


%prep
%setup -q -n %{oname}-%{version}
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
ln -sf $(build-classpath jzlib) build/merge/

%build
export LANG=en_US.ISO8859-1
pushd build
ln -sf $(build-classpath ant-contrib)
ln -sf $(build-classpath junit)
pushd merge
ln -sf $(build-classpath xpp3) xpp.jar
popd
popd
ant  -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build/build.xml jar javadoc jar-test

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 %{oname}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 %{oname}x.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}x-%{version}.jar

install -m 644 %{oname}-test.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-test-%{version}.jar
install -m 644 %{oname}x-debug.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}x-debug-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap jivesoftware %{oname} %{version} JPP %{name}
%add_to_maven_depmap jivesoftware %{oname}x %{version} JPP %{name}x
%add_to_maven_depmap jivesoftware %{oname}x-debug %{version} JPP/%{name} %{name}x-debug

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}x.pom

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -pr documentation/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%files
%{_javadir}/*
%{_mavendepmapfragdir}/*
%{_datadir}/maven2/poms/*
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}*%{version}.jar.*
%endif

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}

%changelog
* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt2_2jpp6
- fixed build with java 7

* Wed Feb 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2.1-alt1_2jpp6
- new version

