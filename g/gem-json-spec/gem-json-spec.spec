%define        gemname json_spec

Name:          gem-json-spec
Version:       1.1.5
Release:       alt1
Summary:       Easily handle JSON in RSpec and Cucumber
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/collectiveidea/json_spec
Vcs:           https://github.com/collectiveidea/json_spec.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(cucumber) >= 1.3 gem(cucumber) < 2
BuildRequires: gem(multi_json) >= 1.0 gem(multi_json) < 2
BuildRequires: gem(rspec) >= 2.0 gem(rspec) < 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(multi_json) >= 1.0 gem(multi_json) < 2
Requires:      gem(rspec) >= 2.0 gem(rspec) < 4
Provides:      gem(json_spec) = 1.1.5


%description
RSpec matchers and Cucumber steps for testing JSON content


%package       -n gem-json-spec-doc
Version:       1.1.5
Release:       alt1
Summary:       Easily handle JSON in RSpec and Cucumber documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета json_spec
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(json_spec) = 1.1.5

%description   -n gem-json-spec-doc
Easily handle JSON in RSpec and Cucumber documentation files.

RSpec matchers and Cucumber steps for testing JSON content

%description   -n gem-json-spec-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета json_spec.


%package       -n gem-json-spec-devel
Version:       1.1.5
Release:       alt1
Summary:       Easily handle JSON in RSpec and Cucumber development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета json_spec
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(json_spec) = 1.1.5
Requires:      gem(bundler) >= 1.0 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14

%description   -n gem-json-spec-devel
Easily handle JSON in RSpec and Cucumber development package.

RSpec matchers and Cucumber steps for testing JSON content

%description   -n gem-json-spec-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета json_spec.


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

%files         -n gem-json-spec-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-json-spec-devel
%doc README.md


%changelog
* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.5-alt1
- + packaged gem with Ruby Policy 2.0
