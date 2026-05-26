Name:           apache-commons-fileupload
Epoch:          1
Version:        1.6.0
Release:        alt1

Summary:        Apache Commons FileUpload is a robust, high-performance, file upload capability to your servlets and web applications
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/fileupload/
VCS:            https://github.com/apache/commons-fileupload

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
The Commons FileUpload package makes it easy to add robust, high-performance,
file upload capability to your servlets and web applications.

FileUpload parses HTTP requests which conform to RFC 1867, "Form-based File
Upload in HTML". That is, if an HTTP request is submitted using the POST method,
and with a content type of "multipart/form-data", then FileUpload can parse that
request, and make the results available in a manner easily used by the caller.

Starting with version 1.3, FileUpload handles RFC 2047 encoded header values.

%javadoc_package

%prep
%setup

%pom_remove_plugin :maven-checkstyle-plugin

%pom_remove_dep portlet-api:portlet-api
rm -r src/main/java/org/apache/commons/fileupload/portlet

%build
# Tests disabled due missing dep portlet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Sat May 16 2026 Evgeniy Serov <scala@altlinux.org> 1:1.6.0-alt1
- Updated to 1.6.0.

* Sun Jun 12 2022 Igor Vlasenko <viy@altlinux.org> 1:1.4-alt1_7jpp11
- java11 build

* Wed Jan 29 2020 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_3jpp8
- fc update

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_1jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_4jpp8
- fc29 update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_3jpp8
- java update

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.3.3-alt1_2jpp8
- new version

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.3.2-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.2-alt1_1jpp8
- new version

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_8jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_7jpp8
- java 8 mass update

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.3-alt1_4jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.2.2-alt3_11jpp7
- new release

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

