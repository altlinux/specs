Name:           apache-commons-codec
Version:        1.22.0
Release:        alt1

Summary:        Apache Commons Codec
License:        Apache-2.0
Group:          Development/Java
URL:            https://commons.apache.org/codec/
VCS:            https://github.com/apache/commons-codec

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

BuildArch:      noarch

%description
The Apache Commons Codec component contains encoders and decoders for formats
such as Base16, Base32, Base64, digest, and Hexadecimal. In addition to these
widely used encoders and decoders, the codec package also maintains a
collection of phonetic encoding utilities.

%javadoc_package

%prep
%setup

%mvn_file : commons-codec %name

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
%doc *.md

%changelog
* Sun May 17 2026 Evgeniy Serov <scala@altlinux.org> 1.22.0-alt1
- Updated to 1.22.0.

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 0:1.15-alt1_4jpp11
- update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0:1.15-alt1_2jpp11
- new version

* Thu Apr 29 2021 Igor Vlasenko <viy@altlinux.org> 0:1.13-alt1_2jpp11
- new version

* Mon May 27 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_6jpp8
- new version

* Tue Feb 05 2019 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_4jpp8
- fc29 update

* Tue May 15 2018 Igor Vlasenko <viy@altlinux.ru> 0:1.11-alt1_3jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_3jpp8
- new fc release

* Wed Feb 03 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt1_2jpp8
- new version

* Fri Jan 22 2016 Igor Vlasenko <viy@altlinux.ru> 0:1.10-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_5jpp7
- new release

* Fri Aug 01 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.8-alt1_1jpp7
- new version

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_5jpp7
- new version

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt2_4jpp7
- added OSGi manifest

* Fri Aug 31 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.6-alt1_4jpp7
- new version

* Sun Jan 02 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_5jpp6
- fixed repolib

* Thu Dec 30 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_5jpp6
- fixed repolib

* Wed Dec 29 2010 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt1_5jpp6
- new version

