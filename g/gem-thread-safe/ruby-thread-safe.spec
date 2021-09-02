%define        gemname thread_safe

Name:          gem-thread-safe
Version:       0.3.6
Release:       alt2.1
Summary:       Thread-safe collections for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/ruby-concurrency/thread_safe
Vcs:           https://github.com/ruby-concurrency/thread_safe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(atomic) >= 1.1.16 gem(atomic) < 2
BuildRequires: gem(rake) >= 13.0.1 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.2 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency atomic >= 1.1.101,atomic < 2
%ruby_alias_names thread_safe,thread-safe
Obsoletes:     ruby-thread-safe < %EVR
Provides:      ruby-thread-safe = %EVR
Provides:      gem(thread_safe) = 0.3.6


%description
A collection of data structures and utilities to make thread-safe programming
in Ruby easier.


%package       -n gem-thread-safe-doc
Version:       0.3.6
Release:       alt2.1
Summary:       Thread-safe collections for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета thread_safe
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(thread_safe) = 0.3.6

%description   -n gem-thread-safe-doc
Thread-safe collections for Ruby documentation files.

A collection of data structures and utilities to make thread-safe programming
in Ruby easier.

%description   -n gem-thread-safe-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета thread_safe.


%package       -n gem-thread-safe-devel
Version:       0.3.6
Release:       alt2.1
Summary:       Thread-safe collections for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета thread_safe
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(thread_safe) = 0.3.6
Requires:      gem(atomic) >= 1.1.16 gem(atomic) < 2
Requires:      gem(rake) >= 13.0.1 gem(rake) < 14
Requires:      gem(rspec) >= 3.2 gem(rspec) < 4

%description   -n gem-thread-safe-devel
Thread-safe collections for Ruby development package.

A collection of data structures and utilities to make thread-safe programming
in Ruby easier.

%description   -n gem-thread-safe-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета thread_safe.


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

%files         -n gem-thread-safe-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-thread-safe-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.6-alt2.1
- ! spec

* Thu Aug 01 2019 Pavel Skrylev <majioa@altlinux.org> 0.3.6-alt2
^ Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus
