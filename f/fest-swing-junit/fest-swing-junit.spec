# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           fest-swing-junit
Version:        1.2.1
Release:        alt1_6jpp7
Summary:        FEST Swing JUnit support

Group:          Development/Java
License:        ASL 2.0
URL:            http://fest.easytesting.org

# svn co http://svn.codehaus.org/fest/tags/fest-swing-junit-1.2.1
# tar cvfj fest-swing-junit-1.2.1.tar.bz2 fest-swing-junit-1.2.1
Source0:        %{name}-%{version}.tar.bz2
Patch0:         fest-swing-junit-remove-fest-test-dep.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  junit
BuildRequires:  commons-codec
BuildRequires:  ant-junit
BuildRequires:  fest-swing = 1.2.1

Requires:       jpackage-utils
Requires:       commons-codec
Requires:       ant-junit
Requires:       junit
Requires:       fest-swing = 1.2.1
Source44: import.info

%description
FEST-Swing provides a simple and intuitive API for
functional testing of Swing user interfaces, resulting in tests that
are compact, easy to write, and read like a specification.
FEST simulates actual user gestures at the operating system level,
ensuring that the application will behave correctly in front of the user.

This package provides integration with JUnit.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0

%build
# Skip tests because that would require dependency on obsolete
# and difficult to package fest-mocks. Upstream is moving
# to mockito for subsequent releases.
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:javadoc

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
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_6jpp7
- new release

* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_4jpp7
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

