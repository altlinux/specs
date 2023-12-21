%define        _unpackaged_files_terminate_build 1
%define        gemname yard-junk

Name:          gem-yard-junk
Version:       0.0.9
Release:       alt1
Summary:       Get rid of the junk in your YARD docs
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zverok/junk_yard
Vcs:           https://github.com/zverok/junk_yard.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rspec-its) >= 1
BuildRequires: gem(saharspec) >= 0
BuildRequires: gem(fakefs) >= 0
BuildRequires: gem(simplecov) >= 0.9
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubygems-tasks) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(backports) >= 3.18
BuildRequires: gem(rainbow) >= 0
BuildConflicts: gem(rspec-its) >= 2
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(yard) >= 0
Requires:      gem(backports) >= 3.18
Requires:      gem(rainbow) >= 0
Provides:      gem(yard-junk) = 0.0.9

%ruby_bindir_to %ruby_bindir

%description
YardJunk is structured logger/error validator plugin for YARD documentation gem.


%package       -n yard-junk
Version:       0.0.9
Release:       alt1
Summary:       Get rid of the junk in your YARD docs executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета yard-junk
Group:         Other
BuildArch:     noarch

Requires:      gem(yard-junk) = 0.0.9

%description   -n yard-junk
Get rid of the junk in your YARD docs executable(s).

YardJunk is structured logger/error validator plugin for YARD documentation gem.

%description   -n yard-junk -l ru_RU.UTF-8
Исполнямка для самоцвета yard-junk.


%package       -n gem-yard-junk-doc
Version:       0.0.9
Release:       alt1
Summary:       Get rid of the junk in your YARD docs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-junk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-junk) = 0.0.9

%description   -n gem-yard-junk-doc
Get rid of the junk in your YARD docs documentation files.

YardJunk is structured logger/error validator plugin for YARD documentation gem.

%description   -n gem-yard-junk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-junk.


%package       -n gem-yard-junk-devel
Version:       0.0.9
Release:       alt1
Summary:       Get rid of the junk in your YARD docs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard-junk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard-junk) = 0.0.9
Requires:      gem(rubocop) >= 0
Requires:      gem(rspec) >= 3
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rspec-its) >= 1
Requires:      gem(saharspec) >= 0
Requires:      gem(fakefs) >= 0
Requires:      gem(simplecov) >= 0.9
Requires:      gem(rake) >= 0
Requires:      gem(rubygems-tasks) >= 0
Requires:      gem(kramdown) >= 0
Conflicts:     gem(rspec-its) >= 2
Conflicts:     gem(simplecov) >= 1

%description   -n gem-yard-junk-devel
Get rid of the junk in your YARD docs development package.

YardJunk is structured logger/error validator plugin for YARD documentation gem.

%description   -n gem-yard-junk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard-junk.


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

%files         -n yard-junk
%doc README.md
%ruby_bindir/yard-junk

%files         -n gem-yard-junk-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yard-junk-devel
%doc README.md


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.9-alt1
- + packaged gem with Ruby Policy 2.0
