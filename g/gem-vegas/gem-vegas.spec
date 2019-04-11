%define        pkgname vegas

Name:          gem-%pkgname
Version:       0.1.11
Release:       alt1
Summary:       Vegas aims to solve the simple problem of creating executable versions of Sinatra/Rack apps
License:       MIT
Group:         Development/Ruby
Url:           http://code.quirkey.com/vegas/
# VCS:         https://github.com/quirkey/vegas.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Vegas aims to solve the simple problem of creating executable versions of
Sinatra/Rack apps. It includes a class Vegas::Runner that wraps Rack/Sinatra
applications and provides a simple command line interface and launching
mechanism.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.11-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
