# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash 1dead92
%global tag_hash 2a7fb9b

Name:           jnr-x86asm
Version:        1.0.2
Release:        alt1_1jpp7
Summary:        Pure-java port of asmjit

Group:          Development/Java
License:        MIT
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils
Source44: import.info

%description
Pure-java port of asmjit (http://code.google.com/p/asmjit/)

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

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
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_5jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_4jpp7
- new version

