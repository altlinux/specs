# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global oname base64
Name:          java-base64
Version:       2.3.8
Release:       alt1_2jpp7
Summary:       Java class for encoding and decoding Base64 notation
Group:         Development/Java
# pom file license comment
# I have released this software into the Public Domain. That
# means you can do whatever you want with it. Really. You don't
# have to match it up with any other open source license -
# just use it. You can rename the files, move the Java packages,
# whatever you want. If your lawyers say you have to have a
# license, contact me, and I'll make a special release to you
# under whatever reasonable license you desire: MIT, BSD, GPL,
# whatever.
License:       Public Domain
URL:           http://iharder.net/base64/
Source0:       https://github.com/omalley/base64/archive/release-%{version}.tar.gz


# test deps
BuildRequires: junit

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit4

Provides:      %{oname} = %{version}-%{release}

BuildArch:     noarch
Source44: import.info

%description
Base64 is a Public Domain Java class for encoding and
decoding Base64 notation. There are one-liner convenience
methods as well as Input and Output Streams.

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{oname}-release-%{version}

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-compiler-plugin']" "<version>2.5.1</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-source-plugin']" "<version>2.1.2</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" "<version>2.9</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-release-plugin']" "<version>2.2.1</version>"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-scm-plugin']" "<version>1.7</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-project-info-reports-plugin']" "<version>2.4</version>"
%pom_xpath_inject "pom:reporting/pom:plugins/pom:plugin[pom:artifactId ='maven-javadoc-plugin']" "<version>2.9</version>"

sed -i "s|<version>2.3.9-SNAPSHOT</version>|<version>%{version}</version>|" pom.xml

%build

mvn-rpmbuild package javadoc:aggregate

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 target/%{oname}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

(
 cd %{buildroot}%{_javadir}
 ln -sf %{name}.jar %{oname}.jar
)

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

(
 cd %{buildroot}%{_javadocdir}
 ln -sf %{name} %{oname}
)

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{oname}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{oname}

%changelog
* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.8-alt1_2jpp7
- new release

