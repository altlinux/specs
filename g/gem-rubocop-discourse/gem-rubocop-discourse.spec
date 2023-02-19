%define        gemname rubocop-discourse

Name:          gem-rubocop-discourse
Version:       2.6.0
Release:       alt1
Summary:       Custom rubocop cops used by Discourse
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/discourse/rubocop-discourse
Vcs:           https://github.com/discourse/rubocop-discourse.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rubocop) >= 1.1.0
BuildRequires: gem(rubocop-rspec) >= 2.0.0
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rubocop) >= 1.1.0
Requires:      gem(rubocop-rspec) >= 2.0.0
Provides:      gem(rubocop-discourse) = 2.6.0


%description
Custom rubocop cops used by Discourse.


%package       -n gem-rubocop-discourse-doc
Version:       2.6.0
Release:       alt1
Summary:       Custom rubocop cops used by Discourse documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubocop-discourse
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubocop-discourse) = 2.6.0

%description   -n gem-rubocop-discourse-doc
Custom rubocop cops used by Discourse documentation files.

%description   -n gem-rubocop-discourse-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubocop-discourse.


%package       -n gem-rubocop-discourse-devel
Version:       2.6.0
Release:       alt1
Summary:       Custom rubocop cops used by Discourse development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubocop-discourse
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubocop-discourse) = 2.6.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 0
Requires:      gem(byebug) >= 0
Conflicts:     gem(rake) >= 14

%description   -n gem-rubocop-discourse-devel
Custom rubocop cops used by Discourse development package.

%description   -n gem-rubocop-discourse-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubocop-discourse.


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

%files         -n gem-rubocop-discourse-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubocop-discourse-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- ^ 2.4.2 -> 2.6.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt1
- + packaged gem with Ruby Policy 2.0
