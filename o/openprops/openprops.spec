Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           openprops
Version:        0.8.5
Release:        alt1_4jpp8
Summary:        An improved java.util.Properties from OpenJDK

License:        GPLv2 with exceptions
URL:            https://github.com/zanata/%{name}
Source0:        https://github.com/zanata/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  jacoco-maven-plugin
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
Group: Development/Java
Summary:        Javadocs for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference COPYING.txt
%doc README.txt

%files -f .mfiles-javadoc javadoc
%doc --no-dereference COPYING.txt


%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_4jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 0.8.5-alt1_2jpp8
- java update

* Wed May 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_3jpp8
- fixed build with maven-javadoc-plugin 3

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_2jpp8
- new jpp release

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_9jpp8
- new version

* Tue Aug 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.6-alt1_4jpp7
- new release

