%define        _unpackaged_files_terminate_build 1
%define        gemname ruby-mysql

Name:          gem-ruby-mysql
Version:       4.1.0
Release:       alt1
Summary:       MySQL connector
License:       MIT
Group:         Development/Ruby
Url:           http://gitlab.com/tmtms/ruby-mysql
Vcs:           http://gitlab.com/tmtms/ruby-mysql.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(power_assert) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ruby-mysql) = 4.1.0


%description
This is MySQL connector. pure Ruby version


%package       -n gem-ruby-mysql-doc
Version:       4.1.0
Release:       alt1
Summary:       MySQL connector documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-mysql
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-mysql) = 4.1.0

%description   -n gem-ruby-mysql-doc
MySQL connector documentation files.

This is MySQL connector. pure Ruby version

%description   -n gem-ruby-mysql-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-mysql.


%package       -n gem-ruby-mysql-devel
Version:       4.1.0
Release:       alt1
Summary:       MySQL connector development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-mysql
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-mysql) = 4.1.0
Requires:      gem(power_assert) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0

%description   -n gem-ruby-mysql-devel
MySQL connector development package.

This is MySQL connector. pure Ruby version

%description   -n gem-ruby-mysql-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-mysql.


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

%files         -n gem-ruby-mysql-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ruby-mysql-devel
%doc README.md


%changelog
* Wed Jan 24 2024 Pavel Skrylev <majioa@altlinux.org> 4.1.0-alt1
- + packaged gem with Ruby Policy 2.0
