# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-util
Version:        1.2.0
Release:        alt2_6jpp7
Summary:        FEST Util

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# git clone https://github.com/alexruiz/fest-util.git
# cd fest-util
# git archive --prefix="fest-util-1.2.0/" --format=tar \
#   d0e86f631f9afcbcc462945894c3bc20ec4d1289 | \
#   bzip2 - >../fest-util-1.2.0.tar.bz2
Source0:        %{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  junit
BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-dependency-plugin

BuildRequires:  mockito
BuildRequires:  fest-common = 1.0.11

Requires:       jpackage-utils
Requires:       mockito
Requires:       junit
Requires:       fest-common = 1.0.11
Source44: import.info

%description
Utility methods used by FEST modules

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%build
mvn-rpmbuild \
        -e \
        install javadoc:javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 644 target/%{name}-%{version}.jar  %{buildroot}%{_javadir}/%{name}.jar

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/

%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_4jpp7
- new version

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt4_0.r1039.1jpp7
- fixed build

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt3_0.r1039.1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt3_0.r1039.1jpp6
- added maven2-plugin-resources dep

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt2_0.r1039.1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt1_0.r1039.1jpp6
- new version

