# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
BuildRequires: unzip
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
%define fedora 25
Name:           openprops
Version:        0.7.1
Release:        alt1_1jpp8
Summary:        An improved java.util.Properties from OpenJDK

Group:          Development/Other
License:        GPLv2 with exceptions
URL:            https://github.com/zanata/%{name}
Source0:        https://github.com/zanata/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-release-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  junit

Requires:       jpackage-utils
Source44: import.info

%description
OpenProps is a tiny Java library which reads and writes .properties files 
using the same code as java.util.Properties from the OpenJDK, but enhanced so
that it preserves the order of entries within the file, and it also preserves
comments in the file.  
This means that a Properties editor or a file converter written to use 
OpenProps won't have to lose comments or mess up the order of entries. 

By using OpenJDK code, OpenProps should handle all the old corner-cases in 
exactly the same way Java does.  The handling of whitespace and comments is
tested by a number of JUnit tests.  But please let me know if you find a bug!

Note the following differences from java.util.Properties:

1. preserves comments and the order of entries in the file
2. storeToXml doesn't use the Sun DTD (or any DTD) because it adds attributes 
   for comments.
3. equals() and hashCode() won't work the same way as with java.util.Properties,
   because they are no longer inherited from Hashtable.  
   All you get is identity equality/hashcode.

Also note that any header comment in the .properties file will be interpreted as
a comment attached to the first message.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version} 
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

%if 0%{?fedora} >= 21
%pom_xpath_inject "pom:build/pom:plugins" "<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-javadoc-plugin</artifactId><version>2.9.1</version><configuration><additionalparam>-Xdoclint:none</additionalparam></configuration><executions><execution><id>attach-javadocs</id><goals><goal>jar</goal></goals></execution></executions></plugin>" 
%else
%pom_xpath_inject "pom:build/pom:plugins" "<plugin><groupId>org.apache.maven.plugins</groupId><artifactId>maven-javadoc-plugin</artifactId><version>2.9.1</version><executions><execution><id>attach-javadocs</id><goals><goal>jar</goal></goals></execution></executions></plugin>"
%endif

 
%build
%mvn_build

%install
%mvn_install
# multiple -f flags in %files: merging -f .mfiles-javadoc into -f .mfiles
cat .mfiles-javadoc >> .mfiles

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.txt COPYING.txt

%doc COPYING.txt


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_9jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4jpp7
- new release

