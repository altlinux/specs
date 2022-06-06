%define        gemname power_assert

Name:          gem-power-assert
Version:       2.0.1
Release:       alt1
Summary:       Power Assert for Ruby
License:       BSD-2-Clause or Ruby
Group:         Development/Ruby
Url:           https://github.com/k-tsj/power_assert
Vcs:           https://github.com/k-tsj/power_assert.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(benchmark-ips) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names power_assert,power-assert
Provides:      gem(power_assert) = 2.0.1


%description
Power Assert shows each value of variables and method calls in the expression.
It is useful for testing, providing which value wasn't correct when the
condition is not satisfied.


%package       -n gem-power-assert-doc
Version:       2.0.1
Release:       alt1
Summary:       Power Assert for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета power_assert
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(power_assert) = 2.0.1

%description   -n gem-power-assert-doc
Power Assert for Ruby documentation files.

Power Assert shows each value of variables and method calls in the expression.
It is useful for testing, providing which value wasn't correct when the
condition is not satisfied.

%description   -n gem-power-assert-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета power_assert.


%package       -n gem-power-assert-devel
Version:       2.0.1
Release:       alt1
Summary:       Power Assert for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета power_assert
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(power_assert) = 2.0.1
Requires:      gem(test-unit) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(benchmark-ips) >= 0

%description   -n gem-power-assert-devel
Power Assert for Ruby development package.

Power Assert shows each value of variables and method calls in the expression.
It is useful for testing, providing which value wasn't correct when the
condition is not satisfied.

%description   -n gem-power-assert-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета power_assert.


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

%files         -n gem-power-assert-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-power-assert-devel
%doc README.md


%changelog
* Sun Apr 03 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- ^ 1.1.7 -> 2.0.1

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.1.7-alt1
- ^ 1.1.4 -> 1.1.7
- ! spec tags, and filename

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.4-alt1
- Bump to 1.1.4
- Use Ruby Policy 2.0

* Tue Jan 15 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- Initial build for Sisyphus, packaged as a gem
