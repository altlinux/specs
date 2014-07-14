BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-test
Version:        1.2.1
Release:        alt5_4jpp7
Summary:        FEST Testing

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# git clone https://github.com/alexruiz/fest-test.git
# cd fest-test
# git archive --prefix="fest-test-1.2.1/" --format=tar \
#   7a43f000480534f393150cbe0cdd0f9eab0e03b8 | \
#   bzip2 - >../fest-test-1.2.1.tar.bz2
Source0:        %{name}-%{version}.tar.bz2

# those two patches make the fest version match with
# the currently packaged (and compatible) version in
# Fedora, and let us use a most up-to-date version of
# the code, rather than an extremely old and
# unmaintained one
Patch0:         fix-parent-version.patch
Patch1:         fix-util-version.patch

BuildArch:      noarch

BuildRequires:  mockito
BuildRequires:  junit
BuildRequires:  jpackage-utils

BuildRequires:  maven
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-dependency-plugin

BuildRequires:  fest-common = 1.0.11
BuildRequires:  fest-util = 1.2.0

Requires:       mockito
Requires:       junit
Requires:       fest-common = 1.0.11
Requires:       fest-util = 1.2.0
Source44: import.info


%description
Utility methods for testing FEST modules

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
* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt5_4jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_4jpp7
- fc release

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt4_0.r1039.1jpp7
- fixed build

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_0.r1039.1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt3_0.r1039.1jpp6
- added maven2-plugin-resources dep

* Sun Jan 09 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_0.r1039.1jpp6
- fixed build

* Fri Sep 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_0.r1039.1jpp6
- new version

