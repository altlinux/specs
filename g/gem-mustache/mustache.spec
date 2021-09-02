%define        gemname mustache

Name:          gem-mustache
Version:       1.1.1
Release:       alt1.1
Summary:       Logic-less Ruby templates
License:       MIT
Group:         Development/Ruby
Url:           http://mustache.github.io/
Vcs:           https://github.com/mustache/mustache.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.6 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.3 gem(rake) < 14
BuildRequires: gem(minitest) >= 5.4 gem(minitest) < 6
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rdoc) >= 4.1 gem(rdoc) < 7
BuildRequires: gem(ronn) >= 0.7 gem(ronn) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(mustache) = 1.1.1


%description
Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."


%package       -n mustache
Version:       1.1.1
Release:       alt1.1
Summary:       Logic-less Ruby templates executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mustache
Group:         Other
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1

%description   -n mustache
Logic-less Ruby templates executable(s).

Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

%description   -n mustache -l ru_RU.UTF-8
Исполнямка для самоцвета mustache.


%package       -n gem-mustache-doc
Version:       1.1.1
Release:       alt1.1
Summary:       Logic-less Ruby templates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1
Obsoletes:     mustache-doc
Provides:      mustache-doc

%description   -n gem-mustache-doc
Logic-less Ruby templates documentation files.

Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

%description   -n gem-mustache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mustache.


%package       -n gem-mustache-devel
Version:       1.1.1
Release:       alt1.1
Summary:       Logic-less Ruby templates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1
Requires:      gem(bundler) >= 1.6 gem(bundler) < 3
Requires:      gem(rake) >= 10.3 gem(rake) < 14
Requires:      gem(minitest) >= 5.4 gem(minitest) < 6
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rdoc) >= 4.1 gem(rdoc) < 7
Requires:      gem(ronn) >= 0.7 gem(ronn) < 1

%description   -n gem-mustache-devel
Logic-less Ruby templates development package.

Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

%description   -n gem-mustache-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mustache.


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

%files         -n mustache
%doc README.md
%_bindir/mustache

%files         -n gem-mustache-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mustache-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1.1
- ! spec

* Mon Dec 09 2019 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt2
- Use Ruby Policy 2.0

* Sun Oct 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed May 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
