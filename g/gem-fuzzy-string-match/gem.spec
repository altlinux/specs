%define        gemname fuzzy-string-match

Name:          gem-fuzzy-string-match
Version:       1.0.1
Release:       alt1
Summary:       fuzzy string matching library
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/kiyoka/fuzzy-string-match
Vcs:           https://github.com/kiyoka/fuzzy-string-match.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 3.1.0
BuildRequires: gem(RubyInline) >= 3.8.6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(RubyInline) >= 3.8.6
Provides:      gem(fuzzy-string-match) = 1.0.1


%description
calculate Jaro Winkler distance.


%package       -n gem-fuzzy-string-match-doc
Version:       1.0.1
Release:       alt1
Summary:       fuzzy string matching library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fuzzy-string-match
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fuzzy-string-match) = 1.0.1

%description   -n gem-fuzzy-string-match-doc
fuzzy string matching library documentation files.

calculate Jaro Winkler distance.

%description   -n gem-fuzzy-string-match-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fuzzy-string-match.


%package       -n gem-fuzzy-string-match-devel
Version:       1.0.1
Release:       alt1
Summary:       fuzzy string matching library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fuzzy-string-match
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fuzzy-string-match) = 1.0.1
Requires:      gem(rspec) >= 3.1.0

%description   -n gem-fuzzy-string-match-devel
fuzzy string matching library development package.

calculate Jaro Winkler distance.

%description   -n gem-fuzzy-string-match-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fuzzy-string-match.


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

%files         -n gem-fuzzy-string-match-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-fuzzy-string-match-devel
%doc README.md


%changelog
* Sun May 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
