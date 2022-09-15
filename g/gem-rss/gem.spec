%define        gemname rss

Name:          gem-rss
Version:       0.2.9
Release:       alt1
Summary:       Family of libraries that support various formats of XML "feeds"
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/rss
Vcs:           https://github.com/ruby/rss.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rexml) >= 0
Provides:      gem(rss) = 0.2.9


%description
Family of libraries that support various formats of XML "feeds".


%package       -n gem-rss-doc
Version:       0.2.9
Release:       alt1
Summary:       Family of libraries that support various formats of XML "feeds" documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rss
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rss) = 0.2.9

%description   -n gem-rss-doc
Family of libraries that support various formats of XML "feeds" documentation
files.

%description   -n gem-rss-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rss.


%package       -n gem-rss-devel
Version:       0.2.9
Release:       alt1
Summary:       Family of libraries that support various formats of XML "feeds" development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rss
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rss) = 0.2.9
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-rss-devel
Family of libraries that support various formats of XML "feeds" development
package.

%description   -n gem-rss-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rss.


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

%files         -n gem-rss-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rss-devel
%doc README.md


%changelog
* Mon Apr 04 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.9-alt1
- + packaged gem with Ruby Policy 2.0
