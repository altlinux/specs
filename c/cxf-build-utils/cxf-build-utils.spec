# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:             cxf-build-utils
Version:          2.4.1
Release:          alt4_4jpp7
Summary:          Apache CXF Build Utils
Group:            Development/Java
License:          ASL 2.0
URL:              http://cxf.apache.org/build-utils.html

# svn export http://svn.apache.org/repos/asf/cxf/build-utils/tags/cxf-build-utils-2.4.1/ cxf-build-utils-2.4.1
# tar cafJ cxf-build-utils-2.4.1.tar.xz cxf-build-utils-2.4.1
Source0:          %{name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-shade-plugin
BuildRequires:    glassfish-fastinfoset
BuildRequires:    maven-surefire-provider-junit4
BuildRequires:    pmd

Requires:         jpackage-utils
Requires:         glassfish-fastinfoset
Requires:         pmd
Source44: import.info

%description
The Apache CXF Build Utils contains common utilities and configuration files
that are used by multiple versions of the CXF builds.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Development/Java
Requires:         jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

sed -i -e '/<version>2.0.7<.version>/d' buildtools/pom.xml

%build
mvn-rpmbuild \
  -Dproject.build.sourceEncoding=UTF-8 \
  install javadoc:aggregate

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}

for module in buildtools xml2fastinfoset-plugin; do
  pushd $module
  install -pm 644 target/cxf-$module-%{version}.jar %{buildroot}%{_javadir}/%{name}/cxf-$module.jar
  install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}-cxf-$module.pom
  %add_maven_depmap JPP.%{name}-cxf-$module.pom %{name}/cxf-$module.jar
  popd
done

install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom
%add_maven_depmap JPP.%{name}.pom

# javadoc
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}

%files
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Sun Jul 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt4_4jpp7
- fixed build

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt3_4jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_4jpp7
- new version

