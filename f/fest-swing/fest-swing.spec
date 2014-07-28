# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-swing
Version:        1.2.1
Release:        alt1_9jpp7
Summary:        FEST Swing

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# from http://svn.codehaus.org/fest/tags/fest-swing-1.2.1
# use make-fest-tarball.sh to generate
Source0:        fest-swing-%{version}.tar.bz2
Source1:        make-fest-tarball.sh

# make sure dependencies match the available packages
Patch0:         remove-mock-deps.patch
Patch1:         fix-assert-deps.patch
Patch2:         fix-parent-pom.patch
Patch3:         fix-encoding.patch

BuildArch:      noarch

BuildRequires:  jcip-annotations
BuildRequires:  jpackage-utils
BuildRequires:  fest-common = 1.0.11
BuildRequires:  fest-util = 1.2.0

BuildRequires:  fest-reflect = 1.3
BuildRequires:  fest-assert = 1.4

BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-dependency-plugin

Requires:       jcip-annotations
Requires:       jpackage-utils

Requires:       fest-common = 1.0.11
Requires:       fest-util = 1.2.0
Requires:       fest-reflect = 1.3
Requires:       fest-assert = 1.4
Source44: import.info

%description
Fluent interface for functional GUI testing

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
%patch2 -p1
%patch3 -p1

# skip test because we don't package fest-mock, since it indirectly
# requires a library who doesn't comply with the allowed lincenses
%build
mvn-rpmbuild \
        -Dmaven.test.skip=true \
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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_9jpp7
- new release

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_7jpp7
- new release

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt4_1jpp7
- fixed build

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3_1jpp7
- fixed build

* Thu Mar 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1jpp7
- fixed build with maven3

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_1jpp6
- added maven2-plugin-resources dep

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_1jpp6
- new version

