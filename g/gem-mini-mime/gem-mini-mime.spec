%define        gemname mini_mime

Name:          gem-mini-mime
Version:       1.1.2
Release:       alt1
Summary:       Minimal mime type library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/discourse/mini_mime
Vcs:           https://github.com/discourse/mini_mime.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-discourse) >= 0
BuildRequires: gem(mime-types) >= 3
BuildRequires: gem(memory_profiler) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildConflicts: gem(mime-types) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names mini_mime,mini-mime
Obsoletes:     ruby-mini_mime
Provides:      ruby-mini_mime
Provides:      gem(mini_mime) = 1.1.2


%description
Minimal mime type implementation for use with the mail and rest-client gem.


%package       -n gem-mini-mime-doc
Version:       1.1.2
Release:       alt1
Summary:       Minimal mime type library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mini_mime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mini_mime) = 1.1.2

%description   -n gem-mini-mime-doc
Minimal mime type library for Ruby documentation files.

Minimal mime type implementation for use with the mail and rest-client gem.

%description   -n gem-mini-mime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mini_mime.


%package       -n gem-mini-mime-devel
Version:       1.1.2
Release:       alt1
Summary:       Minimal mime type library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mini_mime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mini_mime) = 1.1.2
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-discourse) >= 0
Requires:      gem(mime-types) >= 3
Requires:      gem(memory_profiler) >= 0
Requires:      gem(benchmark-ips) >= 0
Conflicts:     gem(mime-types) >= 4

%description   -n gem-mini-mime-devel
Minimal mime type library for Ruby development package.

Minimal mime type implementation for use with the mail and rest-client gem.

%description   -n gem-mini-mime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mini_mime.


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

%files         -n gem-mini-mime-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mini-mime-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.2-alt1
- ^ 1.1.0 -> 1.1.2

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.2 -> 1.1.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- updated (^) 1.0.1 -> 1.0.2
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- updated (^) 1.0.0 -> 1.0.1

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1.1
- Rebuild dor new Ruby autorequirements.

* Thu Apr 12 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
