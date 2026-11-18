%define _unpackaged_files_terminate_build 1

Name: jakarta-transactions
Version: 2.0.1
Release: alt1

Summary: Jakarta Transactions API
License: EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group: Development/Java
URL: https://jakarta.ee/specifications/transactions/
VCS: https://github.com/jakartaee/transactions.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: ee4j-parent
BuildRequires: cdi-api-compat4
BuildRequires: jakarta-interceptors
BuildRequires: maven-plugin-bundle
BuildRequires: maven-plugin-build-helper
BuildRequires: spec-version-maven-plugin
BuildRequires: asciidoctor

%description
Jakarta Transactions provides standard Java interfaces for transaction
demarcation and coordination of XA-aware resource managers.

%package javadoc
Summary: API documentation for Jakarta Transactions
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description javadoc
API documentation for Jakarta Transactions.

%package manual
Summary: Jakarta Transactions specification
License: Eclipse Foundation Specification License v1.0
Group: Documentation

%description manual
The complete Jakarta Transactions specification in HTML format.

%prep
%setup
# Select the genuine CDI 4.1 API and its versioned runtime binding.
%pom_change_dep jakarta.enterprise:jakarta.enterprise.cdi-api \
    jakarta.enterprise:jakarta.enterprise.cdi-api:4.1.0 api
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin api
# Javadoc is generated independently by XMvn.
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin api
%mvn_file :jakarta.transaction-api %name/jakarta.transaction-api

%build
java -version
%mvn_build
asciidoctor -b html5 -d book -a data-uri -a toc=left \
    -a revnumber=2.0 -a revdate=2022-03-31 \
    -D target/manual spec/src/main/asciidoc/transactions-spec.adoc

%install
# These generated source-path links and compiler arguments are build inputs.
rm -rf target/xmvn-apidocs/module-source-path
rm -f target/xmvn-apidocs/args
%mvn_install

%files -f .mfiles
%doc LICENSE.md NOTICE.md

%files javadoc -f .mfiles-javadoc

%files manual
%doc target/manual/transactions-spec.html

%changelog
* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 2.0.1-alt1
- Initial build for ALT.
