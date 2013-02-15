Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: maven-antrun-plugin
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name math
%global short_name commons-%{base_name}3

Name:             apache-commons-math
Version:          3.1.1
Release:          alt1_1jpp7
Summary:          Java library of lightweight mathematics and statistics components

Group:            Development/Java
License:          ASL 1.1 and ASL 2.0 and BSD
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-surefire-provider-junit4
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
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %%{name}.


%prep
%setup -q -n %{short_name}-%{version}-src


%build
mvn-rpmbuild install javadoc:aggregate


%install
install -Dpm 0644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
ln -s %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{short_name}.jar

install -dm 0755 $RPM_BUILD_ROOT%{_mavenpomdir}/
install -pm 0644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -dm 0755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/api*/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/


%files
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*


%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}


%changelog
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

