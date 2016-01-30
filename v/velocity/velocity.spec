Name: velocity
Version: 1.7
Summary: Java-based template engine
License: ASL 2.0
Url: http://velocity.apache.org/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: mvn(org.apache.velocity:velocity) = 1.7
Provides: mvn(org.apache.velocity:velocity:pom:) = 1.7
Provides: mvn(velocity:velocity) = 1.7
Provides: mvn(velocity:velocity:pom:) = 1.7
Provides: velocity = 0:1.7-18.fc23
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-lang:commons-lang)

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: velocity-1.7-18.fc23.cpio

%description
Velocity is a Java-based template engine. It permits anyone to use the
simple yet powerful template language to reference objects defined in
Java code.
When Velocity is used for web development, Web designers can work in
parallel with Java programmers to develop web sites according to the
Model-View-Controller (MVC) model, meaning that web page designers can
focus solely on creating a site that looks good, and programmers can
focus solely on writing top-notch code. Velocity separates Java code
from the web pages, making the web site more maintainable over the long
run and providing a viable alternative to Java Server Pages (JSPs) or
PHP.
Velocity's capabilities reach well beyond the realm of web sites; for
example, it can generate SQL and PostScript and XML (see Anakia for more
information on XML transformations) from templates. It can be used
either as a standalone utility for generating source code and reports,
or as an integrated component of other systems. Velocity also provides
template services for the Turbine web application framework.
Velocity+Turbine provides a template service that will allow web
applications to be developed according to a true MVC model.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_9jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_7jpp7
- new release

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_6jpp7
- fc update

* Thu Sep 13 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.7-alt1_5jpp7
- new version

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt3_1jpp6
- fixed build

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt2_1jpp6
- added velocity:velocity jppmap

* Fri Dec 10 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.6.4-alt1_1jpp6
- new version

* Wed May 12 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt2_4jpp5
- fixes for java6 support

* Mon Feb 22 2010 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_4jpp5
- use default jpp profile

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_3jpp5
- converted from JPackage by jppimport script

* Tue Jan 22 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_2jpp1.7
- pom fixes

* Wed Nov 28 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.5-alt1_1jpp1.7
- updated to new jpackage release

* Thu Nov 01 2007 Igor Vlasenko <viy@altlinux.ru> 1:1.4-alt1_6jpp1.7
- import from jpackage;set epoch 1; overrides unstable version

* Thu May 17 2007 Igor Vlasenko <viy@altlinux.ru> 1.5-alt0.3
- rebuild with excalibur-avalon-logkit

* Fri Dec 02 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.2
- nightly build 20051125053934 

* Sat May 07 2005 Vladimir Lettiev <crux@altlinux.ru> 1.5-alt0.1
- 1.5-dev
- svn snapshot 20050507

* Fri May 06 2005 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1
- Initial build for ALT Linux Sisyphus

