%define        gemname librarian-puppet

Name:          gem-librarian-puppet
Version:       3.0.1.1
Release:       alt0.1
Summary:       Simplify deployment of your Puppet infrastructure
License:       MIT
Group:         Development/Ruby
Url:           http://librarian-puppet.com
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(puppet) >= 0
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(simplecov) >= 0.9.0
BuildRequires: gem(librarianp) >= 0.6.3
BuildRequires: gem(rsync) >= 0
BuildRequires: gem(puppet_forge) >= 2.1
BuildConflicts: gem(cucumber) >= 3.0.0
BuildConflicts: gem(aruba) >= 0.8.0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(puppet_forge) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency puppet_forge >= 3.2.0,puppet_forge < 4
Requires:      gem(librarianp) >= 0.6.3
Requires:      gem(rsync) >= 0
Requires:      gem(puppet_forge) >= 2.1
Conflicts:     gem(puppet_forge) >= 4
Provides:      gem(librarian-puppet) = 3.0.1.1

%ruby_use_gem_version librarian-puppet:3.0.1.1

%description
Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a
path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge such
as Pulp
* Git modules can be installed from a branch, tag or specific commit, optionally
using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all the
modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools that
resolve, fetch, install, and isolate a project's dependencies.


%package       -n librarian-puppet
Version:       3.0.1.1
Release:       alt0.1
Summary:       Simplify deployment of your Puppet infrastructure executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета librarian-puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(librarian-puppet) = 3.0.1.1

%description   -n librarian-puppet
Simplify deployment of your Puppet infrastructure
executable(s).

Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a
path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge such
as Pulp
* Git modules can be installed from a branch, tag or specific commit, optionally
using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all the
modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools that
resolve, fetch, install, and isolate a project's dependencies.

%description   -n librarian-puppet -l ru_RU.UTF-8
Исполнямка для самоцвета librarian-puppet.


%package       -n gem-librarian-puppet-doc
Version:       3.0.1.1
Release:       alt0.1
Summary:       Simplify deployment of your Puppet infrastructure documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета librarian-puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(librarian-puppet) = 3.0.1.1

%description   -n gem-librarian-puppet-doc
Simplify deployment of your Puppet infrastructure documentation
files.

Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a
path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge such
as Pulp
* Git modules can be installed from a branch, tag or specific commit, optionally
using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all the
modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools that
resolve, fetch, install, and isolate a project's dependencies.

%description   -n gem-librarian-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета librarian-puppet.


%package       -n gem-librarian-puppet-devel
Version:       3.0.1.1
Release:       alt0.1
Summary:       Simplify deployment of your Puppet infrastructure development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета librarian-puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(librarian-puppet) = 3.0.1.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(puppet) >= 0
Requires:      gem(minitest) >= 5
Requires:      gem(mocha) >= 0
Requires:      gem(simplecov) >= 0.9.0
Conflicts:     gem(minitest) >= 6

%description   -n gem-librarian-puppet-devel
Simplify deployment of your Puppet infrastructure development
package.

Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a
path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge such
as Pulp
* Git modules can be installed from a branch, tag or specific commit, optionally
using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all the
modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools that
resolve, fetch, install, and isolate a project's dependencies.

%description   -n gem-librarian-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета librarian-puppet.


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

%files         -n librarian-puppet
%doc README.md
%_bindir/librarian-puppet

%files         -n gem-librarian-puppet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-librarian-puppet-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.1.1-alt0.1
- ^ 3.0.1 -> 3.0.1[1]

* Thu Jul 15 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
- ^ 3.0.0 -> 3.0.1

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
