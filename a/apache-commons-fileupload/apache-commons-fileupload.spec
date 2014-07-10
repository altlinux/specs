Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       fileupload
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          1.2.2
Release:          alt3_7jpp7
Summary:          This package provides an api to work with html file upload
License:          ASL 2.0
Group:            Development/Java
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

Patch1:           %{name}-portlet20.patch

BuildRequires:    junit >= 0:3.8.1
BuildRequires:    servlet25
BuildRequires:    apache-commons-io
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-assembly-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-doxia-sitetools
BuildRequires:    maven-idea-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-plugin-bundle
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    portlet-2.0-api

Requires:         jpackage-utils
Requires:         apache-commons-io
Requires:         portlet-2.0-api

Provides:         jakarta-%{short_name} = 1:%{version}-%{release}
Obsoletes:        jakarta-%{short_name} < 1:1.2.2
Source44: import.info
Provides: %{short_name} = %{version}
Conflicts:	jakarta-%{short_name} < 1:%version

%description
The javax.servlet package lacks support for rfc 1867, html file
upload.  This package provides a simple to use api for working with
such data.  The scope of this package is to create a package of Java
utility classes to read multipart/form-data within a
javax.servlet.http.HttpServletRequest

%package javadoc
Summary:          API documentation for %{name}
Group:            Development/Java
Requires:         jpackage-utils

Obsoletes:        jakarta-%{short_name}-javadoc < 1:1.2.1-2
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

# -----------------------------------------------------------------------------

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

%patch1 -p1
# fix gId
sed -i "s|<groupId>portlet-api</groupId>|<groupId>javax.portlet</groupId>|" pom.xml

# -----------------------------------------------------------------------------

%build
# fix build with generics support
mvn-rpmbuild -Dmaven.compile.source=1.5 -Dmaven.compile.target=1.5 install javadoc:javadoc
# -----------------------------------------------------------------------------

%install
# jars
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
pushd $RPM_BUILD_ROOT%{_javadir}
    ln -sf %{name}.jar %{short_name}.jar
popd # come back from javadir

# javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

# pom
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{short_name}.pom
%add_maven_depmap JPP-%{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}"

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :


%files
%doc LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{short_name}.jar
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{short_name}.pom

%files javadoc
%doc LICENSE.txt NOTICE.txt
%doc %{_javadocdir}/%{name}

# -----------------------------------------------------------------------------

%changelog
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

