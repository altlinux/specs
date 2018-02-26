BuildRequires:  oss-parent
BuildRequires: /proc
BuildRequires: jpackage-compat

%global short_name   jcommander
%global group_id     com.beust

Name:             beust-%{short_name}
Version:          1.17
Release:          alt1_4jpp7
Summary:          Java framework for parsing command line parameters
License:          ASL 2.0
Group:            Development/Java
URL:              http://jcommander.org/
# git clone git://github.com/cbeust/jcommander.git
# cd jcommander
# git archive --prefix="beust-jcommander-1.17/" --format=tar jcommander-1.17 | xz > beust-jcommander-1.17.tar.xz
Source0:          %{name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-enforcer-plugin
BuildRequires:    testng

Requires:         jpackage-utils
Source44: import.info

%description
JCommander is a very small Java framework
that makes it trivial to parse command line
parameters (with annotations).

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

# removing spurious-executable-perm
chmod -x license.txt

%build
mvn-rpmbuild install javadoc:aggregate

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%doc license.txt README.markdown
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc license.txt
%doc %{_javadocdir}/%{name}

%changelog
* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_4jpp7
- new version

* Sat Apr 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

