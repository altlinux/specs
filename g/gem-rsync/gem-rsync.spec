%define        pkgname rsync

Name:          gem-%pkgname
Version:       1.0.9
Release:       alt1
Summary:       Ruby/Rsync is a Ruby library that can syncronize files between remote hosts by wrapping a call to the rsync binary
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jbussdieker/ruby-rsync
%vcs           https://github.com/jbussdieker/ruby-rsync.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

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
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.9-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
