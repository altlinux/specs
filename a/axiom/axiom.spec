Serial: 2
Group: Sciences/Mathematics
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           axiom
Version:        1.2.12
Release:        alt1_14jpp8
Summary:        Axis Object Model
License:        ASL 2.0
Url:            http://ws.apache.org/commons/axiom/
# svn export http://svn.apache.org/repos/asf/webservices/commons/tags/axiom/1.2.12/ axiom-1.2.12
# tar caf axiom-1.2.12.tar.xz axiom-1.2.12
Source0:        %{name}-%{version}.tar.xz
# This patch makes several build changes:
# 1) Remove deps on a JAF implementation -- this is built into openjdk 7
# 2) Use the javamail and stax implementations already in Fedora
# 3) Remove maven plugins not present in Fedora, which do not impact the build process
# 4) Remove modules which require additional dependencies not yet in Fedora
Patch0:         axiom-build-fixes.patch

BuildRequires:  apache-rat-plugin
BuildRequires:  apache-commons-logging
BuildRequires:  bea-stax-api
BuildRequires:  javamail
BuildRequires:  jaxen
BuildRequires:  jdepend
BuildRequires:  junit
BuildRequires:  woodstox-core
BuildRequires:  maven-local
BuildRequires:  maven-install-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-plugin-bundle
BuildRequires:  xmlunit
BuildRequires:  /usr/bin/perl

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
%patch0 -p1
rm -rf modules/axiom-jaxen-testsuite/src/main/

# fix eol
%{__perl} -pi -e 's/\r$//g' README.txt NOTICE RELEASE-NOTE.txt

%pom_remove_dep :axiom-testutils modules/axiom-api

%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin -r :maven-source-plugin

%build
# Skipping tests for now due to many extra deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc *.txt
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%doc NOTICE

%changelog
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

