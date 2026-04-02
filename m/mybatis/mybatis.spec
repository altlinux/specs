Name:           mybatis
Version:        3.5.19
Release:        alt1.1

Summary:        SQL Mapping Framework for Java
License:        Apache-2.0
Group:          Development/Java
URL:            http://www.mybatis.org/
VCS:            https://github.com/mybatis/mybatis-3

Source0:        %name-%version.tar
Source1:        m2.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)

BuildArch:      noarch

%description
The MyBatis SQL mapper framework makes it easier to use a relational database
with object-oriented applications. MyBatis couples objects with stored
procedures or SQL statements using an XML descriptor or annotations. Simplicity
is the biggest advantage of the MyBatis data mapper over object relational
mapping tools.

%prep
%setup

test -d ~/.m2 && rm -rf ~/.m2
tar xf %SOURCE1 -C ~

%pom_remove_parent

%build
%mvn_build -f -j -- \
  -Dmaven.compiler.source=1.8 \
  -Dmaven.compiler.target=1.8 \
  -Dmaven.javadoc.source=1.8 \
  -Dmaven.compiler.release=8 \

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%changelog
* Wed Mar 04 2026 Evgeniy Serov <scala@altlinux.org> 3.5.19-alt1.1
- Cosmetic fixes.

* Mon Jan 12 2026 Evgeniy Serov <scala@altlinux.org> 3.5.19-alt1
- Updated to 3.5.19 (bootstrapped).
- Returned to Sisyphus.
- Removed deprecated patches.

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_11jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_9jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_8jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_7jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_5jpp8
- new fc release

* Mon Nov 28 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_4jpp8
- new fc release

* Mon Feb 08 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt1_3jpp8
- java 8 mass update

* Sun Feb 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.2.8-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

