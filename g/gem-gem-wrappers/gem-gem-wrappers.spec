%define        _unpackaged_files_terminate_build 1
%define        gemname gem-wrappers

Name:          gem-gem-wrappers
Version:       1.4.0
Release:       alt1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/rvm/gem-wrappers
Vcs:           https://github.com/rvm/gem-wrappers.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(rubysl-mutex_m) >= 0
BuildRequires: gem(rubysl-singleton) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(gem-wrappers) = 1.4.0


%description
Create gem wrappers for easy use of gems in cron and other system locations.


%package       -n gem-gem-wrappers-doc
Version:       1.4.0
Release:       alt1
Summary:       Create gem wrappers for easy use of gems in cron and other system locations documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-wrappers
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-wrappers) = 1.4.0

%description   -n gem-gem-wrappers-doc
Create gem wrappers for easy use of gems in cron and other system locations
documentation files.

%description   -n gem-gem-wrappers-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-wrappers.


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
%ruby_gemextdir

%files         -n gem-gem-wrappers-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0 without devel
