%define        gemname rails-dom-testing

Name:          gem-rails-dom-testing
Version:       2.0.3.1
Release:       alt1
Summary:       Extracting DomAssertions and SelectorAssertions from ActionView
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/rails-dom-testing
Vcs:           https://github.com/rails/rails-dom-testing.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(nokogiri) >= 1.6
BuildRequires: gem(activesupport) >= 5.0.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(nokogiri) >= 1.6
Requires:      gem(activesupport) >= 5.0.0
Obsoletes:     ruby-rails-dom-testing < %EVR
Provides:      ruby-rails-dom-testing = %EVR
Provides:      gem(rails-dom-testing) = 2.0.3.1

%ruby_use_gem_version rails-dom-testing:2.0.3.1

%description
Extracting DomAssertions and SelectorAssertions from ActionView.

This gem is responsible for comparing HTML doms and asserting that DOM elements
are present in Rails applications. Doms are compared via assert_dom_equal and
assert_dom_not_equal. Elements are asserted via assert_select,
assert_select_encoded, assert_select_email and a subset of the dom can be
selected with css_select. The gem is developed for Rails 4.2 and above, and will
not work on previous versions.


%package       -n gem-rails-dom-testing-doc
Version:       2.0.3.1
Release:       alt1
Summary:       Extracting DomAssertions and SelectorAssertions from ActionView documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-dom-testing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-dom-testing) = 2.0.3.1

%description   -n gem-rails-dom-testing-doc
Extracting DomAssertions and SelectorAssertions from ActionView documentation
files.

%description   -n gem-rails-dom-testing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rails-dom-testing.


%package       -n gem-rails-dom-testing-devel
Version:       2.0.3.1
Release:       alt1
Summary:       Extracting DomAssertions and SelectorAssertions from ActionView development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails-dom-testing
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails-dom-testing) = 2.0.3.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0

%description   -n gem-rails-dom-testing-devel
Extracting DomAssertions and SelectorAssertions from ActionView development
package.

%description   -n gem-rails-dom-testing-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails-dom-testing.


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

%files         -n gem-rails-dom-testing-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rails-dom-testing-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.3.1-alt1
- ^ 2.0.3 -> 2.0.3.1

* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt2
- > Ruby Policy 2.0
- ! spec tags

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus
