Epoch: 1
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_without  portlet

Name:           apache-commons-fileupload
Version:        1.3.3
Release:        alt1_3jpp8
Summary:        API to work with HTML file upload
License:        ASL 2.0
URL:            http://commons.apache.org/fileupload/
BuildArch:      noarch

Source0:        http://www.apache.org/dist/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%if %{with portlet}
BuildRequires:  mvn(javax.portlet:portlet-api)
%endif
Source44: import.info
%define short_name commons-fileupload
Provides: %{short_name} = %{version}
Conflicts:	jakarta-%{short_name} < 1:%version

%description
The javax.servlet package lacks support for RFC-1867, HTML file
upload.  This package provides a simple to use API for working with
such data.  The scope of this package is to create a package of Java
utility classes to read multipart/form-data within a
javax.servlet.http.HttpServletRequest.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n commons-fileupload-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

%if %{with portlet}
# fix gId
sed -i "s|<groupId>portlet-api</groupId>|<groupId>javax.portlet</groupId>|" pom.xml
%else
%pom_remove_dep portlet-api:portlet-api
%pom_xpath_remove pom:properties/pom:commons.osgi.import
%pom_xpath_remove pom:properties/pom:commons.osgi.dynamicImport
rm -r src/main/java/org/apache/commons/fileupload/portlet
%endif

# -----------------------------------------------------------------------------

%mvn_file ":{*}" %{name} @1
%mvn_alias : org.apache.commons:

%build
# fix build with generics support
# tests fail to compile because they use an obsolete version of servlet API (2.4)
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt NOTICE.txt

# -----------------------------------------------------------------------------

%changelog
* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.3.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_8jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_7jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.3-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt3_11jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt3_7jpp7
- fixed BR deps

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt2_7jpp7
- proper Obsoletes on jakarta-* (closes: 27808)

* Sat Sep 08 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt1_7jpp7
- new version

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt4_7jpp6
- fixed build

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt3_7jpp6
- bumped release to properly obsolete jakarta-commons-fileupload
- closes: #27363

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_7jpp6
- new version

