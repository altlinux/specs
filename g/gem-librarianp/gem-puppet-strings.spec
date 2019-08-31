%define        pkgname librarianp

Name:          gem-%pkgname
Version:       0.6.4
Release:       alt1
Summary:       A Framework for Bundlers. Fork to support librarian-puppet
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/librarian
%vcs           https://github.com/voxpupuli/librarian.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Librarian is a framework for writing bundlers, which are tools that resolve,
fetch, install, and isolate a project's dependencies, in Ruby.

A bundler written with Librarian will expect you to provide a specfile listing
your project's declared dependencies, including any version constraints and
including the upstream sources for finding them. Librarian can resolve the spec,
write a lockfile listing the full resolution, fetch the resolved dependencies,
install them, and isolate them in your project.

A bundler written with Librarian will be similar in kind to Bundler, the bundler
for Ruby gems that many modern Rails applications use.


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
* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
