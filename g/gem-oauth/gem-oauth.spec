%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname oauth

Name:          gem-oauth
Version:       1.1.3
Release:       alt1
Summary:       OAuth Core Ruby implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth-ruby
Vcs:           https://github.com/oauth-xx/oauth-ruby.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-apache2
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: zlib-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
%if_enabled check
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(appraisal2) >= 3.0
BuildRequires: gem(backports) >= 3.25.1
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(benchmark) >= 0.4.1
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(em-http-request) >= 1.1.7
BuildRequires: gem(erb) >= 5.0
BuildRequires: gem(gem_bench) >= 2.0.5
BuildRequires: gem(gitmoji-regex) >= 1.0.3
BuildRequires: gem(irb) >= 1.15.2
BuildRequires: gem(kettle-dev) >= 1.1
BuildRequires: gem(kettle-soup-cover) >= 1.0.10
BuildRequires: gem(kettle-test) >= 1.0.6
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(mutex_m) >= 0.2
BuildRequires: gem(oauth-tty) >= 1.0.6
BuildRequires: gem(rack) >= 2.0.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rails) >= 5.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.5
BuildRequires: gem(require_bench) >= 1.0.4
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rubocop-lts) >= 10.0
BuildRequires: gem(rubocop-on-rbs) >= 1.8
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rspec) >= 3.6
BuildRequires: gem(rubocop-ruby2_3) >= 0
BuildRequires: gem(ruby-progressbar) >= 1.13
BuildRequires: gem(snaky_hash) >= 2.0
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(stone_checksums) >= 1.0.2
BuildRequires: gem(stringio) >= 3.0
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(vcr) >= 4
BuildRequires: gem(version_gem) >= 1.1.9
BuildRequires: gem(webmock) >= 3
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(backports) >= 4
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(em-http-request) >= 1.2
BuildConflicts: gem(erb) >= 6
BuildConflicts: gem(gem_bench) >= 3
BuildConflicts: gem(gitmoji-regex) >= 2
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(kettle-dev) >= 2
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kettle-test) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(mutex_m) >= 1
BuildConflicts: gem(oauth-tty) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(require_bench) >= 2
BuildConflicts: gem(rubocop-lts) >= 11
BuildConflicts: gem(rubocop-on-rbs) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(snaky_hash) >= 3
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(version_gem) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.3
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(base64) >= 0.1
Requires:      gem(oauth-tty) >= 1.0.6
Requires:      gem(snaky_hash) >= 2.0
Requires:      gem(version_gem) >= 1.1.9
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(base64) >= 1
Conflicts:     gem(oauth-tty) >= 2
Conflicts:     gem(snaky_hash) >= 3
Conflicts:     gem(version_gem) >= 2
Provides:      gem(oauth) = 1.1.3

%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.


%if_enabled    doc
%package       -n gem-oauth-doc
Version:       1.1.3
Release:       alt1
Summary:       OAuth Core Ruby implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(oauth) = 1.1.3

%description   -n gem-oauth-doc
OAuth Core Ruby implementation documentation files.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth.
%endif


%if_enabled    devel
%package       -n gem-oauth-devel
Version:       1.1.3
Release:       alt1
Summary:       OAuth Core Ruby implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      apache2-devel >= 2.2.5
Requires:      zlib-devel
Requires:      libapr1-devel
Requires:      libaprutil1-devel
Requires:      libssl-devel
Requires:      libcurl-devel
Requires:      apache2-httpd-worker
Requires:      gcc-c++
Requires:      gem(oauth) = 1.1.3
Requires:      gem(appraisal2) >= 3.0
Requires:      gem(backports) >= 3.25.1
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(gitmoji-regex) >= 1.0.3
Requires:      gem(kettle-dev) >= 1.1
Requires:      gem(kettle-test) >= 1.0.6
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(require_bench) >= 1.0.4
Requires:      gem(rest-client) >= 0
Requires:      gem(ruby-progressbar) >= 1.13
Requires:      gem(stone_checksums) >= 1.0.2
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(vcr) >= 4
Requires:      gem(webmock) >= 3
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(backports) >= 4
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(gitmoji-regex) >= 2
Conflicts:     gem(kettle-dev) >= 2
Conflicts:     gem(kettle-test) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(require_bench) >= 2
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(stone_checksums) >= 2

%description   -n gem-oauth-devel
OAuth Core Ruby implementation development package.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-oauth-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oauth-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Sat Mar 21 2026 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.2 -> 1.1.3

* Fri Oct 17 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.0p18 -> 1.1.2

* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0.18-alt0.1
- ^ 1.1.0[1] -> 1.1.0p18

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0.1-alt1
- ^ 1.1.0 -> 1.1.0[1]

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 0.5.6 -> 1.1.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt1
- + packaged gem with Ruby Policy 2.0
