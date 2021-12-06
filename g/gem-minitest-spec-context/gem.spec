%define        gemname minitest-spec-context

Name:          gem-minitest-spec-context
Version:       0.0.4
Release:       alt1
Summary:       Provides context method to MiniTest::Spec
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ywen/minitest-spec-context
Vcs:           https://github.com/ywen/minitest-spec-context.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 6.0 gem(activesupport) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(minitest-spec-context) = 0.0.4


%description
This gem provides a context method for MiniTest::Spec.


%package       -n gem-minitest-spec-context-doc
Version:       0.0.4
Release:       alt1
Summary:       Provides context method to MiniTest::Spec documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-spec-context
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-spec-context) = 0.0.4

%description   -n gem-minitest-spec-context-doc
Provides context method to MiniTest::Spec documentation files.

This gem provides a context method for MiniTest::Spec.

%description   -n gem-minitest-spec-context-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-spec-context.


%package       -n gem-minitest-spec-context-devel
Version:       0.0.4
Release:       alt1
Summary:       Provides context method to MiniTest::Spec development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-spec-context
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-spec-context) = 0.0.4
Requires:      gem(activesupport) >= 6.0 gem(activesupport) < 7

%description   -n gem-minitest-spec-context-devel
Provides context method to MiniTest::Spec development package.

This gem provides a context method for MiniTest::Spec.

%description   -n gem-minitest-spec-context-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-spec-context.


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

%files         -n gem-minitest-spec-context-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-spec-context-devel
%doc README.md


%changelog
* Fri Dec 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
