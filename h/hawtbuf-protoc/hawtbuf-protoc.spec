Name: hawtbuf-protoc
Version: 1.11
Summary: A protobuf compiler as a maven plugin
License: ASL 2.0
Url: https://github.com/fusesource/hawtbuf/
Packager: Igor Vlasenko <viy@altlinux.ru>
Provides: hawtbuf-protoc = 1.11-3.fc23
Provides: mvn(org.fusesource.hawtbuf:hawtbuf-protoc) = 1.11
Provides: mvn(org.fusesource.hawtbuf:hawtbuf-protoc:pom:) = 1.11
Requires: java-headless
Requires: jpackage-utils
Requires: mvn(org.fusesource.hawtbuf:hawtbuf-proto)

BuildArch: noarch
Group: Development/Java
Release: alt0.1jpp
Source: hawtbuf-protoc-1.11-3.fc23.cpio

%description
HawtBuf Protoc: A protobuf compiler as a maven plugin.

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
* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 1.11-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_7jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_5jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.9-alt3_2jpp7
- fixed build

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt2_2jpp7
- fixed maven1 dependency

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1_2jpp7
- initial build

