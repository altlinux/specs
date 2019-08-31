%define        pkgname puppet-forge
%define        gemname puppet_forge

Name:          gem-%pkgname
Version:       2.2.9
Release:       alt1
Summary:       Ruby client for the Puppet Forge API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/forge-ruby
%vcs           https://github.com/puppetlabs/forge-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%gem_replace_version faraday ~> 0.15
%gem_replace_version faraday_middleware ~> 0.13

%description
Access and manipulate the Puppet Forge API from Ruby.

Tools that can be used to access Forge API information on Modules, Users, and
Releases. As well as download, unpack, and install Releases to a directory.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


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

%files         doc
%ruby_gemdocdir

%changelog
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.9-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
