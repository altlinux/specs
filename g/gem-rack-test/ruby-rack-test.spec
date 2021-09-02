%define        gemname rack-test

Name:          gem-rack-test
Version:       1.1.0.1
Release:       alt1
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rack-test/rack-test
Vcs:           https://github.com/rack-test/rack-test.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rack) >= 1.0 gem(rack) < 3
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4
BuildRequires: gem(sinatra) >= 1.0 gem(sinatra) < 3
BuildRequires: gem(rdoc) >= 5.1 gem(rdoc) < 7
BuildRequires: gem(rubocop) >= 0.49 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0.16 gem(simplecov) < 1
BuildRequires: gem(thor) >= 0.19 gem(thor) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 2.2.2,rack < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency thor >= 1.0.1,thor < 2
%ruby_use_gem_version rack-test:1.1.0.1
Requires:      gem(rack) >= 1.0 gem(rack) < 3
Obsoletes:     ruby-rack-test < %EVR
Provides:      ruby-rack-test = %EVR
Provides:      gem(rack-test) = 1.1.0.1


%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on.


%package       -n gem-rack-test-doc
Version:       1.1.0.1
Release:       alt1
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-test) >= 1.1.0 gem(rack-test) < 2

%description   -n gem-rack-test-doc
Rack::Test is a layer on top of Rack's MockRequest similar to Merb's
RequestHelper documentation files.

Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on.

%description   -n gem-rack-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-test.


%package       -n gem-rack-test-devel
Version:       1.1.0.1
Release:       alt1
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-test
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-test) >= 1.1.0 gem(rack-test) < 2
Requires:      gem(rake) >= 12.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4
Requires:      gem(sinatra) >= 1.0 gem(sinatra) < 3
Requires:      gem(rdoc) >= 5.1 gem(rdoc) < 7
Requires:      gem(rubocop) >= 0.49 gem(rubocop) < 2
Requires:      gem(simplecov) >= 0.16 gem(simplecov) < 1
Requires:      gem(thor) >= 0.19 gem(thor) < 2

%description   -n gem-rack-test-devel
Rack::Test is a layer on top of Rack's MockRequest similar to Merb's
RequestHelper development package.

Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on.

%description   -n gem-rack-test-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-test.


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

%files         -n gem-rack-test-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rack-test-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0.1-alt1
- ^ 1.1.0 -> 1.1.0[.1]

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt2
- > Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.

* Tue Jun 13 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.6.3-alt1
- Initial build for Sisyphus
