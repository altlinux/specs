%define        gemname latest_ruby

Name:          gem-latest-ruby
Version:       3.0.1
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is
License:       zlib
Group:         Development/Ruby
Url:           https://github.com/kyrylo/latest_ruby
Vcs:           https://github.com/kyrylo/latest_ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(pry) >= 0 gem(pry) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Requires:      gem(rexml) >= 0
Provides:      gem(latest_ruby) = 3.0.1


%description
Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.


%package       -n gem-latest-ruby-doc
Version:       3.0.1
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета latest_ruby
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(latest_ruby) = 3.0.1

%description   -n gem-latest-ruby-doc
Answers the question of what the latest Ruby version is documentation
files.

Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.

%description   -n gem-latest-ruby-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета latest_ruby.


%package       -n gem-latest-ruby-devel
Version:       3.0.1
Release:       alt1
Summary:       Answers the question of what the latest Ruby version is development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета latest_ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(latest_ruby) = 3.0.1
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(pry) >= 0 gem(pry) < 1

%description   -n gem-latest-ruby-devel
Answers the question of what the latest Ruby version is development
package.

Knows about MRI, Rubinius, JRuby, MagLev and MacRuby.

%description   -n gem-latest-ruby-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета latest_ruby.


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

%files         -n gem-latest-ruby-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-latest-ruby-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- + packaged gem with Ruby Policy 2.0
