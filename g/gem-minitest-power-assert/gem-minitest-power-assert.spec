%define        gemname minitest-power_assert

Name:          gem-minitest-power-assert
Version:       0.3.1
Release:       alt1
Summary:       Power Assert for Minitest
License:       2-clause BSDL
Group:         Development/Ruby
Url:           https://github.com/hsbt/minitest-power_assert
Vcs:           https://github.com/hsbt/minitest-power_assert.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(power_assert) >= 1.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) >= 0
Requires:      gem(power_assert) >= 1.1
Provides:      gem(minitest-power_assert) = 0.3.1


%description
Power Assert for Minitest.


%package       -n gem-minitest-power-assert-doc
Version:       0.3.1
Release:       alt1
Summary:       Power Assert for Minitest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-power_assert
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-power_assert) = 0.3.1

%description   -n gem-minitest-power-assert-doc
Power Assert for Minitest documentation files.

%description   -n gem-minitest-power-assert-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-power_assert.


%package       -n gem-minitest-power-assert-devel
Version:       0.3.1
Release:       alt1
Summary:       Power Assert for Minitest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-power_assert
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-power_assert) = 0.3.1
Requires:      gem(rake) >= 0

%description   -n gem-minitest-power-assert-devel
Power Assert for Minitest development package.

%description   -n gem-minitest-power-assert-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-power_assert.


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

%files         -n gem-minitest-power-assert-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-minitest-power-assert-devel
%doc README.md


%changelog
* Mon Oct 31 2022 Pavel Skrylev <majioa@altlinux.org> 0.3.1-alt1
- + packaged gem with Ruby Policy 2.0
