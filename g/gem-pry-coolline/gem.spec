%define        gemname pry-coolline

Name:          gem-pry-coolline
Version:       0.2.5
Release:       alt1
Summary:       Live syntax-highlighting for the Pry REPL
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pry/pry-coolline
Vcs:           https://github.com/pry/pry-coolline.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(coolline) >= 0.5 gem(coolline) < 1
BuildRequires: gem(riot) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(coolline) >= 0.5 gem(coolline) < 1
Provides:      gem(pry-coolline) = 0.2.5


%description
Live syntax-highlighting for the Pry REPL. The pry-coolline plugin provides
live syntax highlighting for the Pry REPL for Ruby 1.9.2+ (MRI).

It makes use of the coolline gem and the io/console library.
* Install the gem: gem install pry-coolline
* See the source code


%package       -n gem-pry-coolline-doc
Version:       0.2.5
Release:       alt1
Summary:       Live syntax-highlighting for the Pry REPL documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-coolline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-coolline) = 0.2.5

%description   -n gem-pry-coolline-doc
Live syntax-highlighting for the Pry REPL documentation files.

Live syntax-highlighting for the Pry REPL. The pry-coolline plugin provides
live syntax highlighting for the Pry REPL for Ruby 1.9.2+ (MRI).

It makes use of the coolline gem and the io/console library.
* Install the gem: gem install pry-coolline
* See the source code


%description   -n gem-pry-coolline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-coolline.


%package       -n gem-pry-coolline-devel
Version:       0.2.5
Release:       alt1
Summary:       Live syntax-highlighting for the Pry REPL development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-coolline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-coolline) = 0.2.5
Requires:      gem(riot) >= 0

%description   -n gem-pry-coolline-devel
Live syntax-highlighting for the Pry REPL development package.

Live syntax-highlighting for the Pry REPL. The pry-coolline plugin provides
live syntax highlighting for the Pry REPL for Ruby 1.9.2+ (MRI).

It makes use of the coolline gem and the io/console library.
* Install the gem: gem install pry-coolline
* See the source code


%description   -n gem-pry-coolline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-coolline.


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

%files         -n gem-pry-coolline-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-pry-coolline-devel
%doc README.md


%changelog
* Wed Jul 14 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt1
- + packaged gem with Ruby Policy 2.0
