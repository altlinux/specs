%define        _unpackaged_files_terminate_build 1
%define        gemname simplecov-json

Name:          gem-simplecov-json
Version:       0.2
Release:       alt1
Summary:       JSON formatter for SimpleCov code coverage tool for ruby 1.9+
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/vicentllongo/simplecov-json
Vcs:           https://github.com/vicentllongo/simplecov-json.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(mocha) >= 0.14
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(json) >= 0
BuildConflicts: gem(mocha) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
Requires:      gem(simplecov) >= 0
Requires:      gem(json) >= 0
Provides:      gem(simplecov-json) = 0.2


%description
JSON formatter for SimpleCov code coverage tool for ruby 1.9+


%package       -n gem-simplecov-json-doc
Version:       0.2
Release:       alt1
Summary:       JSON formatter for SimpleCov code coverage tool for ruby 1.9+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-json) = 0.2

%description   -n gem-simplecov-json-doc
JSON formatter for SimpleCov code coverage tool for ruby 1.9+ documentation
files.

%description   -n gem-simplecov-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-json.


%package       -n gem-simplecov-json-devel
Version:       0.2
Release:       alt1
Summary:       JSON formatter for SimpleCov code coverage tool for ruby 1.9+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov-json
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simplecov-json) = 0.2
Requires:      gem(rake) >= 0
Requires:      gem(mocha) >= 0.14
Conflicts:     gem(mocha) >= 2

%description   -n gem-simplecov-json-devel
JSON formatter for SimpleCov code coverage tool for ruby 1.9+ development
package.

%description   -n gem-simplecov-json-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov-json.


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

%files         -n gem-simplecov-json-doc
%ruby_gemdocdir

%files         -n gem-simplecov-json-devel


%changelog
* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 0.2-alt1
- + packaged gem with Ruby Policy 2.0
