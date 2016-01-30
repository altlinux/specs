Name: jdom-javadoc
Version: 1.1.3
Summary: Javadoc for jdom
License: ASL 1.1
Url: http://www.jdom.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: jdom-javadoc = 0:1.1.3-9.fc23
Requires: jpackage-utils
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: jdom-javadoc-1.1.3-9.fc23.cpio

%description
Javadoc for jdom.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_5jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_4jpp7
- update

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_3jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_2jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt3_2jpp6
- added jdom:jdom jppmap

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_2jpp6
- added osgi manifest

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_2jpp6
- new jpp release

* Sun Jan 11 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt2_5.5jpp5
- added OSGi manifest for eclipse

* Mon May 07 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0-alt1_5jpp1.7
- converted from JPackage by jppimport script

* Thu Apr 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1
- Initial build for ALTLinux Sisyphus

