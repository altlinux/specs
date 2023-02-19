%define        gemname sass-listen

Name:          gem-sass-listen
Version:       4.0.0
Release:       alt3.1
Summary:       The Listen gem listens to file modifications and notifies you about the changes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/listen
Vcs:           https://github.com/sass/listen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3.5
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.3
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(rubocop) >= 0.25.0
BuildRequires: gem(guard-rubocop) >= 0
BuildRequires: gem(pry-rescue) >= 0
BuildRequires: gem(pry-stack_explorer) >= 0
BuildRequires: gem(gems) >= 0
BuildRequires: gem(netrc) >= 0
BuildRequires: gem(octokit) >= 0
BuildRequires: gem(rb-fsevent) >= 0.9.4
BuildRequires: gem(rb-inotify) >= 0.9.7
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rb-fsevent) >= 1
BuildConflicts: gem(rb-inotify) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(rb-fsevent) >= 0.9.4
Requires:      gem(rb-inotify) >= 0.9.7
Conflicts:     gem(rb-fsevent) >= 1
Conflicts:     gem(rb-inotify) >= 1
Obsoletes:     ruby-sass-listen < %EVR
Provides:      ruby-sass-listen = %EVR
Provides:      gem(sass-listen) = 4.0.0


%description
The Listen gem listens to file modifications and notifies you about the
changes.

Version 4.0 is a fork of the official version 3.0.x branch. Sass need to support
older versions of ruby than Guard wants to support on an ongoing basis, so we
are releasing updates as needed for critical fixes and will support ruby 2.0 and
greater for as long as Sass users need it.


%package       -n gem-sass-listen-doc
Version:       4.0.0
Release:       alt3.1
Summary:       The Listen gem listens to file modifications and notifies you about the changes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-listen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-listen) = 4.0.0

%description   -n gem-sass-listen-doc
The Listen gem listens to file modifications and notifies you about the changes
documentation files.

%description   -n gem-sass-listen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass-listen.


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

%files         -n gem-sass-listen-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt3.1
- ! by closing build deps under check condition
- - devel package

* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt3
- ! spec

* Wed Sep 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt2.1
- Rebuild for new Ruby autorequirements.
- Simplify spec.
- Disable tests.

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 4.0.0-alt2
- Rebuild as ruby gem for openqa

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
