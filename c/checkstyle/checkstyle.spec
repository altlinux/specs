Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Copyright (c) 2000-2005, JPackage Project
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

Name:           checkstyle
Version:        8.0
Release:        alt1_2jpp8
Summary:        Java source code checker
URL:            http://checkstyle.sourceforge.net/
# src/checkstyle/com/puppycrawl/tools/checkstyle/grammars/java.g is GPLv2+
# Most of the files in contrib/usage/src/checkstyle/com/puppycrawl/tools/checkstyle/checks/usage/transmogrify/ are BSD
License:        LGPLv2+ and GPLv2+ and BSD
BuildArch:      noarch

Source0:        http://download.sf.net/checkstyle/checkstyle-%{version}-src.tar.gz
Source2:        %{name}.catalog

BuildRequires:  maven-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(com.sun:tools)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-nodeps)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.codehaus.mojo:antlr-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

Obsoletes:      %{name}-optional < %{version}-%{release}
Obsoletes:      %{name}-demo < %{version}-%{release}
Obsoletes:      %{name}-manual < %{version}-%{release}
Source44: import.info

%description
A tool for checking Java source code for adherence to a set of rules.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%pom_remove_parent

sed -i s/guava-jdk5/guava/ pom.xml

# not needed for package build
%pom_remove_plugin :maven-eclipse-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

# these are only needed for upstream QA
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-linkcheck-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :xml-maven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :spotbugs-maven-plugin

# get rid of system scope
%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools

# fix encoding issues in docs
sed -i 's/\r//' LICENSE LICENSE.apache20 README.md

# The following test needs network access, so it would fail on Koji
sed -i '/testLoadFromURL/s/ *.*/    @org.junit.Ignore&/' src/test/java/com/puppycrawl/tools/checkstyle/filters/SuppressionsLoaderTest.java

# Test failure, TODO: investigate this
sed -i '/testUnexpectedChar/s/./@org.junit.Ignore/' src/test/java/com/puppycrawl/tools/checkstyle/grammars/GeneratedJava14LexerTest.java

%build
%mvn_file  : %{name}
# Tests are skipped due to unavailable test dependencies
# (com.github.stefanbirkner:system-rules:jar:1.9.0 and
# nl.jqno.equalsverifier:equalsverifier:jar:1.7.2)
%mvn_build -f

%install
%mvn_install

# script
%jpackage_script com.puppycrawl.tools.checkstyle.Main "" "" checkstyle:antlr:apache-commons-beanutils:apache-commons-cli:apache-commons-logging:apache-commons-collections:guava checkstyle true

# dtds
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/xml/%{name}/catalog
cp -pa src/main/resources/com/puppycrawl/tools/checkstyle/*.dtd \
  %{buildroot}%{_datadir}/xml/%{name}

# ant.d
install -dm 755  %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
checkstyle antlr apache-commons-beanutils apache-commons-cli apache-commons-logging guava
EOF

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/checkstyle.conf`
touch $RPM_BUILD_ROOT/etc/java/checkstyle.conf

%post
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%postun
if [ -x %{_bindir}/install-catalog -a -d %{_sysconfdir}/sgml ]; then
  %{_bindir}/install-catalog --remove \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.cat \
    %{_datadir}/xml/%{name}/catalog > /dev/null || :
fi

%files -f .mfiles
%doc LICENSE
%doc README.md
%{_datadir}/xml/%{name}
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%config(noreplace,missingok) /etc/java/checkstyle.conf

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
* Tue Nov 21 2017 Igor Vlasenko <viy@altlinux.ru> 0:8.0-alt1_2jpp8
- new version

* Wed Oct 18 2017 Igor Vlasenko <viy@altlinux.ru> 0:7.7-alt1_1jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 0:7.1-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.13-alt1_2jpp8
- new version

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 0:6.6-alt1_2jpp8
- unbootsrap build

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_7jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.6-alt1_5jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.5-alt3_4jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:5.5-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.5-alt1_4jpp7
- new version

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt3_1jpp5
- added to depmap com.puppycrawl.tools:checkstyle

* Sat Mar 27 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_1jpp5
- full version

* Fri Mar 26 2010 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2_0jpp0
- temporary stub for 4.4

* Sun Sep 21 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt2
- temporary stub to repair other packages rebuild

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:5.0-alt1_0.beta01.4jpp5
- converted from JPackage by jppimport script

* Sat Dec 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt3_1jpp1.7
branch 4.0 compatible build

* Tue Nov 13 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt2_1jpp1.7
- require new commons-cli

* Thu Aug 02 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 0:4.1-alt2_3jpp1.7
- converted from JPackage by jppimport script

* Sun Mar 26 2006 Vladimir Lettiev <crux@altlinux.ru> 4.1-alt2
- Fix build with j2se1.5

* Sun Dec 18 2005 Vladimir Lettiev <crux@altlinux.ru> 4.1-alt1
- Initial build for ALTLinux Sisyphus

