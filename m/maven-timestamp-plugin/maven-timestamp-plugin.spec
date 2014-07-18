BuildRequires: maven-plugin-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-timestamp-plugin
Version:        1.1
Release:        alt3_3jpp7
Summary:        Provides formatted timestamps for maven builds

Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/maven-timestamp-plugin
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://maven-timestamp-plugin.googlecode.com/svn/tags/maven-timestamp-plugin-1.1 maven-timestamp-plugin
# tar caf maven-timestamp-plugin-1.1.tar.xz maven-timestamp-plugin 
Source0:        maven-timestamp-plugin-1.1.tar.xz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-timestamp-plugin

Requires:       jpackage-utils
Source44: import.info

%description
There are a few ways to get a timestamp in your maven build. Unfortunately 
most of them make you jump through giant hoops. This maven plugin makes it 
as simple as 1-2-3 to create a timestamp at your disposal.
Also, it enables you to use the syntax of SimpleDateFormat to form custom 
formatted dates. 


%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n %{name}
cat > README << EOT
%{name}-%{version}

%{description}
EOT


%build
mvn-rpmbuild install javadoc:javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}

# jar
install -Dp -m 644 target/%{name}-%{version}-SNAPSHOT.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml  \
  $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc README
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3_3jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3jpp7
- full version

* Thu Aug 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

