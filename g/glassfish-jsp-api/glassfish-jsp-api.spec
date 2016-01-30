Name: glassfish-jsp-api
Version: 2.3.2
Summary: Glassfish J2EE JSP API specification
License: (CDDL or GPLv2 with exceptions) and ASL 2.0
Url: http://java.net/jira/browse/JSP
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: glassfish-jsp-api = 2.3.2-0.3.b01.fc23
Provides: mvn(javax.servlet.jsp:javax.servlet.jsp-api) = 2.3.2.b01
Provides: mvn(javax.servlet.jsp:javax.servlet.jsp-api:pom:) = 2.3.2.b01
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(javax.el:javax.el-api)
Requires: mvn(javax.servlet:javax.servlet-api)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: glassfish-jsp-api-2.3.2-0.3.b01.fc23.cpio

%description
This project provides a container independent specification of JSP
2.2. Note that this package doesn't contain implementation of this
specification. See glassfish-jsp for one of implementations

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
ln -s glassfish-jsp-api/javax.servlet.jsp-api.jar %buildroot/usr/share/java/glassfish-jsp-api.jar

%files -f %name-list
/usr/share/java/glassfish-jsp-api.jar

%changelog
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_6jpp7
- new release

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt2_4jpp7
- fixed maven1 dependency

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4jpp7
- fc update

* Wed Aug 15 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2jpp7
- full version

