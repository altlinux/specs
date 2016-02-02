Epoch: 1
Group: System/Libraries
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           ws-commons-util
Version:        1.0.1
Release:        alt1_32jpp8
Summary:        Common utilities from the Apache Web Services Project

License:        ASL 2.0
URL:            http://archive.apache.org/dist/ws/commons/util/
Source0:        http://archive.apache.org/dist/ws/commons/util/sources/ws-commons-util-1.0.1-src.tar.gz
Patch0:         %{name}-addosgimanifest.patch
BuildArch:      noarch

BuildRequires:  maven-local
Source44: import.info

%description
This is version 1.0.1 of the common utilities from the Apache Web
Services Project.

%package        javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description    javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%patch0

# Remove maven-eclipse-plugin from build dependencies to simplify the
# dependency chain.
%pom_remove_plugin :maven-eclipse-plugin

%mvn_file : %{name}
%mvn_alias org.apache.ws.commons:ws-commons-util org.apache.ws.commons.util:ws-commons-util

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_32jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_27jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_26jpp7
- new release

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.0.1-alt1_23jpp7
- fc update

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt3_3jpp6
- dropped velocity14

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_3jpp6
- new jpp release; build with velocity 14

* Tue Dec 14 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt2_2jpp5
- build with velocity 15

* Mon Jan 12 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0.2-alt1_2jpp5
- added OSGi provides

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.1-alt1_1jpp1.7
- converted from JPackage by jppimport script

