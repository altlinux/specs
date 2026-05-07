Name:           docx4j-xalan-j
Version: 	11.0.0
Release:        alt1

Summary:        Xalan fork for Java 11
License:        Apache-2.0
Group:          Development/Java
URL:            https://github.com/plutext/xalan-j
VCS:            https://github.com/plutext/xalan-j

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(xerces:xercesImpl)

BuildArch:      noarch

%description
Xalan-Java is an XSLT processor for transforming XML documents into HTML, text,
or other XML document types. It implements XSL Transformations (XSLT)
Version 1.0 and XML Path Language (XPath) Version 1.0.

%package        interpretive
Summary:        Xalan interpretive
Group:          Development/Java

%description    interpretive
%summary.

%package        serializer
Summary:        Xalan serializer
Group:          Development/Java

%description    serializer
%summary.

%prep
%setup

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :flatten-maven-plugin
%pom_remove_plugin :maven-shade-plugin xalan-bundled-jar

%mvn_package :xalan-interpretive interpretive
%mvn_package :xalan-serializer serializer

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.md

%files interpretive -f .mfiles-interpretive
%files serializer -f .mfiles-serializer

%changelog
* Thu Apr 23 2026 Evgeniy Serov <scala@altlinux.org> 11.0.0-alt1
- Initial build for Sisyphus.
