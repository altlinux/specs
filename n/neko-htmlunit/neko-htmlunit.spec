Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:          neko-htmlunit
Version:       2.23
Release:       alt1_6jpp8
Summary:       HtmlUnit adaptation of NekoHtml
License:       ASL 2.0
URL:           http://htmlunit.sourceforge.net
# svn export http://svn.code.sf.net/p/htmlunit/code/tags/HtmlUnit\ NekoHtml-2.23 neko-htmlunit-2.23
# tar cJf neko-htmlunit-2.23.tar.xz neko-htmlunit-2.23
Source0:       neko-htmlunit-%{version}.tar.xz

BuildRequires: maven-local
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(xerces:xercesImpl)
# Modified version of NekoHtml
# see https://sourceforge.net/p/htmlunit/mailman/message/34963360/
Provides:      bundled(nekohtml) = 1.9.22

BuildArch:     noarch
Source44: import.info

%description
HtmlUnit adaptation of NekoHtml. It has the
same functionality but exposing HTMLElements
to be overridden.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n neko-htmlunit-%{version}

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-scm-plugin

%mvn_file net.sourceforge.htmlunit:%{name} %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc --no-dereference LICENSE.txt

%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_6jpp8
- new version

* Thu May 31 2018 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_4jpp8
- java update

* Thu Nov 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.23-alt1_3jpp8
- new version

