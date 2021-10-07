%define        gemname mercenary

Name:          gem-mercenary
Version:       0.4.0
Release:       alt1.1
Summary:       Lightweight and flexible library for writing command-line apps in Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jekyll/mercenary
Vcs:           https://github.com/jekyll/mercenary.git
Packager:      Dmitriy Voropaev <voropaevdmtr@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(rubocop-jekyll) >= 0.10.0 gem(rubocop-jekyll) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop-jekyll >= 0.11.0,rubocop-jekyll < 1
Provides:      gem(mercenary) = 0.4.0


%description
Lightweight and flexible library for writing command-line apps in Ruby.


%package       -n gem-mercenary-doc
Version:       0.4.0
Release:       alt1.1
Summary:       Lightweight and flexible library for writing command-line apps in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mercenary
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mercenary) = 0.4.0

%description   -n gem-mercenary-doc
Lightweight and flexible library for writing command-line apps in Ruby
documentation files.

%description   -n gem-mercenary-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mercenary.


%package       -n gem-mercenary-devel
Version:       0.4.0
Release:       alt1.1
Summary:       Lightweight and flexible library for writing command-line apps in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mercenary
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mercenary) = 0.4.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(rubocop-jekyll) >= 0.10.0 gem(rubocop-jekyll) < 1

%description   -n gem-mercenary-devel
Lightweight and flexible library for writing command-line apps in Ruby
development package.

%description   -n gem-mercenary-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mercenary.


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

%files         -n gem-mercenary-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mercenary-devel
%doc README.md


%changelog
* Tue Sep 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1.1
- ! spec

* Tue Mar 16 2021 Dmitriy Voropaev <voropaevdmtr@altlinux.org> 0.4.0-alt1
- initial build
