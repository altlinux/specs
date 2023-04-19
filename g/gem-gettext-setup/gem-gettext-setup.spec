%define        gemname gettext-setup

Name:          gem-gettext-setup
Version:       1.1.0
Release:       alt1
Summary:       A gem that configures gettext for internationalization
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/gettext-setup-gem
Vcs:           https://github.com/puppetlabs/gettext-setup-gem.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.1
BuildRequires: gem(rspec-core) >= 3.1
BuildRequires: gem(rspec-expectations) >= 3.1
BuildRequires: gem(rspec-mocks) >= 3.1
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(fast_gettext) >= 2.1
BuildRequires: gem(gettext) >= 3.4
BuildRequires: gem(locale) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-core) >= 4
BuildConflicts: gem(rspec-expectations) >= 4
BuildConflicts: gem(rspec-mocks) >= 4
BuildConflicts: gem(fast_gettext) >= 3
BuildConflicts: gem(gettext) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fast_gettext) >= 2.1
Requires:      gem(gettext) >= 3.4
Requires:      gem(locale) >= 0
Conflicts:     gem(fast_gettext) >= 3
Conflicts:     gem(gettext) >= 4
Obsoletes:     ruby-gettext-setup < %EVR
Provides:      ruby-gettext-setup = %EVR
Provides:      gem(gettext-setup) = 1.1.0


%description
This is a simple gem to set up i18n for Ruby projects (including Sinatra web
apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a different
locale in their browser preferences, and we support the user's preferred locale,
strings and data formatting will be customized for that locale.


%package       -n gem-gettext-setup-doc
Version:       1.1.0
Release:       alt1
Summary:       A gem that configures gettext for internationalization documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gettext-setup
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gettext-setup) = 1.1.0

%description   -n gem-gettext-setup-doc
A gem that configures gettext for internationalization documentation
files.

This is a simple gem to set up i18n for Ruby projects (including Sinatra web
apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a different
locale in their browser preferences, and we support the user's preferred locale,
strings and data formatting will be customized for that locale.

%description   -n gem-gettext-setup-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gettext-setup.


%package       -n gem-gettext-setup-devel
Version:       1.1.0
Release:       alt1
Summary:       A gem that configures gettext for internationalization development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gettext-setup
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gettext-setup) = 1.1.0
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.1
Requires:      gem(rspec-core) >= 3.1
Requires:      gem(rspec-expectations) >= 3.1
Requires:      gem(rspec-mocks) >= 3.1
Requires:      gem(rubocop) >= 0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-core) >= 4
Conflicts:     gem(rspec-expectations) >= 4
Conflicts:     gem(rspec-mocks) >= 4

%description   -n gem-gettext-setup-devel
A gem that configures gettext for internationalization development
package.

This is a simple gem to set up i18n for Ruby projects (including Sinatra web
apps) using gettext and fast gettext.

This project sets the default locale to English. If the user has set a different
locale in their browser preferences, and we support the user's preferred locale,
strings and data formatting will be customized for that locale.

%description   -n gem-gettext-setup-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gettext-setup.


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

%files         -n gem-gettext-setup-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gettext-setup-devel
%doc README.md


%changelog
* Thu Apr 13 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 1.0.1 -> 1.1.0

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt2
- ! spec

* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1.1
- ! ruby dep tags

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 0.30 -> 1.0post

* Fri Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.30-alt3
- > Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 0.30-alt2
- Update fastgettext to 1.7

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.2
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1.1
- Rebuild with Ruby 2.5.0

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.30-alt1
- New version.

* Sat Dec 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.29-alt1
- New version.

* Tue Sep 26 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt2
- Rebuild with Ruby 2.4.2

* Sat Sep 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.28-alt1
- New version

* Wed Jul 12 2017 Andrey Cherepanov <cas@altlinux.org> 0.26-alt1
- New version

* Wed May 31 2017 Andrey Cherepanov <cas@altlinux.org> 0.25-alt1
- New version

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.24-alt1
- New version
- Package gemspec
- Require dependencies from gemspec

* Thu Mar 30 2017 Andrey Cherepanov <cas@altlinux.org> 0.20-alt1
- New version

* Mon Mar 20 2017 Andrey Cherepanov <cas@altlinux.org> 0.16-alt1
- New version

* Tue Feb 28 2017 Andrey Cherepanov <cas@altlinux.org> 0.13-alt1
- New version

* Mon Oct 24 2016 Andrey Cherepanov <cas@altlinux.org> 0.7-alt1
- Initial build in Sisyphus
