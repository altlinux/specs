Name: tomcat-taglibs-standard
Version: 1.2.5
Summary: Apache Standard Taglib
License: ASL 2.0
Url: http://tomcat.apache.org/taglibs/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(javax.servlet:jstl) = 1.2.5
Provides: mvn(javax.servlet:jstl:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-build-tools) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-build-tools:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-compat) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-compat:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-impl) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-impl:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-jstlel) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-jstlel:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-spec) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard-spec:pom:) = 1.2.5
Provides: mvn(org.apache.taglibs:taglibs-standard:pom:) = 1.2.5
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet.jsp.jstl) = 1.2.5
Provides: mvn(org.eclipse.jetty.orbit:javax.servlet.jsp.jstl:pom:) = 1.2.5
Provides: mvn(org.eclipse.jetty.orbit:org.apache.taglibs.standard.glassfish) = 1.2.5
Provides: mvn(org.eclipse.jetty.orbit:org.apache.taglibs.standard.glassfish:pom:) = 1.2.5
Provides: tomcat-taglibs-standard = 0:1.2.5-1.fc23
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: tomcat-taglibs-standard-1.2.5-1.fc23.cpio

%description
An implementation of the JSP Standard Tag Library (JSTL).

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
* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.2.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

