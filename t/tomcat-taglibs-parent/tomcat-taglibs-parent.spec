# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           tomcat-taglibs-parent
Version:        3
Release:        alt1_3jpp8
Summary:        Apache Taglibs Parent

Group:          Development/Java
License:        ASL 2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        http://svn.apache.org/repos/asf/tomcat/taglibs/taglibs-parent/tags/taglibs-parent-3/pom.xml
BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Source44: import.info

%description
Apache Taglibs Parent pom used for building purposes.

%prep
%setup -q -c -T
cp -p %{SOURCE0} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_mavenpomdir}/%{name}

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 3-alt1_3jpp8
- new version

