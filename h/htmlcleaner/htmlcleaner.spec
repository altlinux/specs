Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-1.8-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		htmlcleaner
Version:	2.2.1
Release:	alt1_15jpp8
Summary:	HTML parser written in Java

License:	BSD
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}%%20v%{version}/%{name}-%{version}-src.zip
URL:		http://htmlcleaner.sourceforge.net/

BuildArch:	noarch

BuildRequires:	ant
BuildRequires:	jdom
BuildRequires:	maven-local
Source44: import.info

%description
HtmlCleaner is open-source HTML parser written in Java. HTML found on Web is
usually dirty, ill-formed and unsuitable for further processing.
For any serious consumption of such documents, it is necessary to first
clean up the mess and bring the order to tags, attributes and ordinary text.
For the given HTML document, HtmlCleaner reorders individual elements and
produces well-formed XML. By default, it follows similar rules that the most
of web browsers use in order to create Document Object Model. However, user
may provide custom tag and rule set for tag filtering and balancing.


%package javadoc
Group: Development/Java
Summary:	API documentation for %{name}
BuildArch: noarch


%description javadoc
This package contains the API documentation for %{name}


%prep
%setup -q -c -T
jar xf %{SOURCE0}
sed -i -e 's!\r!!g' licence.txt

%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin

%pom_xpath_remove pom:build/pom:extensions

# avoid Pre-built JARfiles
JARfiles=""
for j in $(find -name \*.jar); do
if [ ! -L $j ] ; then
JARfiles="$JARfiles $j"
fi
done
if [ ! -z "$JARfiles" ] ; then
echo "These JARfiles should be deleted and symlinked to system JARfiles: $JARfiles"
exit 1
fi


%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%doc licence.txt


%files javadoc -f .mfiles-javadoc
%doc licence.txt


%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_15jpp8
- new version

