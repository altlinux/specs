Name: jboss-jsf-2.2-api
Version: 2.2.0
Summary: JavaServer Faces 2.2 API
License: (CDDL or GPLv2 with exceptions) and ASL 2.0
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-jsf-2.2-api = 2.2.0-4.fc21
Provides: mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec) = 2.2.0
Provides: mvn(org.jboss.spec.javax.faces:jboss-jsf-api_2.2_spec:pom:) = 2.2.0
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.sun:tools)
Requires: mvn(javax.enterprise:cdi-api)
Requires: mvn(javax.inject:javax.inject)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: jboss-jsf-2.2-api-2.2.0-4.fc21.cpio

%description
This package contains JSR-344: JavaServer Faces 2.2 API.

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
* Sat Feb 06 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

