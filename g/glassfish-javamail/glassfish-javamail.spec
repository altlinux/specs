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

%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}

%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/sun-javamail/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
%define jar_name mail

%define jmailver  1.4

Name:           glassfish-javamail
Version:        1.4.0
Release:        alt2_5jpp6
Epoch:          0
Summary:        Glassfish - JavaMail API
License:        CDDL
Group:          Development/Java
URL:            http://glassfish.dev.java.net/
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
#cvs -d :pserver:guest@cvs.dev.java.net:/cvs checkout glassfish/mail
Source1:        %{name}-%{version}-LICENCE.tar.gz
#cvs -d :pserver:guest@cvs.dev.java.net:/cvs checkout glassfish/bootstrap ... this tar is a tar of the legal folder under glassfish/bootstrap
Source2:        mail-1.4.pom
Source3:        mail-dsn-1.4.pom
Source4:        mail-imap-1.4.pom
Source5:        mail-mailapi-1.4.pom
Source6:        mail-pop3-1.4.pom
Source7:        mail-smtp-1.4.pom

Source8:        %{name}-component-info.xml
Patch0:         %{name}-%{version}-ant-hack.patch
BuildRequires: ant >= 0:1.6.5
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: glassfish-jaf
Requires: glassfish-jaf
Provides:       javamail = 0:%{jmailver}
Provides:       javamail-monolithic = 0:%{jmailver}
Source44: import.info

%description
JavaMail Api from Glassfish

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       javamail-javadoc = 0:%{jmailver}
BuildArch: noarch

%description javadoc
%{summary}.

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
%setup -q -n %{name} 
%setup -q -n %{name} -T -D -a 1
%patch0 -p1

%build
export CLASSPATH=
export OPT_JAR_LIST=:
ant -Dant.build.javac.source=1.5 -Dant.build.javac.target=1.5 -Djavaee.jar=$(build-classpath glassfish-jaf) release

%install

# jars
install -d -m 0755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -p -m 0644 build/release/%{jar_name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-monolithic-%{version}.jar
install -m 644 build/release/lib/dsn.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/dsn-%{version}.jar
install -m 644 build/release/lib/imap.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/imap-%{version}.jar
install -m 644 build/release/lib/mailapi.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/mailapi-%{version}.jar
install -m 644 build/release/lib/pop3.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/pop3-%{version}.jar
install -m 644 build/release/lib/smtp.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/smtp-%{version}.jar

%add_to_maven_depmap javax.mail mail %{version} JPP %{name}-monolithic
%add_to_maven_depmap javax.mail dsn %{version} JPP/%{name} dsn
%add_to_maven_depmap javax.mail imap %{version} JPP/%{name} imap
%add_to_maven_depmap javax.mail mailapi %{version} JPP/%{name} mailapi
%add_to_maven_depmap javax.mail pop3 %{version} JPP/%{name} pop3
%add_to_maven_depmap javax.mail smtp %{version} JPP/%{name} smtp

pushd $RPM_BUILD_ROOT%{_javadir}
ln -sf %{name}-monolithic-%{version}.jar %{name}.jar
ln -sf %{name}-monolithic-%{version}.jar %{name}-monolithic.jar
#ln -sf %{name}-monolithic-%{version}.jar javamail.jar
popd

(cd $RPM_BUILD_ROOT%{_javadir}/%{name}
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo ${jar} | sed "s|-%{version}||g"`;done)
touch $RPM_BUILD_ROOT%{_javadir}/javamail.jar

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/poms
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}.pom
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP-%{name}-monolithic.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-dsn.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-imap.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-mailapi.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-pop3.pom
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/poms/JPP.%{name}-smtp.pom

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%if %with repolib
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i "s/@VERSION@/%{version}-brew/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{repodirsrc}
install -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
cp -p $RPM_BUILD_ROOT%{_javadir}/%{name}.jar $RPM_BUILD_ROOT%{repodirlib}/mail.jar
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_%{name}<<EOF
%{_javadir}/javamail.jar	%{_javadir}/%{name}-monolithic-%{version}.jar	10100
EOF

%if %with repolib
%define compatrepodir %{_javadir}/repository.jboss.com/glassfish/javamail/%{version}-brew
install -d -m 755 $RPM_BUILD_ROOT%{compatrepodir}/
ln -s $(relative %{repodir}/lib %{compatrepodir}/lib) $RPM_BUILD_ROOT%{compatrepodir}/lib
ln -s $(relative %{repodir}/src %{compatrepodir}/src) $RPM_BUILD_ROOT%{compatrepodir}/src
cp -a $RPM_BUILD_ROOT%{repodir}/component-info.xml $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
sed -i s,sun-javamail,glassfish/javamail, $RPM_BUILD_ROOT%{compatrepodir}/component-info.xml
%endif

%files
%_altdir/javamail_%{name}
%doc build/META-INF/LICENSE.txt
%{_javadir}/%{name}-monolithic-%{version}.jar
%{_javadir}/%{name}-monolithic.jar
%{_javadir}/%{name}.jar
%{_datadir}/maven2/poms/*
%{_mavendepmapfragdir}/*
%{_javadir}/%{name}
%exclude %{_javadir}/javamail.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%if %with repolib
%files repolib
%{_javadir}/repository.jboss.com
%endif

%changelog
* Wed Oct 20 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_5jpp6
- jbossas42 compatible repolib

* Tue Sep 28 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_4jpp6
- new jpackage release

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_3jpp5
- fixed repocop warnings

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_3jpp5
- converted from JPackage by jppimport script

* Wed Jul 02 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_1jpp5
- converted from JPackage by jppimport script

