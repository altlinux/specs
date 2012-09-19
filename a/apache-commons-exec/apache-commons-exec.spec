Epoch: 0
BuildRequires: /bin/ping
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name exec
%global short_name commons-%{base_name}

Name:           apache-commons-exec
Version:        1.1
Release:        alt1_6jpp7
Summary:        Java library to reliably execute external processes from within the JVM

Group:          Development/Java
License:        ASL 2.0
URL:            http://commons.apache.org/exec/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  iputils
BuildRequires:  maven-surefire-maven-plugin
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-idea-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-release-plugin
Requires:       jpackage-utils
BuildArch:      noarch
Source44: import.info

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{?epoch:%epoch:}%{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{short_name}-%{version}-src

# Shell scripts used for unit tests must be executable (see
# http://commons.apache.org/exec/faq.html#environment-testing)
chmod a+x src/test/scripts/*.sh


%build
mvn-rpmbuild -Dmaven.test.skip=true install javadoc:javadoc


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_mavenpomdir}
cp -p pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar


%files
%doc LICENSE.txt NOTICE.txt STATUS
%{_mavenpomdir}/*
%{_javadir}/*.jar
%{_mavendepmapfragdir}/*

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Wed Sep 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1-alt1_6jpp7
- new version

* Mon Jan 10 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt2_6jpp6
- excluded repolib from main package

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_6jpp6
- renamed; new jpp version

