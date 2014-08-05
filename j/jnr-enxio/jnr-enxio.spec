# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global commit_hash d320a2c
%global tag_hash 8dc2020

Name:           jnr-enxio
Version:        0.3
Release:        alt1_3jpp7
Summary:        Unix sockets for Java
Group:          Development/Java
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        ASL 2.0 and LGPLv3
URL:            http://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/tarball/%{version}/jnr-%{name}-%{version}-0-g%{commit_hash}.tar.gz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  jnr-constants
BuildRequires:  jnr-ffi

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4

Requires:       jpackage-utils
Requires:       jnr-constants
Requires:       jnr-ffi
Source44: import.info

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

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
%doc LICENSE
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%{_javadir}/%{name}.jar

%files javadoc
%doc LICENSE
%{_javadocdir}/%{name}

%changelog
* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_3jpp7
- new version

