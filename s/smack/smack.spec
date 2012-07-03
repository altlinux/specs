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

%define gcj_support 0


Name:           smack
Version:        3.1.0
Release:        alt1_3jpp6
Epoch:          0
Summary:        Open Source XMPP (Jabber) client library

Group:          Development/Java
License:        Apache Software License 2.0
URL:            http://www.igniterealtime.org/projects/smack/index.jsp
Source0:        http://www.igniterealtime.org/downloads/download-landing.jsp?file=smack/smack_src_3_1_0.tar.gz
Source1:        http://repo1.maven.org/maven2/jivesoftware/smack/3.1.0/smack-3.1.0.pom
Source2:        http://repo1.maven.org/maven2/jivesoftware/smackx/3.1.0/smackx-3.1.0.pom
Source3:        http://maven.reucon.com/public/org/igniterealtime/smack/smackx-debug/3.1.0/smackx-debug-3.1.0.pom
Patch0:         smack-3.1.0-build.patch

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
%setup -q -n smack_src_3_1_0
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
rm -rf jingle
%patch0 -b .sav0
ln -sf $(build-classpath jzlib) build/merge/

%build
pushd build
ln -sf $(build-classpath ant-contrib)
ln -sf $(build-classpath junit)
pushd merge
ln -sf $(build-classpath xpp3) xpp.jar
popd
popd
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -f build/build.xml jar javadoc jar-test

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}

install -m 644 target/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
install -m 644 target/%{name}x.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}x-%{version}.jar

install -m 644 target/%{name}-test.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-test-%{version}.jar
install -m 644 target/%{name}x-debug.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}x-debug-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

%add_to_maven_depmap org.igniterealtime.smack %{name} %{version} JPP %{name}
%add_to_maven_depmap org.igniterealtime.smack %{name}x %{version} JPP %{name}x
%add_to_maven_depmap org.igniterealtime.smack %{name}x-debug %{version} JPP %{name}x-debug

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -m 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
install -m 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}x.pom
install -m 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}x-debug.pom

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
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_3jpp6
- new jpp relase

* Wed Apr 01 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.1.0-alt1_1jpp5
- new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.5.0-alt1_3jpp1.7
- converted from JPackage by jppimport script

