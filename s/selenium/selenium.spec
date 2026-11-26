# vim: set ft=spec: -*- rpm-spec -*-
%global        selenium_version 4.54.0
%global        selenium_manager_version 0.4.54
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%def_enable    java

Name:          selenium
Version:       %selenium_version
Release:       alt1
Summary:       A browser automation framework and ecosystem
License:       Apache-2.0
Group:         Development/Tools
Url:           https://www.seleniumhq.org
Vcs:           https://github.com/seleniumhq/selenium.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Source1:       selenium-java-poms-%version.tar
Source2:       selenium-manager-vendor-%selenium_manager_version.tar.xz
Source3:       selenium-manager-THIRD-PARTY-NOTICES.txt
Patch:         alt-build.patch
BuildRequires(pre): rpm-macros-ruby
BuildRequires(pre): setup-rb
BuildRequires(pre): rake
BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-rust-toolchain-common
BuildRequires: rust >= 1.93
BuildRequires: pkgconfig(liblzma)
%if_enabled java
BuildRequires(pre): rpm-macros-java
BuildRequires: esbuild >= 0.23.0
BuildRequires: git-core
BuildRequires: python3
BuildRequires: java-17-openjdk-devel
BuildRequires: maven-local-openjdk17
BuildRequires: mvn(com.github.javaparser:javaparser-core)
BuildRequires: mvn(com.google.auto.service:auto-service) >= 1.1.1
BuildRequires: mvn(com.google.auto.service:auto-service-annotations) >= 1.1.1
BuildRequires: mvn(com.google.guava:guava) >= 33.8.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-api) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-context) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-exporter-logging) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-sdk) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-sdk-common) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-sdk-extension-autoconfigure) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-sdk-extension-autoconfigure-spi) >= 1.68.0
BuildRequires: mvn(io.opentelemetry:opentelemetry-sdk-trace) >= 1.68.0
BuildRequires: mvn(net.bytebuddy:byte-buddy) >= 1.18.17
BuildRequires: mvn(org.altlinux.bootstrap:rules-java-runfiles)
BuildRequires: mvn(org.apache.maven.plugins:maven-antrun-plugin) >= 3.1.0
BuildRequires: mvn(org.jetbrains:annotations) >= 26.1.0
BuildRequires: mvn(org.jspecify:jspecify) >= 1.0.1
%endif
%if_enabled check
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(debug) >= 1.7
BuildRequires: gem(git) >= 1.19
BuildRequires: gem(logger) >= 1.4
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.5
BuildRequires: gem(rubyzip) >= 1.2.2
BuildRequires: gem(steep) >= 2.0
BuildRequires: gem(webmock) >= 3.5
BuildRequires: gem(webrick) >= 1.7
BuildRequires: gem(websocket) >= 1.0
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(debug) >= 2
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(rubyzip) >= 4.0
BuildConflicts: gem(steep) >= 3
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(websocket) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency git >= 1.19
%ruby_use_gem_dependency rack >= 2.0
Requires:      gem(selenium-devtools) = 0.158.0
Requires:      gem(selenium-webdriver) = 4.54.0

%description
Selenium is an umbrella project encapsulating a variety of tools and libraries
enabling web browser automation. Selenium specifically provides infrastructure
for the W3C WebDriver specification a platform and language-neutral coding
interface compatible with all major web browsers.

The project is made possible by volunteer contributors who've generously donated
thousands of hours in code development and upkeep.


%package       -n gem-selenium-devtools
Version:       0.158.0
Release:       alt1
Summary:       A browser automation framework and ecosystem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.3
Requires:      rubygems >= 1.3.1
Requires:      gem(selenium-webdriver) = 4.54.0
Provides:      gem(selenium-devtools) = 0.158.0

%description   -n gem-selenium-devtools
Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.


%if_enabled    doc
%package       -n gem-selenium-devtools-doc
Version:       0.158.0
Release:       alt1
Summary:       A browser automation framework and ecosystem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета selenium-devtools
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selenium-devtools) = 0.158.0

%description   -n gem-selenium-devtools-doc
A browser automation framework and ecosystem documentation files.

Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.

%description   -n gem-selenium-devtools-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета selenium-devtools.
%endif


%if_enabled    devel
%package       -n gem-selenium-devtools-devel
Version:       0.158.0
Release:       alt1
Summary:       A browser automation framework and ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium-devtools
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-devtools) = 0.158.0
Requires:      gem(git) >= 1.19
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.5
Requires:      gem(webmock) >= 3.5
Requires:      gem(webrick) >= 1.7
Requires:      gem(yard) >= 0.9.11
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2

%description   -n gem-selenium-devtools-devel
A browser automation framework and ecosystem development package.

Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.

%description   -n gem-selenium-devtools-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium-devtools.
%endif


%package       -n gem-selenium-webdriver
Version:       4.54.0
Release:       alt1
Summary:       A browser automation framework and ecosystem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      ruby >= 3.3
Requires:      rubygems > 1.3.1
Requires:      gem(selenium-devtools) = 0.158.0
Requires:      gem(base64) >= 0.2
Requires:      gem(logger) >= 1.4
Requires:      gem(rubyzip) >= 1.2.2
Requires:      gem(websocket) >= 1.0
Conflicts:     gem(base64) >= 1
Conflicts:     gem(logger) >= 2
Conflicts:     gem(rubyzip) >= 4.0
Conflicts:     gem(websocket) >= 2
Obsoletes:     ruby-selenium-webdriver < %EVR
Provides:      ruby-selenium-webdriver = %EVR
Provides:      gem(selenium-webdriver) = 4.54.0

%description   -n gem-selenium-webdriver
Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.


%if_enabled    doc
%package       -n gem-selenium-webdriver-doc
Version:       4.54.0
Release:       alt1
Summary:       A browser automation framework and ecosystem documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета selenium-webdriver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = 4.54.0

%description   -n gem-selenium-webdriver-doc
A browser automation framework and ecosystem documentation files.

Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.

%description   -n gem-selenium-webdriver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета selenium-webdriver.
%endif


%if_enabled    devel
%package       -n gem-selenium-webdriver-devel
Version:       4.54.0
Release:       alt1
Summary:       A browser automation framework and ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium-webdriver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = 4.54.0
Requires:      gem(git) >= 1.19
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.5
Requires:      gem(webmock) >= 3.5
Requires:      gem(webrick) >= 1.7
Requires:      gem(yard) >= 0.9.34
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(yard) >= 1

%description   -n gem-selenium-webdriver-devel
A browser automation framework and ecosystem development package.

Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.

%description   -n gem-selenium-webdriver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium-webdriver.
%endif


%if_enabled    devel
%package       -n selenium-devel
Version:       4.54.0
Release:       alt1
Summary:       A browser automation framework and ecosystem
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem-selenium-webdriver-devel = 4.54.0-alt1
Requires:      gem-selenium-devtools-devel = 0.158.0-alt1
Requires:      selenium = %EVR
Requires:      gem(base64) >= 0.2
Requires:      gem(git) >= 1.19
Requires:      gem(logger) >= 1.4
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.75
Requires:      gem(rubocop-performance) >= 1.25
Requires:      gem(rubocop-rake) >= 0.7
Requires:      gem(rubocop-rspec) >= 3.5
Requires:      gem(rubyzip) >= 1.2.2
Requires:      gem(webmock) >= 3.5
Requires:      gem(webrick) >= 1.7
Requires:      gem(websocket) >= 1.0
Requires:      gem(yard) >= 0.9.36
Conflicts:     gem(base64) >= 1
Conflicts:     gem(logger) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(rubyzip) >= 4.0
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(websocket) >= 2
Conflicts:     gem(yard) >= 0.10

%description   -n selenium-devel
A browser automation framework and ecosystem development package.

Selenium is an umbrella project encapsulating a variety of tools and libraries
enabling web browser automation. Selenium specifically provides infrastructure
for the W3C WebDriver specification a platform and language-neutral coding
interface compatible with all major web browsers.

The project is made possible by volunteer contributors who've generously donated
thousands of hours in code development and upkeep.

%description   -n selenium-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium. %endif
%endif



%if_enabled    java
%package       -n mvn-selenium
Summary:       Selenium WebDriver client for Java
Group:         Development/Java
BuildArch:     noarch
Requires:      cargo-selenium-manager-cli >= 0.4.54
Requires:      java >= 17

%description   -n mvn-selenium
Selenium WebDriver Java bindings and their Maven metadata. Selenium Manager
discovers browser and driver executables for local sessions on Linux.
%endif


%package       -n cargo-selenium-manager-cli
Version:       %selenium_manager_version
Summary:       Browser and driver discovery for Selenium
Group:         Development/Tools

%description   -n cargo-selenium-manager-cli
Selenium Manager discovers supported browsers and WebDriver executables.


%prep
%if_enabled java
%setup -a1 -a2
%else
%setup -a2
%endif
%autopatch -p1

mv vendor rust/
%rust_prep -p rust
install -pm 0644 %SOURCE3 rust/selenium-manager-THIRD-PARTY-NOTICES.txt

cat >> rust/.cargo/config.toml <<'EOF_LZMA'

# Use Sisyphus's liblzma for xz2.
[target.%rust_host_triple.lzma]
rustc-link-lib = ["dylib=lzma"]
EOF_LZMA

%if_enabled java
pushd selenium-java
%pom_xpath_set pom:project/pom:version %selenium_version \
   pom.xml selenium-modules/selenium-code-generator
%pom_xpath_remove -f "pom:dependency/pom:scope[.='runtime']" \
   selenium-modules/selenium-*
%pom_add_dep com.google.auto.service:auto-service:1.1.1:provided \
   selenium-modules/selenium-{chrome-driver,chromium-driver,edge-driver,firefox-driver} \
   selenium-modules/selenium-{http,ie-driver,remote-driver,safari-driver,support} \
   selenium-modules/selenium-devtools-*
%pom_xpath_inject pom:project "$(cat cdp-build.xml)" \
   selenium-modules/selenium-devtools-*
%pom_xpath_inject pom:project "$(cat bidi-build.xml)" \
   selenium-modules/selenium-remote-driver
%mvn_package :selenium-java-rpm-reactor __noinstall
%mvn_package :selenium-code-generator __noinstall
popd
%endif

%build
%ruby_build
pushd rust
%rust_build --locked
popd
%if_enabled java
export JAVA_HOME=%_prefix/lib/jvm/java-17-openjdk
pushd selenium-java
revision=$(git get-tar-commit-id < %SOURCE0)
xmvn --batch-mode --offline --non-recursive antrun:run@stage-java \
   "-Dselenium.build.revision=${revision:0:12}"
%mvn_build -j -- -Dmaven.compiler.release=17 \
   -Dproject.build.sourceEncoding=UTF-8
popd
%endif

%install
%ruby_install
pushd rust
%rust_install selenium-manager
popd
%if_enabled java
export JAVA_HOME=%_prefix/lib/jvm/java-17-openjdk
pushd selenium-java
%mvn_install
popd
%endif

%check
%ruby_test
pushd rust
%rust_test --locked --lib
popd
test "$(%buildroot%_bindir/selenium-manager --version)" = "selenium-manager %selenium_manager_version"


%if_enabled    java
%files         -n mvn-selenium -f selenium-java/.mfiles
%doc LICENSE NOTICE
%endif

%files

%files         -n cargo-selenium-manager-cli
%doc rust/LICENSE rust/NOTICE rust/README.md
%doc rust/selenium-manager-THIRD-PARTY-NOTICES.txt
%_bindir/selenium-manager

%files         -n gem-selenium-devtools
%doc LICENSE README.md
%ruby_gemspecdir/selenium-devtools-0.158.0.gemspec
%ruby_gemslibdir/selenium-devtools-0.158.0

%if_enabled    doc
%files         -n gem-selenium-devtools-doc
%doc LICENSE README.md
%ruby_gemsdocdir/selenium-devtools-0.158.0
%endif

%if_enabled    devel
%files         -n gem-selenium-devtools-devel
%doc LICENSE README.md
%endif

%files         -n gem-selenium-webdriver
%doc LICENSE README.md
%ruby_gemspecdir/selenium-webdriver-4.54.0.gemspec
%ruby_gemslibdir/selenium-webdriver-4.54.0

%if_enabled    doc
%files         -n gem-selenium-webdriver-doc
%doc LICENSE README.md
%ruby_gemsdocdir/selenium-webdriver-4.54.0
%endif

%if_enabled    devel
%files         -n gem-selenium-webdriver-devel
%doc LICENSE README.md
%endif

%if_enabled    devel
%files         -n selenium-devel
%endif


%changelog
* Wed Nov 25 2026 Pavel Skrylev <majioa@altlinux.org> 4.54.0-alt1
- ^ 4.50.0 -> 4.54.0
- + Added the Java WebDriver client as mvn-selenium.
- + Packaged Selenium Manager with its vendored Cargo sources.
- + Integrated the packaged Selenium Manager with the Java client.
- * Switched the Java build to XMvn and declared the Java runtime.
- ! Fixed the Maven generator version for the DevTools and BiDi modules.

* Mon Oct 05 2026 Pavel Skrylev <majioa@altlinux.org> 4.50.0-alt1
- ^ 4.38.0 -> 4.50.0

* Sun Nov 23 2025 Pavel Skrylev <majioa@altlinux.org> 4.38.0-alt1
- ^ 4.25.0 -> 4.38.0

* Mon Oct 28 2024 Pavel Skrylev <majioa@altlinux.org> 4.25.0-alt1
- ^ 4.19.0 -> 4.25.0

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 4.19.0-alt1
- ^ 3.142.7 -> 4.19.0

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.2
- ! fixed deps to gems

* Thu Apr 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.1
- + obsolete/provides pair for gem-selenium-webdriver

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1
- updated (^) 3.141.59 -> 3.142.7
- changed (*) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.141.59-alt1
- added (+) initial build with a packaged gem with usage Ruby Policy 2.0
