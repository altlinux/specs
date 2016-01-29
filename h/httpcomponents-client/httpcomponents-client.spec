Name: httpcomponents-client
Version: 4.5
Summary: HTTP agent implementation based on httpcomponents HttpCore
License: ASL 2.0
Url: http://hc.apache.org/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: httpcomponents-client = 4.5-2.fc23
Provides: mvn(org.apache.httpcomponents:httpclient) = 4.5
Provides: mvn(org.apache.httpcomponents:httpclient:pom:) = 4.5
Provides: mvn(org.apache.httpcomponents:httpcomponents-client:pom:) = 4.5
Provides: mvn(org.apache.httpcomponents:httpmime) = 4.5
Provides: mvn(org.apache.httpcomponents:httpmime:pom:) = 4.5
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-codec:commons-codec)
Requires: mvn(commons-logging:commons-logging)
Requires: mvn(org.apache.httpcomponents:httpcore)
Requires: publicsuffix-list

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: httpcomponents-client-4.5-2.fc23.cpio

%description
HttpClient is a HTTP/1.1 compliant HTTP agent implementation based on
httpcomponents HttpCore. It also provides reusable components for
client-side authentication, HTTP state management, and HTTP connection
management. HttpComponents Client is a successor of and replacement
for Commons HttpClient 3.x. Users of Commons HttpClient are strongly
encouraged to upgrade.

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
* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 4.5-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_3jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.5-alt1_1jpp7
- new version

* Thu Aug 21 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt3_3jpp7
- added maven-local BR:

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2_3jpp7
- NMU rebuild to move poms and fragments

* Sun Sep 09 2012 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1_3jpp7
- new version

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1_1jpp7
- full version

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

