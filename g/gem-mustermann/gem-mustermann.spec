Name:          gem-mustermann
Version:       3.0.0
Release:       alt1
Summary:       The Amazing Mustermann
License:       MIT
Group:         Development/Ruby
Url:           http://sinatrarb.com/mustermann/
Vcs:           https://github.com/sinatra/mustermann.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ruby2_keywords) >= 0.0.1
BuildRequires: gem(hansi) >= 0.2.0
BuildRequires: gem(support) >= 0
BuildConflicts: gem(ruby2_keywords) >= 0.1
BuildConflicts: gem(hansi) >= 0.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names gem-mustermann,mustermann
Requires:      gem(ruby2_keywords) >= 0.0.1
Conflicts:     gem(ruby2_keywords) >= 0.1
Obsoletes:     ruby-mustermann < %EVR
Provides:      ruby-mustermann = %EVR
Provides:      ruby-gem-mustermann = %EVR
Provides:      gem(mustermann) = 3.0.0


%description
Mustermann is your personal string matching expert.

A library implementing patterns that behave like regular expressions.


%package       -n gem-mustermann-doc
Version:       3.0.0
Release:       alt1
Summary:       Your personal string matching expert documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustermann
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustermann) = 3.0.0

%description   -n gem-mustermann-doc
Your personal string matching expert documentation files.

A library implementing patterns that behave like regular expressions.

%description   -n gem-mustermann-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mustermann.


%package       -n gem-mustermann-devel
Version:       3.0.0
Release:       alt1
Summary:       Your personal string matching expert development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustermann
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann) = 3.0.0

%description   -n gem-mustermann-devel
Your personal string matching expert development package.

A library implementing patterns that behave like regular expressions.

%description   -n gem-mustermann-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mustermann.


%package       -n gem-mustermann-contrib
Version:       3.0.0
Release:       alt1
Summary:       The Amazing Mustermann
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann) = 3.0.0
Requires:      gem(hansi) >= 0.2.0
Requires:      gem(support) >= 0
Conflicts:     gem(hansi) >= 0.3
Provides:      gem(mustermann-contrib) = 3.0.0

%description   -n gem-mustermann-contrib
A meta gem depending on all other official mustermann gems.

Mustermann is your personal string matching expert.


%package       -n gem-mustermann-contrib-doc
Version:       3.0.0
Release:       alt1
Summary:       The Amazing Mustermann documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustermann-contrib
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustermann-contrib) = 3.0.0

%description   -n gem-mustermann-contrib-doc
The Amazing Mustermann documentation files.

A meta gem depending on all other official mustermann gems.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-contrib-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mustermann-contrib.


%package       -n gem-mustermann-contrib-devel
Version:       3.0.0
Release:       alt1
Summary:       The Amazing Mustermann development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustermann-contrib
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustermann-contrib) = 3.0.0

%description   -n gem-mustermann-contrib-devel
The Amazing Mustermann development package.

A meta gem depending on all other official mustermann gems.

Mustermann is your personal string matching expert.

%description   -n gem-mustermann-contrib-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mustermann-contrib.


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

%files         -n gem-mustermann-doc
%doc README.md
%ruby_gemsdocdir/mustermann-3.0.0

%files         -n gem-mustermann-devel
%doc README.md

%files         -n gem-mustermann-contrib
%doc README.md
%ruby_gemspecdir/mustermann-contrib-3.0.0.gemspec
%ruby_gemslibdir/mustermann-contrib-3.0.0

%files         -n gem-mustermann-contrib-doc
%doc README.md
%ruby_gemsdocdir/mustermann-contrib-3.0.0

%files         -n gem-mustermann-contrib-devel
%doc README.md


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 1.1.1 -> 3.0.0
- ! of closing build deps under check condition

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1.1
- ! spec

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
