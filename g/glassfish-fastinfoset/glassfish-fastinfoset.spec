# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
BuildRequires: maven
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name: glassfish-fastinfoset
Version: 1.2.12
Release: alt5_7jpp7
Summary: Fast Infoset
Group: Development/Java
License: ASL 2.0
URL: https://fi.dev.java.net

# svn export https://svn.java.net/svn/fi~svn/tags/1_2_12/ glassfish-fastinfoset-1.2.12
# find glassfish-fastinfoset-1.2.12/ -name '*.class' -delete
# find glassfish-fastinfoset-1.2.12/ -name '*.jar' -delete
# rm -rf glassfish-fastinfoset-1.2.12/roundtrip-tests
# tar czf glassfish-fastinfoset-1.2.12-src-svn.tar.gz glassfish-fastinfoset-1.2.12
Source0: %{name}-%{version}-src-svn.tar.gz

# Replace javax.xml.bind jsr173_api with stax (bea-)stax-api:
Patch0: %{name}-%{version}-pom.patch

BuildRequires: jpackage-utils
BuildRequires: bea-stax-api
BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-jxr
BuildRequires: maven-plugin-tools-api
BuildRequires: maven-project-info-reports-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-source-plugin
BuildRequires: xsom
BuildRequires: maven-surefire-provider-junit4

Requires: bea-stax-api
Requires: jpackage-utils
Requires: xsom

BuildArch: noarch
Source44: import.info


%package javadoc
Group: Development/Java
Summary: Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch


%description
Fast Infoset specifies a standardized binary encoding for the XML Information
Set. An XML infoset (such as a DOM tree, StAX events or SAX events in
programmatic representations) may be serialized to an XML 1.x document or, as
specified by the Fast Infoset standard, may be serialized to a fast infoset
document.  Fast infoset documents are generally smaller in size and faster to
parse and serialize than equivalent XML documents.


%description javadoc
This package contains javadoc for %{name}.


%prep
%setup -q
%patch0 -p1


%build
mvn-rpmbuild install javadoc:aggregate


%install

# Jar files:
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 fastinfoset/target/FastInfoset-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/FastInfoset.jar

# POM files:
install -d -m 755 %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}-project.pom
cp -p fastinfoset/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

# Javadoc files.
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -rp target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/.

# Dependencies map:
%add_maven_depmap JPP-%{name}-project.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

install -d $RPM_BUILD_ROOT/%_altdir; cat >$RPM_BUILD_ROOT/%_altdir/FastInfoset_glassfish-fastinfoset<<EOF
%{_javadir}/FastInfoset.jar	%{_javadir}/%name.jar	300
EOF



%files
%{_javadir}/*
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*

%_altdir/FastInfoset_glassfish-fastinfoset
%exclude %{_javadir}*/FastInfoset.jar



%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt5_7jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt5_4jpp7
- NMU rebuild to move poms and fragments

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt4_4jpp7
- bugfix in alternative

* Wed Sep 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt3_4jpp7
- rised priority of alternative

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt2_4jpp7
- shared FastInfoset.jar symlink as alternative

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.12-alt1_4jpp7
- new version

