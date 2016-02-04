Name: jboss-jstl-1.2-api
Version: 1.0.3
Summary: JSP Standard Template Library 1.2 API
License: CDDL or GPLv2 with exceptions
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-jstl-1.2-api = 1.0.3-10.fc22
Provides: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec) = 1.0.3.Final
Provides: mvn(org.jboss.spec.javax.servlet.jstl:jboss-jstl-api_1.2_spec:pom:) = 1.0.3.Final
Requires: java-headless
Requires: jboss-el-2.2-api
Requires: jboss-jsp-2.2-api
Requires: jboss-servlet-3.0-api
Requires: jpackage-utils
Requires: jpackage-utils
Requires: xalan-j2

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: jboss-jstl-1.2-api-1.0.3-10.fc22.cpio

%description
Java Server Pages Standard Template Library 1.2 API.

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
* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_6jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt2_4jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_4jpp7
- new version

