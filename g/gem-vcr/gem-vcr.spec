%define        gemname vcr

Name:          gem-vcr
Version:       6.1.0
Release:       alt1
Summary:       Record your test suite's HTTP interactions and replay them during future test runs
License:       Hippocratic-2.1 or MIT
Group:         Development/Ruby
Url:           https://github.com/vcr/vcr
Vcs:           https://github.com/vcr/vcr.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(faraday) >= 0.11.0
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(pry) >= 0.9
BuildRequires: gem(pry-doc) >= 0.6
BuildRequires: gem(codeclimate-test-reporter) >= 0.4
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(hashdiff) >= 1.0.0
BuildRequires: gem(cucumber) >= 7.0
BuildRequires: gem(aruba) >= 0.14.14
BuildRequires: gem(httpclient) >= 0
BuildRequires: gem(excon) >= 0.62.0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(relish) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(sinatra) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(typhoeus) >= 1.1.0
BuildRequires: gem(patron) = 0.6.3
BuildRequires: gem(em-http-request) >= 0
BuildRequires: gem(curb) >= 0.9.0
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(pry-doc) >= 1
BuildConflicts: gem(codeclimate-test-reporter) >= 2
BuildConflicts: gem(hashdiff) >= 2.0.0
BuildConflicts: gem(cucumber) >= 8
BuildConflicts: gem(aruba) >= 0.15
BuildConflicts: gem(typhoeus) >= 1.2
BuildConflicts: gem(curb) >= 0.10
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
Provides:      gem(vcr) = 6.1.0


%description
Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.


%package       -n gem-vcr-doc
Version:       6.1.0
Release:       alt1
Summary:       Record your test suite's HTTP interactions and replay them during future test runs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vcr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vcr) = 6.1.0

%description   -n gem-vcr-doc
Record your test suite's HTTP interactions and replay them during future test
runs documentation files.

Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.

%description   -n gem-vcr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vcr.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-vcr-doc
%ruby_gemdocdir


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 6.1.0-alt1
- ^ 6.0.0 -> 6.1.0 (no devel)

* Wed Oct 19 2022 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1.1
- !dep for build requires to novel gems

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.0.0 -> 6.0.0

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
