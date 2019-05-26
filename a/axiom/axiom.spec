Group: Sciences/Mathematics
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           axiom
Version:        1.2.14
Release:        alt1_4jpp8
Epoch:          2
Summary:        Axis Object Model
License:        ASL 2.0
Url:            http://ws.apache.org/commons/axiom/
Source0:        http://archive.apache.org/dist/ws/axiom/%{version}/axiom-%{version}-source-release.zip

Patch0:         port-to-mime4j-0.8.1.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(javax.mail:mail)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.sf.saxon:saxon)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.james:apache-mime4j-core) >= 0.8.1
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.codehaus.woodstox:woodstox-core-asl)
BuildRequires:  mvn(org.jvnet.jaxb2.maven2:maven-jaxb2-plugin)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xmlunit:xmlunit)

Requires:       mvn(org.apache.james:apache-mime4j-core) >= 0.8.1

BuildArch:      noarch
Source44: import.info

Provides: ws-commons-%name = 0:%version-%release
Conflicts:  ws-commons-%name <= 0:1.2.12-alt2_7jpp7
Obsoletes:  ws-commons-%name <= 0:1.2.12-alt2_7jpp7


%description
AXIOM stands for AXis Object Model (also known as OM - Object Model)
and refers to the XML info-set model that was initially developed for
Apache Axis2.

%package javadoc
Group: Sciences/Mathematics
Summary:        API Documentation for %{name}
BuildArch: noarch

%description javadoc
%{summary}.

%prep
%setup -q
%patch0

# Disable plugins not needed for RPM builds
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :gmaven-plugin

# Don't build and attach manuals due to unavailable plugin "com.agilejava.docbkx:docbkx-maven-plugin"
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :build-helper-maven-plugin

# No need to build dist assembly for RPM builds
%pom_remove_plugin :maven-assembly-plugin

# Change to modern OSGi dependencies
%pom_change_dep -r org.osgi:org.osgi.core org.osgi:osgi.core
%pom_change_dep -r org.osgi:org.osgi.compendium org.osgi:osgi.cmpn

# Mordern JREs supply these APIs
%pom_remove_dep :geronimo-activation_1.1_spec modules/axiom-{dom,parent,api,testutils,impl}
%pom_remove_dep :geronimo-stax-api_1.0_spec modules/axiom-{tests,parent,api,testutils,impl}

# Fix dep on mail API and saxon
%pom_change_dep :geronimo-javamail_1.4_spec javax.mail:mail:1.4 modules/axiom-{dom,parent,api,impl}
%pom_remove_dep :saxon-dom modules/axiom-dom-testsuite

# This plugin is used to get all possible stax implementations for testing against, which
# is impossible in Fedora; removing this means only testing against the JRE implementation
%pom_remove_plugin :maven-dependency-plugin modules/axiom-api

# Disable test suites due to unavailable deps "crimson", "org.ops4j.*"
%pom_disable_module modules/axiom-osgi-tests
%pom_disable_module modules/axiom-integration

# Don't build samples
%pom_disable_module modules/axiom-samples

# Don't ship tests
%mvn_package ":*-{tests,testsuite}" __noinstall
%mvn_package ":axiom-{build,test}utils" __noinstall

%build
# Skipping tests for now due to unexplained failures
%mvn_build -- -DskipTests

%install
%mvn_install

%files -f .mfiles
%doc *.txt
%doc --no-dereference LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE NOTICE

%changelog
* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2:1.2.14-alt1_4jpp8
- new version

* Fri Jun 01 2018 Igor Vlasenko <viy@altlinux.ru> 2:1.2.14-alt1_2jpp8
- new version

* Tue May 08 2018 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_19jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_17jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_15jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_14jpp8
- new fc release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_12jpp8
- new fc release

* Thu Feb 04 2016 Igor Vlasenko <viy@altlinux.ru> 2:1.2.12-alt1_11jpp8
- java 8 mass update

* Fri Jul 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2009.05-alt2
- Applied repocop patch and fixed freedesktop category

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.2009.05-alt1
- May 2009 release

* Sun Dec 14 2008 Ilya Mashkin <oddity@altlinux.ru> 1:3.2007.09-alt4
- rebuild with dynamic bfd
- remove post/postun

* Mon Jan 07 2008 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2007.09-alt3
- Axiom conflicts with fricas.

* Sun Sep 30 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2007.09-alt2
- Build gcl with statsysbfd.

* Sat Sep 29 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2007.09-alt1
- Axiom (September 2007).

* Fri Oct 27 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.09-alt3
- Fixed graphics problem (sockio).

* Thu Oct 19 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.09-alt2

* Thu Oct 19 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.09-alt1
- Axiom (September 2006).
- Use gcl-2.6.8pre since gcl-2.6.8pre2 has problems with graphics.

* Sat Oct 14 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.04-alt3
- Disable locbfd.

* Thu Oct 12 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.04-alt2
- Rebuilt with new toolchain.

* Tue May 09 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.04-alt1
- Axiom (April 2006).

* Thu Mar 30 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.01-alt4
- Desktop menu file.

* Mon Feb 13 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.01-alt3
- Fixed BuldRequires for new xorg.

* Sun Jan 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.01-alt2
- Fixed gcl configure bug revealed by bash 3.1.1.

* Fri Jan 06 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.2006.01-alt1
- Axiom (January 2006).

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:3.9-alt2.1
- Rebuilt with libreadline.so.5.

* Sun Oct 30 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.9-alt2
- Fixed for x86_64.

* Fri Sep 09 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.9-alt1
- Axiom 3.9 (September 2005). 

* Sun Jun 05 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.6-alt1
- Axiom 3.6 (June 2005).

* Sun Apr 10 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.4-alt1
- Axiom 3.4 (April 2005). 

* Wed Feb 02 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.0-alt0.20050201
- Axiom 3.0 beta (February 2005). 

* Sat Jan 01 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1:3.0-alt0.20041230
- Axiom 3.0 beta (January 2005).
- Graphics now works (use axiom-sman).

* Mon Dec 13 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040831-alt3
- Fix directories.

* Fri Nov 05 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040831-alt2
- Building GCL with locbfd due to new binutils incompatibility.
 

* Mon Sep 06 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040831-alt1
- CVS 08.31.2004.

* Sun May 09 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040509-alt1
- Axiom book.

* Tue Apr 13 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt3
- New GCL 2.6.2 CVS 13.04.2003 pre release - 25 percent buld speed-up.

* Mon Mar 01 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt2
- BuildRequires fix. 

* Sat Feb 28 2004 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.20040228-alt1
- Build with our own GCL 2.6.2 pre release (not external GCL yet).

* Fri Dec 19 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.03
- Build option to disable regression test.

* Thu Dec 11 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.02
- Fix spadroot path problem (export AXIOM=/usr/lib/axiom/mnt/linux).

* Sun Nov 30 2003 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 3.0-alt0.01
- Initial ALT Linux release.

