# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           apache-parent
Version:        10
Release:        alt2_7jpp7
Summary:        Parent pom file for Apache projects
Group:          Development/Java
License:        ASL 2.0
URL:            http://apache.org/
Source0:        http://svn.apache.org/repos/asf/maven/pom/tags/apache-10/pom.xml
BuildArch:      noarch

BuildRequires:  maven
BuildRequires:  jpackage-utils
BuildRequires: apache-resource-bundles apache-jar-resource-bundle
BuildRequires:  maven-remote-resources-plugin

Requires:       jpackage-utils
Requires: apache-resource-bundles apache-jar-resource-bundle
Requires:       maven-remote-resources-plugin
Source44: import.info

%description
This package contains the parent pom file for apache projects.


%prep
%setup -n %{name}-%{version} -Tc

# This simplifies work with child projects that can use generics
cp %{SOURCE0} .
sed -i 's:<source>1.4</source>:<source>1.5</source>:' pom.xml
sed -i 's:<target>1.4</target>:<target>1.5</target>:' pom.xml


%build


%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml \
        $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 10-alt2_7jpp7
- rebuild with new apache-resource-bundles

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 10-alt1_7jpp7
- fc update

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 10-alt1_5jpp7
- new release

