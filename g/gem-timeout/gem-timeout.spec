%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname timeout

Name:          gem-timeout
Version:       0.4.1
Release:       alt1
Summary:       Auto-terminate potentially long-running operations in Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/timeout
Vcs:           https://github.com/ruby/timeout.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(timeout) = 0.4.1


%description
Auto-terminate potentially long-running operations in Ruby.


%if_enabled    doc
%package       -n gem-timeout-doc
Version:       0.4.1
Release:       alt1
Summary:       Auto-terminate potentially long-running operations in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета timeout
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(timeout) = 0.4.1

%description   -n gem-timeout-doc
Auto-terminate potentially long-running operations in Ruby documentation files.

%description   -n gem-timeout-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета timeout.
%endif


%if_enabled    devel
%package       -n gem-timeout-devel
Version:       0.4.1
Release:       alt1
Summary:       Auto-terminate potentially long-running operations in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета timeout
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(timeout) = 0.4.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-timeout-devel
Auto-terminate potentially long-running operations in Ruby development package.

%description   -n gem-timeout-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета timeout.
%endif


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

%if_enabled    doc
%files         -n gem-timeout-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-timeout-devel
%doc README.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
