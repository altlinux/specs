# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-reflect
Version:        1.3
Release:        alt2_10jpp7
Summary:        FEST Reflection

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# git clone https://github.com/alexruiz/fest-reflect.git
# cd fest-reflect
# git archive --prefix="fest-reflect-1.3/" --format=tar \
#   1d1da6a9c1f445906c409a1c0df68052ec6d0ad4 | \
#   bzip2 - >../fest-reflect-1.3.tar.bz2
Source0:        %{name}-%{version}.tar.bz2

# bump up the version number of the fest-util dependency
# so that it matches the fedora packaged one
Patch0:         fix-util-version.patch

# fix a spurious failing test
Patch1:         fest-reflect-fix-failing-test.patch

BuildArch:      noarch

BuildRequires:  mockito
BuildRequires:  junit
BuildRequires:  jpackage-utils

BuildRequires:  fest-common = 1.0.11
BuildRequires:  fest-util = 1.2.0
BuildRequires:  fest-test = 1.2.1

BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-dependency-plugin

Requires:       jpackage-utils
Requires:       fest-common = 1.0.11
Requires:       fest-util = 1.2.0
Source44: import.info

%description
Fluent Interface that simplifies usage of Java Reflection

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_10jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_8jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8jpp7
- new version

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt4_1jpp7
- fixed build

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_1jpp6
- added maven2-plugin-resources dep

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp6
- new version

