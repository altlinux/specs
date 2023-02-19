%define        gemname rack-test

Name:          gem-rack-test
Version:       2.0.0
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
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 5.0
BuildRequires: gem(minitest-global_expectations) >= 0
BuildRequires: gem(rack) >= 1.3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 1.3
Obsoletes:     ruby-rack-test < %EVR
Provides:      ruby-rack-test = %EVR
Provides:      gem(rack-test) = 2.0.0


%description
Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on.


%package       -n gem-rack-test-doc
Version:       2.0.0
Release:       alt1
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-test
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-test) = 2.0.0

%description   -n gem-rack-test-doc
Rack::Test is a layer on top of Rack's MockRequest similar to Merb's
RequestHelper documentation files.

Rack::Test is a small, simple testing API for Rack apps. It can be used on its
own or as a reusable starting point for Web frameworks and testing libraries to
build on.

%description   -n gem-rack-test-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-test.


%package       -n gem-rack-test-devel
Version:       2.0.0
Release:       alt1
Summary:       Rack::Test is a layer on top of Rack's MockRequest similar to Merb's RequestHelper development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-test
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-test) = 2.0.0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 5.0
Requires:      gem(minitest-global_expectations) >= 0

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
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.1.0[1] -> 2.0.0

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
