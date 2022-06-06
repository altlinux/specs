%define        gemname rspec_junit_formatter

Name:          gem-rspec-junit-formatter
Version:       0.5.1
Release:       alt1
Summary:       RSpec JUnit XML formatter
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sj26/rspec_junit_formatter
Vcs:           https://github.com/sj26/rspec_junit_formatter.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec-core) >= 2 gem(rspec-core) < 4 gem(rspec-core) > 2.12.0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(nokogiri) >= 1.8.2 gem(nokogiri) < 2
BuildRequires: gem(rake) >= 0
BuildRequires: gem(coderay) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rspec-core) >= 2 gem(rspec-core) < 4 gem(rspec-core) > 2.12.0
Provides:      gem(rspec_junit_formatter) = 0.5.1


%description
RSpec results that your continuous integration service can read. RSpec 2 & 3
results that your CI can read. Jenkins, Buildkite, CircleCI, Gitlab, and
probably more, too.


%package       -n gem-rspec-junit-formatter-doc
Version:       0.5.1
Release:       alt1
Summary:       RSpec JUnit XML formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec_junit_formatter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rspec_junit_formatter) = 0.5.1

%description   -n gem-rspec-junit-formatter-doc
RSpec JUnit XML formatter documentation files.

RSpec results that your continuous integration service can read. RSpec 2 & 3
results that your CI can read. Jenkins, Buildkite, CircleCI, Gitlab, and
probably more, too.

%description   -n gem-rspec-junit-formatter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec_junit_formatter.


%package       -n gem-rspec-junit-formatter-devel
Version:       0.5.1
Release:       alt1
Summary:       RSpec JUnit XML formatter development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec_junit_formatter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rspec_junit_formatter) = 0.5.1
Requires:      gem(bundler) >= 0
Requires:      gem(appraisal) >= 0
Requires:      gem(nokogiri) >= 1.8.2 gem(nokogiri) < 2
Requires:      gem(rake) >= 0
Requires:      gem(coderay) >= 0

%description   -n gem-rspec-junit-formatter-devel
RSpec JUnit XML formatter development package.

RSpec results that your continuous integration service can read. RSpec 2 & 3
results that your CI can read. Jenkins, Buildkite, CircleCI, Gitlab, and
probably more, too.

%description   -n gem-rspec-junit-formatter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec_junit_formatter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rspec-junit-formatter-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rspec-junit-formatter-devel
%doc README.md


%changelog
* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with Ruby Policy 2.0
