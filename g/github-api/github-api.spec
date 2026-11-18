%define _unpackaged_files_terminate_build 1

Name: github-api
Version: 1.330
Release: alt1

Summary: GitHub API for Java
License: MIT
Group: Development/Java
URL: https://github-api.kohsuke.org/
VCS: https://github.com/hub4j/github-api.git

Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-java
BuildRequires: maven-local
BuildRequires: java-21-openjdk-devel
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: annotation-indexer
BuildRequires: bridge-method-injector
BuildRequires: jjwt
BuildRequires: jjwt-api
BuildRequires: jjwt-impl
BuildRequires: jjwt-jackson
BuildRequires: mvn(com.squareup.okhttp3:okhttp)
BuildRequires: jackson-bom
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.apache.commons:commons-lang3)
BuildRequires: mvn(commons-lang:commons-lang)
BuildRequires: mvn(commons-io:commons-io)
BuildRequires: mvn(com.github.spotbugs:spotbugs-annotations)
BuildRequires: mvn(com.squareup.okio:okio-jvm)
BuildRequires: mvn(com.google.code.findbugs:jsr305)
BuildRequires: mvn(com.tngtech.archunit:archunit)
BuildRequires: mvn(org.hamcrest:hamcrest)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires: mvn(org.mockito:mockito-core)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.slf4j:slf4j-simple)

%description
Complete GitHub API including repository, organization, application and JWT
authorization support, URLConnection and OkHttp connectors, generated binary
compatibility bridges and the Java11 HTTP client overlay.

%package javadoc
Summary: API documentation for %name
Group: Development/Java

%description javadoc
API documentation for GitHub API for Java.

%prep
%setup
# These optional adapters require unsupported OkHttp 2/3 APIs.
rm -f \
    src/main/java/org/kohsuke/github/extras/OkHttpConnector.java \
    src/main/java/org/kohsuke/github/extras/OkHttp3Connector.java \
    src/main/java/org/kohsuke/github/extras/okhttp3/OkHttpConnector.java \
    src/main/java/org/kohsuke/github/extras/okhttp3/ObsoleteUrlFactory.java
%pom_xpath_remove pom:build/pom:extensions
%pom_remove_plugin org.springframework.boot:spring-boot-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin :maven-project-info-reports-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin
%pom_remove_plugin com.github.spotbugs:spotbugs-maven-plugin
%pom_remove_plugin com.github.siom79.japicmp:japicmp-maven-plugin
%pom_xpath_remove 'pom:profiles/pom:profile[pom:id="test-jwt-slow-multireleasejar-flaky"]'
%pom_xpath_set pom:properties/pom:okhttp3.version 5.5.1
%pom_xpath_set pom:properties/pom:okio.version 3.18.2
%pom_xpath_set pom:properties/pom:jjwt.suite.version 0.13.0
%pom_remove_dep com.squareup.okhttp3:okhttp-urlconnection
%pom_remove_dep com.squareup.okhttp:okhttp-urlconnection
%pom_xpath_set 'pom:dependencies/pom:dependency[pom:artifactId="okio"]/pom:artifactId' okio-jvm
%pom_xpath_set 'pom:dependencies/pom:dependency[pom:artifactId="bridge-method-annotation"]/pom:groupId' io.jenkins.tools
%pom_xpath_set 'pom:dependencies/pom:dependency[pom:artifactId="bridge-method-annotation"]/pom:version' 1.32
%pom_xpath_set 'pom:build/pom:plugins/pom:plugin[pom:artifactId="bridge-method-injector"]/pom:groupId' io.jenkins.tools
%pom_xpath_set 'pom:build/pom:plugins/pom:plugin[pom:artifactId="bridge-method-injector"]/pom:version' 1.32
%pom_xpath_set 'pom:build/pom:plugins/pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration/pom:annotationProcessorPaths/pom:annotationProcessorPath/pom:version' 1.213.v92788b_1f0a_21
%pom_remove_dep org.springframework.boot:spring-boot-starter-test
%pom_remove_dep com.github.npathai:hamcrest-optional
%pom_remove_dep org.awaitility:awaitility
%pom_remove_dep commons-fileupload:commons-fileupload
%pom_remove_dep commons-discovery:commons-discovery
%pom_remove_dep org.kohsuke.stapler:stapler
%pom_remove_dep org.kohsuke.stapler:stapler-jetty
%pom_remove_dep org.eclipse.jgit:org.eclipse.jgit
%pom_remove_dep org.kohsuke:wordnet-random-name
%pom_remove_dep com.github.tomakehurst:wiremock-jre8-standalone
%pom_remove_dep com.google.code.gson:gson
%pom_add_dep 'com.google.guava:guava:33.8.0-jre:test'
%pom_add_dep 'commons-lang:commons-lang:2.6:test'
# Test-only WireMock, Spring AOT and Stapler suites and their dependent helpers.
rm -f \
    src/test/java/org/kohsuke/HookApp.java \
    src/test/java/org/kohsuke/github/AbstractGHAppInstallationTest.java \
    src/test/java/org/kohsuke/github/AbstractGitHubWireMockTest.java \
    src/test/java/org/kohsuke/github/AbuseLimitHandlerTest.java \
    src/test/java/org/kohsuke/github/AotIntegrationTest.java \
    src/test/java/org/kohsuke/github/AotTestApplication.java \
    src/test/java/org/kohsuke/github/AotTestRuntimeHints.java \
    src/test/java/org/kohsuke/github/AppInstallationAuthorizationProviderTest.java \
    src/test/java/org/kohsuke/github/AppTest.java \
    src/test/java/org/kohsuke/github/CommitTest.java \
    src/test/java/org/kohsuke/github/EnterpriseManagedSupportTest.java \
    src/test/java/org/kohsuke/github/EnumTest.java \
    src/test/java/org/kohsuke/github/GHAppExtendedTest.java \
    src/test/java/org/kohsuke/github/GHAppInstallationTest.java \
    src/test/java/org/kohsuke/github/GHAppTest.java \
    src/test/java/org/kohsuke/github/GHAuthenticatedAppInstallationTest.java \
    src/test/java/org/kohsuke/github/GHAutolinkTest.java \
    src/test/java/org/kohsuke/github/GHBranchProtectionTest.java \
    src/test/java/org/kohsuke/github/GHBranchTest.java \
    src/test/java/org/kohsuke/github/GHCheckRunBuilderTest.java \
    src/test/java/org/kohsuke/github/GHCodeownersErrorTest.java \
    src/test/java/org/kohsuke/github/GHContentIntegrationTest.java \
    src/test/java/org/kohsuke/github/GHDeployKeyTest.java \
    src/test/java/org/kohsuke/github/GHDeploymentTest.java \
    src/test/java/org/kohsuke/github/GHDiscussionTest.java \
    src/test/java/org/kohsuke/github/GHEventPayloadTest.java \
    src/test/java/org/kohsuke/github/GHExternalGroupTest.java \
    src/test/java/org/kohsuke/github/GHGistTest.java \
    src/test/java/org/kohsuke/github/GHGistUpdaterTest.java \
    src/test/java/org/kohsuke/github/GHIssueEventAttributeTest.java \
    src/test/java/org/kohsuke/github/GHIssueEventTest.java \
    src/test/java/org/kohsuke/github/GHIssueTest.java \
    src/test/java/org/kohsuke/github/GHLicenseTest.java \
    src/test/java/org/kohsuke/github/GHMarketplacePlanTest.java \
    src/test/java/org/kohsuke/github/GHMilestoneTest.java \
    src/test/java/org/kohsuke/github/GHObjectTest.java \
    src/test/java/org/kohsuke/github/GHOrganizationTest.java \
    src/test/java/org/kohsuke/github/GHPersonTest.java \
    src/test/java/org/kohsuke/github/GHProjectCardTest.java \
    src/test/java/org/kohsuke/github/GHProjectColumnTest.java \
    src/test/java/org/kohsuke/github/GHProjectTest.java \
    src/test/java/org/kohsuke/github/GHPublicKeyTest.java \
    src/test/java/org/kohsuke/github/GHPullRequestTest.java \
    src/test/java/org/kohsuke/github/GHRateLimitTest.java \
    src/test/java/org/kohsuke/github/GHReleaseTest.java \
    src/test/java/org/kohsuke/github/GHRepositoryForkBuilderTest.java \
    src/test/java/org/kohsuke/github/GHRepositoryStatisticsTest.java \
    src/test/java/org/kohsuke/github/GHRepositoryTest.java \
    src/test/java/org/kohsuke/github/GHTagTest.java \
    src/test/java/org/kohsuke/github/GHTeamBuilderTest.java \
    src/test/java/org/kohsuke/github/GHTeamTest.java \
    src/test/java/org/kohsuke/github/GHTreeBuilderTest.java \
    src/test/java/org/kohsuke/github/GHUserTest.java \
    src/test/java/org/kohsuke/github/GHVerificationReasonTest.java \
    src/test/java/org/kohsuke/github/GHWorkflowRunTest.java \
    src/test/java/org/kohsuke/github/GHWorkflowTest.java \
    src/test/java/org/kohsuke/github/GitHubConnectionTest.java \
    src/test/java/org/kohsuke/github/GitHubStaticTest.java \
    src/test/java/org/kohsuke/github/GitHubTest.java \
    src/test/java/org/kohsuke/github/GitHubWireMockRule.java \
    src/test/java/org/kohsuke/github/Github2faTest.java \
    src/test/java/org/kohsuke/github/LifecycleTest.java \
    src/test/java/org/kohsuke/github/RateLimitCheckerTest.java \
    src/test/java/org/kohsuke/github/RateLimitHandlerTest.java \
    src/test/java/org/kohsuke/github/RepositoryTrafficTest.java \
    src/test/java/org/kohsuke/github/RequesterRetryTest.java \
    src/test/java/org/kohsuke/github/WireMockMultiServerRule.java \
    src/test/java/org/kohsuke/github/WireMockRule.java \
    src/test/java/org/kohsuke/github/WireMockRuleConfiguration.java \
    src/test/java/org/kohsuke/github/WireMockStatusReporterTest.java \
    src/test/java/org/kohsuke/github/extras/GitHubCachingTest.java \
    src/test/java/org/kohsuke/github/extras/OkHttpConnectorTest.java \
    src/test/java/org/kohsuke/github/extras/authorization/AuthorizationTokenRefreshTest.java \
    src/test/java/org/kohsuke/github/extras/authorization/JWTTokenProviderTest.java \
    src/test/java/org/kohsuke/github/extras/okhttp3/GitHubCachingTest.java \
    src/test/java/org/kohsuke/github/extras/okhttp3/OkHttpConnectorTest.java \
    src/test/java/org/kohsuke/github/extras/okhttp3/OkHttpGitHubConnectorTest.java

%build
%mvn_build -- --fail-at-end

%install
%mvn_install
rm -f %buildroot%_javadocdir/%name/args

%files -f .mfiles
%doc LICENSE.txt README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Nov 17 2026 Ivan Khanas <xeno@altlinux.org> 1.330-alt1
- Initial build for ALT.
