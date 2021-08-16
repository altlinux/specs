%define        gemname indexer

Name:          gem-indexer
Version:       0.3.0
Release:       alt1
Summary:       Enable Your Project's Metadata
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.com/indexer
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(nokogiri) >= 1.5
BuildRequires: gem(kramdown) >= 0.14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names index
Requires:      gem(nokogiri) >= 1.5
Requires:      gem(kramdown) >= 0.14
Provides:      gem(indexer) = 0.3.0


%description
Indexer provides projects with a universal metadata format.


%package       -n index
Version:       0.3.0
Release:       alt1
Summary:       Enable Your Project's Metadata executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета indexer
Group:         Other
BuildArch:     noarch

Requires:      gem(indexer) = 0.3.0

%description   -n index
Enable Your Project's Metadata executable(s).

Indexer provides projects with a universal metadata format.

%description   -n index -l ru_RU.UTF-8
Исполнямка для самоцвета indexer.


%package       -n gem-indexer-doc
Version:       0.3.0
Release:       alt1
Summary:       Enable Your Project's Metadata documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета indexer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(indexer) = 0.3.0

%description   -n gem-indexer-doc
Enable Your Project's Metadata documentation files.

Indexer provides projects with a universal metadata format.

%description   -n gem-indexer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета indexer.


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

%files         -n index
%doc README.md
%_bindir/index

%files         -n gem-indexer-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
