%define        gemname numerizer

Name:          gem-numerizer
Version:       0.2.0
Release:       alt1
Summary:       Numerizer is a gem to help with parsing numbers in natural language from strings (ex forty two)
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jduff/numerizer
Vcs:           https://github.com/jduff/numerizer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(numerizer) = 0.2.0


%description
Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two). It was extracted from the awesome Chronic gem
http://github.com/evaryont/chronic.


%package       -n gem-numerizer-doc
Version:       0.2.0
Release:       alt1
Summary:       Numerizer is a gem to help with parsing numbers in natural language from strings (ex forty two) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета numerizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(numerizer) = 0.2.0

%description   -n gem-numerizer-doc
Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two) documentation files.

Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two). It was extracted from the awesome Chronic gem
http://github.com/evaryont/chronic.

%description   -n gem-numerizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета numerizer.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-numerizer-doc
%doc README.rdoc
%ruby_gemdocdir


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
