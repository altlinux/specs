%define        pkgname puppet-strings

Name:          gem-%pkgname
Version:       2.2.0
Release:       alt1
Summary:       The next generation Puppet documentation extraction and presentation tool
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/puppet-strings
%vcs           https://github.com/puppetlabs/puppet-strings.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Puppet Strings generates documentation for Puppet code and extensions written
in Puppet and Ruby. Strings processes code and YARD-style code comments
to create documentation in HTML, Markdown, or JSON formats.


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
* Thu Jun 20 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
