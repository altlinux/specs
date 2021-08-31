%define        gemname minitest-global_expectations

Name:          gem-minitest-global-expectations
Version:       1.0.1
Release:       alt1
Summary:       Support minitest expectation methods for all objects
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jeremyevans/minitest-global_expectations
Vcs:           https://github.com/jeremyevans/minitest-global_expectations.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) > 5 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) > 5 gem(minitest) < 6
Provides:      gem(minitest-global_expectations) = 1.0.1


%description
minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.


%package       -n gem-minitest-global-expectations-doc
Version:       1.0.1
Release:       alt1
Summary:       Support minitest expectation methods for all objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-global_expectations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-global_expectations) = 1.0.1

%description   -n gem-minitest-global-expectations-doc
Support minitest expectation methods for all objects documentation
files.

minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.

%description   -n gem-minitest-global-expectations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-global_expectations.


%package       -n gem-minitest-global-expectations-devel
Version:       1.0.1
Release:       alt1
Summary:       Support minitest expectation methods for all objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-global_expectations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-global_expectations) = 1.0.1

%description   -n gem-minitest-global-expectations-devel
Support minitest expectation methods for all objects development
package.

minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.

%description   -n gem-minitest-global-expectations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-global_expectations.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitest-global-expectations-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-global-expectations-devel
%doc README.rdoc


%changelog
* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
