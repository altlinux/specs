Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven-local unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           apache-mime4j
Version:        0.7.2
Release:        alt3_3jpp7
Summary:        Apache JAMES Mime4j

Group:          Development/Java
License:        ASL 2.0
URL:            http://james.apache.org/mime4j
Source0:        http://apache.online.bg//james/mime4j/apache-mime4j-project-%{version}-source-release.zip
BuildArch: noarch

BuildRequires: apache-commons-logging
BuildRequires: log4j
BuildRequires: junit
BuildRequires: apache-commons-io
BuildRequires: apache-james-project
BuildRequires: javacc-maven-plugin
BuildRequires: maven-remote-resources-plugin
BuildRequires: apache-rat-plugin
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
Requires: apache-commons-logging
Requires: log4j
Requires: apache-commons-io
Source44: import.info

%description
Java stream based MIME message parser

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n %{name}-project-%{version}
rm -fr stage
# prevents rat plugin from failing the build
rm -fr DEPENDENCIES

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}-project.pom

%add_maven_depmap JPP-%{name}-project.pom

for sub in core dom storage; do
    # install jar
    install -Dpm 644 ${sub}/target/%{name}-${sub}-%{version}.jar \
            $RPM_BUILD_ROOT/%{_javadir}/%{name}/${sub}.jar;

    # intall pom
    install -Dpm 644 ${sub}/pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP.%{name}-${sub}.pom

    # maven depmap
    %add_maven_depmap JPP.%{name}-${sub}.pom %{name}/${sub}.jar
done

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}/
rm -rf target/site/api*

%files
%doc LICENSE NOTICE RELEASE_NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt3_3jpp7
- rebuild with maven-local

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt2_3jpp7
- rebuild with new apache-resource-bundles

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.7.2-alt1_3jpp7
- new release

* Thu Mar 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt3_2jpp6
- dropped felix-maven2 dependency

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt2_2jpp6
- fixed build with maven3

* Sat Jan 29 2011 Igor Vlasenko <viy@altlinux.ru> 0:0.6-alt1_2jpp6
- new version

