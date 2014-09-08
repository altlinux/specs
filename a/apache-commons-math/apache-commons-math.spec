Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global short_name commons-math3

Name:             apache-commons-math
Version:          3.2
Release:          alt2_3jpp7
Summary:          Java library of lightweight mathematics and statistics components
Group:            Development/Java
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/math/
Source0:          http://www.apache.org/dist/commons/math/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
Requires:         jpackage-utils
BuildArch:        noarch
Source44: import.info

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "org.apache.commons:%{short_name}" "%{short_name}:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_3jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt2_1jpp7
- rebuild with maven-local

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.2-alt1_1jpp7
- new version

* Wed Feb 13 2013 Igor Vlasenko <viy@altlinux.ru> 0:3.1.1-alt1_1jpp7
- fc update

* Thu Sep 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt2_2jpp7
- added jpp compat symlink

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.0-alt1_2jpp7
- new version

* Tue Sep 18 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt4_5jpp6
- build without mojo-* plugins

* Mon Mar 19 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt3_5jpp6
- fixed build with maven3

* Wed Feb 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt2_5jpp6
- fixed jakarta symlink

* Tue Feb 01 2011 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt1_5jpp6
- build with maven2-plugin-shade

