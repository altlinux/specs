%define        pkgname graphql-batch

Name:          gem-%pkgname
Version:       0.4.0
Release:       alt1
Summary:       A query batching executor for the graphql gem 
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Shopify/graphql-batch
# VCS:         https://github.com/Shopify/graphql-batch.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Provides an executor for the graphql gem which allows queries to be batched.


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
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%changelog
* Wed Jun 05 2019 Pavel Skrylev <majioa@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
