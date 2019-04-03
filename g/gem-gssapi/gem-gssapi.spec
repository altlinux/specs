%define        pkgname gssapi

Name:          gem-%pkgname
Version:       1.2.0
Release:       alt1
Summary:       A Ruby FFI wrapper around GSSAPI 
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zenchild/gssapi
# VCS:         https://github.com/zenchild/gssapi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

This is a wrapper around the system GSSAPI library (MIT only at this time).
It exposes the low-level GSSAPI methods like gss_init_sec_context and gss_wrap
and also provides an easier to use wrapper on top of this for common usage
scenarios.

I'm going to try and maintain most of the docs in the Github WIKI for this
project so please check there for documentation and examples.

https://github.com/zenchild/gssapi/wiki

Also check out the examples directory for some stubbed out client/server
examples.

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

%files doc
%ruby_gemdocdir

%changelog
* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
