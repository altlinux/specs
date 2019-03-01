%define        pkgname airbrussh

Name:          gem-%pkgname
Version:       1.3.1
Release:       alt1
Summary:       Airbrussh pretties up your SSHKit and Capistrano output
Group:         Development/Ruby
License:       MIT
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/mattbrictson/airbrussh
# VCS:         https://github.com/mattbrictson/airbrussh.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Airbrussh is a concise log formatter for Capistrano and SSHKit. It displays
well-formatted, useful log output that is easy to read. Airbrussh also saves
Capistrano's verbose output to a separate log file just in case you need
additional details for troubleshooting.

As of April 2016, Airbrussh is bundled with Capistrano 3.5, and is Capistrano's
default formatter! There is nothing additional to install or enable. Continue
reading to learn more about Airbrussh's features and configuration options.

If you aren't yet using Capistrano 3.5 (or wish to use Airbrussh with SSHKit
directly), refer to the advanced/legacy usage section for installation
instructions.


%package       doc
Summary:       Documentation files for %pkgname gem
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %pkgname gem

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
* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
