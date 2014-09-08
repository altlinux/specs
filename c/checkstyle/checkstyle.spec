Epoch: 0
%filter_from_requires /^.usr.bin.run/d
BuildRequires: /proc
BuildRequires: jpackage-compat
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
Version:        5.6
Release:        alt1_7jpp7
Summary:        Java source code checker
URL:            http://checkstyle.sourceforge.net/
# src/checkstyle/com/puppycrawl/tools/checkstyle/grammars/java.g is GPLv2+
# Most of the files in contrib/usage/src/checkstyle/com/puppycrawl/tools/checkstyle/checks/usage/transmogrify/ are BSD
License:        LGPLv2+ and GPLv2+ and BSD
Group:          Development/Java
Source0:        http://download.sf.net/checkstyle/checkstyle-%{version}-src.tar.gz
Source2:        %{name}.catalog

# Used for releases only, no use for us
Patch0:         0001-Remove-sonatype-parent.patch

# not available in Fedora yet
Patch1:         0002-Remove-linkcheck-plugin.patch

# get rid of eclipse dependency
Patch2:         0003-Remove-eclipse-plugin.patch


BuildRequires:  antlr-maven-plugin
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-cli
BuildRequires:  apache-commons-logging
BuildRequires:  guava
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

BuildArch:      noarch

Obsoletes:      %{name}-optional < %{version}-%{release}
# revisit later, maybe manual will come back when change from ant to
# maven build system will settle down
Obsoletes:      %{name}-manual < %{version}-%{release}
Source44: import.info

%description
A tool for checking Java source code for adherence to a set of rules.

%package        demo
Group:          Development/Java
Summary:        Demos for %{name}
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

# these are only needed for upstream QA
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :exec-maven-plugin

# fix encoding issues in docs
sed -i 's/\r//' LICENSE LICENSE.apache20 README RIGHTS.antlr \
         checkstyle_checks.xml sun_checks.xml suppressions.xml \
         contrib/hooks/*.pl src/site/resources/css/*css \
         java.header

# The following test needs network access, so it would fail on Koji
rm -f src/tests/com/puppycrawl/tools/checkstyle/filters/SuppressionsLoaderTest.java

%build
%mvn_file  : %{name}
%mvn_build


%install
%mvn_install

# script
%jpackage_script com.puppycrawl.tools.checkstyle.Main "" "" checkstyle:antlr:apache-commons-beanutils:apache-commons-cli:apache-commons-logging:guava checkstyle true

# dtds
install -Dm 644 %{SOURCE2} %{buildroot}%{_datadir}/xml/%{name}/catalog
cp -pa src/checkstyle/com/puppycrawl/tools/checkstyle/*.dtd \
  %{buildroot}%{_datadir}/xml/%{name}

# javadoc
install -dm 755  %{buildroot}%{_javadocdir}/%{name}
cp -par target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# demo
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -par contrib/* %{buildroot}%{_datadir}/%{name}

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
%doc LICENSE README
%doc checkstyle_checks.xml java.header sun_checks.xml suppressions.xml
%{_datadir}/xml/%{name}
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/ant.d/%{name}
%config(noreplace,missingok) /etc/java/checkstyle.conf

%files demo
%{_datadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE


%changelog
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

