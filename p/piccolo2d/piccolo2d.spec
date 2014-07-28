# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           piccolo2d
Version:        1.3.1
Release:        alt2_2jpp7
Summary:        Structured 2D graphics toolkit

Group:          Development/Java
License:        BSD
URL:            http://code.google.com/p/piccolo2d/
Source0:        http://piccolo2d.googlecode.com/files/%{name}-%{version}-src.tar.gz
Source2:        %{name}-settings.xml
BuildRequires:  maven-local
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-site-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-doxia-sitetools
BuildRequires:  eclipse-swt

Requires: eclipse-swt

BuildArch: noarch
Source44: import.info

%description
A revolutionary way to create robust, full-featured graphical
applications in Java with striking visual effects such
as zooming, animation and multiple representations.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n piccolo2d-%{version}-src
sed -i -e "s|\[3\.3\.0-v3346\,)|3\.3\.0-v3346|g" swt/pom.xml
mkdir -p .m2/org/eclipse/swt/gtk/linux/x86/3.3.0-v3346/
mkdir -p .m2/org/eclipse/swt/gtk/linux/x86_64/3.3.0-v3346/
ln -s %{_libdir}/java/swt.jar .m2/org/eclipse/swt/gtk/linux/x86/3.3.0-v3346/x86-3.3.0-v3346.jar  
ln -s %{_libdir}/java/swt.jar .m2/org/eclipse/swt/gtk/linux/x86_64/3.3.0-v3346/x86_64-3.3.0-v3346.jar 

%build
mvn-rpmbuild -e \
        -Dmaven.test.skip=true \
        install javadoc:aggregate

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 core/target/*.jar %{buildroot}%{_javadir}/%{name}/%{name}-core.jar
install -m 644 extras/target/*.jar %{buildroot}%{_javadir}/%{name}/%{name}-extras.jar
install -m 644 swt/target/*.jar %{buildroot}%{_javadir}/%{name}/%{name}-swt.jar


# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 parent/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-parent.pom
install -pm 644 core/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-core.pom
install -pm 644 extras/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-extras.pom
install -pm 644 swt/pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP.%{name}-%{name}-swt.pom

%add_maven_depmap JPP.%{name}-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-core.pom %{name}/%{name}-core.jar
%add_maven_depmap JPP.%{name}-%{name}-extras.pom %{name}/%{name}-extras.jar
%add_maven_depmap JPP.%{name}-%{name}-swt.pom %{name}/%{name}-swt.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/api*/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%doc license-piccolo.txt 

%files javadoc
%{_javadocdir}/%{name}
%doc license-piccolo.txt 

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_2jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt2_1jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1_1jpp7
- new release

* Tue Feb 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_0.svn702.4jpp6
- fixed build

* Sat Oct 30 2010 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_0.svn702.4jpp6
- new version

