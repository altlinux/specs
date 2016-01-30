Name: base64coder
Version: 20101219
Summary: Fast and compact Base64 encoder/decoder Java library
License: EPL or LGPLv2+ or GPLv2+ or ASL 2.0+ or BSD
Url: http://www.source-code.biz/base64coder/java/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: base64coder = 20101219-13.fc23
Provides: mvn(biz.source_code:base64coder) = 2010.12.19
Provides: mvn(biz.source_code:base64coder:pom:) = 2010.12.19
Requires: java-headless
Requires: jpackage-utils

BuildArch: noarch
Group: Development/Java
Release: alt2jpp
Source: base64coder-20101219-13.fc23.cpio

%description
Base64Coder is a fast and compact Base64 encoder/decoder class.

There is no Base64 encoder/decoder in the standard Java SDK class
library.  The undocumented classes sun.misc.BASE64Encoder and
sun.misc.BASE64Decoder should not be used.

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
* Thu Jan 28 2016 Igor Vlasenko <viy@altlinux.ru> 20101219-alt2jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_9jpp7
- new release

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_7jpp7
- update

* Mon Aug 20 2012 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_5jpp7
- new release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 20101219-alt1_2jpp7
- new version

