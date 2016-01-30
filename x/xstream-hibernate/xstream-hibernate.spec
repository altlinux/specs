Name: xstream-hibernate
Version: 1.4.8
Summary: hibernate module for xstream
License: BSD
Url: http://xstream.codehaus.org/
Epoch: 0
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(com.thoughtworks.xstream:xstream-hibernate) = 1.4.8
Provides: mvn(com.thoughtworks.xstream:xstream-hibernate:pom:) = 1.4.8
Provides: xstream-hibernate = 1.4.8-2.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(com.thoughtworks.xstream:xstream)
Requires: mvn(org.hibernate:hibernate-core)
Requires: xstream

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: xstream-hibernate-1.4.8-2.fc23.cpio

%description
hibernate module for xstream.

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
* Fri Jan 29 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.4.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_5jpp7
- new release

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp7
- fc update

* Thu Feb 02 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_4jpp6
- new jpp relase

* Sat Mar 06 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.3.1-alt1_1jpp5
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.3-alt1_2jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_3jpp5
- converted from JPackage by jppimport script

* Thu Nov 15 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.2.2-alt1_1jpp1.7
- updated to new jpackage release

* Tue Jul 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.1.3-alt1_1jpp1.7
- converted from JPackage by jppimport script

