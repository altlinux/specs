%define        gemname strong_json

Name:          gem-strong-json
Version:       2.1.2
Release:       alt1
Summary:       Type check JSON objects
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/soutaro/strong_json
Vcs:           https://github.com/soutaro/strong_json.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(strong_json) = 2.1.2


%description
Type check JSON objects


%package       -n gem-strong-json-doc
Version:       2.1.2
Release:       alt1
Summary:       Type check JSON objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета strong_json
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(strong_json) = 2.1.2

%description   -n gem-strong-json-doc
Type check JSON objects documentation files.

%description   -n gem-strong-json-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета strong_json.


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

%files         -n gem-strong-json-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- + packaged gem with Ruby Policy 2.0
