Name: apache-commons-validator
Version: 1.4.1
Summary: Apache Commons Validator
License: ASL 2.0
Url: http://commons.apache.org/validator/
Epoch: 1
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: apache-commons-validator = 1.4.1-1.fc23
Provides: mvn(commons-validator:commons-validator) = 1.4.1
Provides: mvn(commons-validator:commons-validator:pom:) = 1.4.1
Provides: mvn(org.apache.commons:commons-validator) = 1.4.1
Provides: mvn(org.apache.commons:commons-validator:pom:) = 1.4.1
Requires: java-headless
Requires: java-headless
Requires: jpackage-utils
Requires: jpackage-utils
Requires: mvn(commons-beanutils:commons-beanutils)
Requires: mvn(commons-collections:commons-collections)
Requires: mvn(commons-digester:commons-digester)
Requires: mvn(commons-logging:commons-logging)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: apache-commons-validator-1.4.1-1.fc23.cpio

%description
A common issue when receiving data either electronically or from user input is
verifying the integrity of the data. This work is repetitive and becomes even
more complicated when different sets of validation rules need to be applied to
the same set of data based on locale for example. Error messages may also vary
by locale. This package attempts to address some of these issues and speed
development and maintenance of validation rules.

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
* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.4.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_6jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.4.0-alt1_4jpp7
- new version

* Mon Mar 18 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.3.1-alt1_9jpp7
- fc update

* Sat Sep 15 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_0.r832761.5jpp6
- marked oro as essential dependency due to maven-site-plugin

* Sat Feb 26 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_0.r832761.5jpp6
- new version

