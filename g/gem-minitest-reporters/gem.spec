%define        gemname minitest-reporters

Name:          gem-minitest-reporters
Version:       1.4.3
Release:       alt1
Summary:       Create customizable Minitest output formats
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/CapnKernul/minitest-reporters
Vcs:           https://github.com/capnkernul/minitest-reporters.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.0 gem(minitest) < 6
BuildRequires: gem(ansi) >= 0
BuildRequires: gem(ruby-progressbar) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(rubocop) >= 0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
Requires:      gem(minitest) >= 5.0 gem(minitest) < 6
Requires:      gem(ansi) >= 0
Requires:      gem(ruby-progressbar) >= 0
Requires:      gem(builder) >= 0
Provides:      gem(minitest-reporters) = 1.4.3


%description
Death to haphazard monkey-patching! Extend Minitest through simple hooks.


%package       -n gem-minitest-reporters-doc
Version:       1.4.3
Release:       alt1
Summary:       Create customizable Minitest output formats documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-reporters
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-reporters) = 1.4.3

%description   -n gem-minitest-reporters-doc
Create customizable Minitest output formats documentation files.

Death to haphazard monkey-patching! Extend Minitest through simple hooks.

%description   -n gem-minitest-reporters-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-reporters.


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

%files         -n gem-minitest-reporters-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- + packaged gem with Ruby Policy 2.0
