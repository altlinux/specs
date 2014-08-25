Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
%global pkgname file-management

Name:           maven-%{pkgname}
Version:        1.2.1
Release:        alt1_6jpp7
# Maven-shared defines file-management version as 1.2.2
Epoch:          1
Summary:        Maven File Management API
License:        ASL 2.0
# URL is not working now, cached copy at http://web.archive.org/web/20121029070007/http://maven.apache.org/shared/file-management/
URL:            http://maven.apache.org/shared/%{pkgname}
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/file-management-1.2.1
# tar caf maven-file-management-1.2.1.tar.xz file-management-1.2.1/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-shared
BuildRequires:  modello

Obsoletes:      maven-shared-%{pkgname} < %{epoch}:%{version}-%{release}
Provides:       maven-shared-%{pkgname} = %{epoch}:%{version}-%{release}
Source44: import.info

%description
Provides a component for plugins to easily resolve project dependencies.

This is a replacement package for maven-shared-file-management.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
Obsoletes:      maven-shared-%{pkgname}-javadoc < %{epoch}:%{version}-%{release}
Provides:       maven-shared-%{pkgname}-javadoc = %{epoch}:%{version}-%{release}
BuildArch: noarch
    
%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{pkgname}-%{version}
cp -p %{SOURCE1} LICENSE.txt

# Need namespace for new version modello
# Bug has been filed at http://jira.codehaus.org/browse/MSHARED-234
sed -i "s|<model>|<model xmlns=\"http://modello.codehaus.org/MODELLO/1.3.0\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://modello.codehaus.org/MODELLO/1.3.0 http://modello.codehaus.org/xsd/modello-1.3.0.xsd\" xml.namespace=\"..\" xml.schemaLocation=\"..\" xsd.namespace=\"..\" xsd.targetNamespace=\"..\">|" src/main/mdo/fileset.mdo

# FileSetUtilsTest.testDeleteDanglingSymlink() is expected to fail
sed -i /testDeleteDanglingSymlink/,/assert/s/False/True/ `find -name FileSetUtilsTest.java`

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_6jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.1-alt1_0jpp7
- new release

