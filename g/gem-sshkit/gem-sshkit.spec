%define        pkgname sshkit

Name:          gem-%pkgname
Version:       1.18.2
Release:       alt1
Summary:       A toolkit for deploying code and assets to servers in a repeatable, testable, reliable way
Group:         Development/Ruby
License:       MIT
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
Url:           https://github.com/capistrano/sshkit
# VCS:         https://github.com/capistrano/sshkit.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
SSHKit is a toolkit for running commands in a structured way on one or more
servers.


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
* Thu Mar 07 2019 Pavel Skrylev <majioa@altlinux.org> 1.18.2-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
