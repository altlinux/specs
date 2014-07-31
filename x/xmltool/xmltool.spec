Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           xmltool
Version:        3.3
Release:        alt3_8jpp7
Summary:        Tool to manage XML documents through a Fluent Interface

Group:          Development/Java
License:        ASL 2.0
URL:            http://code.google.com/p/xmltool
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://xmltool.googlecode.com/svn/tags/xmltool-3.3 xmltool
# tar cfJ xmltool-3.3.tar.xz xmltool
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-surefire-provider-testng
BuildRequires: apache-resource-bundles apache-jar-resource-bundle

Requires:       jpackage-utils
Source44: import.info

%description
XMLTool is a very simple Java library to be able to do all sorts of common 
operations with an XML document. Java developers often end up writing the same 
code for processing XML, transforming, etc. This easy to use class puts it all 
together, using the Fluent Interface pattern to facilitate XML manipulations. 

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

# Fix end-of-line encoding
sed -i 's/\r//' LICENSE.txt


%build
# Remove dep on maven-wagon and maven-license plugins
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin com.google.code.maven-license-plugin:maven-license-plugin

# Disable tests because they require an internet connection to run!
mvn-rpmbuild \
  -Dmaven.test.skip=true \
  install javadoc:javadoc


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
install -Dp -m 644 target/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp target/site/apidocs/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc LICENSE.txt
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*


%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_8jpp7
- new release

* Sat Jul 12 2014 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt3_5jpp7
- rebuild with new apache-resource-bundles

* Tue Oct 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt2_5jpp7
- new fc release

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt2_4jpp7
- applied repocop patches

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_4jpp7
- dropped obsoletes on mojo-maven2-plugin-cobertura

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt1_2jpp6
- new jpp release

* Sat Sep 03 2011 Igor Vlasenko <viy@altlinux.ru> 0:3.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

