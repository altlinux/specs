%define        gemname sass-listen

Name:          gem-sass-listen
Version:       4.0.0
Release:       alt3
Summary:       The Listen gem listens to file modifications and notifies you about the changes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/listen
Vcs:           https://github.com/sass/listen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rb-fsevent) >= 0.9.4 gem(rb-fsevent) < 1
BuildRequires: gem(rb-inotify) >= 0.9.7 gem(rb-inotify) < 1
BuildRequires: gem(bundler) >= 1.3.5 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(rb-fsevent) >= 0.9.4 gem(rb-fsevent) < 1
Requires:      gem(rb-inotify) >= 0.9.7 gem(rb-inotify) < 1
Obsoletes:     ruby-sass-listen < %EVR
Provides:      ruby-sass-listen = %EVR
Provides:      gem(sass-listen) = 4.0.0


%description
The Listen gem listens to file modifications and notifies you about the changes.

Version 4.0 is a fork of the official version 3.0.x branch. Sass need to support
older versions of ruby than Guard wants to support on an ongoing basis, so we
are releasing updates as needed for critical fixes and will support ruby 2.0 and
greater for as long as Sass users need it.


%package       -n gem-sass-listen-doc
Version:       4.0.0
Release:       alt3
Summary:       The Listen gem listens to file modifications and notifies you about the changes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sass-listen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sass-listen) = 4.0.0

%description   -n gem-sass-listen-doc
The Listen gem listens to file modifications and notifies you about the changes
documentation files.

Version 4.0 is a fork of the official version 3.0.x branch. Sass need to support
older versions of ruby than Guard wants to support on an ongoing basis, so we
are releasing updates as needed for critical fixes and will support ruby 2.0 and
greater for as long as Sass users need it.

%description   -n gem-sass-listen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sass-listen.


%package       -n gem-sass-listen-devel
Version:       4.0.0
Release:       alt3
Summary:       The Listen gem listens to file modifications and notifies you about the changes development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sass-listen
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sass-listen) = 4.0.0
Requires:      gem(bundler) >= 1.3.5 gem(bundler) < 3

%description   -n gem-sass-listen-devel
The Listen gem listens to file modifications and notifies you about the changes
development package.

Version 4.0 is a fork of the official version 3.0.x branch. Sass need to support
older versions of ruby than Guard wants to support on an ongoing basis, so we
are releasing updates as needed for critical fixes and will support ruby 2.0 and
greater for as long as Sass users need it.

%description   -n gem-sass-listen-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sass-listen.


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

%files         -n gem-sass-listen-devel
%doc README.md


%changelog
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
