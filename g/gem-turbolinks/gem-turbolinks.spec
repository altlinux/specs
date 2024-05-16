%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname turbolinks

Name:          gem-turbolinks
Version:       5.2.1
Release:       alt1.2
Summary:       Turbolinks makes navigating your web application faster
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/turbolinks/turbolinks
Vcs:           https://github.com/turbolinks/turbolinks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(turbolinks-source) >= 5.2
BuildConflicts: gem(turbolinks-source) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(turbolinks-source) >= 5.2
Conflicts:     gem(turbolinks-source) >= 6
Obsoletes:     ruby-turbolinks < %EVR
Provides:      ruby-turbolinks = %EVR
Provides:      gem(turbolinks) = 5.2.1


%description
Turbolinks(r) makes navigating your web application faster. Get the performance
benefits of a single-page application without the added complexity of a
client-side JavaScript framework. Use HTML to render your views on the server
side and link to pages as usual. When you follow a link, Turbolinks
automatically fetches the page, swaps in its <body>, and merges its <head>, all
without incurring the cost of a full page load.


%if_enabled    doc
%package       -n gem-turbolinks-doc
Version:       5.2.1
Release:       alt1.2
Summary:       Turbolinks makes navigating your web application faster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета turbolinks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(turbolinks) = 5.2.1

%description   -n gem-turbolinks-doc
Turbolinks makes navigating your web application faster documentation
files.

Turbolinks(r) makes navigating your web application faster. Get the performance
benefits of a single-page application without the added complexity of a
client-side JavaScript framework. Use HTML to render your views on the server
side and link to pages as usual. When you follow a link, Turbolinks
automatically fetches the page, swaps in its <body>, and merges its <head>, all
without incurring the cost of a full page load.

%description   -n gem-turbolinks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета turbolinks.
%endif


%if_enabled    devel
%package       -n gem-turbolinks-devel
Version:       5.2.1
Release:       alt1.2
Summary:       Turbolinks makes navigating your web application faster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета turbolinks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(turbolinks) = 5.2.1

%description   -n gem-turbolinks-devel
Turbolinks makes navigating your web application faster development
package.

Turbolinks(r) makes navigating your web application faster. Get the performance
benefits of a single-page application without the added complexity of a
client-side JavaScript framework. Use HTML to render your views on the server
side and link to pages as usual. When you follow a link, Turbolinks
automatically fetches the page, swaps in its <body>, and merges its <head>, all
without incurring the cost of a full page load.

%description   -n gem-turbolinks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета turbolinks.
%endif


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

%if_enabled    doc
%files         -n gem-turbolinks-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-turbolinks-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 5.2.1-alt1.2
- ! fixed spec by restoring package

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 5.2.1-alt1.1
- fixed (!) spec

* Thu Sep 19 2019 Pavel Skrylev <majioa@altlinux.org> 1:5.2.1-alt1
- updated (^) v5.2.1
- used (>) Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1:2.5.4-alt2
- Added new epoch.

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 2.5.4-alt1
- Downgrade to 2.5.4 for foreman.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Fri Jul 27 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1.1
- Use appropriate source from https://github.com/turbolinks/turbolinks-rails.
- Rebuild with new Ruby autorequirements.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- Initial build for Sisyphus
