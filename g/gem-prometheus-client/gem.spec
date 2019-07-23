%define        pkgname prometheus-client

Name:          gem-%pkgname
Version:       0.9.0
Release:       alt1
Summary:       A suite of instrumentation metric primitivesthat can be exposed through a web services interface
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/prometheus/client_ruby
%vcs           https://github.com/prometheus/client_ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
A suite of instrumentation metric primitives for Ruby that can be exposed
through a HTTP interface. Intended to be used together with a Prometheus server.


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
* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
