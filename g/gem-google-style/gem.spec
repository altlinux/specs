%define        gemname google-style

Name:          gem-google-style
Version:       1.25.1
Release:       alt1
Summary:       Collection of rubocop rules
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/ruby-style/tree/master/
Vcs:           https://github.com/googleapis/ruby-style.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rubocop) >= 1.9 gem(rubocop) < 2
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 1.9 gem(rubocop) < 2
Provides:      gem(google-style) = 1.25.1


%description
Shared style guide for Google's ruby projects


%package       -n gem-google-style-devel
Version:       1.25.1
Release:       alt1
Summary:       Collection of rubocop rules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-style
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-style) = 1.25.1
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rake) >= 12.3 gem(rake) < 14

%description   -n gem-google-style-devel
Collection of rubocop rules development package.

Shared style guide for Google's ruby projects

%description   -n gem-google-style-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-style.


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

%files         -n gem-google-style-devel
%doc README.md


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.25.1-alt1
- + packaged gem with Ruby Policy 2.0
