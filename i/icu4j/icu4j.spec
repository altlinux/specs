BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
AutoReq: yes,noosgi

Name: icu4j
Version: 4.4.2.2
Summary: International Components for Unicode for Java
License: MIT and EPL
Url: http://site.icu-project.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: java
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: icu4j-4.4.2.2-12.fc18.cpio

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

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
* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

%changelog
* Thu Sep 08 2011 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2-alt1_2jpp6
- update to new release by jppimport

* Mon Feb 28 2011 Igor Vlasenko <viy@altlinux.ru> 1:4.2.1-alt1_1jpp6
- new version

* Mon Jan 25 2010 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_3jpp6
- new version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0:3.8.1-alt1_4jpp6
- new version

* Fri Jul 25 2008 Igor Vlasenko <viy@altlinux.ru> 0:3.6.1-alt1.6_2jpp5
- build for eclipse 3.3.2

* Fri Nov 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.6.1-alt1_1.3jpp5.0
- converted from JPackage by jppimport script

* Wed May 09 2007 Igor Vlasenko <viy@altlinux.ru> 0:3.4.5-alt1_1jpp1.7
- converted from JPackage by jppimport script

