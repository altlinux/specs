# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           joda-convert
Version:        1.3
Release:        alt1_1jpp7
Summary:        Java library for conversion to and from standard string formats

Group:          Development/Java
License:        ASL 2.0 

URL:            https://github.com/JodaOrg/joda-convert/
# wget -O joda-convert-1.3.tar.gz https://github.com/JodaOrg/joda-convert/tarball/v1.3
Source0:        joda-convert-1.3.tar.gz

BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-changes-plugin
BuildRequires:  maven-project-info-reports-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  junit4
BuildRequires:  dos2unix

Requires:       jpackage-utils
Source44: import.info

%description
Java library to enable conversion to and from standard string formats.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JodaOrg-joda-convert-df6d6c9

%build
mvn-rpmbuild install javadoc:javadoc
for x in LICENSE.txt NOTICE.txt RELEASE-NOTES.txt; do
    dos2unix $x
done

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_1jpp7
- new version

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_3jpp7
- new version

