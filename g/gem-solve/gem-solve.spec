%define        gemname solve

Name:          gem-solve
Version:       4.0.4
Release:       alt1
Summary:       A Ruby version constraint solver implementing Semantic Versioning 2.0.0-rc.1
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/berkshelf/solve
Vcs:           https://github.com/berkshelf/solve.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(thor) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(spork) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(dep_selector) >= 1.0
BuildRequires: gem(fuubar) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-spork) >= 0
BuildRequires: gem(guard-yard) >= 0
BuildRequires: gem(coolline) >= 0
BuildRequires: gem(libnotify) >= 0
BuildRequires: gem(semverse) >= 1.1
BuildRequires: gem(molinillo) >= 0.6
BuildConflicts: gem(dep_selector) >= 2
BuildConflicts: gem(semverse) >= 4.0
BuildConflicts: gem(molinillo) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(semverse) >= 1.1
Requires:      gem(molinillo) >= 0.6
Conflicts:     gem(semverse) >= 4.0
Conflicts:     gem(molinillo) >= 1
Provides:      gem(solve) = 4.0.4


%description
A Ruby version constraint solver


%package       -n gem-solve-doc
Version:       4.0.4
Release:       alt1
Summary:       A Ruby version constraint solver implementing Semantic Versioning 2.0.0-rc.1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета solve
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(solve) = 4.0.4

%description   -n gem-solve-doc
A Ruby version constraint solver implementing Semantic Versioning 2.0.0-rc.1
documentation files.

%description   -n gem-solve-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета solve.


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

%files         -n gem-solve-doc
%ruby_gemdocdir


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 4.0.4-alt1
- + packaged gem with Ruby Policy 2.0 (no devel)
