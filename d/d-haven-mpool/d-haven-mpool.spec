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


Name:           d-haven-mpool
Version:        1.0
Release:        alt1_5jpp6
Epoch:          0
Summary:        D-Haven Managed Pool async
License:        ASL 2.0
Group:          Development/Java
URL:            http://d-haven.org/
# cvs -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/d-haven login
# cvs -z3 -d:pserver:anonymous@cvs.sourceforge.net:/cvsroot/d-haven co -P managed-pool
Source0:        d-haven-mpool-1.0-src.tar.gz
Source4:        d-haven-mpool-1.0-jpp-depmap.xml
Source5:        d-haven-mpool-1.0.pom
Patch0:         d-haven-mpool-1.0-build_xml.patch
Requires(post): jpackage-utils >= 0:1.7.5
Requires(postun): jpackage-utils >= 0:1.7.5
Requires:       concurrent
Requires:       d-haven-event
BuildRequires:  jpackage-utils >= 0:1.7.5
BuildRequires:  ant >= 0:1.7.1
BuildRequires:  junit
BuildRequires:  concurrent
BuildRequires:  d-haven-event
BuildArch:      noarch
Source44: import.info

%description
D-Haven Managed Pool is a library designed to provide pools
that are asynchronously managed in a background thread.  The
pool system is very flexible and can accommodate just about
every need.  It boasts the ability to add pool listeners so
that you can instrument and intercept the pooled objects when
they are created, destroyed, acquired, and released.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n managed-pool
find . -name "*.jar" | xargs -t rm
%patch0 -p0

%build
export CLASSPATH=$(build-classpath concurrent d-haven-event junit)
CLASSPATH=${CLASSPATH}:target/classes:target/test-classes
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Dbuild.sysclasspath=only jar javadoc

%install

# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/managed-pool-1.0.jar \
$RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)

# poms
%add_to_maven_depmap %{name} managed-pool %{version} JPP %{name}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr target/docs/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}
# FIXME: (dwalluck): breaks --short-circuit
rm -rf target/docs/apidocs

%files
%doc LICENSE.txt
%{_javadir}/*
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}


%changelog
* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp6
- new jpp relase

* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_4jpp5
- fixed repocop warnings

* Tue Jul 31 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_3jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_2jpp1.7
- converted from JPackage by jppimport script

