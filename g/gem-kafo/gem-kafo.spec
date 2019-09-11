%define        pkgname kafo

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1.1
Summary:       A gem for making installations based on puppet user friendly 
License:       GPLv3+
Group:         Development/Ruby
Url:           https://github.com/theforeman/kafo
%vcs           https://github.com/theforeman/kafo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version highline ~> 2.0
%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
A puppet based installer and configurer (not-only) for Foreman and Katello
projects. Kafo is a ruby gem that allows you to create fancy user interfaces
for puppet modules. It's some kind of a nice frontend to a
"echo "include some_modules" | puppet apply"

Suppose you work on software which you want to distribute to a machine in
an infrastructure managed by puppet. You write a puppet module for your app.
But now you also want to be able to distribute your app to a machine outside of
your puppet infrastructure (e.g. install it to your clients) or you want
to install it in order to create a puppet infrastructure itself (e.g. foreman
or foreman-proxy).

With kafo you can reuse your puppet modules for creating an installer. Even
better: After the installation you can easily modify your configuration. All
using the very same puppet modules.

With your installer you can also provide multiple configuration files defining
different installation scenarios.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n %pkgname
%_bindir/%{pkgname}*

%files         doc
%ruby_gemdocdir

%changelog
* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- ! spec according to changelog rules

* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- + package gem with usage Ruby Policy 2.0
