Name:           ognl
Version:        3.4.11
Release:        alt1

Summary:        Object-Graph Navigation Language
License:        Apache-2.0
Group:          Development/Java
URL:            http://www.ognl.org/
VCS:            https://github.com/orphan-oss/ognl

Source0:        %name-%version.tar

BuildRequires(pre):  maven-local
BuildRequires:  jpackage-default

BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(javassist:javassist)
BuildRequires:  mvn(org.easymock:easymock)

BuildArch:      noarch

%description
OGNL stands for Object-Graph Navigation Language; it is an expression language
for getting and setting properties of Java objects. You use the same expression
for both getting and setting the value of a property.

The ognl.Ognl class contains convenience methods for evaluating OGNL
expressions. You can do this in two stages, parsing an expression into an
internal form and then using that internal form to either set or get the value
of a property; or you can do it in a single stage, and get or set a property
using the String form of the expression directly.

OGNL started out as a way to set up associations between UI components and
controllers using property names. As the desire for more complicated
associations grew, Drew Davidson created what he called KVCL, for Key-Value
Coding Language, egged on by Luke Blanshard. Luke then reimplemented the
language using ANTLR, came up with the new name, and, egged on by Drew, filled
it out to its current state. Later on Luke again reimplemented the language
using JavaCC. Further maintenance on all the code is done by Drew
(with spiritual guidance from Luke).

%javadoc_package

%prep
%setup

%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt *.md

%changelog
* Mon Apr 20 2026 Evgeniy Srrov <scala@altlinux.org> 3.4.11-alt1
- Updated to 3.4.11.
- Returned to Sisyphus.

* Fri Jul 11 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.7.3-alt2_1jpp6
- NMU rebuild to move _mavenpomdir and _mavendepmapfragdir

* Fri Jan 27 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.7.3-alt1_1jpp6
- new version

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt2_3jpp5
- fixed repocop warnings

* Wed Nov 26 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_3jpp5
- build w/java5

* Wed Mar 19 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_3jpp1.7
- updated to new jpp release

* Wed Jul 18 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.6.9-alt1_2jpp1.7
- converted from JPackage by jppimport script

