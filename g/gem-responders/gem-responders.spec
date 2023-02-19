%define        gemname responders

Name:          gem-responders
Version:       3.0.1
Release:       alt1
Summary:       A set of Rails responders to dry up your application
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/plataformatec/responders
Vcs:           https://github.com/plataformatec/responders.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(activemodel) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rails-controller-testing) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(railties) >= 5.0
BuildRequires: gem(actionpack) >= 5.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 5.0
Requires:      gem(actionpack) >= 5.0
Obsoletes:     ruby-responders < %EVR
Provides:      ruby-responders = %EVR
Provides:      gem(responders) = 3.0.1


%description
A set of responders modules to dry up your Rails 4.2+ app.


%package       -n gem-responders-doc
Version:       3.0.1
Release:       alt1
Summary:       A set of Rails responders to dry up your application documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета responders
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(responders) = 3.0.1

%description   -n gem-responders-doc
A set of Rails responders to dry up your application documentation files.

A set of responders modules to dry up your Rails 4.2+ app.

%description   -n gem-responders-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета responders.


%package       -n gem-responders-devel
Version:       3.0.1
Release:       alt1
Summary:       A set of Rails responders to dry up your application development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета responders
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(responders) = 3.0.1
Requires:      gem(activemodel) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(rails-controller-testing) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0

%description   -n gem-responders-devel
A set of Rails responders to dry up your application development package.

A set of responders modules to dry up your Rails 4.2+ app.

%description   -n gem-responders-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета responders.


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

%files         -n gem-responders-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-responders-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Mon Mar 02 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- updated (^) 2.4.0 -> 3.0.0
- used (>) Ruby Policy 2.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.4.0-alt1
- Initial gemified build for Sisyphus
