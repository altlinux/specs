Packager: Igor Vlasenko <viy@altlinux.ru>
Obsoletes: jaf = 1.0.2-alt2
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

%define jafver  1.1

Name:           sun-jaf
Version:        1.1
Release:        alt5_3jpp5
Epoch:          0
Summary:        JavaBeans Activation Framework
License:        CDDL
Url:            https://glassfish.dev.java.net/javaee5/mail/
Source0:        sun-jaf-1.1-src.tar.gz 
# cvs -d :pserver:guest@cvs.dev.java.net:/cvs export -r JAF-1_1 glassfish/activation
Source1:        activation-1.1.pom
Source2:        CDDLv1.0.html

Group:          Development/Java
BuildRequires: ant >= 0:1.6.5
BuildRequires: jpackage-utils >= 0:1.7.3
%if ! %{gcj_support}
BuildArch:      noarch
%endif
%if %{gcj_support}
BuildRequires: gnu-crypto
BuildRequires: java-gcj-compat-devel
Requires(post): java-gcj-compat
Requires(postun): java-gcj-compat
%endif
Provides:       jaf = 0:%{jafver}
Provides:       jaf_api = 0:%{jafver}
Provides:       jaf_1_1_api

%description
JavaBeans Activation Framework (JAF) is a standard extension
to the Java platform that lets you take advantage of standard
services to: determine the type of an arbitrary piece of data;
encapsulate access to it; discover the operations available
on it; and instantiate the appropriate bean to perform the
operation(s).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Documentation
Provides:       jaf-javadoc = 0:%{jafver}

%description javadoc
%{summary}.

%prep
%setup -q -n activation
# remove all binary libs
for j in $(find . -name "*.jar"); do
    mv $j $j.no
done

%build
if [ -z "$JAVA_HOME" ]; then export JAVA_HOME=/usr/lib/jvm/java; fi
ant -Dant.build.javac.source=1.4 -Dant.build.javac.target=1.4 release

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 build/release/activation.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
%add_to_maven_depmap javax.activation activation %{version} JPP %{name}

(cd $RPM_BUILD_ROOT%{_javadir} 
ln -s %{name}-%{version}.jar jaf-%{jafver}.jar
ln -s %{name}-%{version}.jar jaf_api.jar
ln -s %{name}-%{version}.jar jaf_1_1_api.jar
for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# poms
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_datadir}/maven2/default_poms/JPP-%{name}.pom

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr build/release/docs/javadocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

install -d -m 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -pm 644 %{SOURCE2} \
           $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/CDDLv1.0.html

%if %{gcj_support}
export CLASSPATH=$(build-classpath gnu-crypto)
%{_bindir}/aot-compile-rpm
%endif
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_%{name}<<EOF
%{_javadir}/jaf.jar	%{_javadir}/%{name}.jar	10099
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_api_%{name}<<EOF
%{_javadir}/jaf_api.jar	%{_javadir}/%{name}.jar	10099
EOF
install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/jaf_1_1_api_%{name}<<EOF
%{_javadir}/jaf_1_1_api.jar	%{_javadir}/%{name}.jar	10099
EOF

cat >>$RPM_BUILD_ROOT/%_altdir/jaf_%{name}<<EOF
%{_javadir}/activation.jar	%{_javadir}/%{name}-%version.jar	10099
EOF

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
    rm -f %{_javadocdir}/%{name}
fi

%files
%_altdir/jaf_1_1_api_%{name}
%_altdir/jaf_api_%{name}
%_altdir/jaf_%{name}
%{_docdir}/%{name}-%{version}/CDDLv1.0.html
%dir %{_docdir}/%{name}-%{version}
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%{_datadir}/maven2/default_poms/*
%{_mavendepmapfragdir}
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}
%{_libdir}/gcj/%{name}/%{name}-%{version}.jar.*
%endif
%{_javadir}/jaf-%{jafver}.jar
#%ghost %{_javadir}/jaf.jar
#%ghost %{_javadir}/jaf_api.jar
#%ghost %{_javadir}/jaf_1_1_api.jar


%files javadoc
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%changelog
* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_3jpp5
- built with java 5

* Sat Dec 22 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_3jpp1.7
- converted from JPackage by jppimport script

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt5_1jpp1.7
fixed candidate for activation.jar alternative

* Mon Dec 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt4_1jpp1.7
restored lost jaf.jar alternative

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt3_1jpp1.7
fixed activation.jar alternative

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt2_1jpp1.7
added activation.jar alternative

* Wed Aug 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_1jpp1.7
- updated to new jpackage version

* Fri Dec 19 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.2-alt2
- Added unzip to BuildRequires

* Wed Sep 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.0.2-alt1
- Ported to Sisyphus from JPackage
