Name: httpunit
Version: 1.7
Summary: Automated web site testing toolkit
License: MIT and ASL 2.0
Url: http://httpunit.sourceforge.net/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: httpunit = 0:1.7-18.fc23
Provides: mvn(httpunit:httpunit) = 1.7
Provides: mvn(httpunit:httpunit:pom:) = 1.7
Requires: java-headless
Requires: jpackage-utils
Requires: junit
Requires: nekohtml
Requires: rhino
Requires: tomcat-servlet-3.1-api

BuildArch: noarch
Group: Development/Java
Release: alt4jpp
Source: httpunit-1.7-18.fc23.cpio

%description
HttpUnit emulates the relevant portions of browser behavior, including form
submission, JavaScript, basic http authentication, cookies and automatic page
redirection, and allows Java test code to examine returned pages either as
text, an XML DOM, or containers of forms, tables, and links.
A companion framework, ServletUnit is included in the package.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt4jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_11jpp7
- update

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt3_4jpp6
- fixed build

* Tue Mar 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt2_4jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_4jpp6
- new jpp relase

* Tue Nov 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.7-alt1_1jpp5
- new version

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.6.2-alt1_1jpp1.7
- converted from JPackage by jppimport script

