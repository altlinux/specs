%define        gemname kafo

Name:          gem-kafo
Version:       6.5.0
Release:       alt1
Summary:       A gem for making installations based on puppet user friendly
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo
Vcs:           https://github.com/theforeman/kafo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-reporters) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(json_pure) >= 0
BuildRequires: gem(puppet) >= 4.5.0
BuildRequires: gem(puppet-strings) >= 1.2.1
BuildRequires: gem(metadata-json-lint) >= 0
BuildRequires: gem(puppetlabs_spec_helper) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(kafo_wizards) >= 0
BuildRequires: gem(ansi) >= 0
BuildRequires: gem(kafo_parsers) >= 0.1.6
BuildRequires: gem(clamp) >= 0.6.2
BuildRequires: gem(highline) >= 1.6.21
BuildRequires: gem(powerbar) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(puppet) >= 8.0.0
BuildConflicts: gem(logging) >= 3.0.0
BuildConflicts: gem(clamp) >= 2
BuildConflicts: gem(highline) >= 3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency clamp >= 1.3.2,clamp < 2
Requires:      gem(kafo_wizards) >= 0
Requires:      gem(ansi) >= 0
Requires:      gem(kafo_parsers) >= 0.1.6
Requires:      gem(clamp) >= 0.6.2
Requires:      gem(highline) >= 1.6.21
Requires:      gem(powerbar) >= 0
Conflicts:     gem(logging) >= 3.0.0
Conflicts:     gem(clamp) >= 2
Conflicts:     gem(highline) >= 3.0
Provides:      gem(kafo) = 6.5.0


%description
A puppet based installer and configurer (not-only) for Foreman and Katello
projects. Kafo is a ruby gem that allows you to create fancy user interfaces for
puppet modules. It's some kind of a nice frontend to a "echo "include
some_modules" | puppet apply"

Suppose you work on software which you want to distribute to a machine in an
infrastructure managed by puppet. You write a puppet module for your app. But
now you also want to be able to distribute your app to a machine outside of your
puppet infrastructure (e.g. install it to your clients) or you want to install
it in order to create a puppet infrastructure itself (e.g. foreman or
foreman-proxy).

With kafo you can reuse your puppet modules for creating an installer. Even
better: After the installation you can easily modify your configuration. All
using the very same puppet modules.

With your installer you can also provide multiple configuration files defining
different installation scenarios.


%package       -n kafo
Version:       6.5.0
Release:       alt1
Summary:       A gem for making installations based on puppet user friendly executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета kafo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kafo) = 6.5.0

%description   -n kafo
A gem for making installations based on puppet user friendly executable(s).

A puppet based installer and configurer (not-only) for Foreman and Katello
projects. Kafo is a ruby gem that allows you to create fancy user interfaces for
puppet modules. It's some kind of a nice frontend to a "echo "include
some_modules" | puppet apply"

Suppose you work on software which you want to distribute to a machine in an
infrastructure managed by puppet. You write a puppet module for your app. But
now you also want to be able to distribute your app to a machine outside of your
puppet infrastructure (e.g. install it to your clients) or you want to install
it in order to create a puppet infrastructure itself (e.g. foreman or
foreman-proxy).

With kafo you can reuse your puppet modules for creating an installer. Even
better: After the installation you can easily modify your configuration. All
using the very same puppet modules.

With your installer you can also provide multiple configuration files defining
different installation scenarios.

%description   -n kafo -l ru_RU.UTF-8
Исполнямка для самоцвета kafo.


%package       -n gem-kafo-doc
Version:       6.5.0
Release:       alt1
Summary:       A gem for making installations based on puppet user friendly documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kafo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kafo) = 6.5.0

%description   -n gem-kafo-doc
A gem for making installations based on puppet user friendly documentation
files.

A puppet based installer and configurer (not-only) for Foreman and Katello
projects. Kafo is a ruby gem that allows you to create fancy user interfaces for
puppet modules. It's some kind of a nice frontend to a "echo "include
some_modules" | puppet apply"

Suppose you work on software which you want to distribute to a machine in an
infrastructure managed by puppet. You write a puppet module for your app. But
now you also want to be able to distribute your app to a machine outside of your
puppet infrastructure (e.g. install it to your clients) or you want to install
it in order to create a puppet infrastructure itself (e.g. foreman or
foreman-proxy).

With kafo you can reuse your puppet modules for creating an installer. Even
better: After the installation you can easily modify your configuration. All
using the very same puppet modules.

With your installer you can also provide multiple configuration files defining
different installation scenarios.

%description   -n gem-kafo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kafo.


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

%files         -n kafo
%doc README.md
%_bindir/kafo-configure
%_bindir/kafo-export-params
%_bindir/kafofy

%files         -n gem-kafo-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 6.5.0-alt1
- ^ 6.4.0 -> 6.5.0 (no devel)

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 6.4.0-alt1
- ^ 3.0.0 -> 6.4.0

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- ! spec according to changelog rules

* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- + package gem with usage Ruby Policy 2.0
