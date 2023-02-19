%define        gemname jquery-turbolinks

Name:          gem-jquery-turbolinks
Version:       2.1.0.1
Release:       alt0.1
Summary:       jQuery plugin for drop-in fix binded events problem caused by Turbolinks
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kossnocorp/jquery.turbolinks
Vcs:           https://github.com/kossnocorp/jquery.turbolinks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         turbolinks-gem.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(uglifier) >= 0
BuildRequires: gem(guard) >= 0
BuildRequires: gem(guard-rake) >= 0
BuildRequires: gem(talks) = 0.4.0
BuildRequires: gem(terminal-notifier) >= 0
BuildRequires: gem(railties) >= 3.1.0
BuildRequires: gem(gitlab-turbolinks-classic) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 3.1.0
Requires:      gem(gitlab-turbolinks-classic) >= 0
Provides:      gem(jquery-turbolinks) = 2.1.0.1


%description
This gem does not work with Turbolinks 5+, and is not compatible with many
jQuery plugins. We do not recommend using it. Instead, please consider writing
your JavaScript in a way that makes it compatible with Turbolinks. These
resources can help:

* RSJS - A reasonable structure for JS, a document outlining how to write
  JavaScript as "behaviors" that will be compatible with Turbolinks.

* onmount - 1kb library to run something when a DOM element appears and when it
  exits.

Rationale: making jQuery plugins compatible with Turbolinks requires more than
simply dropping in a library. It should be able to setup and teardown its
changes as needed, which is something you can't automate. jQuery Turbolinks's
approach worked well enough for many libraries back in 2013, but today this is
no longer the case. Given its utility is very limited, we've decided to no
longer maintain this library.


%package       -n gem-jquery-turbolinks-doc
Version:       2.1.0.1
Release:       alt0.1
Summary:       jQuery plugin for drop-in fix binded events problem caused by Turbolinks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jquery-turbolinks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jquery-turbolinks) = 2.1.0.1

%description   -n gem-jquery-turbolinks-doc
jQuery plugin for drop-in fix binded events problem caused by Turbolinks
documentation files.

This gem does not work with Turbolinks 5+, and is not compatible with many
jQuery plugins. We do not recommend using it. Instead, please consider writing
your JavaScript in a way that makes it compatible with Turbolinks. These
resources can help:

* RSJS - A reasonable structure for JS, a document outlining how to write
  JavaScript as "behaviors" that will be compatible with Turbolinks.

* onmount - 1kb library to run something when a DOM element appears and when it
  exits.

Rationale: making jQuery plugins compatible with Turbolinks requires more than
simply dropping in a library. It should be able to setup and teardown its
changes as needed, which is something you can't automate. jQuery Turbolinks's
approach worked well enough for many libraries back in 2013, but today this is
no longer the case. Given its utility is very limited, we've decided to no
longer maintain this library.

%description   -n gem-jquery-turbolinks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jquery-turbolinks.


%package       -n gem-jquery-turbolinks-devel
Version:       2.1.0.1
Release:       alt0.1
Summary:       jQuery plugin for drop-in fix binded events problem caused by Turbolinks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета jquery-turbolinks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(jquery-turbolinks) = 2.1.0.1
Requires:      gem(uglifier) >= 0

%description   -n gem-jquery-turbolinks-devel
jQuery plugin for drop-in fix binded events problem caused by Turbolinks
development package.

This gem does not work with Turbolinks 5+, and is not compatible with many
jQuery plugins. We do not recommend using it. Instead, please consider writing
your JavaScript in a way that makes it compatible with Turbolinks. These
resources can help:

* RSJS - A reasonable structure for JS, a document outlining how to write
  JavaScript as "behaviors" that will be compatible with Turbolinks.

* onmount - 1kb library to run something when a DOM element appears and when it
  exits.

Rationale: making jQuery plugins compatible with Turbolinks requires more than
simply dropping in a library. It should be able to setup and teardown its
changes as needed, which is something you can't automate. jQuery Turbolinks's
approach worked well enough for many libraries back in 2013, but today this is
no longer the case. Given its utility is very limited, we've decided to no
longer maintain this library.

%description   -n gem-jquery-turbolinks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета jquery-turbolinks.


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

%files         -n gem-jquery-turbolinks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-jquery-turbolinks-devel
%doc README.md


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 2.1.0.1-alt0.1
- ^ 2.1.0 -> 2.1.0[1]

* Fri May 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1.1
- ! spec syntax, and tags
- ! replace require dep to gitlab-turbolinks-classic

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
