Name: jboss-jsp-2.2-api
Version: 1.0.1
Summary: JavaServer(TM) Pages 2.2 API
License: CDDL or GPLv2 with exceptions
Url: http://www.jboss.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-jsp-2.2-api = 1.0.1-10.fc22
Provides: mvn(javax.servlet.jsp:jsp-api) = 1.0.1.Final
Provides: mvn(javax.servlet.jsp:jsp-api:pom:) = 1.0.1.Final
Provides: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec) = 1.0.1.Final
Provides: mvn(org.jboss.spec.javax.servlet.jsp:jboss-jsp-api_2.2_spec:pom:) = 1.0.1.Final
Requires: java-headless
Requires: jboss-el-2.2-api
Requires: jboss-servlet-3.0-api
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: jboss-jsp-2.2-api-1.0.1-10.fc22.cpio

%description
JSR-000245: JavaServer(TM) Pages 2.2

# sometimes commpress gets crazy (see maven-scm-javadoc for details)
%set_compress_method none
%prep
cpio -idmu --quiet --no-absolute-filenames < %{SOURCE0}

%build
cpio --list < %{SOURCE0} | sed -e 's,^\.,,' > %name-list

%install
mkdir -p $RPM_BUILD_ROOT
for i in usr var etc; do
[ -d $i ] && mv $i $RPM_BUILD_ROOT/
done


%files -f %name-list

%changelog
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3jpp7
- fixed build

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new version

