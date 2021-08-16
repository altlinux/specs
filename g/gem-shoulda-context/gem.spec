%define        gemname shoulda-context

Name:          gem-shoulda-context
Version:       2.0.0
Release:       alt1
Summary:       Context framework extracted from Shoulda
License:       MIT
Group:         Development/Ruby
Url:           http://thoughtbot.com/community/
Vcs:           https://github.com/thoughtbot/shoulda-context.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(shoulda-context) = 2.0.0


%description
Context framework extracted from Shoulda. Minitest & Test::Unit context
framework.


%package       -n convert-to-should-syntax
Version:       2.0.0
Release:       alt1
Summary:       Context framework extracted from Shoulda executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета shoulda-context
Group:         Other
BuildArch:     noarch

Requires:      gem(shoulda-context) = 2.0.0

%description   -n convert-to-should-syntax
Context framework extracted from Shoulda executable(s).

Context framework extracted from Shoulda. Minitest & Test::Unit context
framework.

%description   -n convert-to-should-syntax -l ru_RU.UTF-8
Исполнямка для самоцвета shoulda-context.


%package       -n gem-shoulda-context-doc
Version:       2.0.0
Release:       alt1
Summary:       Context framework extracted from Shoulda documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета shoulda-context
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(shoulda-context) = 2.0.0

%description   -n gem-shoulda-context-doc
Context framework extracted from Shoulda documentation files.

Context framework extracted from Shoulda. Minitest & Test::Unit context
framework.

%description   -n gem-shoulda-context-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета shoulda-context.


%package       -n gem-shoulda-context-devel
Version:       2.0.0
Release:       alt1
Summary:       Context framework extracted from Shoulda development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета shoulda-context
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(shoulda-context) = 2.0.0

%description   -n gem-shoulda-context-devel
Context framework extracted from Shoulda development package.

Context framework extracted from Shoulda. Minitest & Test::Unit context
framework.

%description   -n gem-shoulda-context-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета shoulda-context.


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

%files         -n convert-to-should-syntax
%doc README.md
%_bindir/convert_to_should_syntax

%files         -n gem-shoulda-context-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-shoulda-context-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
