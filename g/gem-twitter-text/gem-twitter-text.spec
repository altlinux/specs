%define        gemname twitter-text

Name:          gem-twitter-text
Version:       3.1.0.1
Release:       alt1.1
Summary:       Twitter Text Libraries
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/twitter/twitter-text
Vcs:           https://github.com/twitter/twitter-text.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(multi_json) >= 1.3
BuildRequires: gem(nokogiri) >= 1.10.9
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(unf) >= 0.1.0
BuildRequires: gem(idn-ruby) >= 0
BuildConflicts: gem(multi_json) >= 2
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(unf) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency unf >= 0.2.0.1,unf < 1
%ruby_use_gem_dependency nokogiri >= 1.15.5,nokogiri < 2
Requires:      gem(unf) >= 0.1.0
Requires:      gem(idn-ruby) >= 0
Conflicts:     gem(unf) >= 1
Obsoletes:     twitter-text < %EVR
Provides:      twitter-text = %EVR
Provides:      gem(twitter-text) = 3.1.0.1

%ruby_use_gem_version twitter-text:3.1.0.1

%description
This repo is a collection of libraries and conformance tests to standardize
parsing of Tweet text. It synchronizes development, testing, creating issues,
and pull requests for twitter-text's implementations and specification. These
libraries are responsible for determining the quantity of characters in a Tweet
and identifying and linking any url, @username, #hashtag, or $cashtag.


%package       -n gem-twitter-text-doc
Version:       3.1.0.1
Release:       alt1.1
Summary:       Twitter Text Libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета twitter-text
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(twitter-text) = 3.1.0.1

%description   -n gem-twitter-text-doc
Twitter Text Libraries documentation files.

This repo is a collection of libraries and conformance tests to standardize
parsing of Tweet text. It synchronizes development, testing, creating issues,
and pull requests for twitter-text's implementations and specification. These
libraries are responsible for determining the quantity of characters in a Tweet
and identifying and linking any url, @username, #hashtag, or $cashtag.

%description   -n gem-twitter-text-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета twitter-text.


%package       -n gem-twitter-text-devel
Version:       3.1.0.1
Release:       alt1.1
Summary:       Twitter Text Libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета twitter-text
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(twitter-text) = 3.1.0.1
Requires:      gem(test-unit) >= 0
Requires:      gem(multi_json) >= 1.3
Requires:      gem(nokogiri) >= 1.10.9
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(multi_json) >= 2
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-twitter-text-devel
Twitter Text Libraries development package.

This repo is a collection of libraries and conformance tests to standardize
parsing of Tweet text. It synchronizes development, testing, creating issues,
and pull requests for twitter-text's implementations and specification. These
libraries are responsible for determining the quantity of characters in a Tweet
and identifying and linking any url, @username, #hashtag, or $cashtag.

%description   -n gem-twitter-text-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета twitter-text.


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

%files         -n gem-twitter-text-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-twitter-text-devel
%doc README.md


%changelog
* Thu Dec 07 2023 Pavel Skrylev <majioa@altlinux.org> 3.1.0.1-alt1.1
- ! fixed spec format

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.0.1-alt1
- ^ 3.1.0 -> 3.1.0.1

* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.1 -> 3.1.0
- * recomsotions packages in spec

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
