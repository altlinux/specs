Packager: Igor Vlasenko <viy@altlinux.ru>
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
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


Summary:        Fake SMTP Server
Name:           dumbster
Version:        1.6
Release:        alt1_6jpp6
Epoch:          0
License:        Apache Software License 2.0
URL:            http://quintanasoft.com/dumbster/
Group:          Development/Java
#cvs -z3 -d:pserver:anonymous@dumbster.cvs.sourceforge.net:/cvsroot/dumbster co -P dumbster
#tar czf dumbster-1.6.tar.gz dumbster
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-1.6.pom
Patch0:         %{name}-SimpleSmtpServer.patch
BuildRequires: ant >= 0:1.6
BuildRequires: jpackage-utils >= 0:1.6
BuildRequires: jaf
BuildRequires: javamail
BuildRequires: junit
Requires: jaf
Requires: java-sasl
Requires: javamail

%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%else
BuildArch:      noarch
%endif
Source44: import.info


%description
The Dumbster is a very simple fake SMTP server designed for
unit and system testing applications that send email messages.
It responds to all standard SMTP commands but does not deliver
messages to the user. The messages are stored within the
Dumbster for later extraction and verification.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%patch0

%build
pushd lib
ln -sf $(build-classpath javamail)
ln -sf $(build-classpath jaf)
ln -sf $(build-classpath junit)
ln -sf $(build-classpath sasl)
popd

export OPT_JAT_LIST=:
export CLASSPATH=

ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 jar javadoc

%install

# jars
mkdir -p $RPM_BUILD_ROOT%{_javadir}

install -m 0644 build/%{name}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
cp -pr %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}.pom
%add_to_maven_depmap dumbster %{name} 1.6 JPP %{name}

install -dm 755 $RPM_BUILD_ROOT%{_javadir}/maven2
ln -s %{_datadir}/maven2/poms $RPM_BUILD_ROOT%{_javadir}/maven2/poms

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
  rm -f %{_javadocdir}/%{name}
fi

%files
%doc license.txt
%{_javadir}/*.jar
%{_datadir}/maven2/poms
%{_javadir}/maven2
%{_mavendepmapfragdir}

%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif


%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_6jpp6
- added pom

* Wed Jun 03 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_3jpp5
- smtp test was too long idle

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_2jpp1.7
- converted from JPackage by jppimport script

