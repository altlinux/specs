# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash 47d9618
%global tag_hash a69c89c

Name:           jnr-posix
Version:        2.4.0
Release:        alt1_1jpp7
Summary:        Java Posix layer
Group:          Development/Java
License:        CPL or GPLv2+ or LGPLv2+
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz

BuildRequires:  jpackage-utils
BuildRequires:  jnr-constants
BuildRequires:  jnr-ffi
BuildRequires:  jffi
BuildRequires:  objectweb-asm4

BuildRequires:  maven-local
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils
Requires:       jnr-constants
Requires:       jnr-ffi
Requires:       jffi
Requires:       objectweb-asm4

BuildArch:      noarch
Source44: import.info

%description
jnr-posix is a lightweight cross-platform POSIX emulation layer for Java, 
written in Java and is part of the JNR project 

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n jnr-%{name}-%{tag_hash}

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

%build
# TODO: some tests still fail
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
%doc LICENSE.txt README.txt
%{_javadir}/%{name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/*

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1_1jpp7
- new version

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_3jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.8-alt1_2jpp7
- new version

