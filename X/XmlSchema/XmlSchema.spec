Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           XmlSchema
Version:        1.4.7
Release:        alt1_16jpp8
Summary:        Lightweight schema object model
License:        ASL 2.0
URL:            http://ws.apache.org/commons/XmlSchema
BuildArch:      noarch

# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/XmlSchema/XmlSchema-1.4.7
# tar cJf XmlSchema-1.4.7.tar.xz XmlSchema-1.4.7
Source0:        %{name}-%{version}.tar.xz
Source1:        LICENSE-2.0.txt

# maven-site-plugin is broken by the lack of cvsjava in maven-scm. 
# cvsjava was removed when netbeans was orphaned.
Patch1:         %{name}-no-site-plugin.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(xmlunit:xmlunit)

BuildRequires:  dos2unix
Source44: import.info

Provides: ws-commons-%name = 0:%version-%release
Conflicts:  ws-commons-%name <= 0:1.4.7-alt3_7jpp7
Obsoletes:  ws-commons-%name <= 0:1.4.7-alt3_7jpp7


%description
Commons XMLSchema is a lightweight schema object model that can be 
used to manipulate or generate a schema.

%package javadoc
Group: Development/Java
Summary:      API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

# This is provided by modern Java environments
%pom_remove_dep "org.apache.ws.commons:ws-commons-java5"

# Fix line endings
cp -p %{SOURCE1} .
dos2unix LICENSE-2.0.txt README.txt RELEASE-NOTE.txt

%mvn_file :%{name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE-2.0.txt README.txt RELEASE-NOTE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_16jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_15jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_14jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_13jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_12jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.4.7-alt1_11jpp8
- java 8 mass update

