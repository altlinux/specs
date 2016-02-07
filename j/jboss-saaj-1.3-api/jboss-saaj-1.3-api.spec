Name: jboss-saaj-1.3-api
Version: 1.0.2
Summary: SOAP with Attachments API for Java 1.3
License: CDDL or GPLv2 with exceptions
Url: http://www.jboss.org
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jboss-saaj-1.3-api = 1.0.2-9.fc22
Provides: mvn(org.jboss.spec.javax.xml.soap:jboss-saaj-api_1.3_spec) = 1.0.2.Final
Provides: mvn(org.jboss.spec.javax.xml.soap:jboss-saaj-api_1.3_spec:pom:) = 1.0.2.Final
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt3jpp
Source: jboss-saaj-1.3-api-1.0.2-9.fc22.cpio

%description
The SOAP with Attachments API for Java Version 1.3 classes.

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
* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_6jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_5jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_3jpp7
- new version

