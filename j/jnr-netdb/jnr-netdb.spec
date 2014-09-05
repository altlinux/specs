# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash 483bad4
%global tag_hash b9ee256

Name:    jnr-netdb
Version: 1.1.1
Release: alt1_2jpp7
Summary: Network services database access for java

Group:   System/Libraries
License: ASL 2.0
URL:     http://github.com/jnr/%{name}/
Source0: https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: jnr-ffi
BuildRequires: junit4
BuildRequires: jffi

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires: jpackage-utils
Requires: jnr-ffi
Source44: import.info

%description
jnr-netdb is a java interface to getservbyname(3), getservbyport(3)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
mvn-rpmbuild install javadoc:aggregate

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE README
%{_javadir}/*
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_2jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_6jpp7
- new version

