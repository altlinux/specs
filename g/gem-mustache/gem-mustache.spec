%define        _unpackaged_files_terminate_build 1
%define        gemname mustache

Name:          gem-mustache
Version:       1.1.1.17
Release:       alt0.1
Summary:       Logic-less Ruby templates
License:       MIT
Group:         Development/Ruby
Url:           http://mustache.github.io/
Vcs:           https://github.com/mustache/mustache.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-deps.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(rake) >= 10.3
BuildRequires: gem(minitest) >= 5.4
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(ruby-prof) >= 0
BuildRequires: gem(rdoc) >= 4.1
BuildRequires: gem(ronn-ng) >= 0.7
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 1.0.0
BuildConflicts: gem(bundler) >= 3.0
BuildConflicts: gem(rake) >= 14.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7.0
BuildConflicts: gem(ronn-ng) >= 1
BuildConflicts: gem(codeclimate-test-reporter) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency codeclimate-test-reporter >= 1.0.9,codeclimate-test-reporter < 2
Provides:      gem(mustache) = 1.1.1.17

%ruby_use_gem_version mustache:1.1.1.17
%ruby_bindir_to %ruby_bindir

%description
Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."


%package       -n mustache
Version:       1.1.1.17
Release:       alt0.1
Summary:       Logic-less Ruby templates executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета mustache
Group:         Other
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1.17

%description   -n mustache
Logic-less Ruby templates executable(s).

Logic-less Ruby templates inspired by ctemplate and et, Mustache is a
framework-agnostic way to render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation: it is
impossible to embed application logic in this template language."

%description   -n mustache -l ru_RU.UTF-8
Исполнямка для самоцвета mustache.


%package       -n gem-mustache-doc
Version:       1.1.1.17
Release:       alt0.1
Summary:       Logic-less Ruby templates documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mustache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1.17
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
Version:       1.1.1.17
Release:       alt0.1
Summary:       Logic-less Ruby templates development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mustache
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mustache) = 1.1.1.17
Requires:      gem(bundler) >= 1.6
Requires:      gem(rake) >= 10.3
Requires:      gem(minitest) >= 5.4
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(ruby-prof) >= 0
Requires:      gem(rdoc) >= 4.1
Requires:      gem(ronn-ng) >= 0.7
Requires:      gem(simplecov) >= 0
Requires:      gem(codeclimate-test-reporter) >= 1.0.0
Conflicts:     gem(bundler) >= 3.0
Conflicts:     gem(rake) >= 14.0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7.0
Conflicts:     gem(ronn-ng) >= 1
Conflicts:     gem(codeclimate-test-reporter) >= 2

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
%autopatch

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
%ruby_bindir/mustache
%_mandir/mustache.*xz

%files         -n gem-mustache-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mustache-devel
%doc README.md


%changelog
* Tue Dec 19 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.1.17-alt0.1
- ^ 1.1.1 -> 1.1.1p16

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
