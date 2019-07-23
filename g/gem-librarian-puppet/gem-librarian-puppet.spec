%define        pkgname librarian-puppet

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       Simplify deployment of your Puppet infrastructure
License:       MIT
Group:         Development/Ruby
Url:           http://librarian-puppet.com
%vcs           https://github.com/voxpupuli/librarian-puppet.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Librarian-puppet is a bundler for your puppet infrastructure. You can use
librarian-puppet to manage the puppet modules your infrastructure depends on,
whether the modules come from the Puppet Forge, Git repositories or just a path.

* Librarian-puppet can reuse the dependencies listed in your Modulefile or
  metadata.json
* Forge modules can be installed from Puppetlabs Forge or an internal Forge
  such as Pulp
* Git modules can be installed from a branch, tag or specific commit, optionally
  using a path inside the repository
* Modules can be installed from GitHub using tarballs, without needing Git
  installed
* Modules can be installed from a filesystem path
* Module dependencies are resolved transitively without needing to list all
  the modules explicitly

Librarian-puppet manages your modules/ directory for you based on your
Puppetfile. Your Puppetfile becomes the authoritative source for what modules
you require and at what version, tag or branch.

Once using Librarian-puppet you should not modify the contents of your modules
directory. The individual modules' repos should be updated, tagged with a new
release and the version bumped in your Puppetfile.

It is based on Librarian, a framework for writing bundlers, which are tools that
resolve, fetch, install, and isolate a project's dependencies.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n %pkgname
Summary:       Executable for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n %pkgname
Executable for %gemname gem.


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
%_bindir/%pkgname

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
