%define        gemname simplecov-html

Name:          gem-simplecov-html
Version:       0.12.3
Release:       alt1
Summary:       HTML formatter for SimpleCov code coverage tool for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/colszowka/simplecov-html
Vcs:           https://github.com/colszowka/simplecov-html.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-simplecov-html < %EVR
Provides:      ruby-simplecov-html = %EVR
Provides:      gem(simplecov-html) = 0.12.3

%description
Generates a nice HTML report of your SimpleCov ruby code coverage results on
Ruby 1.9 using client-side Javascript quite extensively.


%package       -n gem-simplecov-html-doc
Version:       0.12.3
Release:       alt1
Summary:       Default HTML formatter for SimpleCov code coverage tool for ruby 2.4+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-html
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-html) = 0.12.3

%description   -n gem-simplecov-html-doc
Default HTML formatter for SimpleCov code coverage tool for ruby 2.4+
documentation files.

Default HTML formatter for SimpleCov code coverage tool for ruby 2.4+

%description   -n gem-simplecov-html-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-html.


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

%files         -n gem-simplecov-html-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Apr 23 2021 Pavel Skrylev <majioa@altlinux.org> 0.12.3-alt1
- ^ 0.10.2 -> 0.12.3

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue Aug 15 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.2-alt1
- New version

* Thu May 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.10.1-alt1
- New version

* Tue Oct 25 2016 Andrey Cherepanov <cas@altlinux.org> 0.10.0-alt1
- Initial build in Sisyphus
