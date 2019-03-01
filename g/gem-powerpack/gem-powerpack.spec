%define        pkgname powerpack

Name:          gem-%pkgname
Version:       0.1.2
Release:       alt1
Summary:       Some useful extensions to the core Ruby classes
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bbatsov/powerpack
# VCS:         https://github.com/bbatsov/powerpack.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(rake)
BuildRequires: gem(rspec)
BuildRequires: gem(yard)

%description
Powerpack offers some useful extensions to the standard Ruby classes (kind of
like ActiveSupport, but less ambitious and more modular).

The project has several design goals:

* minimalistic - we don't add every possible extensions, we focus only on
  the stuff that are commonly requested and would be often useful in practice
* modular - all extensions can be loaded individually (often they are just
  individual methods)
* safe - you can't end up accidentally overriding some existing method
  definition with Powerpack's extensions


%package       doc
Summary:       Documentation files for %pkgname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{pkgname} gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
