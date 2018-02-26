Packager: Igor Vlasenko <viy@altlinux.ru>
Obsoletes: javamail = 1.3.1-alt1
Obsoletes: javamail = 1.3.1-alt2
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

%define gcj_support 0

%define jmailver 1.4

Name:           sun-mail
Version:        1.4
Release:        alt1_3jpp5
Epoch:          0
Summary:        JavaMail library
License:        CDDL
Url:            https://glassfish.dev.java.net/javaee5/mail/
Source0:        sun-javamail-1.4-src.tar.gz
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r JAVAMAIL-1_4 glassfish/mail
Source1:        CDDLv1.0.html
Source2:        sun-mail-1.4.pom
Source3:        sun-mail-dsn-1.4.pom
Source4:        sun-mail-imap-1.4.pom
Source5:        sun-mail-mailapi-1.4.pom
Source6:        sun-mail-pop3-1.4.pom
Source7:        sun-mail-smtp-1.4.pom
Patch0:         sun-mail-1.4-build.patch

Group:          Development/Java
BuildRequires: ant >= 0:1.6.5
BuildRequires: jpackage-utils >= 0:1.7.2
BuildRequires: sun-jaf
BuildRequires: gnu-crypto-sasl-jdk1.4
Requires: sun-jaf
Requires: gnu-crypto-sasl-jdk1.4
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Provides:       javamail = 0:%{jmailver}
Provides:       javamail-monolithic = 0:%{jmailver}
Provides:    javamail_1_4_api = %{version}-%{release}
Provides:    javamail_api = 0:1.4

%description
The JavaMail API provides a platform-independent and 
protocol-independent framework to build mail and messaging 
applications. The JavaMail API is available as an optional 
package for use with Java SE platform and is also included 
in the Java EE platform.
The JavaMail 1.4 release includes many API improvements 
approved by the Java Community Process via JSR-919. It also 
includes improvements in MIME parsing performance and support 
for parsing and constructing Delivery Status Notifications. 
Note: You will also need the JavaBeans Activation Framework 
(JAF) extension that provides the javax.activation package. 
We suggest you use version 1.1 of JAF, the latest release.
 

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       javamail-javadoc = 0:%{jmailver}

%description javadoc
%{summary}.

%prep
%setup -q -n mail
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done
%patch0 -b .sav0

%build
export CLASSPATH=%(build-classpath sasl)
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 -Djavaee.jar=$(build-classpath sun-jaf) release 

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 644 build/release/mail.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-monolithic-%{version}.jar
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

(cd $RPM_BUILD_ROOT%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
touch $RPM_BUILD_ROOT%{_javadir}/javamail.jar # for %ghost

touch $RPM_BUILD_ROOT%{_javadir}/javamail_api.jar # for %ghost
touch $RPM_BUILD_ROOT%{_javadir}/javamail_1_4_api.jar # for %ghost

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP-%{name}-monolithic.pom
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP.%{name}-dsn.pom
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP.%{name}-imap.pom
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP.%{name}-mailapi.pom
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP.%{name}-pop3.pom
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP.%{name}-smtp.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 %{SOURCE1} \
     $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/CDDLv1.0.html

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_%{name}<<EOF
%{_javadir}/javamail.jar	%{_javadir}/%{name}-monolithic-%{version}.jar	010400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_api_%{name}<<EOF
%{_javadir}/javamail_api.jar	%{_javadir}/sun-mail/mailapi.jar	010400
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/javamail_1_4_api_%{name}<<EOF
%{_javadir}/javamail_1_4_api.jar	%{_javadir}/sun-mail/mailapi.jar	010400
EOF

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%_altdir/javamail_1_4_api_%{name}
%_altdir/javamail_api_%{name}
%_altdir/javamail_%{name}
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%{_javadir}/%{name}-monolithic.jar
%{_javadir}/%{name}-monolithic-%{version}.jar
%{_javadir}/%{name}
%exclude %{_javadir}/javamail.jar
%exclude %{_javadir}/javamail_api.jar
%exclude %{_javadir}/javamail_1_4_api.jar
%{_datadir}/maven2/default_poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-monolithic-%{version}.jar.*
%{_libdir}/gcj/%{name}/dsn-%{version}.jar.*
%endif
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Fri Mar 27 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp5
- fixed repocop warnings

* Wed Mar 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_3jpp1.7
- updated to new jpp release

* Sat Dec 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_2jpp1.7
- new jpackage build

* Tue Oct 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_1jpp1.7
- updated to new jpackage release

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt2
- Added unzip to BuildRequires

* Wed Sep 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.3.1-alt1
- Ported to Sisyphus from JPackage
