%define        gemname vcr

Name:          gem-vcr
Version:       6.0.0
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
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(test-unit) >= 3.1.4 gem(test-unit) < 4
BuildRequires: gem(rake) >= 10.1 gem(rake) < 14
BuildRequires: gem(pry) >= 0.9 gem(pry) < 1
BuildRequires: gem(pry-doc) >= 0.6 gem(pry-doc) < 2
BuildRequires: gem(codeclimate-test-reporter) >= 0.4 gem(codeclimate-test-reporter) < 2
BuildRequires: gem(yard) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(hashdiff) >= 1.0.0.beta1 gem(hashdiff) < 2.0.0
# BuildRequires: gem(cucumber) >= 3.1 gem(cucumber) < 4
# BuildRequires: gem(aruba) >= 0.14.14 gem(aruba) < 0.15
BuildRequires: gem(faraday) >= 0.11.0 gem(faraday) < 2.0.0
BuildRequires: gem(httpclient) >= 0
BuildRequires: gem(excon) >= 0.62.0
BuildRequires: gem(timecop) >= 0
BuildRequires: gem(json) >= 0
# BuildRequires: gem(relish) >= 0
BuildRequires: gem(mime-types) >= 0
BuildRequires: gem(sinatra) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency pry-doc >= 1.1.0,pry-doc < 2
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
Provides:      gem(vcr) = 6.0.0


%description
Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.


%package       -n gem-vcr-doc
Version:       6.0.0
Release:       alt1
Summary:       Record your test suite's HTTP interactions and replay them during future test runs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vcr
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vcr) = 6.0.0

%description   -n gem-vcr-doc
Record your test suite's HTTP interactions and replay them during future test
runs documentation files.

Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.

%description   -n gem-vcr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vcr.


%package       -n gem-vcr-devel
Version:       6.0.0
Release:       alt1
Summary:       Record your test suite's HTTP interactions and replay them during future test runs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vcr
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vcr) = 6.0.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(test-unit) >= 3.1.4 gem(test-unit) < 4
Requires:      gem(rake) >= 10.1 gem(rake) < 14
Requires:      gem(pry) >= 0.9 gem(pry) < 1
Requires:      gem(pry-doc) >= 0.6 gem(pry-doc) < 2
Requires:      gem(codeclimate-test-reporter) >= 0.4 gem(codeclimate-test-reporter) < 2
Requires:      gem(yard) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(hashdiff) >= 1.0.0.beta1 gem(hashdiff) < 2.0.0
# Requires:      gem(cucumber) >= 3.1 gem(cucumber) < 4
# Requires:      gem(aruba) >= 0.14.14 gem(aruba) < 0.15
Requires:      gem(faraday) >= 0.11.0 gem(faraday) < 2.0.0
Requires:      gem(httpclient) >= 0
Requires:      gem(excon) >= 0.62.0
Requires:      gem(timecop) >= 0
Requires:      gem(json) >= 0
# Requires:      gem(relish) >= 0
Requires:      gem(mime-types) >= 0
Requires:      gem(sinatra) >= 0

%description   -n gem-vcr-devel
Record your test suite's HTTP interactions and replay them during future test
runs development package.

Record your test suite's HTTP interactions and replay them during future test
runs for fast, deterministic, accurate tests.

%description   -n gem-vcr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vcr.


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

%files         -n gem-vcr-devel


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt1
- ^ 5.0.0 -> 6.0.0

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
