Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 2.0.1
%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.ws.rs-api
Name:          glassfish-jax-rs-api
Version:       2.0.1
Release:       alt1_6jpp8
Summary:       JAX-RS API Specification (JSR 339)
License:       CDDL or GPLv2 with exceptions
URL:           http://jax-rs-spec.java.net/
# git clone git://java.net/jax-rs-spec~api glassfish-jax-rs-api
# (cd glassfish-jax-rs-api/ && git archive --format=tar --prefix=glassfish-jax-rs-api-2.0.1/ 2.0.1 | xz > ../glassfish-jax-rs-api-2.0.1.tar.xz)
Source0:       %{name}-%{namedversion}.tar.xz

BuildRequires: junit
BuildRequires: jvnet-parent

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
BuildRequires: maven-resources-plugin
BuildRequires: spec-version-maven-plugin

# Disabled on rawhide: texlive is broken
%if 0
# This is pdfTeX, Version 3.1415926-2.5-1.40.14 (TeX Live 2013)
# restricted \write18 enabled.
# kpathsea: Running mktexfmt pdflatex.fmt
# I can't find the format file `pdflatex.fmt'!
# make: *** [spec.pdf] Error 1
BuildRequires: texlive-collection-basic
BuildRequires: texlive-base
BuildRequires: texlive-bibtex-bin
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive texlive-collection-basic texlive-context texlive-dist
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
BuildRequires: texlive-collection-basic
BuildRequires: texlive texlive-collection-basic
BuildRequires: texlive-collection-basic
BuildRequires: texlive-collection-basic
%endif

BuildArch:     noarch
Source44: import.info

%description
JAX-RS Java API for RESTful Web Services (JSR 339).

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%if 0
%package manual
Group: Development/Java
Summary:       Manual for %{name}
BuildArch: noarch

%description manual
This package contains documentation for %{name}.
%endif

%prep
%setup -q -n %{name}-%{namedversion}
find . -name '*.jar' -delete
find . -name '*.class' -delete

%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin src/jax-rs-api

# Reporting mojo's can only be called from ReportDocumentRender
%pom_remove_plugin org.apache.maven.plugins:maven-jxr-plugin src/jax-rs-api
%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin src/jax-rs-api
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin src/jax-rs-api
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin src/jax-rs-api
%pom_remove_plugin org.apache.maven.plugins:maven-deploy-plugin src/jax-rs-api

%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-javadoc-plugin' ]/pom:executions" src/jax-rs-api

%pom_xpath_remove "pom:build/pom:finalName" src/jax-rs-api

sed -i "s|dvips|pdftex|" spec/spec.tex

sed -i '/check-module/d' src/jax-rs-api/pom.xml

cp -p src/etc/config/copyright.txt .
sed -i 's/\r//' copyright.txt src/examples/pom.xml

%build

(
cd src/jax-rs-api
%mvn_file :%{oname} %{name}
%mvn_build
)

%if 0
cd spec
make clean all
%endif

%install

(
cd src/jax-rs-api
%mvn_install
)

%files -f src/jax-rs-api/.mfiles
%doc --no-dereference copyright.txt

%files javadoc -f src/jax-rs-api/.mfiles-javadoc
%doc --no-dereference copyright.txt

%if 0
%files manual
%doc spec/spec.pdf src/examples
%doc --no-dereference copyright.txt
%endif

%changelog
* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_6jpp8
- java update

* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_5jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_4jpp8
- new jpp release

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2jpp8
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.0-alt1_4jpp7
- new release

