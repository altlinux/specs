%define        gemname simplecov

Name:          gem-simplecov
Version:       0.21.2
Release:       alt1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/colszowka/simplecov
Vcs:           https://github.com/simplecov-ruby/simplecov/tree/v0.21.2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(docile) >= 1.1 gem(docile) < 2
BuildRequires: gem(simplecov-html) >= 0.11 gem(simplecov-html) < 1
BuildRequires: gem(simplecov_json_formatter) >= 0.1 gem(simplecov_json_formatter) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names base,extra,monorepo,parallel_tests,rspec_rails
Requires:      gem(docile) >= 1.1 gem(docile) < 2
Requires:      gem(simplecov-html) >= 0.11 gem(simplecov-html) < 1
Requires:      gem(simplecov_json_formatter) >= 0.1 gem(simplecov_json_formatter) < 1
Obsoletes:     ruby-simplecov < %EVR
Provides:      ruby-simplecov = %EVR
Provides:      gem(simplecov) = 0.21.2

%description
SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.


%package       -n gem-simplecov-doc
Version:       0.21.2
Release:       alt1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov) = 0.21.2

%description   -n gem-simplecov-doc
Code coverage for Ruby 1.9+ with a powerful configuration library and automatic
merging of coverage across test suites documentation files.

SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.

%description   -n gem-simplecov-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov.


%package       -n gem-simplecov-devel
Version:       0.21.2
Release:       alt1
Summary:       Code coverage for Ruby 1.9+ with a powerful configuration library and automatic merging of coverage across test suites development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета simplecov
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(simplecov) = 0.21.2

%description   -n gem-simplecov-devel
Code coverage for Ruby 1.9+ with a powerful configuration library and automatic
merging of coverage across test suites development package.

SimpleCov is a code coverage analysis tool for Ruby. It uses Ruby's built-in
Coverage library to gather code coverage data, but makes processing its results
much easier by providing a clean API to filter, group, merge, format, and
display those results, giving you a complete code coverage suite that can be set
up with just a couple lines of code.

%description   -n gem-simplecov-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета simplecov.


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

%files         -n gem-simplecov-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-simplecov-devel
%doc README.md


%changelog
* Thu May 27 2021 Pavel Skrylev <majioa@altlinux.org> 0.21.2-alt1
- ^ 0.17.0 -> 0.21.2

* Tue Jul 09 2019 Pavel Skrylev <majioa@altlinux.org> 0.17.0-alt1
- Bump to 0.17.0
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Mar 16 2018 Andrey Cherepanov <cas@altlinux.org> 0.16.1-alt1
- New version.

* Thu Feb 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt0.M70C.1
- Rebuild with Ruby 2.4.3

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.1-alt1
- New version

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.15.0-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.1-alt1
- New version

* Fri Mar 17 2017 Andrey Cherepanov <cas@altlinux.org> 0.14.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13.0-alt1
- new version 0.13.0

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt2
- Rebuild with missing requirements

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.12.0-alt1
- Initial build in Sisyphus
