%define        gemname digest-crc

Name:          gem-digest-crc
Version:       0.6.3
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/digest-crc#readme
Vcs:           https://github.com/postmodern/digest-crc.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 12.0.0 gem(rake) < 14.0.0
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(rspec)
BuildRequires: gem(rubygems-tasks)
BuildRequires: gem(yard)
BuildRequires: gem(kramdown)
BuildRequires: gem(kramdown-parser-gfm)
BuildRequires: gem(github-markup)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency github-markup >= 1,github-markup < 5
Requires:      gem(rake) >= 12.0.0 gem(rake) < 14.0.0
Provides:      gem(digest-crc) = 0.6.3

%ruby_on_build_rake_tasks build:c_exts

%description
Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.


%package       -n gem-digest-crc-doc
Version:       0.6.3
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest-crc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.6.3

%description   -n gem-digest-crc-doc
A Cyclic Redundancy Check (CRC) library for Ruby documentation files.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета digest-crc.


%package       -n gem-digest-crc-devel
Version:       0.6.3
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby development files
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest-crc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake) >= 12.0.0 gem(rake) < 14.0.0
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(rspec)
Requires:      gem(rubygems-tasks)
Requires:      gem(yard)
Requires:      gem(kramdown)
Requires:      gem(kramdown-parser-gfm)
Requires:      gem(github-markup)

%description   devel
Development files for %gemname gem.

%description   devel -l ru_RU.UTF8
Файлы заголовков для самоцвета %gemname.


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

%files         -n gem-digest-crc-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-digest-crc-devel
%ruby_includedir/*


%changelog
* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
