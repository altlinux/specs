%define        gemname simplecov_json_formatter

Name:          gem-simplecov-json-formatter
Version:       0.1.2
Release:       alt1
Summary:       JSON formatter for SimpleCov
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fede-moya/simplecov_json_formatter
Vcs:           https://github.com/fede-moya/simplecov_json_formatter.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names simplecov_json_formatter,simplecov-json-formatter
Provides:      gem(simplecov_json_formatter) = 0.1.2

%description
JSON formatter for SimpleCov.


%package       -n gem-simplecov-json-formatter-doc
Version:       0.1.2
Release:       alt1
Summary:       JSON formatter for SimpleCov documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov_json_formatter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov_json_formatter) = 0.1.2

%description   -n gem-simplecov-json-formatter-doc
JSON formatter for SimpleCov documentation files.

JSON formatter for SimpleCov.

%description   -n gem-simplecov-json-formatter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov_json_formatter.


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

%files         -n gem-simplecov-json-formatter-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Apr 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0
